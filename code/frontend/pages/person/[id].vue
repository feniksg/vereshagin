<template>
  <div class="person-page">
    <div v-if="isValid" class="biography-container">
      <!-- Пример «оборотки» по образцу, который вы прислали -->
      <div class="biography-header">
        <img
          class="bio-photo"
          src="/img/landing/img/family/vasiliyvasilevichvereshagin.png"
          alt="Василий Васильевич Верещагин"
        />
        <div class="bio-text">
          <h1>Василий Васильевич Верещагин</h1>
          <p class="life-dates">1842 — 1904</p>
          <p class="short-intro">
            Русский живописец, писатель, один из самых известных баталистов второй половины XIX века.
          </p>
        </div>
      </div>

      <!-- Здесь можно вставить расширенную биографию (контент может быть любым, как у вас в макете) -->
      <div class="detailed-bio">
        <h2>Детство и отрочество</h2>
        <p>
          Василий Верещагин родился в Череповце и в 9 лет родители определили его в кадетский морской корпус. «Корпус терпеть не мог» — вспоминал художник. Ещё во время учёбы он посещал рисовальную школу, знакомился с художниками. В 1860 году, вопреки воле родителей, поступил в Академию художеств. В это же время пробовал себя в литературе: предложил свой «Рассказ старого охотника» петербургской газете «Голос».
        </p>

        <h2>Картины Туркестанской серии</h2>
        <p>
          В 1867 году поступил на службу к туркестанскому генерал-губернатору фон Каупману штатным художником. Вскоре крепость с русскими войсками оказалась в осаде — местные жители восстали. Верещагин участвовал в битве с бухарцами и получил Орден Святого Георгия 4-го класса «за отвагу». Привезённые из Туркестана картины художник представил в 1869 году в Петербурге. Благодаря ним посетители впервые увидели Среднюю Азию: невольничий рынок, нищих опиумоедов и женщин, полностью укутанных в одежды. В Туркестанскую серию вошли 13 полотен, 81 этюд и 133 рисунка. В 1873 году весь цикл выставили в Хрустальном дворце в Лондоне.
        </p>

        <h2>Первая персональная выставка</h2>
        <p>
          Первая масштабная выставка Верещагина прошла в Петербурге в 1874 году. Сразу нашлось множество желающих посмотреть картины, но высшие чины сочли работы слишком «непатриотичными», потому что художник изображал ужасы войны, а не триумфальную сторону. Павел Третьяков, напротив, купил весь туркестанский цикл за 97 000 рублей.
        </p>

        <!-- … сюда можно дописать всё, что нужно по вашему макету … -->
      </div>
    </div>

    <div v-else class="not-found">
      <h2>Страница не найдена</h2>
      <p>Информация о данном человеке отсутствует.</p>
      <NuxtLink to="/">← Вернуться на главную</NuxtLink>
    </div>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()
const personId = Number(route.params.id)

// Пока считаем единственным «валидным» id = 9
const isValid = personId === 9
</script>

<style scoped>
.person-page {
  max-width: 800px;
  margin: 0 auto;
  padding: 40px 20px;
}

.biography-header {
  display: flex;
  align-items: center;
  gap: 24px;
  margin-bottom: 32px;
}

.bio-photo {
  width: 200px;
  height: auto;
  object-fit: cover;
  border: 4px solid #f0f0f0;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
}

.bio-text {
  max-width: 500px;
}

.bio-text h1 {
  font-size: 32px;
  margin: 0 0 8px 0;
}

.life-dates {
  font-size: 14px;
  margin: 0 0 16px 0;
  color: #555;
}

.short-intro {
  font-size: 16px;
  line-height: 1.5;
}

.detailed-bio {
  margin-top: 32px;
}

.detailed-bio h2 {
  font-size: 24px;
  margin: 24px 0 8px 0;
}

.detailed-bio p {
  font-size: 14px;
  line-height: 1.6;
  margin: 0 0 16px 0;
}

/* Страница 404 (или “нет данных”) */
.not-found {
  text-align: center;
  padding: 100px 20px;
}
.not-found h2 {
  font-size: 28px;
  margin-bottom: 16px;
}
.not-found p {
  margin-bottom: 24px;
  font-size: 14px;
}
</style>
