import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ArchieveView from '@/views/ArchieveView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/archive/:title',
      name: 'archive',
      component: ArchieveView,
      props: (route) => ({ title: route.params.title }),
    }
  ],
})

export default router
