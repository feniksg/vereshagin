import { createRouter, createWebHistory } from 'vue-router'
import MediaPage from '@/pages/MediaPage.vue'
import EventDetailPage from '@/pages/EventDetailPage.vue'
// ... если есть другие страницы, импортируйте их сюда ...

const routes = [
  {
    path: '/media',
    name: 'Media',
    component: MediaPage
  },
  {
    path: '/media/:id',
    name: 'EventDetail',
    component: EventDetailPage,
    props: true
  },
  // сюда же — 404, About, и т.д.
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
