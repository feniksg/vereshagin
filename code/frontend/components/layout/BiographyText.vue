<template>
    <div class="item-biography-container">
        <div class="biography-title">
            <div class="title">
                <h1>{{ title }}</h1>
            </div>

            <div class="year">
                <h2>{{ year }}</h2>
            </div>
        </div>
        <div class="text">
            <p>{{ text }}</p>
        </div>
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
    year: {
        type: String,
        default: 'год-год гг.',
        required: true,
    },
    text: {
        type: String,
        default: 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a,',
        required: true,
    },
});
</script>

<style lang="scss" scoped>
.item-biography-container{
    display: flex;
    justify-content: space-between;
    gap: 10%;
    padding-inline: 150px;
    padding-block: 50px;

    .biography-title {
        display: flex;
        flex-direction: column;
        gap: 20px;
        min-width: 50%;
        max-width: 50%;
    }
    .text {
        width: 45%;
        font-size: 16px;
        white-space: pre-wrap;
    }
}
</style>