<template>
  <section class="art-section">
    <h2>Живопись</h2>
    <div class="cards-list-navigation">
      <img src="@/assets/img/landing/svg/arr-left.svg" alt="Back" class="arr-left" @click="prev" />
      <div class="carousel">
        <div class="slides" :style="translateStyle">
          <router-link
            v-for="(item, index) in items"
            :key="index"
            :to="`/painting/${item.id}`"
            class="slide"
          >
            <img :src="item.src" :alt="item.title" />
            <p class="title">{{ item.title }}</p>
            <p class="info">
              {{ item.date }}<span v-if="item.size">, {{ item.size }}</span>
            </p>
          </router-link>
        </div>
      </div>
      <img src="@/assets/img/landing/svg/arr-right.svg" alt="Forward" class="arr-right" @click="next" />
    </div>
    <router-link :to="archiveLink" class="archive-btn">ПЕРЕЙТИ В АРХИВ</router-link>
  </section>
</template>

<script setup>
import { ref, computed, onMounted, onBeforeUnmount } from 'vue'

const props = defineProps({
  items: { type: Array, default: () => [] },
  archiveLink: { type: String, required: true }
})

const current = ref(0)
const perPage = ref(3)

function updatePerPage() {
  if (typeof window !== 'undefined') {
    perPage.value = window.innerWidth < 768 ? 1 : 3
  }
}

function next() {
  const max = Math.max(props.items.length - perPage.value, 0)
  if (current.value >= max) {
    current.value = 0
  } else {
    current.value = Math.min(current.value + perPage.value, max)
  }
}

function prev() {
  const max = Math.max(props.items.length - perPage.value, 0)
  if (current.value <= 0) {
    current.value = max
  } else {
    current.value = Math.max(current.value - perPage.value, 0)
  }
}

const translateStyle = computed(() => ({
  transform: `translateX(-${(100 / perPage.value) * current.value}%)`
}))

onMounted(() => {
  updatePerPage()
  window.addEventListener('resize', updatePerPage)
})

onBeforeUnmount(() => {
  if (typeof window !== 'undefined')
    window.removeEventListener('resize', updatePerPage)
})
</script>

<style scoped lang="scss">
.art-section {
  padding: 0 0 60px 0;
  text-align: center;

  h2 {
    margin-bottom: 20px;
    font-size: 32px;
  }

  .cards-list-navigation {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 20px;
    padding: 0 150px;

    .arr-left,
    .arr-right {
      cursor: pointer;
      opacity: 0.7;
      transition: opacity 0.3s;
      &:hover { opacity: 1; }
    }

    .carousel {
      // overflow: hidden;
      flex: 1;
    }

    .slides {
      display: flex;
      transition: transform 0.5s;
    }

    .slide {
      flex: 0 0 calc(100% / 3);
      padding: 0 10px;
      overflow: hidden;
      display: block;
      text-decoration: none;
      color: inherit;
      transition: transform 0.3s;

      img {
        width: 100%;
        height: 220px;
        object-fit: cover;
        border-radius: 8px;
        display: block;
      }
      .title {
        margin: 10px 0 4px;
        font-weight: 500;
      }
      .info {
        font-size: 14px;
        opacity: 0.6;
      }
      &:hover {
        transform: scale(1.05);
      }
    }
  }

  .archive-btn {
    display: inline-block;
    margin-top: 30px;
    padding: 12px 24px;
    border: 1px solid #000;
    border-radius: 8px;
    text-decoration: none;
    color: inherit;
    transition: opacity 0.3s;
    &:hover { opacity: 0.7; }
  }
}

@media (max-width: 767px) {
  .cards-list-navigation {
    padding: 0 20px;

    .slide {
      flex-basis: 100%;
      img {
        height: 200px;
      }
    }
  }
}
</style>
