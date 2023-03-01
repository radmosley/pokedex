<template>
    <div class="container">
        <div class="mb-3">
            <label for="exampleInputEmail1" class="form-label">Username</label>
            <input type="email" v-model="username" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
        </div>
        <div class="mb-3">
            <label for="exampleInputPassword1" class="form-label">Password</label>
            <input type="password" v-model="password" class="form-control" id="exampleInputPassword1">
        </div>
        <button type="submit" @click="login()" class="btn btn-primary me-2">login</button>
        <router-link to="/register"><button type="submit" class="btn btn-primary">register</button></router-link>
        
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'LoginView',
    data() {
        return {
            username: '',
            password: '',
        }
    },
    methods: {
        login(){
            if(!this.username && !this.password){
                return
            } else {
                axios({
                    method: 'post',
                    url:'http://localhost:8000/u/login',
                    data: {
                        'username': this.username,
                        'password': this.password,
                    }
                })
            }
        }
    }
}
</script>