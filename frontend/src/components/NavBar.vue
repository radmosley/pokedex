<template>
    <nav class="navbar bg-dark">
      <div class="container">
        <h1 class="navbar-brand text-light"><router-link to="/">Pokedex</router-link></h1>
        <div>
          <router-link to="/login">login</router-link>
          <router-link to="/register">register</router-link>
        </div>
      </div>
    </nav>
</template>

<script>
export default {
  name: 'NavBar',
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
