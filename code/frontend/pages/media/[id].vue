<template>
  <div class="event-page">
    <EventDetail v-if="event" :event="event" />
    <div v-else class="not-found">
      <h2>Событие не найдено</h2>
      <NuxtLink to="/media">Вернуться к списку</NuxtLink>
    </div>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { ref, onMounted } from 'vue'
import axios from 'axios'
import EventDetail from '@/components/EventDetail.vue'
import { events as fallbackEvents } from '@/data/events'

const API_URL = 'http://localhost:8000'
const categoryNames = { 1: 'Конференция', 2: 'Программа', 3: 'Выставка' }
const fallbackMap = Object.fromEntries(fallbackEvents.map(e => [e.id, e]))

const route = useRoute()
const event = ref(null)

function mergeEvent(item) {
  const fallback = fallbackMap[item.id] || {}
  return {
    id: item.id,
    date: item.created_at
      ? new Date(item.created_at).toLocaleDateString('ru-RU', {
          day: '2-digit',
          month: 'short',
          year: 'numeric'
        })
      : fallback.date,
    title: item.title || fallback.title,
    cover: item.photo || fallback.cover,
    category: categoryNames[item.category] || fallback.category,
    status: item.status || fallback.status,
    description: item.text || fallback.description,
    location: fallback.location,
    price: fallback.price,
    contact: fallback.contact,
    gallery: fallback.gallery
  }
}

async function fetchEvent() {
  try {
    const { data } = await axios.get(`${API_URL}/api/v1/media-items/${route.params.id}`)
    event.value = mergeEvent(data)
  } catch (e) {
    console.error('Ошибка загрузки события', e)
    const fb = fallbackMap[Number(route.params.id)]
    if (fb) event.value = fb
  }
}

onMounted(fetchEvent)
</script>

<style scoped>
.not-found {
  text-align: center;
  padding: 100px 20px;
}
</style>