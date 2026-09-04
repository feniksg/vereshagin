<template>
  <div class="media-page">
    <main>
      <!-- CURRENT EVENTS -->

      <section v-if="current.length" class="current-events">
        <img class="back-header" src="/img/landing/img/media/backheader.jpg" alt="" />
        <h1 class="section-title">Медиа</h1>
        <!-- <div class="banners">
          <div v-for="item in current" :key="item.id" class="banner-card">
            <img :src="item.cover" alt="" />
            <div class="banner-title">{{ item.title }}</div>
          </div>
        </div> -->
      </section>

      <!-- ALL EVENTS WITH FILTERS -->
      <section class="events-section">
        <aside class="filters" :class="{ collapsed: isMobile }">
          <input
            v-model="search"
            type="text"
            class="filter-search"
            placeholder="Поиск"
          />

          <div class="filter-group">
            <div class="filter-title">Категория</div>
            <label
              v-for="c in categories"
              :key="c"
              class="checkbox"
            >
              <input type="checkbox" :value="c" v-model="filterCats" />
              {{ c }}
            </label>
          </div>

          <hr class="divider" />

          <div class="filter-group">
            <div class="filter-title">Статус</div>
            <label
              v-for="s in statuses"
              :key="s"
              class="checkbox"
            >
              <input type="checkbox" :value="s" v-model="filterStatus" />
              {{ s }}
            </label>
          </div>
        </aside>

        <div class="events-content">
          <div class="events-grid">
            <NuxtLink
              v-for="item in paged"
              :key="item.id"
              :to="`/media/${item.id}`"
              class="event-card"
            >
              <img :src="item.cover" alt="" />
              <p class="event-date">{{ item.date }}</p>
              <h3 class="event-name">{{ item.title }}</h3>
            </NuxtLink>
          </div>

          <nav class="pagination">
            <button
              class="pag-btn"
              :disabled="page === 1"
              @click="page--"
            >‹</button>

            <span
              v-for="n in pagesToShow"
              :key="n + ''"
              class="pag-page"
              :class="{ active: n === page, ellipsis: n === '...'}"
              @click="typeof n === 'number' && (page = n)"
            >
              {{ n }}
            </span>

            <button
              class="pag-btn"
              :disabled="page === pages"
              @click="page++"
            >›</button>
          </nav>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import axios from 'axios'

import { useRoute } from 'vue-router'
import { events as fallbackEvents } from '@/data/events'

const API_URL = 'http://localhost:8000'

const route = useRoute()

const search = ref('')
const filterCats = ref([])
const filterStatus = ref([])
const categories = ['Конференция', 'Программа', 'Выставка']
const statuses = ['Будет', 'Идёт', 'Прошло']

// detect mobile
const isMobile = ref(false)
function onResize() {
  isMobile.value = window.innerWidth < 768
}
onMounted(() => {
  onResize()
  window.addEventListener('resize', onResize)
  fetchEvents()
})

// source data
const categoryNames = { 1: 'Конференция', 2: 'Программа', 3: 'Выставка' }
const fallbackMap = Object.fromEntries(fallbackEvents.map(e => [e.id, e]))
const raw = ref([])

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

async function fetchEvents() {
  try {
    const { data } = await axios.get(`${API_URL}/api/v1/media-items`)
    raw.value = data.results.map(mergeEvent)
  } catch (e) {
    console.error('Ошибка загрузки мероприятий', e)
    raw.value = fallbackEvents
  }
}

const current = computed(() => raw.value.filter(e => e.status === 'Идёт'))

// filtering
const filtered = computed(() =>
  raw.value.filter(item => {
    const byCat = !filterCats.value.length || filterCats.value.includes(item.category)
    const bySt = !filterStatus.value.length || filterStatus.value.includes(item.status)
    const bySr = item.title.toLowerCase().includes(search.value.toLowerCase())
    return byCat && bySt && bySr
  })
)

// pagination
const page = ref(1)
const perPage = 6
const pages = computed(() => Math.ceil(filtered.value.length / perPage))
const paged = computed(() => {
  const start = (page.value - 1) * perPage
  return filtered.value.slice(start, start + perPage)
})


function applyQueryFilters() {
  const cat = route.query.cat
  const status = route.query.status
  filterCats.value = categories.includes(cat) ? [cat] : []
  filterStatus.value = statuses.includes(status) ? [status] : []
}

watch(() => route.query, applyQueryFilters, { immediate: true })

watch([search, filterCats, filterStatus], () => {
  page.value = 1
})

