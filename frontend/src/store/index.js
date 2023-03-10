import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios'
import jwt_decode from 'jwt-decode'

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    jwt: localStorage.getItem('token'),
    endpoints: {
      obtainToken: 'localhost:8000/u/login',
      refreshToken: 'localhost:8000/u/login/refresh',
    },
  },
  getters: {},
  mutations: {
    updateToken(state, newToken) {
      localStorage.setItem('token', newToken);
      state.jwt = newToken;
    },
    removeToken(state) {
      localStorage.remove('token');
      state, null;
    },
  },
  actions: {
    obtainToken(username, password){
      const payload = {
        username: username,
        password: password
      }
      axios.post(
        this.state.endpoints.obtainToken, payload
        ).then((response)=>{
          this.commit('updateToken', response.data.token)
      }).catch((error) => {
        console.log(error)
      })
    },
    refreshToken(){
      const payload = {
        token: this.state.jwt
      }
      axios.post(this.state.endpoints.refreshToken, payload).then((response)=>{
        this.commit('updateToken', response.data.token)
      }).catch((error)=>{
        console.log(error)
      })
    },
    inspectToken(){
      const token = this.state.jwt
      if(token){
        const decoded = jwt_decode(token)
        const exp = decoded.exp
        const orig_iat = decoded.orig_iat
        if(exp - (Date.now()/1000) < 1800 && (Date.now()/1000 - orig_iat < 628200)){
          this.dispatch('refreshToken')
        } else if (exp - Date.now()/1000 < 1000){
          return
        } else {
          // prompt user to relog
        }
      }
    }
  },
  modules: {},
});
