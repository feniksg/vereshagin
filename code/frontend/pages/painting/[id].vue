<template>
  <div class="detail-page" v-if="item">
    <button class="back-btn" @click="goBack">← Назад</button>

    <!-- ландшафт -->
    <template v-if="!isPortrait">
      <header
        class="hero"
        :style="{ backgroundImage: `url(${item.src})` }"
      />
      <section class="info gray-bg">
        <h1>{{ item.title }}</h1>
        <div class="meta">
          {{ item.date }}
          <span v-if="item.size">, {{ item.size }}</span>
        </div>
        <p class="description landscape">{{ item.description }}</p>
      </section>
    </template>

    <!-- портрет -->
    <template v-else>
      <div class="portrait-container">
        <img :src="item.src" alt="" class="portrait-img" />
        <div class="portrait-info">
          <h1>{{ item.title }}</h1>
          <div class="meta">
            {{ item.date }}
            <span v-if="item.size">, {{ item.size }}</span>
          </div>
          <p class="description portrait">{{ item.description }}</p>
        </div>
      </div>
    </template>
  </div>

  <div v-else class="not-found">
    <h2>Работа не найдена</h2>
    <NuxtLink to="/">Вернуться на главную</NuxtLink>
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
const isPortrait = ref(false)

async function fetchItem() {
  try {
    const { data } = await axios.get(`${API_URL}/api/v1/art-items/${route.params.id}`)
    item.value = {
      src:         data.photo,
      title:       data.title,
      date:        data.year,
      size:        data.width && data.height ? `${data.width}×${data.height} см` : null,
      description: data.desc
    }
    await detectOrientation()
  } catch (err) {
    console.error(err)
  }
}

function goBack() {
  router.back()
}

async function detectOrientation() {
  if (!item.value) return
  const img = new Image()
  img.src = item.value.src
  try {
    await img.decode()
    isPortrait.value = img.naturalHeight > img.naturalWidth
  } catch {
    isPortrait.value = false
  }
}

onMounted(fetchItem)
</script>

<style scoped>
.detail-page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}
.back-btn {
  background: none;
  border: none;
  font-size: 16px;
  cursor: pointer;
  margin-bottom: 16px;
}
.hero {
  width: 100%;
  height: 600px;
  background-size: cover;
  background-position: center;
  border-radius: 12px;
}
.gray-bg {
  background: #f7f7f7;
  padding: 24px;
  border-radius: 8px;
  margin-top: 16px;
}
.portrait-container {
  display: flex;
  flex-wrap: wrap;
  gap: 24px;
  margin-top: 16px;
}
.portrait-img {
  max-width: 100%;
  height: auto;
  border-radius: 12px;
  flex: 1 1 400px;
}
.portrait-info {
  flex: 1 1 400px;
}
.meta {
  color: #666;
  margin: 8px 0;
}
.description {
  line-height: 1.6;
}
.description.landscape {
  margin-top: 16px;
}
.not-found {
  text-align: center;
  padding: 60px 20px;
}
</style>
