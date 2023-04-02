<template>
<div class="d-flex flex-column main_content">
<div class="d-flex flex-row p-2 bg-dark">
<img src="http://via.placeholder.com/80" alt="placeholder image">
    <h3 class="text-light">{{ user_data }}</h3>
    <ul class="nav">
      <li class="nav-item">
        <a href="#" class="nav-link text-light" aria-current="page">
          pokemon collected: 0 of 150
        </a>
      </li>
      <li>
        <a href="#" class="nav-link text-light">
          <button class="btn btn-success throw text-dark" :click="catchPokemon()">throw</button> 
          <span> :30 pokeballs</span>
        </a>
      </li>
    </ul>
    <div class="modal" tabindex="-1" role="dialog">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">Modal title</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <p>Modal body text goes here.</p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-primary">Save changes</button>
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>
  </div>
    <main>
    <div class="d-flex flex-row flex-wrap justify-content-center">
    <div v-for="mons in pokemon" :key="mons.id">

      <div class="card m-2" style="width: 10rem;">
  <img v-if="mons.image_front_default" :src="mons.image_front_default" class="card-img-top" alt="...">
  <img v-else :src="mons.image_front_shiny" class="card-img-top" alt="...">
  <ul class="list-group list-group-flush">
  <li class="list-group-item"><a :href="mons.link">{{ mons.name }}</a></li>
  <li class="list-group-item"><span v-for="type in mons.type_info" :key="type.name">{{ type.name }}</span></li>
  </ul>
    </div>
</div>
    </div>
    </main>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'HomeView',
    data(){
        return {
            user_data: '',
            pokemon: [],
        }
    },
    created(){
        this.getMe()
        this.getPokemon()
    },
    methods: {
        getMe(){
            axios.get('/api/v1/users/me').then(response => {
                console.log(response)
                this.user_data = response.data.username
            }).catch(error => {
                console.log(error)
            })
        },
        getPokemon(){
            axios({
      url: '/api/pokemon/',
      method: 'get'
    }).then(res => {
      for (let i = 0; i < res.data.length; ++i) {
        this.pokemon.push(res.data[i])
        this.pokemon[i].link = "/pokemon/" + res.data[i].number
        // console.log(this.pokemon[i].link)
      }
    })
        },
        catchPokemon(){
          console.log('caught')
        },
    }
}
</script>
