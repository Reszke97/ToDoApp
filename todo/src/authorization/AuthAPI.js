import axios from 'axios';
import store from '../store/index';



let baseURL = ''

if(process.env.VUE_APP_API_URL === ''){
	baseURL = 'http://127.0.0.1:8000'
	console.log(baseURL)
}
else{
	baseURL = process.env.VUE_APP_API_URL+ ':'+ process.env.VUE_APP_PORT
	console.log(baseURL)
}

const AUTH_API = axios.create({
    baseURL: baseURL,
    timeout: 5000,
    headers: {
        Authorization: localStorage.getItem('token')
            ? 'JWT ' + localStorage.getItem('token')
            : null,
            'Content-Type': 'application/json',
            accept: 'application/json',
    },
})

AUTH_API.interceptors.response.use(
	(response) => {
		return response;
	},
	async function (error) {
		const originalRequest = error.config;

		if (typeof error.response === 'undefined') {
			alert(
				error
			);
			store.commit('setIsAuthenticated', false)
			return Promise.reject(error);
		}

		if(
			(
				error.response.status === 401 && (
					error.response.data.detail === 'Token contained no recognizable user identification' 
					||  originalRequest.url === '/api/v1/token/verify/'
				)
			)
			|| error.response.status === 400
		){
			alert('Niepoprawny token')
			store.commit('setIsAuthenticated', false)
			return Promise.reject(error);
		}

		if (
			error.response.status === 401 &&
			originalRequest.url === '/api/v1/token/refresh/'
		) {
			
			// window.location.href = 'http://localhost:8080/login';
			alert('Token się wysypał, zaloguj się ponownie')
			store.commit('setIsAuthenticated', false)
			return Promise.reject(error);
		}

		if (
			(error.response.data.code === 'token_not_valid' || error.response.data.detail === 'Authentication credentials were not provided.') &&
			originalRequest.url !== '/api/v1/token/verify/' &&
			error.response.status === 401 &&
			error.response.statusText === 'Unauthorized'
		) {
			const refreshToken = localStorage.getItem('refreshToken');

			try{
				if (refreshToken) {
					const tokenParts = JSON.parse(atob(refreshToken.split('.')[1]));
	
					// exp date in token is expressed in seconds, while now() returns milliseconds:
					const now = Math.ceil(Date.now() / 1000);
	
					if (tokenParts.exp > now) {
						return AUTH_API
							.post('/api/v1/token/refresh/', { refresh: localStorage.getItem('refreshToken') })
							.then((response) => {
								store.commit('setToken', {
									access: response.data.access,
									refresh: response.data.refresh
								})

								store.commit('setIsAuthenticated', true);
	
								AUTH_API.defaults.headers['Authorization'] =
									'JWT ' + response.data.access;
								originalRequest.headers['Authorization'] =
									'JWT ' + response.data.access;
									
								return AUTH_API(originalRequest)
							})
							.catch((err) => {
								store.commit('setIsAuthenticated', false);
								return Promise.reject(error);
							});
					} else {
						alert('Token wygasł', tokenParts.exp, now);
						store.commit('setIsAuthenticated', false);
						// window.location.href = 'http://localhost:8080/login';
					}
				} else {
					store.commit('setIsAuthenticated', false);
					// window.location.href = 'http://localhost:8080/login';
				}
			}catch( error ){
				alert(error)
				// return
			}
		}
		return Promise.reject(error);
	}
);
export {AUTH_API}