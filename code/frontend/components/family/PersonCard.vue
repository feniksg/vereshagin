<!-- src/components/family/PersonCard.vue -->
<template>
  <div
    class="person-card"
    :class="{ 'main-card': isMain }"
    :data-person-id="person.id"
    @click="handleClick"
  >
    <div class="card-inner">
      <!-- Front side -->
      <div class="card-front">
        <div class="photo-wrapper">
          <img
            v-if="photoUrl"
            :src="photoUrl"
            :alt="person.fullName"
            class="person-photo"
          />
          <div v-else class="photo-placeholder"></div>

          <img
            :src="frameUrl"
            alt="frame"
            class="frame-overlay"
          />

          <div class="name-label">{{ person.fullName }}</div>
        </div>
      </div>

      <!-- Back side -->
      <div class="card-back">
        <img
          :src="rambackUrl"
          alt="back"
          class="frame-back"
        />
        <div class="back-content">
          <div class="dates">
            <span>{{ person.dateFrom }}</span>
            <span class="dash">—</span>
            <span>{{ person.dateTo || '?' }}</span>
          </div>
          <div class="description">{{ person.description }}</div>
          <div class="back-name">{{ person.fullName }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'

const props = defineProps({
  person: {
    type: Object,
    required: true
  }
})

const router = useRouter()

// Обработка клика: только у главного Верещагина (id=9) переходим на страницу
function handleClick() {
  if (props.person.id === 9) {
    router.push('/biography')
  }
}

// Пути к изображениям в папке public/img/landing/img/family
const photoUrl = computed(() => {
  if (props.person.photo) {
    return `/img/landing/img/family/${props.person.photo}`
  }
  return props.person.gender === 'female'
    ? '/img/landing/img/family/nonamewomen.png'
    : '/img/landing/img/family/noname.png'
})

const frameUrl = '/img/landing/img/family/ram.png'
const rambackUrl = '/img/landing/img/family/ramback.png'

const isMain = computed(() => props.person.id === 9)
</script>

<style scoped>
.person-card {
  perspective: 800px;
  width: 203px;          
  height: 252px;         
  position: relative;
  flex-shrink: 0;
  cursor: pointer;
}

.person-card:not(.main-card) {
  cursor: default;
}

.person-card.main-card {
  width: 270px;
  height: 330px;
}

.card-inner {
  width: 100%;
  height: 100%;
  position: relative;
  transform-style: preserve-3d;
  transition: transform 1s ease;
}

.person-card:hover .card-inner {
  transform: rotateY(180deg);
}

.card-front,
.card-back {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
}

.card-front {
  z-index: 2;
}

.photo-wrapper {
  width: 100%;
  height: 100%;
  position: relative;
  overflow: hidden;
}

.person-photo {
  position: absolute;
  top: 16px;
  left: 12px;
  width: calc(100% - 24px);
  height: calc(100% - 48px);
  object-fit: cover;
  z-index: 1;
}

.photo-placeholder {
  position: absolute;
  top: 16px;
  left: 12px;
  width: calc(100% - 24px);
  height: calc(100% - 48px);
  background-color: #d8d8d8;
  z-index: 1;
}

.frame-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: contain;
  z-index: 2;
  pointer-events: none;
}

.name-label {
  position: absolute;
  bottom: 16px;
  left: 0;
  width: 100%;
  text-align: center;
  font-family: 'Roboto', sans-serif;
  font-size: 18px;
  color: #333;
  z-index: 3;
  line-height: 1.2;
}

.card-back {
  transform: rotateY(180deg);
  display: flex;
  align-items: center;
  justify-content: center;
}

.frame-back {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: 1;
}

.back-content {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  padding: 24px 12px;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  z-index: 2;
}

.dates {
  font-family: 'Roboto', sans-serif;
  font-size: 16px;
  display: flex;
  align-items: center;
  gap: 12px;
}

.dash {
  width: 40px;
  text-align: center;
}

.description {
  font-family: 'Roboto', sans-serif;
  font-size: 12px;
  text-align: center;
  line-height: 1.4;
  overflow: hidden;
  flex-grow: 1;
  margin: 20px 0;
}

.back-name {
  font-family: 'Roboto', sans-serif;
  font-size: 16px;
  text-align: center;
  color: #333;
}
</style>
