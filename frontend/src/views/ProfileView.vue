<template>
    <div class="profile">
      {{ pokemon[0].name }}
    </div>
  </template>
<script>
import axios from 'axios'
export default {
    name: 'ProfileView',
    data(){
      return {
        pokemon: []
      }
    },

    created(){
      axios({
      url: 'http://localhost:8000/api/pokemon/' + this.$route.params.id,
      method: 'get'
    }).then(res => {
      this.pokemon.push(res.data)
      console.log(this.pokemon)
    })
    }
}
</script>