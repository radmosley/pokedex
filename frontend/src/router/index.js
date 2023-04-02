import { createRouter, createWebHistory } from 'vue-router'
import Register from '@/views/RegisterView.vue'
import Login from '@/views/LoginView.vue'
import Home from '@/views/HomeView.vue'
import PokemonProfile from '@/views/PokemonProfile.vue'

const routes = [
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  {
    path: '/home',
    name: 'Home',
    component: Home,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/pokemon/:id',
    name: 'PokemonProfile',
    component: PokemonProfile,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach(() => {
  console.log(router)
  // if(
  //   !localStorage.access && 
  //   !localStorage.refresh &&
  //   to.name !== 'Login' &&
  //   to.name !== 'Register'
  //   ){
  //   return {name: 'Login'}
  // }
})

export default router