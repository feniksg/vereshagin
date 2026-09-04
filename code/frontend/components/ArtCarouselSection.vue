<template>
  <section class="art-section">
    <h2 class="section-title">{{ title }}</h2>

    <div class="cards-list-navigation">
      <button class="nav-btn prev" @click="prev" :disabled="current === 0">‹</button>

      <div class="carousel-viewport">
        <div class="carousel-track" :style="trackStyle">
          <router-link
            v-for="item in items"
            :key="item.id"
            :to="`${routeBase}/${item.id}`"
            class="carousel-slide"
          >
            <img :src="item.src" :alt="item.title" />
            <p class="slide-title">{{ item.title }}</p>
            <p class="slide-info">
              {{ item.date }}
              <span v-if="item.size">, {{ item.size }}</span>
              <span v-else-if="item.format">, {{ item.format }}</span>
              <span v-else-if="item.year">{{ item.year }}</span>
            </p>
          </router-link>
        </div>
      </div>

      <button class="nav-btn next" @click="next" :disabled="current >= maxOffset">›</button>
    </div>

    <router-link :to="archiveLink" class="archive-btn">ПЕРЕЙТИ В АРХИВ</router-link>
  </section>
</template>

<script setup>
import { ref, computed, onMounted, onBeforeUnmount } from 'vue'

const props = defineProps({
  title:       { type: String, required: true },
  items:       { type: Array,   default: () => [] },
  routeBase:   { type: String,  required: true },
  archiveLink: { type: String,  required: true }
})

const current = ref(0)
const perPage = ref(3)

function updatePerPage() {
  perPage.value = window.innerWidth < 768 ? 1 : 3
  if (current.value > maxOffset.value) {
    current.value = maxOffset.value
  }
}

const maxOffset = computed(() =>
  Math.max(props.items.length - perPage.value, 0)
)

function next() {
  current.value = current.value >= maxOffset.value
    ? 0
    : current.value + perPage.value
}

function prev() {
  current.value = current.value <= 0
    ? maxOffset.value
    : current.value - perPage.value
}

const trackStyle = computed(() => ({
  transform: `translateX(-${(100 / perPage.value) * current.value}%)`
}))

onMounted(() => {
  updatePerPage()
  window.addEventListener('resize', updatePerPage)
})
onBeforeUnmount(() => {
  window.removeEventListener('resize', updatePerPage)
})
</script>

<style scoped lang="scss">
.art-section {
  max-width: 1440px;
  margin: 0 auto 60px;
  padding: 0 20px;
  text-align: center;

  .section-title {
    font-size: 32px;
    margin-bottom: 24px;
  }

  .cards-list-navigation {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 16px;
  }

  .nav-btn {
    background: none;
    border: none;
    font-size: 2rem;
    line-height: 1;
    cursor: pointer;
    width: 40px;
    height: 40px;
    color: #333;
    &:disabled {
      opacity: 0.3;
      cursor: default;
    }
  }

  .carousel-viewport {
    overflow: hidden;
    flex: 1;
  }

  .carousel-track {
    display: flex;
    transition: transform 0.5s ease;
    gap: 16px;
  }

  .carousel-slide {
    flex: 0 0 calc((100% - 32px) / 3);
    text-decoration: none;
    color: inherit;
    display: flex;
    flex-direction: column;
    align-items: center;

    img {
      width: 100%;
      height: 220px;
      object-fit: cover;
      border-radius: 8px;
      transition: filter 0.3s;
    }
    /* при ховере — затемняем */
    &:hover img {
      filter: brightness(70%);
    }

    .slide-title {
      margin: 12px 0 4px;
      font-weight: 500;
    }
    .slide-info {
      font-size: 14px;
      color: #666;
    }
  }

  .archive-btn {
    display: inline-block;
    margin-top: 24px;
    padding: 10px 24px;
    border: 1px solid #000;
    border-radius: 8px;
    text-decoration: none;
    color: #000;
    transition: background-color 0.3s, color 0.3s;
    &:hover {
      background-color: #000;
      color: #fff;
    }
  }
}

/* Один слайд на мобилах */
@media (max-width: 767px) {
  .carousel-slide {
    flex: 0 0 100%;
  }
  .carousel-slide img {
    height: 180px;
  }
}
</style>
