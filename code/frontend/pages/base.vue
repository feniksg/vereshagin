<template>
    <section>
        <div class="base-title">
            <img class="bg-header" src="@/assets/img/landing/img/header-archive.png" alt="">
            <h1 class="header-title">Основное</h1>
        </div>

        <div class="change-base-container">
            <a href="/biography" class="block-container">
                <img src="@/assets/img/landing/img/archive-block.png" alt="" class="block-background"/>
                <h2>Биография</h2>
            </a>
            <a href="/familyTree" class="block-container">
                <img src="@/assets/img/landing/img/archive-block.png" alt="" class="block-background"/>
                <h2>Семейное древо</h2>
            </a>
            <a href="/imageArchive" class="block-container">
                <img src="@/assets/img/landing/img/archive-block.png" alt="" class="block-background"/>
                <h2>Живопись</h2>
            </a>
            <a href="/imageArchive" class="block-container">
                <img src="@/assets/img/landing/img/archive-block.png" alt="" class="block-background"/>
                <h2>Графика</h2>
            </a>
            <a href="/textArchive" class="block-container">
                <img src="@/assets/img/landing/img/archive-block.png" alt="" class="block-background"/>
                <h2>Книги</h2>
            </a>
        </div>
    </section>
</template>

<script setup>

</script>

<style lang="scss" scoped>
    .base-title{
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: -70px;
        
        .bg-header{
            width: 100vw;
            position: relative;
            z-index: -1;
            max-width: var(--max-width);
            background: #292727;
        }

        .header-title{
            position: absolute;
        }
    }

    .change-base-container {
        background-color: #292727;
        padding-block-start: 50px;
        padding-block-end: 150px;
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 30px;
        justify-content: center;
        align-items: center;
        justify-items: center;
        max-width: var(--max-width);
        margin: 0 auto;
    }

    .block-container {
        position: relative;
        width: 300px;
        height: 200px;
        border-radius: 20px;
        overflow: hidden;
        display: flex;
        justify-content: center;
        align-items: center;
        box-shadow: inset 0 0 50px rgba(0, 0, 0, 1);
        transition: transform 0.3s ease, filter 0.3s ease;

        &:hover {
            transform: scale(1.05);
        }

        &:hover .block-background {
            filter: brightness(0.5);
        }

        &:hover h2 {
            color: #fff;
        }
    }

    .block-background {
        position: absolute;
        top: 0;
        left: 0;
        width: 150%;
        height: 100%;
        object-fit: cover;
        transition: filter 0.3s ease;
    }

    .block-container h2 {
        position: relative;
        font-size: 24px;
        text-align: center;
        z-index: 2;
        transition: color 0.3s ease;
    }

</style>