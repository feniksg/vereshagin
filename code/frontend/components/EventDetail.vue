<template>
  <div class="event-detail">
    <header class="hero" :style="{ backgroundImage: `url(${event.cover})` }">
      <div class="overlay">
        <div class="wrapper">
            <h1 class="title">{{ event.title }}</h1>
            <p class="subtitle">
                {{ event.description || 'Описание скоро появится…' }}
            </p>
        </div>
      </div>
    </header>

    <main class="main">
      <section class="info grid">
        <div class="details">
          <h2>Детали события</h2>
          <p><strong>Дата:</strong> {{ event.date }}</p>
          <p><strong>Место:</strong> {{ event.location }}</p>
          <p><strong>Категория:</strong> {{ event.category }}</p>
          <p><strong>Статус:</strong> {{ event.status }}</p>
        </div>
        <div class="tickets">
          <h2>Стоимость билетов</h2>
          <p>Взрослый: {{ event.price.adult }} ₽</p>
          <p>Пенсионный: {{ event.price.pension }} ₽</p>
          <p>Детский: {{ event.price.child }} ₽</p>
          <p class="contact">Телефон: {{ event.contact.phone }}</p>
        </div>
      </section>

        <section class="about grid">
            <div class="text">
                <h2>О событии</h2>
                <p>{{ event.description }}</p>
                <p>
                    Это событие станет отличным поводом ближе познакомиться с
                    творчеством художника и открыть новые грани его наследия. Вас ждут
                    экскурсии, интерактивные занятия и тематические лекции.
                </p>
            </div>
            <Carousel :images="event.gallery" />
        </section>
    </main>
  </div>
</template>

<script setup>
import { defineProps } from 'vue'
import Carousel from '@/components/Carousel.vue'

const props = defineProps({
  event: {
    type: Object,
    required: true
  }
})
</script>

<style scoped>
.event-detail {
    .hero {
        position: relative;
        height: 60vh;
        background-size: cover;
        background-position: center;
    }
    .overlay {
        background: rgba(0, 0, 0, 0.45);
        color: #fff;
        height: 100%;
        display: flex;
        align-items: center;
    }
    .wrapper {
        max-width: 1440px;
        margin: 0 auto;
        padding: 0 20px;
    }
    .title {
        font-size: 36px;
        margin-bottom: 16px;
    }
    .subtitle {
        font-size: 18px;
        max-width: 600px;
    }

    .main {
        max-width: 1440px;
        margin: 0 auto;
        padding: 40px 20px;
    }

    .info.grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 48px;
        margin-bottom: 40px;
  }
    .info h2 {
        font-family: 'Playfair Display', serif;
        font-size: 24px;
        margin-bottom: 16px;
    }
    .info p {
        margin: 6px 0;
    }

    .about.grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 48px;
        align-items: start;
    }
    .about h2 {
        font-family: 'Playfair Display', serif;
        font-size: 24px;
        margin-bottom: 16px;
    }
    .about .text p {
        line-height: 1.6;
        margin-bottom: 1em;
    }
}

@media (max-width: 768px) {
    .info.grid, .about.grid {
        grid-template-columns: 1fr;
    }
}
</style>
