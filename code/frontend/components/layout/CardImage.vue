<template>
    <div 
      @mouseover="hover = true" 
      @mouseleave="hover = false" 
      class="card-image"
    >
      <img :src="src" alt="" class="art">
      <div v-if="hover" class="image-shadow"></div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  // Состояние hover
  const hover = ref(false);
  
  // // Импортируем ВСЕ изображения из assets
  // const images = import.meta.glob('@/assets/img/landing/img/*', { eager: true });
  
  const props = defineProps({
    src: String,
  });
  
  // // Вычисляем путь к изображению
  // const resolvedSrc = computed(() => {
  //   if (!props.src) return ''; // Если путь пустой, ничего не рендерим
  
  //   return images[`/assets/${props.src}`]?.default || '';
  // });
  </script>
  
  <style lang="scss" scoped>
  .card-image {
      position: relative;
      display: inline-block; /* Чтобы размеры соответствовали картинке */
  }
  
  .art {
      width: 100%;
      border-radius: 0.5rem;
      display: block; /* Убирает лишние отступы */
  }
  
  .image-shadow {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-color: rgba(0, 0, 0, 0.5);
      border-radius: 10px;
      transition: opacity 0.3s ease-in-out;
  }
  </style>
  