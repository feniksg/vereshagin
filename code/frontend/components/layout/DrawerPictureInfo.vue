
<template>
    <div>
        <img class="open-icon" @click="openDrawer" src="@/assets/img/landing/svg/arr-right-wbg.svg" alt="Подробная информация" @contextmenu.prevent/>
        <!-- <button @click="openDrawer">Открыть Drawer</button> -->
        <div class="drawer-picture-info" :class="{open: isOpen}">
            <div class="text_full_info">
                <h1>{{ title }}</h1>
                <h2 class="year-and-size">{{ year_and_size }}</h2>
                <p v-html="formattedText"></p>
                <button @click="closeDrawer">Закрыть</button>
            </div>
        </div>
    </div>
</template>

<script setup>
    import {ref, onMounted, computed } from 'vue';
    const props = defineProps({
        height: Number,
        title: String,
        year_and_size: String,
        text: String
    })

    const drawerHeight=ref(0)
    const isOpen = ref(false)

    const formattedText = computed(() => {
        return props.text.replace(/\n/g, '<br>')
    })

    onMounted(() => {
        drawerHeight.value=props.height
    })

    const openDrawer = () => {
        isOpen.value=true;
    }

    const closeDrawer = () => {
        isOpen.value=false;
    }
</script>

<style scoped>
    .drawer-picture-info {
        position:fixed;
        top:0;
        left: -50%;
        height: drawerHeight + 'px';
        background-image: url('@/assets/img/landing/img/bg-info-picture.png');
        width: 50%;
        background-size: cover;
        background-position: center;
        overflow: auto;
        display: flex;
        align-items: center;
        z-index: 5;
    }
    .drawer-picture-info.open {
        left: 0;
    }
    .text_full_info {
        width: 85%;
        padding: 130px 100px;
        text-align: center;
    }
    .text_full_info p {
        padding: 20px;
        text-align: justify;
    }
    .year-and-size {
        padding-top: 50px;
        margin-top: 0px;
        margin-bottom: 80px;
    }
    button {
        margin-top: 30px;
    }
    .open-icon {
        position: fixed;
        bottom: 20px;
        left: 20px;
        z-index: 4;
        border-radius: 10px;
        box-shadow: 0px 0px 3px 0px black;
    }
</style>