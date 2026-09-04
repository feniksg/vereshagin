<template>
  <div class="main-container">
    <!-- Header -->
    <div class="image-container">
      <img
        class="back-header"
        src="/img/landing/img/media/backheader.jpg"
        alt=""
      />
      <img
        class="land-bg"
        src="@/assets/img/landing/img/header-archive.png"
        alt=""
      />
      <h1 class="header-title">Архив изображений</h1>
    </div>

    <div class="content-container">
      <!-- Sidebar filters -->
      <aside class="filter-container">
        <div class="sidebar">
          <!-- Поиск по названию -->
          <input
            type="text"
            v-model="search"
            class="search"
            placeholder="Поиск"
          />

          <!-- Фильтр по категории -->
          <div class="filter-block">
            <h2>Категория</h2>
            <label
              v-for="cat in categories_art"
              :key="cat.id"
              class="custom-checkbox"
            >
              <input
                type="checkbox"
                :checked="selectedCategory === cat.id"
                @change="toggleCategory(cat.id)"
              />
              <span class="checkbox"></span>
              {{ cat.name }}
            </label>
          </div>

          <hr />

          <!-- Фильтр по периоду -->
          <div class="filter-block">
            <h2>Период</h2>
            <div class="year-range">
              <label>
                <input
                  type="number"
                  v-model.number="startYear"
                  min="1800"
                  max="2100"
                  placeholder="с"
                />
              </label>
              <label>
                <input
                  type="number"
                  v-model.number="endYear"
                  min="1800"
                  max="2100"
                  placeholder="по"
                />
              </label>
            </div>
            <label
              v-for="range in periodRanges"
              :key="range.label"
              class="custom-checkbox"
            >
              <input
                type="checkbox"
                :checked="selectedPeriod === range.label"
                @change="applyPresetPeriod(range)"
              />
              <span class="checkbox"></span>
              {{ range.label }}
            </label>
          </div>

          <hr />

          <!-- Фильтр по серии -->
          <div class="filter-block">
            <h2>Серия</h2>
            <label
              v-for="serie in series"
              :key="serie.id"
              class="custom-checkbox"
            >
              <input
                type="checkbox"
                :checked="selectedSeries === serie.id"
                @change="toggleSeries(serie.id)"
              />
              <span class="checkbox"></span>
              {{ serie.name }}
            </label>
          </div>

          <hr />

          <!-- Кнопка расширенного поиска -->
          <button class="btn-search" @click="fetchCards">
            Расширенный поиск
          </button>
        </div>
      </aside>

      <!-- Галерея изображений -->
      <div class="arts-container">
        <div class="art-column">
          <NuxtLink
            v-for="card in cards"
            :key="card.id"
            :to="`/imageArchive/${card.id}`"
            class="arts"
          >
            <Art :src="card.src" class="art" />
            <div class="text-wrapper">
              <h2 class="title-art">{{ card.title }}</h2>
            </div>
          </NuxtLink>
        </div>
      </div>
    </div>

    <!-- Пагинация -->
    <div class="pagination">
      <img
        src="@/assets/img/landing/svg/arr-left.svg"
        alt="Назад"
        class="arr-left"
        @click="prevPage"
        v-if="currentPage > 1"
      />
      <img
        src="@/assets/img/landing/svg/arr-left.svg"
        alt="Назад"
        class="arr-left-disabled"
        v-if="currentPage === 1"
      />
      <div class="page-number">
        <span
          v-for="page in totalPages"
          :key="page"
          @click="goToPage(page)"
          :class="{ active: page === currentPage }"
        >
          {{ page }}
        </span>
      </div>
      <img
        src="@/assets/img/landing/svg/arr-right.svg"
        alt="Вперёд"
        class="arr-right"
        @click="nextPage"
        v-if="currentPage < totalPages"
      />
      <img
        src="@/assets/img/landing/svg/arr-right.svg"
        alt="Вперёд"
        class="arr-right-disabled"
        v-if="currentPage === totalPages"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'
import Art from '@/components/layout/CardImage.vue'

const API_URL = 'http://localhost:8000'
const route = useRoute()

// Поисковый ввод и данные
const search = ref('')
const categories_art = ref([])
const series = ref([])
const cards = ref([])

// Годовой диапазон
const startYear = ref(null)
const endYear = ref(null)

// Фильтры
const selectedCategory = ref(
  route.query.category ? Number(route.query.category) : null
)
const selectedSeries   = ref(null)

// Предустановленные периоды
const periodRanges = [
  { label: '1843—1874', from: 1843, to: 1874 },
  { label: '1844—1867', from: 1844, to: 1867 },
  { label: '1887—1900', from: 1887, to: 1900 },
]
const selectedPeriod = ref(null)

// Пагинация
const itemsPerPage = 16
const currentPage  = ref(1)
const totalPages   = ref(1)

// Переключаем категории и сразу перезагружаем
function toggleCategory(id) {
  selectedCategory.value = selectedCategory.value === id ? null : id
  currentPage.value = 1
  fetchCards()
}

// Переключаем серии
function toggleSeries(id) {
  selectedSeries.value = selectedSeries.value === id ? null : id
  currentPage.value = 1
  fetchCards()
}

