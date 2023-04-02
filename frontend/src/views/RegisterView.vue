<template>
    <div class="container">
    <h2>Register</h2>
    <form @submit.prevent="registerUser()">
  <div class="mb-3">
    <input type="text" class="form-control" v-model="username" placeholder="username">
  </div>
  <div class="mb-3">
    <input type="email" v-model="email" class="form-control" placeholder="email">
  </div>
  <div class="mb-3">
    <input type="password" v-model="password" class="form-control" placeholder="password">
  </div>
  <div class="mb-3">
    <input type="password" v-model="password2" class="form-control" placeholder="confirm password">
  </div>
  <button type="submit" class="btn btn-primary me-3">register</button>
  <button class="btn btn-primary"><a href="/">login</a></button>
  </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'RegisterView',
    data(){
        return {
            username: '',
            password: '',
            password2: '',
            email: '',
        }
    },
    methods: {
        registerUser(){
            const formData = {
                username: this.username,
                password: this.password,
                password2: this.password2,
                email: this.email,
            }
            axios.post('/api/v1/users/', formData).then(response=> {
                console.log(response)
                this.$route.push('/home')
            }).catch(error => {
                console.log(error)
            })
        }
    }
}
</script>

<style>
input[type=text] > .form-control {
  color: white;
}

input:focus {
  color: white;
}
</style>