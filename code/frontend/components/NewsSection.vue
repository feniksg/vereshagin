<template>
  <section class="news">
    <!-- Фильтры -->
    <div class="news-category-select">
      <button
        v-for="cat in categories"
        :key="cat"
        class="news-btn"
        :class="{ selected: selected === cat }"
        @click="select(cat)"
      >
        {{ cat }}
      </button>
    </div>

    <!-- Сетка новостей -->
    <div class="news-cards">
      <router-link
        v-for="item in pagedItems"
        :key="item.id"
        :to="`/media/${item.id}`"
        class="news-card"
      >
        <div class="image-container">
          <img :src="item.cover" :alt="item.title" />
        </div>
        <p class="date">{{ item.date }}</p>
        <h2 class="title">{{ item.title }}</h2>
        <p class="short-desc">{{ item.description }}</p>
      </router-link>
    </div>

    <!-- Пагинация -->
    <!-- <div class="pagination">
      <button
        class="pag-btn"
        :disabled="page === 1"
        @click="prev"
      >
        ‹
      </button>
      <span class="page-info">{{ page }} / {{ pages }}</span>
      <button
        class="pag-btn"
        :disabled="page === pages"
        @click="next"
      >
        ›
      </button>
    </div> -->
  </section>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'
import { events as fallbackEvents } from '@/data/events'

const API_URL = 'http://localhost:8000'
const itemsPerPage = 6

// Мапа для слияния с заглушками
const fallbackMap = Object.fromEntries(
  fallbackEvents.map(e => [e.id, e])
)

// Соответствия категорий
const categoryNames = {
  1: 'Конференция',
  2: 'Программа',
  3: 'Выставка'
}

// Состояние
const raw = ref([])
const selected = ref('Все')
const page = ref(1)

// Функция слияния API-данных и локальных заглушек
function mergeEvent(item) {
  const fb = fallbackMap[item.id] || {}
  return {
    id: item.id,
    date: item.created_at
      ? new Date(item.created_at).toLocaleDateString('ru-RU', {
          day: '2-digit', month: 'short', year: 'numeric'
        })
      : fb.date,
    title: item.title || fb.title,
    cover: item.photo || fb.cover,
    category: categoryNames[item.category] || fb.category,
    status: item.status || fb.status,
    description: item.text || fb.description
  }
}

// Запрос новостей с бэка
async function fetchEvents() {
  try {
    const { data } = await axios.get(`${API_URL}/api/v1/media-items`)
    raw.value = data.results.map(mergeEvent)
  } catch (e) {
    console.error('Ошибка загрузки новостей', e)
    raw.value = fallbackEvents
  }
}

onMounted(fetchEvents)

// Динамические категории
const categories = computed(() => {
  const cats = Array.from(new Set(raw.value.map(e => e.category)))
  return ['Все', ...cats]
})

// Фильтрация
const filteredItems = computed(() => {
  return selected.value === 'Все'
    ? raw.value
    : raw.value.filter(e => e.category === selected.value)
})

// Пагинация
const pages = computed(() => Math.ceil(filteredItems.value.length / itemsPerPage))
const pagedItems = computed(() => {
  const start = (page.value - 1) * itemsPerPage
  return filteredItems.value.slice(start, start + itemsPerPage)
})

// Обработчики
function select(cat) {
  selected.value = cat
  page.value = 1
}
function prev() {
  if (page.value > 1) page.value--
}
function next() {
  if (page.value < pages.value) page.value++
}
</script>

<style scoped>
.news {
  padding: 60px 20px;
  background: #fff;
}

/* Фильтры */
.news-category-select {
  display: flex;
  justify-content: center;
  gap: 16px;
  margin-bottom: 40px;
}
.news-btn {
  padding: 12px 24px;
  border: 1px solid #333;
  background: #fff;
  border-radius: 8px;
  font-size: 14px;
  cursor: pointer;
}
.news-btn.selected {
  background: #333;
  color: #fff;
}

/* Сетка */
.news-cards {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 32px;
  max-width: 1200px;
  margin: 0 auto 40px;
}
.news-card {
  display: flex;
  flex-direction: column;
  text-decoration: none;
}
.image-container {
  width: 100%;
  padding-top: 66.66%;
  position: relative;
  overflow: hidden;
}
.image-container img {
  position: absolute;
  top: 0; left: 0;
  width: 100%; height: 100%;
  object-fit: cover;
}
.date {
  margin: 16px 0 8px;
  font-size: 12px;
  color: rgba(0,0,0,0.6);
  text-transform: uppercase;
}
.title {
  font-size: 16px;
  margin: 0 0 8px;
  line-height: 1.3;
  color: #000;
}
.short-desc {
  font-size: 14px;
  line-height: 1.5;
  color: #333;
}

/* Пагинация */
.pagination {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 16px;
  margin-bottom: 80px;
}
.pag-btn {
  width: 40px;
  height: 40px;
  border: 1px solid #333;
  background: #fff;
  font-size: 24px;
  line-height: 1;
  cursor: pointer;
}
.pag-btn:disabled {
  opacity: 0.3;
  cursor: default;
}
.page-info {
  font-size: 14px;
}
</style>