<template>
    <div class="container d-flex flex-row flex-wrap">
      <div v-for="poke in pokemon" :key="poke.id" class="card m-2">
        <img :src="poke.image_front" class="card-img-top" width="150px">
        <div class="card-body">
          <h3 class="card-title"><a id="pokenotes" :href="poke.link">{{ poke.name }}</a></h3>
        </div>
      </div>
    </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import axios from 'axios'

export default {
  name: 'HomeView',
  components: {
    // HelloWorld
  },
  data() {
    return {
      pokemon: [],
      pokenotes: [],
    }
  },

  created() {
    axios({
      url: 'http://localhost:8000/api/pokemon/',
      method: 'get'
    }).then(res => {
      for (let i = 0; i < res.data.length; ++i) {
        this.pokemon.push(res.data[i])
        this.pokemon[i].link = "/pokemon/" + res.data[i].number
      }
    })
  }
}
</script>
