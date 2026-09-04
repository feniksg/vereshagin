<template>
    <div class="slider-container">
        <div class="slider">
            <button @click="prevSlide">Назад</button>
            <div class="slides" :style="{transform: `translateX(-${currentSlide * 100}%)`}">
                <div class="slide" v-for="(slide, index) in slides" :key="index">
                    <img :src="slide.image" :alt="slide.alt" />
                </div>
            </div>
            <div class="caption"><h2>{{ currentCaption }}</h2></div>
            <button @click="nextSlide">Вперед</button>
        </div>
    </div>
</template>

<script setup>
    import { ref, computed } from 'vue';

    const currentSlide=ref(0);
    const slides = [
        {image: "images/1.png", alt: 'Slide 1', caption: 'Название картины 1'},
        {image: "images/2.png", alt: 'Slide 2', caption: 'Название картины 2'},
        // {image: "images/3.png", alt: 'Slide 3', caption: 'Название картины 3'},
    ];

    const currentCaption = computed(() => slides[currentSlide.value].caption);

    const prevSlide = () => {
        currentSlide.value = (currentSlide.value - 1 + slides.length) % slides.length;
    };

    const nextSlide = () => {
        currentSlide.value = (currentSlide.value + 1) % slides.length;
    };
</script>


<style scoped>
    .slider-container {
        background: #fff;
        padding: 70px 150px;
    }
    .slider {
        position: relative;
        overflow: hidden;
        width: 100%;
        max-width: 600px;
        max-height: 600px;
        margin-inline: auto;
    }

    .slides {
        display: flex;
        transition: transform 0.5s ease;
    }

    .slide {
        min-width: 100%;
        justify-content: center;
        align-items: center;
    }

    img {
        width: 100%;
        display: block;
    }

    .caption {
        text-align: center;
        margin-top: 10px;
        font-size: 1.2em;
    }
</style>