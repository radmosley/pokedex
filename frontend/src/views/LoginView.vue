<template>
    <div class="container">
    <h2>Login</h2>
    <form @submit.prevent="loginUser">
  <div class="mb-3">
    <input type="text" v-model="username" class="form-control bg-dark" placeholder="username">
  </div>
  <div class="mb-3">
    <input type="password" v-model="password" class="form-control bg-dark" placeholder="password" id="exampleInputPassword1">
  </div>
  <button type="submit" class="btn btn-primary me-3">login</button>
  <button type="submit" class="btn btn-primary"><a href="/register">register</a></button>
</form>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'LoginView',
    data(){
        return {
            username: '',
            password: ''
        }
    },
    methods: {
        loginUser(){
            axios.defaults.headers.common['Authorization'] = ''
            localStorage.removeItem['access']

            const formData = {
                username: this.username,
                password: this.password
            }
            
            axios.post('/api/v1/jwt/create', formData).then(response => {
                console.log(response)
                const access = response.data.access
                const refresh = response.data.refresh

                this.$store.commit('setAccess', access)
                this.$store.commit('setRefresh', refresh)

                axios.defaults.headers.common['Authorization'] = ' JWT ' + access
                localStorage.setItem('access', access)
                localStorage.setItem('refresh', refresh)
                this.$router.push('/home')
            }).catch(error => {
                console.log(error)
            })
        }
    }
}
</script>

<style>
.form-control::placeholder {
    color: #FFFFFF;
}
</style>