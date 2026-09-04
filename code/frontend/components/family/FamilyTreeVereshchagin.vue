<template>
  <div class="family-tree-container" ref="treeContainer">
    <!-- Canvas, рисующий все соединения -->
    <ConnectionLines :connections="allConnections" />

    <!-- generation-0 (верхняя строка) -->
    <div class="generation generation-0">
      <PersonCard
        v-for="person in generation0"
        :key="person.id"
        :person="person"
        :data-person-id="person.id"
      />
    </div>

    <!-- generation-1 (вторая строка) -->
    <div class="generation generation-1">
      <PersonCard
        v-for="person in generation1"
        :key="person.id"
        :person="person"
        :data-person-id="person.id"
      />
    </div>

    <!-- generation-main (центральная пара) -->
    <div class="generation generation-main">
      <PersonCard
        :person="mainMale"
        :data-person-id="mainMale.id"
      />
      <PersonCard
        :person="mainFemale"
        :data-person-id="mainFemale.id"
      />
    </div>

    <!-- generation-2 (третья строка) -->
    <div class="generation generation-2">
      <PersonCard
        v-for="person in generation2"
        :key="person.id"
        :person="person"
        :data-person-id="person.id"
      />
    </div>

    <!-- generation-3 (нижний единственный) -->
    <div class="generation generation-3">
      <PersonCard
        :person="generation3"
        :data-person-id="generation3.id"
      />
    </div>
  </div>
</template>

<script setup>
import PersonCard from './PersonCard.vue'
import ConnectionLines from './ConnectionLines.vue'

// ============ ДАННЫЕ ДЛЯ КАРТОЧЕК (дополнили dateFrom, dateTo, description) ============
const generation0 = [
  {
    id: 1,
    fullName: 'Анна Николаевна Верещагина',
    photo: 'annanicolaevnavereshagina.png',
    gender: 'female',
    dateFrom: '1819',
    dateTo: '1881',
    description: 'Русская дворянка, мать художника'
  },
  {
    id: 2,
    fullName: 'Василий Васильевич Верещагин',
    photo: 'vasiliyvasilevichvereshagin.png',
    gender: 'male',
    dateFrom: '1842',
    dateTo: '1904',
    description: 'Русский живописец, писатель, один из самых известных баталистов второй половины XIX века'
  }
]

const generation1 = [
  {
    id: 3,
    fullName: 'Мария Васильевна Верещагина',
    photo: null,
    gender: 'female',
    dateFrom: '1845',
    dateTo: '1897',
    description: 'Первая дочь художника; умерла от болезни в детстве'
  },
  {
    id: 4,
    fullName: 'Алексей Васильевич Верещагин',
    photo: null,
    gender: 'male',
    dateFrom: '1849',
    dateTo: null,
    description: 'Сын художника; сведений мало'
  },
  {
    id: 5,
    fullName: 'Михаил Васильевич Верещагин',
    photo: null,
    gender: 'male',
    dateFrom: '1846',
    dateTo: '1922',
    description: 'Сын художника, служил в армии, позже занимался литературой'
  },
  {
    id: 6,
    fullName: 'Николай Васильевич Верещагин',
    photo: 'nicolayvasilevichvereshagin.png',
    gender: 'male',
    dateFrom: '1842',
    dateTo: '1885',
    description: 'Сын, служил в Русской армии'
  },
  {
    id: 7,
    fullName: 'Сергей Васильевич Верещагин',
    photo: 'sergeyvasilevichvereshagin.png',
    gender: 'male',
    dateFrom: '1848',
    dateTo: '1892',
    description: 'Сын художника, жил в Санкт-Петербурге'
  },
  {
    id: 8,
    fullName: 'Александр Васильевич Верещагин',
    photo: 'aleksandrvasilevichvereshagin.png',
    gender: 'male',
    dateFrom: '1850',
    dateTo: '1909',
    description: 'Сын художника, русский генерал-лейтенант, писатель'
  }
]

