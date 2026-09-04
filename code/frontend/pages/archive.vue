<template>
    <section>
        <div class="archive-title">
            <img class="bg-header" src="@/assets/img/landing/img/header-archive.png" alt="">
            <h1 class="header-title">Архив</h1>
        </div>

        <div class="change-archive-container">
            <a href="/textArchive" class="text-archive-container">
                <img src="@/assets/img/landing/img/archive-block.png" alt="" class="block-text-archive-background"/>
                <h2>Архив текстов</h2>
            </a>
            <a href="/imageArchive" class="image-archive-container">
                <img src="@/assets/img/landing/img/archive-block.png" alt="" class="block-image-archive-background"/>
                <h2>Архив изображений</h2>
            </a>
        </div>
    </section>
</template>

<script setup>

</script>

<style lang="scss" scoped>
    .archive-title{
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

    .change-archive-container {
        background-color: #292727;
        padding-block-start: 50px;
        padding-block-end: 150px;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 15%;
    }

    .text-archive-container,
    .image-archive-container {
        position: relative;
        width: 300px;
        height: 200px;
        border-radius: 20px;
        overflow: hidden;
        display: flex;
        justify-content: center;
        align-items: center;
        box-shadow: inset 0 0 50px rgba(0, 0, 0, 1); // виньетка
        transition: transform 0.3s ease, filter 0.3s ease;
    }

    .block-text-archive-background,
    .block-image-archive-background {
        position: absolute;
        top: 0;
        left: 0;
        width: 150%;
        height: 100%;
        object-fit: cover;
        transition: filter 0.3s ease;
    }

    .text-archive-container h2,
    .image-archive-container h2 {
        position: relative;
        font-size: 24px;
        text-align: center;
        z-index: 2;
        transition: color 0.3s ease;
    }

    .text-archive-container:hover,
    .image-archive-container:hover {
        transform: scale(1.05);
    }

    .text-archive-container:hover .block-text-archive-background,
    .image-archive-container:hover .block-image-archive-background {
        filter: brightness(0.5);
    }

    .text-archive-container:hover h2,
    .image-archive-container:hover h2 {
        color: #fff;
        filter: brightness(1.2);
    }

</style>