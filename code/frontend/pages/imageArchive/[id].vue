<template>
  <div class="detail-page" v-if="item">
    <NuxtLink to="/imageArchive" class="back">Назад к архиву</NuxtLink>
    <img :src="item.photo" :alt="item.title" class="detail-img" />
    <h1>{{ item.title }}</h1>
    <p class="meta">{{ item.year }}</p>
    <p class="size" v-if="item.width && item.height">{{ item.width }}×{{ item.height }} см</p>
    <p class="desc" v-if="item.desc">{{ item.desc }}</p>
  </div>
  <div v-else class="not-found">
    <h2>Картина не найдена</h2>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const API_URL = 'http://localhost:8000'
const route = useRoute()
const item = ref(null)

async function fetchItem() {
  try {
    const { data } = await axios.get(`${API_URL}/api/v1/art-items/${route.params.id}`)
    item.value = data
  } catch (e) {
    console.error('Ошибка загрузки картины', e)
  }
}

onMounted(fetchItem)
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
}
.detail-img {
  width: 100%;
  max-height: 600px;
  object-fit: contain;
  border-radius: 8px;
  margin-bottom: 20px;
}
.meta {
  font-size: 18px;
  opacity: 0.7;
}
.desc {
  text-align: justify;
  margin-top: 20px;
}
</style>
