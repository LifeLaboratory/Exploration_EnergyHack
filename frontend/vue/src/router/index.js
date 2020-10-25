import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import NavProfile from '@/components/navs/NavProfile'
import CreateProfile from '@/components/CreateProfile'
import Company from '@/components/Company'
import Details from '@/components/Details'
Vue.use(VueRouter)

const routes = [
  {
    path: '/profile',
    component: NavProfile,
    children: [
      {
        path: '',
        component: CreateProfile
      },
      {
        path: 'list',
        component: Company,
      },
      {
        path: 'detail/:id',
        component: Details
      }
    ]
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
