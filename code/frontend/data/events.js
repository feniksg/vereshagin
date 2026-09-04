// src/data/events.js

export const events = [
  {
    id: 1,
    date: '1 янв. 2024',
    title: 'Выставка М.Ведясовой «Однажды зимой»',
    cover: '/img/landing/img/news/news1.png',
    category: 'Выставка',
    status: 'Прошло',
    description: 'В экспозиции каменного дома-музея Верещагиных открыта выставка «Однажды зимой». Здесь представлены работы вологодской художницы и педагога Марии Ведясовой.',
    location: 'Каменный дом-музей Верещагиных',
    price: { adult: 200, pension: 180, child: 160 },
    contact: { phone: '+7 (8202) 49-33-16', address: 'г. Череповец, Советский пр., 30 А' },
    gallery: [
      '/img/landing/img/news/news1.png',
      '/img/landing/img/news/news2.png'
    ]
  },
  {
    id: 2,
    date: '14 фев. 2024',
    title: 'Конференция «Искусство и история»',
    cover: '/img/landing/img/news/news2.png',
    category: 'Конференция',
    status: 'Будет',
    description: 'Международная конференция историков искусства. Обсуждение новых исследований и находок в области русского и зарубежного искусства.',
    location: 'ЧГУ, аудитория 205',
    price: { adult: 0, pension: 0, child: 0 },
    contact: { phone: '+7 (8202) 55-65-97', address: 'Пр-т Луначарского, 5, Череповец' },
    gallery: [
      '/img/landing/img/news/news2.png',
      '/img/landing/img/news/news3.png'
    ]
  },
  {
    id: 3,
    date: '25 окт. 2023',
    title: 'Программа «Сказка ложь, но в ней намёк»',
    cover: '/img/landing/img/news/news3.png',
    category: 'Программа',
    status: 'Идёт',
    description: 'Интерактивная семейная программа по мотивам народных сказок. Участники перевоплощаются в героев и решают загадки.',
    location: 'Дом-музей Верещагиных',
    price: { adult: 150, pension: 120, child: 100 },
    contact: { phone: '+7 (8202) 49-33-16', address: 'ул. Социалистическая, 22' },
    gallery: [
      '/img/landing/img/news/news3.png',
      '/img/landing/img/news/news4.png'
    ]
  },
  {
    id: 4,
    date: '1 авг. 2022',
    title: 'Программа к 180-летию Василия Верещагина',
    cover: '/img/landing/img/news/news4.png',
    category: 'Программа',
    status: 'Прошло',
    description: 'Юбилейная программа включала фестиваль стрит-арта, открытие новой экспозиции и экскурсии по музее.',
    location: 'Каменный дом-музей',
    price: { adult: 250, pension: 200, child: 150 },
    contact: { phone: '+7 (8202) 49-33-26', address: 'ул. Социалистическая, 28' },
    gallery: [
      '/img/landing/img/news/news4.png',
      '/img/landing/img/news/news5.png'
    ]
  },
  {
    id: 5,
    date: '5 мар. 2024',
    title: 'Выставки современной графики',
    cover: '/img/landing/img/news/news5.png',
    category: 'Выставка',
    status: 'Будет',
    description: 'Первая в Череповце выставка работ современных графиков из разных регионов России.',
    location: 'Галерея «Верещагин»',
    price: { adult: 180, pension: 140, child: 120 },
    contact: { phone: '+7 (8202) 55-65-97', address: 'Пр-т Луначарского, 5' },
    gallery: [
      '/img/landing/img/news/news5.png',
      '/img/landing/img/news/news6.png'
    ]
  },
  {
    id: 6,
    date: '20 нояб. 2022',
    title: 'Мастер-классы по созданию народных кукол',
    cover: '/img/landing/img/news/news6.png',
    category: 'Программа',
    status: 'Прошло',
    description: 'Практические занятия по изготовлению традиционных кукол-оберегов из ткани и ниток.',
    location: 'Дом ремёсел',
    price: { adult: 300, pension: 250, child: 200 },
    contact: { phone: '+7 (8202) 49-33-16', address: 'ул. Социалистическая, 22' },
    gallery: [
      '/img/landing/img/news/news6.png',
      '/img/landing/img/news/news1.png'
    ]
  },
  {
    id: 7,
    date: '10 мар. 2023',
    title: 'Выставка «Краски Азии»',
    cover: '/img/landing/img/news/news1.png',
    category: 'Выставка',
    status: 'Прошло',
    description: 'Коллекция восточных пейзажей и портретов из частных собраний.',
    location: 'Каменный дом-музей',
    price: { adult: 220, pension: 180, child: 140 },
    contact: { phone: '+7 (8202) 49-33-26', address: 'ул. Социалистическая, 28' },
    gallery: [
      '/img/landing/img/news/news1.png',
      '/img/landing/img/news/news2.png'
    ]
  },
  {
    id: 8,
    date: '30 апр. 2023',
    title: 'Конференция по реставрации картин',
    cover: '/img/landing/img/news/news2.png',
    category: 'Конференция',
    status: 'Идёт',
    description: 'Специалисты со всей страны обсуждают современные методы реставрации живописи.',
    location: 'ЧГУ, Малый зал',
    price: { adult: 0, pension: 0, child: 0 },
    contact: { phone: '+7 (8202) 55-65-97', address: 'Пр-т Луначарского, 5' },
    gallery: [
      '/img/landing/img/news/news2.png',
      '/img/landing/img/news/news3.png'
    ]
  },
  {
    id: 9,
    date: '12 июн. 2023',
    title: 'Лекция «История костюма»',
    cover: '/img/landing/img/news/news3.png',
    category: 'Программа',
    status: 'Будет',
    description: 'Лекция о традиционном русском костюме и символике орнаментов.',
    location: 'Дом-музей Верещагиных',
    price: { adult: 120, pension: 100, child: 80 },
    contact: { phone: '+7 (8202) 49-33-16', address: 'ул. Социалистическая, 22' },
    gallery: [
      '/img/landing/img/news/news3.png',
      '/img/landing/img/news/news4.png'
    ]
  },
  {
    id: 10,
    date: '7 авг. 2023',
    title: 'Выставка «Пленэр в Череповце»',
    cover: '/img/landing/img/news/news4.png',
    category: 'Выставка',
    status: 'Будет',
    description: 'Работы участников пленэра на берегах Шексны и Вологды.',
    location: 'Галерея «Верещагин»',
    price: { adult: 200, pension: 160, child: 120 },
    contact: { phone: '+7 (8202) 55-65-97', address: 'Пр-т Луначарского, 5' },
    gallery: [
      '/img/landing/img/news/news4.png',
      '/img/landing/img/news/news5.png'
    ]
  },
  {
    id: 11,
    date: '21 сен. 2023',
    title: 'Семинар живописи маслом',
    cover: '/img/landing/img/news/news5.png',
    category: 'Программа',
    status: 'Идёт',
    description: 'Практический семинар для начинающих художников по масляной живописи.',
    location: 'Дом ремёсел',
    price: { adult: 350, pension: 300, child: 250 },
    contact: { phone: '+7 (8202) 49-33-26', address: 'ул. Социалистическая, 28' },
    gallery: [
      '/img/landing/img/news/news5.png',
      '/img/landing/img/news/news6.png'
    ]
  },
  {
    id: 12,
    date: '2 дек. 2023',
    title: 'Конференция искусствоведов',
    cover: '/img/landing/img/news/news6.png',
    category: 'Конференция',
    status: 'Будет',
    description: 'Ключевые доклады по новейшим исследованиям в области искусства.',
    location: 'ЧГУ, Большой зал',
    price: { adult: 0, pension: 0, child: 0 },
    contact: { phone: '+7 (8202) 55-65-97', address: 'Пр-т Луначарского, 5' },
    gallery: [
      '/img/landing/img/news/news6.png',
      '/img/landing/img/news/news1.png'
    ]
  }
]
