<template>
    <div class="card-text">
        <img class="text-book-image" :src="image" alt="Book" @contextmenu.prevent>
        <div class="text-book-info">
            <h3 class="text-book-title">{{ title }}</h3>
            <p class="author">{{ author }}</p>
            <p class="year">{{ year }}</p>
        </div>
    </div>
</template>

<script setup>
defineProps({
    image: String,
    title: String,
    author: String,
    year: String,
});
</script>

<style lang="scss" scoped>
    .card-text {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        gap: 10px;
        color:#000;
        cursor: pointer;
        max-width: 350px;
        .text-book-image {
            max-width: 350px;
        }
        .text-book-info {
            display: flex;
            flex-direction: column;
            gap: 10px;
            .text-book-title {
                font-weight: 500;
                font-size: 20px;
                padding: 10px 0;
                margin: 0;
            }
            .author {
                font-weight: 400;
                font-size: 20px;
                opacity: 0.6;
                margin: 20px 0 0 0;
            }
            .year {
                font-weight: 400;
                font-size: 16px;
                margin: 10px 0 0 0;
            }
        }
         &:hover {
            transform: scale(1.05);
        }
    }
    
</style>