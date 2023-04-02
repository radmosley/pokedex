<template>
    <div>
    <p>
    {{ number }}
    {{ name }}
    <span v-for="type in types" :key="type.id">
    {{ type.name }}
    </span>
    </p>
    <img :src="image" class="card-img-top" alt="...">
    <hr>
    <h3>Abilities</h3>
    <p v-for="ability in abilities" :key="ability.ability_id">
    {{ ability.ability_name }}
    </p>
    <h3>Possible Moves</h3>
    <p v-for="move in moves" :key="move.id">
    {{ move.name }}
    </p>
    </div>
</template>
<script>
import axios from 'axios';

export default {
    name: 'PokemonProfile',
    data(){
        return {
            number: '',
            name: '',
            types: [],
            image: '',
            abilities: [],
            moves: [],
        }
    },
    methods: {

      getAPokemon(){
        axios({
          url: '/api/pokemon/' + this.$route.params.id,
          method: 'get'
        }).then(res => {
          this.number = res.data.number
          this.types = res.data.type_info
          this.name = res.data.name
          if(res.data.image_front_default){
            this.moves = res.data.image_front_default
          } else {
            this.image = res.data.image_front_shiny
          }
          this.abilities = res.data.ability_info
          this.moves = res.data.move_info
        })
          }
        },
        created(){
        this.getAPokemon()
    },
}
</script>