const mainMale = {
  id: 9,
  fullName: 'Василий Васильевич Верещагин',
  photo: 'vasiliyvasilevichvereshagin(1).png',
  gender: 'male',
  dateFrom: '1842',
  dateTo: '1904',
  description: 'Русский живописец, писатель, один из самых известных баталистов второй половины XIX века'
}

const mainFemale = {
  id: 10,
  fullName: 'Лидия Васильевна Андреевская',
  photo: 'lidiavasilevnaandreevskaya.png',
  gender: 'female',
  dateFrom: '1865',
  dateTo: '1911',
  description: 'Вторая жена художника, талантливая пианистка'
}

const generation2 = [
  {
    id: 11,
    fullName: 'Лидия Васильевна Верещагина',
    photo: null,
    gender: 'female',
    dateFrom: '1892',
    dateTo: '1982',
    description: 'Мемуаристка; жила в Чехии. В 1970 году в Карловых Варах подготовила книгу воспоминаний об отце'
  },
  {
    id: 12,
    fullName: 'Лидия Васильевна Верещагина',
    photo: 'lidiavasilevnavereshagina.png',
    gender: 'female',
    dateFrom: '1898',
    dateTo: '1930',
    description: 'Дочь художника; скончалась после родов'
  },
  {
    id: 13,
    fullName: 'Василий Васильевич Верещагин',
    photo: 'vasiliyvasilevichvereshagin(2).png',
    gender: 'male',
    dateFrom: '1893',
    dateTo: '1975',
    description: 'Сын художника, служил морским офицером'
  },
  {
    id: 14,
    fullName: 'Анна Васильевна Верещагина',
    photo: 'annavasilevichvereshagin.png',
    gender: 'female',
    dateFrom: '1894',
    dateTo: '1919',
    description: 'Дочь художника; до конца неизвестна её судьба (предполагают, что умерла во время Гражданской войны от тифа)'
  }
]

const generation3 = {
  id: 15,
  fullName: 'Александр Сергеевич Плевако',
  photo: 'aleksandrsergeevichplevako.png',
  gender: 'male',
  dateFrom: '1930',
  dateTo: '2021',
  description: 'Единственный внук художника. Был усыновлён Сергеем Фёдоровичем Плевако, юрист, писатель'
}

// ============ Connection-списки ============
const connectionsLevel0 = [
  { from: 1, to: 3 },
  { from: 1, to: 4 },
  { from: 1, to: 5 },
  { from: 2, to: 6 },
  { from: 2, to: 7 },
  { from: 2, to: 8 },
  { from: 1, to: 9 },
  { from: 2, to: 9 }
]

const connectionsMain = [
  { from: 9, to: 11 },
  { from: 9, to: 12 },
  { from: 9, to: 13 },
  { from: 9, to: 14 },
  { from: 10, to: 11 },
  { from: 10, to: 12 },
  { from: 10, to: 13 },
  { from: 10, to: 14 }
]

const connectionsLevel2 = [
  { from: 12, to: 15 }
]

// Объединяем все три массива в один
const allConnections = [
  ...connectionsLevel0,
  ...connectionsMain,
  ...connectionsLevel2
]
</script>

<style scoped>
.family-tree-container {
  position: relative;
  width: 100%;
  height: 1700px; /* при необходимости скорректируйте высоту */
  /* background-color: #f6f4f0; */
}

/* ------------------------------------ */
/* Абсолютное позиционирование «поколений» */
/* ------------------------------------ */
.generation {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  align-items: flex-start;
  z-index: 2; /* поверх Canvas */
}

/* generation-0 (верхняя строка) */
.generation-0 {
  top: 20px;
  gap: 60px;
}

/* generation-1 (вторая строка) */
.generation-1 {
  top: 320px;
  justify-content: space-between;
  width: 80%;
}

/* generation-main (центральная пара) */
.generation-main {
  top: 620px;
  gap: 100px;
}

/* generation-2 (третья строка) */
.generation-2 {
  top: 980px;
  justify-content: space-between;
  width: 60%;
}

/* generation-3 (нижний единственный) */
.generation-3 {
  top: 1250px;
}
</style>
