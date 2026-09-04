<template>
  <div class="detail-page">
    <NuxtLink to="/books" class="back">← Назад к списку</NuxtLink>

    <div v-if="item" class="detail">
      <img :src="item.photo" :alt="item.title" />
      <h1>{{ item.title }}</h1>
      <p class="info">
        {{ item.author }}, {{ item.year }}
      </p>
      <p class="description">{{ item.description }}</p>
      <a
        v-if="item.away_link"
        :href="item.away_link"
        target="_blank"
        rel="noopener"
      >
        Читать онлайн
      </a>
    </div>

    <div v-else class="not-found">
      <h2>Книга не найдена</h2>
      <NuxtLink to="/books">Вернуться к архиву</NuxtLink>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'

const API_URL = 'http://localhost:8000'
const route = useRoute()
const router = useRouter()

const item = ref(null)

async function fetchBook() {
  try {
    const { data } = await axios.get(
      `${API_URL}/api/v1/books/${route.params.id}`
    )
    item.value = data
  } catch {
    item.value = null
  }
}

function goBack() {
  router.push('/books')
}

onMounted(fetchBook)
</script>

<style scoped>
.detail-page {
  max-width: 800px;
  margin: 0 auto;
  padding: 40px 20px;
  text-align: center;
}
.back {
  display: inline-block;
  margin-bottom: 20px;
  color: #2f3438;
  text-decoration: none;
}
.detail img {
  width: 100%;
  max-height: 500px;
  object-fit: contain;
  border-radius: 8px;
  margin-bottom: 20px;
}
.info {
  font-size: 18px;
  color: #555;
  margin-bottom: 16px;
}
.description {
  text-align: justify;
  line-height: 1.6;
  margin-bottom: 24px;
}
.not-found {
  padding: 80px 20px;
}
</style>
