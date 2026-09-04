<!-- /frontend/pages/vereshagin.vue -->
<template>
  <div class="vereshagin-page">
    <!-- HERO-блок -->
    <section class="hero">
      <div class="hero-container">
        <div class="hero-media">
          <img
            src="/img/landing/img/family/vershagin.png"
            alt="Василий Верещагин"
            class="hero-image"
          />
          <div class="hero-dates">
            <span>1842</span>
            <span class="hero-dash">—</span>
            <span>1904</span>
          </div>
        </div>
        <div class="hero-text">
          <h1 class="hero-title">
            Василий Васильевич Верещагин
          </h1>
          <p class="hero-subtitle">
            Русский живописец, писатель, один из самых известных баталистов
            второй половины XIX века
          </p>
        </div>
      </div>
    </section>

    <!-- Раздел «Биография» -->
    <section class="biography">
      <!-- Детство и отрочество -->
      <div class="bio-item">
        <div class="bio-left">
          <h2>Детство и отрочество</h2>
          <div class="bio-date">1842–1860 гг.</div>
        </div>
        <div class="bio-right">
          <p>
            Василий Верещагин родился в Череповце, и в 9 лет родители определили его
            в кадетский морской корпус. «Корпус терпеть не мог» — вспоминал
            художник. Ещё во время учёбы он посещал рисовальную школу и знакомился
            с художниками. В 1860 году, вопреки воле родителей, поступил в
            Академию художеств и даже пробовал себя в литературном творчестве:
            предложил «Рассказ старого охотника» газете «Голос».
          </p>
        </div>
      </div>

      <!-- Картины Туркестанской серии -->
      <div class="bio-item">
        <div class="bio-left">
          <h2>Картины Туркестанской серии</h2>
          <div class="bio-date">1867–1873 гг.</div>
        </div>
        <div class="bio-right">
          <p>
            В 1867 году Верещагин поступил штатным художником к туркестанскому
            генерал-губернатору фон Кауфману. Вскоре крепость попала в осаду, он
            участвовал в битве с бухарцами и получил орден Святого Георгия IV класса
            за отвагу. Этюды и полотна он представил публике в 1869 году, открыв
            европейцам неизвестный облик Средней Азии.
          </p>
        </div>
      </div>

      <!-- Балканский поход -->
      <div class="bio-item">
        <div class="bio-left">
          <h2>Балканский поход и новые батальные полотна</h2>
          <div class="bio-date">1877–1880 гг.</div>
        </div>
        <div class="bio-right">
          <p>
            Весточка о войне с турками застала Верещагина в Париже. Он добровольцем
            отправился на Балканы, участвовал в штурме Плевны и изобразил картину
            «Царские именины» — без триумфа, лишь с горем на поле брани.
          </p>
        </div>
      </div>

      <!-- Индийское путешествие -->
      <div class="bio-item">
        <div class="bio-left">
          <h2>Индийское путешествие</h2>
          <div class="bio-date">1903 г.</div>
        </div>
        <div class="bio-right">
          <p>
            В 1903 году он отправился в Индию, писал буддийские храмы и религиозные
            сцены. После возвращения узнал о звании профессора Академии художеств,
            но отказался от него, назвав «все чины и отличия в искусстве
            безусловно вредными».
          </p>
        </div>
      </div>
    </section>

    <!-- Галерея фотографий -->
    <section class="gallery">
      <h2 class="gallery-title">Фотографии</h2>
      <div class="carousel">
        <button class="arrow prev" @click="prev">‹</button>
        <img
          :src="images[current]"
          :alt="titles[current]"
          class="carousel-image"
        />
        <button class="arrow next" @click="next">›</button>
      </div>
      <p class="carousel-caption">{{ titles[current] }}</p>
    </section>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const images = [
  '/img/landing/img/family/vereshagin_photo1.png',
  '/img/landing/img/family/vereshagin_photo2.png',
  '/img/landing/img/family/vereshagin_photo3.png'
]

const titles = [
  'В мастерской в Санкт-Петербурге',
  'На фоне Туркестанской серии',
  'Портрет в Лондоне'
]

const current = ref(0)
function prev() {
  current.value = (current.value + images.length - 1) % images.length
}
function next() {
  current.value = (current.value + 1) % images.length
}
</script>

<style scoped>
.vereshagin-page {
  font-family: 'Roboto', sans-serif;
  color: #111;
}

/* HERO */
.hero {
  background-color: #1f1f1f;
  color: #f6f4f0;
  padding: 80px 20px;
}
.hero-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 40px;
  flex-wrap: wrap;
}
.hero-media {
  flex: 1 1 300px;
  text-align: center;
}
.hero-image {
  max-width: 100%;
  height: auto;
  border: 4px solid #ddd;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
}
.hero-dates {
  margin-top: 16px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 14px;
}
.hero-dash {
  margin: 0 12px;
}
.hero-text {
  flex: 1 1 300px;
  max-width: 500px;
  text-align: left;
}
.hero-title {
  font-size: 48px;
  line-height: 1.2;
  margin-bottom: 16px;
}
.hero-subtitle {
  font-size: 18px;
  line-height: 1.4;
  margin: 0;
}

/* BIOGRAPHY */
.biography {
  background: #f6f4f0;
  padding: 60px 20px;
}
.bio-item {
  display: grid;
  grid-template-columns: 1fr 2fr;
  column-gap: 60px;
  row-gap: 24px;
  max-width: 1100px;
  margin: 0 auto 48px;
}
.bio-left h2 {
  font-size: 32px;
  margin: 0 0 8px;
}
.bio-date {
  font-size: 16px;
  color: #555;
}
.bio-right p {
  margin: 0;
  line-height: 1.6;
  font-size: 16px;
}

/* GALLERY */
.gallery {
  padding: 40px 20px;
  text-align: center;
  background: #fff;
}
.gallery-title {
  font-size: 32px;
  margin-bottom: 24px;
}
.carousel {
  position: relative;
  display: inline-block;
}
.carousel-image {
  max-width: 600px;
  width: 100%;
  height: auto;
  object-fit: contain;
}
.arrow {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: none;
  border: none;
  font-size: 48px;
  color: #333;
  cursor: pointer;
  padding: 0 12px;
}
.prev { left: -60px; }
.next { right: -60px; }
.carousel-caption {
  margin-top: 12px;
  font-size: 16px;
}
</style>
