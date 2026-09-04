<template>
    <div class="container">
        <h1>{{ title }}</h1>
        <p>Страница в разработке...</p>
    </div>
</template>

<script setup>
import { defineProps } from 'vue';


const props = defineProps({
    title: {
        type: String,
        default: 'Заголовок',
        required: true,
    },
});
</script>

<style lang="scss" scoped>
    .container {
        width: 100vw;
        height: 50vh;
        background-color: antiquewhite;
        margin-block: 20px;
        
        h1 {
            margin-bottom: 20px;
        }

        p {
            text-align: center;
        }
    }
</style>

