<template>
  <section class="contacts-section">
    <h2>Контакты</h2>
    <div class="contacts">
      <div class="contact" v-for="(item, index) in contacts" :key="index">
        <h3>{{ item.title }}</h3>
        <img :src="item.src" :alt="item.title" />
        <p class="address">{{ item.address }}</p>
        <p v-if="item.phone">{{ item.phone }}</p>
        <p v-if="item.email">{{ item.email }}</p>
      </div>
    </div>
  </section>
</template>

<script setup>
const props = defineProps({
  contacts: { type: Array, default: () => [] }
})
</script>

<style scoped lang="scss">
.contacts-section {
  padding: 60px 20px;
  text-align: center;

  h2 {
    margin-bottom: 40px;
    font-size: 32px;
  }

  .contacts {
    display: flex;
    justify-content: center;
    gap: 40px;

    .contact {
      max-width: 400px;

      h3 {
        margin-bottom: 16px;
        font-size: 24px;
      }

      img {
        width: 100%;
        border-radius: 8px;
        border: 1px solid #ccc;
        margin-bottom: 12px;
      }

      .address {
        font-weight: 500;
      }

      p {
        margin: 4px 0;
      }
    }
  }
}

@media (max-width: 767px) {
  .contacts {
    flex-direction: column;
    gap: 20px;
  }
}
</style>
