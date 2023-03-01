<template>
  <div id="app">
  <NavBar></NavBar>
      <!-- <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link> -->
    <router-view />
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
export default {
  name: 'app',
  components: {
    NavBar,
  }
}
</script>