// Применяем предустановленный период
function applyPresetPeriod(range) {
  if (selectedPeriod.value === range.label) {
    selectedPeriod.value = null
    startYear.value = null
    endYear.value = null
  } else {
    selectedPeriod.value = range.label
    startYear.value = range.from
    endYear.value = range.to
  }
  currentPage.value = 1
  fetchCards()
}

// Навигация по страницам
async function prevPage() {
  if (currentPage.value > 1) {
    currentPage.value--
    await fetchCards()
  }
}
async function nextPage() {
  if (currentPage.value < totalPages.value) {
    currentPage.value++
    await fetchCards()
  }
}
async function goToPage(page) {
  currentPage.value = page
  await fetchCards()
}

// Загружаем справочные данные для фильтров
async function fetchData() {
  const [catsRes, seriesRes] = await Promise.all([
    axios.get(`${API_URL}/api/v1/art-categories`),
    axios.get(`${API_URL}/api/v1/art-series`)
  ])
  categories_art.value = catsRes.data.results
  series.value = seriesRes.data.results
}

// Основной запрос карточек
async function fetchCards() {
  const params = {
    page: currentPage.value,
    page_size: itemsPerPage,
    search: search.value,
    category: selectedCategory.value || '',
    series: selectedSeries.value || ''
  }
  if (startYear.value) params.year__gte = startYear.value
  if (endYear.value)   params.year__lte = endYear.value

  try {
    const resp = await axios.get(`${API_URL}/api/v1/art-items`, { params })
    cards.value = resp.data.results.map(item => ({
      id:    item.id,
      src:   item.photo,
      title: item.title
    }))
    totalPages.value = Math.ceil(resp.data.count / itemsPerPage)
  } catch (e) {
    console.error('Ошибка загрузки карточек', e)
  }
}

// Если в URL приходит ?category=1 или 2 — сразу применяем
watch(
  () => route.query.category,
  (newCat) => {
    selectedCategory.value = newCat ? Number(newCat) : null
    currentPage.value = 1
    fetchCards()
  }
)

// Перезагружаем при изменении фильтров поиска
watch(
  [search, selectedCategory, selectedSeries, startYear, endYear],
  () => {
    currentPage.value = 1
    fetchCards()
  }
)

// При старте — получаем справочные и карточки
onMounted(async () => {
  await fetchData()
  await fetchCards()
})
</script>

<style lang="scss" scoped>
.main-container {
  max-width: 1920px;
  margin: 0 auto;
}

.image-container {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: -43px 0 64px;

  .back-header {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    z-index: -2;
  }
  .land-bg {
    width: 100vw;
    position: relative;
    z-index: -1;
  }
  .header-title {
    position: absolute;
    z-index: 1;
  }
}

.content-container {
  display: flex;
  padding: 20px;
  gap: 30px;
}

.filter-container {
  flex: 0 0 300px;
  .search {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #e3e3e2;
    border-radius: 5px;
    background: #e3e3e2;
  }
}

.filter-block {
  margin: 0 0 20px 15px;
  h2 {
    margin: 40px 0 10px 0;
    font-weight: bold;
  }
  .year-range {
    display: flex;
    gap: 10px;
    margin-bottom: 10px;
    input {
      width: 95px;
      padding: 10px;
      border: 1px solid #e3e3e2;
      border-radius: 5px;
      background: #e3e3e2;
    }
  }
}

hr {
  border: none;
  height: 1px;
  background: #111;
  margin: 10px 0;
}

.custom-checkbox {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
  input[type="checkbox"] {
    display: none;
  }
  .checkbox {
    width: 20px;
    height: 20px;
    border: 2px solid #ccc;
    border-radius: 3px;
    margin-right: 10px;
    position: relative;
  }
  input[type="checkbox"]:checked + .checkbox {
    background: #d5cbb3;
    border-color: #d5cbb3;
    &:after {
      content: '';
      position: absolute;
      left: 6px;
      top: 2px;
      width: 6px; height: 12px;
      border: solid black;
      border-width: 0 1px 1px 0;
      transform: rotate(45deg);
    }
  }
}

.btn-search {
  display: block;
  width: 100%;
  padding: 10px;
  margin: 40px 0;
  background: #e3e3e2;
  color: grey;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  &:hover { color: #111; }
}

.arts-container {
  flex: 1;
  padding: 20px;
}
.art-column {
  column-count: 3;
  column-gap: 25px;
}
.arts {
  display: inline-block;
  width: 100%;
  margin-bottom: 25px;
  text-decoration: none;
}
.art {
  width: 100%;
  display: block;
  border-radius: 8px;
  object-fit: cover;
}
.text-wrapper {
  margin-top: 10px;
  .title-art {
    font-weight: bold;
    text-align: center;
    font-size: 1.2rem;
  }
}

.pagination {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 20px;
  padding: 0 150px;
  .arr-left, .arr-right { cursor: pointer; }
  .page-number span {
    padding: 20px;
    font-size: 20px;
    cursor: pointer;
    &.active {
      font-weight: 700;
      color: #111;
    }
  }
}
</style>
