<template>
    <div class="categories-text">
        <h2 class="category-title">{{ title }}</h2>
        <img :src="icon" alt="Icon" class="category-icon" @contextmenu.prevent/>
    </div>
</template>

<script setup>
defineProps({
    title: {
        type: String,
        required: true,
    },
    icon: {
        type: String,
        required: true,
    },
});
</script>

<style lang="scss" scoped>
    .categories-text {
        width: 190px;
        height: 190px;
        background-color: #EDE9DF;
        border-radius: 10px;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 15px;
        text-align: center;
        padding: 25px;
        cursor: pointer;
        &:hover {
            background-color: #D5CBB3;
        }
        &:active {
            background-color: #D5CBB3;
        }
    }
    .categories-title {
        font-weight: 500;
    }
    .categories-icon {
        height: 80px;
        pointer-events: none;
    }
</style>