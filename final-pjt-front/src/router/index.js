import Vue from 'vue'
import VueRouter from 'vue-router'
import MainView from '../views/MainView'
import SearchView from '../views/SearchView'
import RecommendView from '../views/RecommendView'
import CommunityView from '../views/CommunityView'
import ProfileView from '../views/ProfileView'
import SignUpView from '../views/SignUpView'
import MovieDetailView from '../views/MovieDetailView'
Vue.use(VueRouter)

const routes = [

  {
    path: '/',
    name: 'MainView',
    component: MainView
  },
  {
    path: '/search',
    name: 'SearchView',
    component: SearchView
  },
  {
    path: '/recommend',
    name: 'RecommendView',
    component: RecommendView
  },
  {
    path: '/community',
    name: 'CommunityView',
    component: CommunityView
  },
  {
    path: '/profile/:id',
    name: 'ProfileView',
    component: ProfileView
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },
  {
    path: '/movie/:id',
    name: 'MovieDetailView',
    component: MovieDetailView
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