// dynamic pagesToShow with ellipses
const pagesToShow = computed(() => {
  const total = pages.value
  const curr = page.value
  if (total <= 7) {
    return Array.from({ length: total }, (_, i) => i + 1)
  }
  const left = curr <= 4
  const right = curr >= total - 3
  const result = []
  if (left) {
    result.push(1, 2, 3, 4, 5, '...', total)
  } else if (right) {
    result.push(1, '...', total - 4, total - 3, total - 2, total - 1, total)
  } else {
    result.push(1, '...', curr - 1, curr, curr + 1, '...', total)
  }
  return result
})
</script>

<style scoped lang="scss">
.media-page {
  main {
    max-width: 1440px;
    margin: 0 auto;
  }
}

// CURRENT EVENTS
.current-events {
  position: relative;
  // background: #fcf2e9;
  padding: 40px 20px;
  text-align: center;

  .back-header {
    position: absolute;
    top: 0;
    left: -250px;
    width: 150%;
    z-index: -1;
  }

  .section-title {
    padding-top: 40px;
    margin-bottom: 24px;
    position: relative;
    z-index: 1;
  }

  .banners {
    padding-top: 80px;
    display: flex;
    gap: 24px;
    justify-content: center;
    flex-wrap: wrap;

    .banner-card {
      border-radius: 16px;
      overflow: hidden;
      flex: 1 1 300px;
      width: 406px;

      img {
        width: 100%;
        display: block;
      }
      .banner-title {
        padding: 12px;
        font-size: 16px;
        background: #fff;
      }
    }
  }
}

// ALL EVENTS
.events-section {
  display: flex;
  padding: 40px 20px;
  gap: 32px;

  .filters {
    flex: 0 0 280px;
    background: #fff;
    padding: 24px;
    border-radius: 16px;
    position: sticky;
    top: 100px;

    &.collapsed { 
      display: none; 
    }

    .filter-search {
      width: 100%; padding: 10px;
      border: 1px solid #ccc; 
      border-radius: 8px;
      background: #f2f2f2; 
      margin-bottom: 24px;
    }

    .filter-group {
      margin-bottom: 24px;
      .filter-title {
        font-size: 18px; 
        font-weight: 600;
        margin-bottom: 12px;
      }
      .checkbox {
        display: flex; 
        align-items: center; 
        gap: 8px;
        font-size: 14px; 
        margin-bottom: 8px;
        input { 
          width:16px; 
          height:16px; 
          border-radius:4px; 
        }
      }
    }

    .divider {
      border: none; 
      border-top: 1px solid #e0e0e0;
      margin: 24px 0;
    }
  }

  .events-content {
    flex: 1;

    .events-grid {
      display: grid;
      grid-template-columns: repeat(3,1fr);
      gap: 24px;
      // ensure exactly two rows (6 items) per page
    }

    .event-card {
      background: #fff;
      overflow: hidden;
      border-radius: 16px;  
      cursor: pointer;
      transition: transform 0.2s;

      img {
        width: 100%;
        border-radius: 16px;
        display: block;
      }
      .event-date {
        font-size: 12px;
        color: rgba(0,0,0,0.6);
        padding: 8px 12px 0;
      }
      .event-name {
        font-size: 16px;
        font-weight: 600;
        padding: 4px 12px 12px;
        margin: 0;
      }

      &:hover { 
        transform: translateY(-4px); 
      }
    }

    .pagination {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 16px;
      margin-top: 32px;

      .pag-btn {
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        width: 40px; 
        height:40px;
        border:1px solid #000000; 
        background:#fff;
        padding: 0;
        border-radius:50%; 
        font-size:30px; 
        line-height:1;
        color: #000;
        background: none;
        font: inherit;
        color: inherit;
        cursor: pointer;
        outline: none;
        
        cursor:pointer;
        &:disabled { 
          opacity:.3; 
          cursor:default; 
        }
      }

      .pag-page {
        font-size:14px;
        cursor:pointer;
        &.active { 
          font-weight:bold; 
          // color:#111; 
        }
        &.ellipsis { 
          cursor: default; 
        }
      }
    }
  }
}

// RESPONSIVE
@media (max-width: 992px) {
  .events-grid { 
    grid-template-columns: repeat(2,1fr); 
  }
}
@media (max-width: 768px) {
  .events-section { 
    flex-direction: column; 
  }
  .filters { 
    display: none; 
  }
  .events-grid { 
    grid-template-columns: 1fr; 
  }
}
</style>
