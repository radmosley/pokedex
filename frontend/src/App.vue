<template>
  <nav class="navbar">
  <div>
  <h1 class="navbar-brand m-auto"><router-link class="navbar-brand m-auto" to="/home">Pokedex</router-link></h1>
  </div>
  <ul class="navbar-nav d-flex flex-row">
  <li class="nav-item" v-if="show_login">
    <router-link class="login" to="/">login</router-link>
  </li>
  <li class="nav-item" v-else>
  <a href="#" class="register" @click="logout">logout</a>
  </li>
  <li class="nav-item">
    <router-link class="register" v-if="show_login" to="/register">register</router-link>
  </li>
  </ul>
  </nav>
  <router-view/>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  data(){
    return {show_login: Boolean}
  },
  beforeCreate(){
    this.$store.commit('initializeStore')
    const access = this.$store.state.access
    if(access){
      axios.defaults.headers.common['Authorization'] = 'JWT' + access
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  },
  created(){
    if(this.$store.state.access){
      this.show_login = false
    } 
    if(!this.$store.state.access) {
      this.show_login = true
    }
  },

  methods: {
    logout(){
      localStorage.access = ''
      localStorage.refresh = ''
      this.show_login = true
    }
  }
}
</script>
<style>
.navbar-brand {
  color: #FFCB05;
  font-size: 1.5rem;
  font-weight: bold;
  /* -webkit-text-stroke: 1px blue; */
  text-decoration: none;
  margin-left: 20px;
}

.navbar {
  background-color: #81211D;
}

.navbar-nav {
  margin-right: 20px;
}

.login {
  color: #FFCB05;
  text-decoration: none;
  font-weight: bold;
  margin-right: 10px;
}

.logout {
  color: #df8986;
  text-decoration: none;
  font-weight: bold;
  margin-right: 10px;
}

.register {
  color: #24AFFD;
  font-weight: bold;
  text-decoration: none;
}

.throw {
  background-color: #74FF06;
}
</style>