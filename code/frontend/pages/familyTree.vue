<template>
  <section class="family-tree-page">
    <h1 class="family-tree-title">Семейное древо</h1>
    <FamilyTreeVereshchagin />
  </section>
</template>

<script setup>
import FamilyTreeVereshchagin from '@/components/family/FamilyTreeVereshchagin.vue'
</script>

<style scoped>
.family-tree-page {
  text-align: center;
  padding: 40px 0;
  background: url('/img/landing/img/family/back.png') center/cover no-repeat;
}
.family-tree-title {
  font-family: 'Playfair Display', serif;
  font-size: 32px;
  margin-bottom: 24px;
}
</style>
