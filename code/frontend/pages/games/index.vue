<template>
  <section class="games-page">
    <h1 class="page-title">Игры</h1>
    <div class="games-grid">
      <NuxtLink
        v-for="game in games"
        :key="game.id"
        :to="game.link"
        class="game-card"
      >
        {{ game.title }}
      </NuxtLink>
    </div>
  </section>
</template>

<script setup>
const games = [
  { id: 1, title: 'Пазлы', link: '#' },
  { id: 2, title: 'Пятнашки', link: '#' },
  { id: 3, title: 'Название картин', link: '#' },
  { id: 4, title: 'Фрагменты картин', link: '#' }
]
</script>

<style scoped>
.games-page {
  max-width: 1440px;
  margin: 0 auto;
  padding: 40px;
  text-align: center;
}
.page-title {
  font-family: 'Playfair Display', serif;
  font-size: 32px;
  margin-bottom: 24px;
}
.games-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 24px;
}
.game-card {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 200px;
  height: 120px;
  background: #e3e3e2;
  border-radius: 8px;
  text-decoration: none;
  color: inherit;
  font-size: 18px;
}
</style>
