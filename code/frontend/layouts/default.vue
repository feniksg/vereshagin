<script lang="ts" setup>

</script>

<template>
    <section class="flex" style="min-height: 100vh;">
        <LayoutHeader/>
        <div class="content">
            <slot/>
        </div>
        <LayoutFooter/>
    </section>
</template>

<style scoped>
    .flex{
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-direction: column;
    }
    .content{
        flex: 1;
        width: 100vw;
    }
</style>

