<template>
    <section>
        <div class="title-text-archive">
            <div class="text-archive">
                <img class="bg-header" src="@/assets/img/landing/img/header-archive.png" alt="">
                <h1 class="header-title">Архив текстов</h1>
            </div>
        </div>
        <div class="filters">
            <div class=input-group>
                <input v-model="search" type="text" class="search" placeholder="Поиск" />
                <div class="filter-period">
                    <h2>Период</h2>
                    <div class="input-dates">
                        <input v-model.number="from" type="number" class="search-date" placeholder="с" />
                        <input v-model.number="to" type="number" class="search-date" placeholder="по" />
                    </div>
                </div>
            </div>
            <div class="categories">
                <CategoriesText title="Воспоминания" :icon="iconMemoirs" />
                <CategoriesText title="Библиография" :icon="iconBibliography" />
                <CategoriesText title="Произведения" :icon="iconWorks" />
                <CategoriesText title="Конференции" :icon="iconConferences" />
                <CategoriesText title="Книги" :icon="iconBooks" />
                <CategoriesText title="Документы" :icon="iconDocuments" />
                <CategoriesText title="Научные труды" :icon="iconScientificPapers" />
                <CategoriesText title="Выставки" :icon="iconExhibitions" />
            </div>
        </div>
        <div class="cards-books">
            <div class="cards-list">
                <NuxtLink
                    v-for="book in filteredBooks"
                    :key="book.id"
                    :to="`/books/${book.id}`"
                >
                    <CardText :image="book.photo" :title="book.title" :author="book.author" :year="book.year" />
                </NuxtLink>
            </div>
            <div class="cards-list-navigation">
                <img src="@/assets/img/landing/svg/arr-left.svg" alt="Back" class="arr-left"/>
                <div class="page-number">
                    <span style="font-weight: 700">1</span>
                    <span>2</span>
                    <span>3</span>
                    <span>4</span>
                    <span>5</span>
                </div>
                <img src="@/assets/img/landing/svg/arr-right.svg" alt="Forward" class="arr-right"/>
            </div>
        </div>
    </section>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'
import CategoriesText from '@/components/layout/CategoriesText.vue'
import CardText from '@/components/layout/CardText.vue'

import iconMemoirs from '@/assets/img/landing/svg/categories-text/memoirs.svg';
import iconBibliography from '@/assets/img/landing/svg/categories-text/bibliography.svg';
import iconWorks from '@/assets/img/landing/svg/categories-text/works.svg';
import iconConferences from '@/assets/img/landing/svg/categories-text/conferences.svg';
import iconDocuments from '@/assets/img/landing/svg/categories-text/documents.svg';
import iconScientificPapers from '@/assets/img/landing/svg/categories-text/scientific-papers.svg';
import iconExhibitions from '@/assets/img/landing/svg/categories-text/exhibitions.svg';
import iconBooks from '@/assets/img/landing/svg/categories-text/books.svg'

const API_URL = 'http://localhost:8000'

const books = ref([])

const search = ref('')
const from = ref('')
const to = ref('')

async function fetchBooks() {
  try {
    const { data } = await axios.get(`${API_URL}/api/v1/books`)
    books.value = data.results
  } catch (e) {
    console.error('Ошибка загрузки книг', e)
  }
}

onMounted(fetchBooks)

const filteredBooks = computed(() => {
  return books.value.filter(b => {
    const year = Number(b.year)
    const matchSearch = b.title.toLowerCase().includes(search.value.toLowerCase()) ||
      b.author.toLowerCase().includes(search.value.toLowerCase())
    const matchFrom = !from.value || year >= from.value
    const matchTo = !to.value || year <= to.value
    return matchSearch && matchFrom && matchTo
  })
})
</script>

<style lang="scss" scoped>
    .text-archive{
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: -43px;
        margin-bottom: 64px;
        .bg-header{
            width: 100vw;
            position: relative;
            z-index: -1;
            max-width: var(--max-width);
        }

        .header-title{
            position: absolute;
        }
    }
    .filters{
        display: flex;
        justify-content: center;
        padding: 0 150px;
        gap: 25px;

        .input-group{
            width: auto;
            display: flex;
            flex-direction: column;
            gap: 40px;
            
            input {
                background: #E3E3E2;
                border-radius: 5px;
                padding: 10px;
                border: none;
                &:focus{
                    outline: none;
                }
            }
            .input-dates{
                display: flex;
                gap: 25px;
            }
            .search{
                width: 265px;
            }
            h2 {
                font-weight: 700;
                padding: 20px;
                margin: 0;
            }
            .search-date{
                width: 96px;
            }
        }
        .categories{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
        }
    }
    .cards-list{
        display: grid;
        justify-content: center;
        justify-items: center;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 40px;
        padding: 50px 150px;
        margin-bottom: 50px;
    }
    .cards-list-navigation{
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 20px;
        padding: 0 150px;

        .arr-left, .arr-right{
            cursor: pointer;
        }
        .page-number{
            display: flex;
            span{
                padding: 20px;
                font-size: 20px;
                font-weight: 400;
                cursor: pointer;
            }
        }
    }
</style>