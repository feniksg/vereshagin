<template>
  <div class="detail-page" v-if="item">
    <template v-if="!isPortrait">
      <button class="back-btn" @click="goBack">Назад</button>
      <header class="hero" :style="{ backgroundImage: `url(${item.src})` }" />
      <section class="info gray-bg">
        <h1>{{ item.title }}</h1>
        <div class="meta">{{ item.date }}{{ item.size ? ', ' + item.size : item.format ? ', ' + item.format : '' }}</div>
        <p class="description landscape">{{ item.description }}</p>
      </section>
    </template>
    <template v-else>
      <button class="back-btn" @click="goBack">Назад</button>
      <div class="portrait-container">
        <img :src="item.src" alt="" class="portrait-img" />
        <div class="portrait-info">
          <h1>{{ item.title }}</h1>
          <div class="meta">{{ item.date }}{{ item.size ? ', ' + item.size : item.format ? ', ' + item.format : '' }}</div>
          <p class="description portrait">{{ item.description }}</p>
        </div>
      </div>
    </template>
  </div>
  <div v-else class="not-found">
    <h2>Работа не найдена</h2>
    <NuxtLink to="/imageArchive">Вернуться к архиву</NuxtLink>
  </div>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router'
import { onMounted, ref } from 'vue'
import axios from 'axios'

const API_URL = 'http://localhost:8000'
const route = useRoute()
const router = useRouter()

const item = ref(null)
const type = route.params.type

async function fetchItem() {
  try {
    const { data } = await axios.get(`${API_URL}/api/v1/art-items/${route.params.id}`)
    item.value = {
      ...data,
      src: data.photo,
      date: data.year,
      size: data.width && data.height ? `${data.width}×${data.height} см` : null,
      description: data.desc
    }
    await detectOrientation()
  } catch (e) {
    console.error('Ошибка загрузки картины', e)
  }
}

const isPortrait = ref(false)
async function detectOrientation() {
  if (!item.value) return
  const img = new Image()
  img.src = item.value.src
  try {
    await img.decode()
    isPortrait.value = img.height > img.width
  } catch (_) {
    isPortrait.value = false
  }
}

function goBack() {
  router.push('/imageArchive')
}

onMounted(fetchItem)
</script>

<style scoped>
.detail-page {
  max-width: 1440px;
  margin: 0 auto;
  padding: 0 40px;
}
.back-btn {
  font-size: 14px;
  color: #007BFF;
  background: none;
  border: none;
  cursor: pointer;
  margin: 20px 0;
}
h1 {
  /* font-family: 'Playfair Display'; */
  font-size: 32px;
  margin: 16px 0;
  text-align: center;
}
.meta {
  font-size: 20px;
  color: #666;
  text-align: center;
  margin-bottom: 24px;
}
.description {
  font-size: 16px;
  color: #333;
  line-height: 1.6;
}
.landscape.description {
  margin-top: 24px;
}
.hero {
  border-radius: 16px;
  height: 800px;
  background-size: cover;
  background-position: center;
}
.gray-bg {
  background: #f5f5f5;
  padding: 40px;
}
.portrait-container {
  display: flex;
  gap: 40px;
  align-items: flex-start;
}
.portrait-img {
  width: 100%;
  border-radius: 16px;
}
.portrait-info {
  width: 60%;
}
.not-found {
  text-align: center;
  padding: 100px 20px;
}
</style>
