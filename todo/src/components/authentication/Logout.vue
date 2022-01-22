<template>
    
</template>

<script>
    import axios from 'axios'
    export default {
        data: () => ({
            }),
        created(){
            axios.post(this.$store.state.baseURL+'/api/v1/user/logout/', {
                refresh_token: localStorage.getItem('refreshToken'),
            })
            .then(response => {
                this.$store.commit('userLogout')
                window.location.href = '/login'
            })
            .catch(error => {
                this.$store.commit('userLogout')
                window.location.href = '/login'
            })
        },
    }
</script>