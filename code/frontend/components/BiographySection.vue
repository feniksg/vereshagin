<template>
  <section class="centered biography-section">
    <div class="biography">
      <div class="dates">
        <span class="date">1842</span>
        <div class="custom-hr"></div>
        <span class="date">1904</span>
      </div>
      <h1>Биография</h1>

      <!-- Детство и отрочество -->
      <div class="biography-item">
        <div class="base">Детство и отрочество</div>
        <div class="primary">
          Василий Верещагин родился в Череповце и в 9 лет родители
          определили его в кадетский морской корпус. «Корпус терпеть
          не мог» — вспоминал художник. Во время учебы он посещал
          рисовальную школу и знакомился с художниками. В 1860 году
          против воли родителей поступил в Академию художеств, а также
          пробовал себя в литературе, предложив свой «Рассказ старого охотника»
          для петербургской газеты «Голос».
        </div>
        <div class="base bdate">1842–1860 гг.</div>
      </div>
      <div class="custom-hr"></div>

      <!-- Туркестанская серия -->
      <div class="biography-item">
        <div class="base">Картины Туркестанской серии</div>
        <div class="primary">
          В 1867 году поступил штатным художником к генерал-губернатору
          Туркестана Константину фон Кауфману. Принимал участие в сражениях
          с бухарцами, получил орден Святого Георгия IV класса. В 1869 году
          привёз на родину серию из 13 полотен, 81 этюда и 133 рисунка,
          которые в 1873 году выставили в Хрустальном дворце Лондона.
        </div>
        <div class="base bdate">1867–1873 гг.</div>
      </div>
      <div class="custom-hr"></div>

      <!-- Первая персональная выставка -->
      <div class="biography-item">
        <div class="base">Первая персональная выставка</div>
        <div class="primary">
          В 1874 году прошла первая масштабная петербургская выставка:
          вместо триумфальных баталий художник показал страдания солдат.
          Критики называли работы «антипатриотичными», но Третьяков купил
          весь цикл за 97 000 руб. Иван Крамской называл её успехом.
        </div>
        <div class="base bdate">1874 г.</div>
      </div>
      <div class="custom-hr"></div>

      <!-- Индийское путешествие -->
      <div class="biography-item">
        <div class="base">Индийское путешествие Верещагина</div>
        <div class="primary">
          В 1874–1876 гг. вместе с женой побывал в Бомбее, Джайпуре,
          Дели, Агре, Ладаке и Кашмире, три месяца — в Гималаях и Сиккиме.
          Писал храмы, монастыри, религиозные обряды и портреты монахов.
        </div>
        <div class="base bdate">1874–1876 гг.</div>
      </div>
      <div class="custom-hr"></div>

      <!-- Балканский поход -->
      <div class="biography-item">
        <div class="base">Балканский поход и новые батальные полотна</div>
        <div class="primary">
          Услышав о войне с турками в Париже, отправился добровольцем
          на Балканы. Был ранен при штурме Плевны, но запечатлел поле
          брани без пафоса. В 1879 году выставил балканскую серию в Париже,
          где продемонстрировал сочувствие к солдатам.
        </div>
        <div class="base bdate">1877–1880 гг.</div>
      </div>
      <div class="custom-hr"></div>

      <!-- Путешествие в Японию -->
      <div class="biography-item">
        <div class="base">Путешествие в Японию</div>
        <div class="primary">
          В 1903 году посетил Японию: изучал храмы, пейзажи, буддийские
          обряды. В 1904 году броненосец «Петропавловск», на котором он плывёт,
          подорвался у Порт-Артура, и художник погиб.
        </div>
        <div class="base bdate">1903–1904 гг.</div>
      </div>
    </div>
  </section>
</template>

<script setup>
// чисто статическая секция, скрипт не нужен
</script>

<style scoped>
.centered {
  text-align: center;
  margin-top: 48px;
}
.biography {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 85%;
  margin: 0 auto 80px;
}
.dates {
  display: flex;
  align-items: center;
  gap: 24px;
  margin-bottom: 24px;
}
.date {
  font-size: 24px;
  font-weight: bold;
}
.custom-hr {
  width: 70%;
  border: none;
  border-top: 1px solid #ccc;
  margin: 24px 0;
}
.biography-item {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  width: 100%;
  gap: 24px;
  padding: 0 10%;
  transition: background 0.3s;
}
.base {
  width: 200px;
  font-size: 20px;
  font-weight: 500;
  color: #333;
  line-height: 1.2;
  transition: color 0.3s;
}
.primary {
  flex: 1;
  font-size: 14px;
  color: #555;
  line-height: 1.6;
  max-height: calc(1.6em * 4);
  overflow: hidden;
  transition: max-height 0.5s;
}
.bdate {
  width: 160px;
  text-align: right;
  font-size: 16px;
  color: #777;
}
.biography-item:hover .primary {
  max-height: 100vh;
}
.biography-item:hover .base {
  color: #000;
}
</style>
