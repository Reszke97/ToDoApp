import Vue from 'vue'
import Vuex from 'vuex'
import { AUTH_API } from '../authorization/AuthAPI'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    accessToken: localStorage.getItem("token"),
    refreshToken: localStorage.getItem("refreshToken"),
    isAuthenticated: false,
    baseURL: 'http://127.0.0.1:8000'
  },
  mutations: {
    setToken (state, { access, refresh }) {
      localStorage.setItem( 'token', access );
      localStorage.setItem( 'refreshToken', refresh );
      AUTH_API.defaults.headers['Authorization'] = 'JWT ' + access;
      state.accessToken = access
      state.refreshToken = refresh
    },

    setBaseURL(state, value){
      state.baseURL = value
    },

    setRefreshToken (state){
      state.refreshToken = localStorage.getItem('refreshToken')
    },

    userLogout (state){
      if(state.isAuthenticated){
        if(localStorage.getItem("token")){
          localStorage.removeItem("token")
        }
        localStorage.removeItem("refreshToken")
        state.accessToken = null
        state.refreshToken = null
        state.isAuthenticated = false;
        AUTH_API.defaults.headers['Authorization'] = null;
      }
    },

    setIsAuthenticated (state, value){
      state.isAuthenticated = value
    },

    destroyToken (state) {
      state.accessToken = null
      state.refreshToken = null
      state.authenticated = false;
    },
  },
})