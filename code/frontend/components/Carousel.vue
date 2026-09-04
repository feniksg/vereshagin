<template>
  <div class="carousel">
    <button class="carousel-btn prev" @click="prev">‹</button>
    <img
      v-if="images.length"
      :src="images[current]"
      alt=""
      class="carousel-image"
    />
    <button class="carousel-btn next" @click="next">›</button>
    <div class="indicators" v-if="images.length > 1">
      <span
        v-for="(img, i) in images"
        :key="i"
        :class="{ active: i === current }"
        @click="go(i)"
      ></span>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'

const props = defineProps({
  images: {
    type: Array,
    default: () => []
  }
})

const current = ref(0)

// Если список картинок изменился, сбрасываем на первую
watch(() => props.images, () => {
  current.value = 0
})

function prev() {
  if (!props.images.length) return
  current.value =
    (current.value - 1 + props.images.length) % props.images.length
}

function next() {
  if (!props.images.length) return
  current.value = (current.value + 1) % props.images.length
}

function go(i) {
  current.value = i
}
</script>

<style scoped>
.carousel {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}
.carousel-image {
  max-width: 100%;
  max-height: 400px;
  object-fit: contain;
}
.carousel-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(0,0,0,0.5);
  border: none;
  color: #fff;
  font-size: 1.5rem;
  width: 2.5rem;
  height: 2.5rem;
  cursor: pointer;
}
.carousel-btn.prev { left: 10px; }
.carousel-btn.next { right: 10px; }
.indicators {
  position: absolute;
  bottom: 10px;
  display: flex;
  gap: 8px;
}
.indicators span {
  width: 10px;
  height: 10px;
  background: #ccc;
  border-radius: 50%;
  cursor: pointer;
}
.indicators span.active {
  background: #333;
}
</style>
