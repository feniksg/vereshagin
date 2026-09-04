<script setup lang="ts">
import { ChevronDown } from 'lucide-vue-next';
    import { ref, onMounted } from 'vue'
    import { useRouter } from 'vue-router'

    const router = useRouter()
    const isAuthenticated = ref(false)

    onMounted(() => {
    isAuthenticated.value = !!localStorage.getItem('token')
    })

    const goToAuth = (mode: 'login' | 'register') => {
    router.push(`/auth?mode=${mode}`)
    }
</script>

<template>
  <div class="header">
    <div class="header-container">
      <NuxtLink to="/" class="logo">
        <img src="@/assets/img/landing/img/logo.png" alt="logo" />
      </NuxtLink>

      <nav>
        <ul class="topmenu">
          <!-- Медиа -->
          <li>
            <div class="item-topmenu">
              <NuxtLink to="/media" class="item-menu">Медиа</NuxtLink>
              <ChevronDown class="submenu-icon"/>
            </div>
            <ul class="submenu">
              <li><NuxtLink to="/media">Все</NuxtLink></li>
              <li>
                <NuxtLink
                  :to="{ path: '/media', query: { cat: 'Конференция' } }"
                >Конференции</NuxtLink>
              </li>
              <li>
                <NuxtLink
                  :to="{ path: '/media', query: { cat: 'Программа' } }"
                >Программы</NuxtLink>
              </li>
              <li>
                <NuxtLink
                  :to="{ path: '/media', query: { cat: 'Выставка' } }"
                >Выставки</NuxtLink>
              </li>
            </ul>
          </li>

          <!-- Основное -->
          <li>
            <div class="item-topmenu">
              <NuxtLink to="/base" class="item-menu">Основное</NuxtLink>
              <ChevronDown class="submenu-icon"/>
            </div>
            <ul class="submenu">
              <li><NuxtLink to="/biography">Биография</NuxtLink></li>
              <li><NuxtLink to="/familyTree">Семейное древо</NuxtLink></li>
              <li>
                <!-- переходим сразу в архив изображений, фильтр «Живопись» = category=1 -->
                <NuxtLink
                  :to="{ path: '/imageArchive', query: { category: 1 } }"
                >Живопись</NuxtLink>
              </li>
              <li>
                <!-- фильтр «Графика» = category=2 -->
                <NuxtLink
                  :to="{ path: '/imageArchive', query: { category: 2 } }"
                >Графика</NuxtLink>
              </li>
              <li>
                <!-- текстовый архив в раздел «Книги» -->
                <NuxtLink to="/books">Книги</NuxtLink>
              </li>
            </ul>
          </li>

          <!-- Архив -->
          <li>
            <div class="item-topmenu">
              <NuxtLink to="/archive" class="item-menu">Архив</NuxtLink>
              <ChevronDown class="submenu-icon"/>
            </div>
            <ul class="submenu">
              <li><NuxtLink to="/imageArchive">Архив изображений</NuxtLink></li>
              <li><NuxtLink to="/textArchive">Архив текстов</NuxtLink></li>
            </ul>
          </li>

          <!-- Игры -->
          <li>
            <NuxtLink to="/games" class="item-menu">Игры</NuxtLink>
          </li>
        </ul>
      </nav>

      <!-- Пользователь -->
      <div v-if="isAuthenticated" class="user">
        <NuxtLink to="/profile">
          <img src="@/assets/img/landing/svg/user.svg" alt="user" />
        </NuxtLink>
      </div>

      <!-- Логин / Регистрация -->
      <div v-else class="login">
        <a class="login_button" @click="goToAuth('login')">Вход</a>
        <button class="reg_button" @click="goToAuth('register')">
          Регистрация
        </button>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
    .logo {
        img {
            box-sizing:unset;
        }
    }
    a {
        text-decoration: none;
        color: inherit;
    }
    li {
        list-style: none;
    }
    ul {
        padding: 0;
        margin: 0;
    }
    .header{
        height: 100%;
        display: flex;
        justify-content: center;
        width: 100%;
        background-color: var(--color-background);
        z-index: 10;
        .header-container{
            width: 90%;
            display: flex;
            align-items: center;
            padding: 0.5rem;
            justify-content: space-between;
            max-width: 1440px;
        }
        .user{
            display: flex;
            align-items: center;
            img {
                height: 40px;
                width: 40px;
            }
        }
        .topmenu {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin: 0 15%;
            gap: 1.5rem;
            margin: 0;
            li:hover > .submenu {
                visibility: visible;
                opacity: 1;
            }
            li{
                &:hover {
                    .submenu-icon {
                        transform: rotate(180deg);
                    }
                }
            }
        }
        .item-topmenu {
            display: flex;
            align-items: center;
            margin-right: 65px;
            cursor: pointer;
            
        }
        .submenu-icon {
            transition: transform 0.3s ease;
        }
        .item-menu {
            margin: 0 10px;
        }
        .item-menu:last-child{
            margin-left: 2.5rem;
        }
        .submenu {
            position: absolute;       
            z-index: 11;
            transition: .3s linear;
            visibility: hidden;
            opacity: 0;
            margin-left: -70px;
            background-color: #fff;
            border-radius: 10px;
            margin-top: 10px;
            a {
                padding: 20px 57px;
                text-align: center;
                display: block;
                &:hover {
                    background-color: #f2f2f2;
                }
            }
        }
        nav {
            display: flex;
            justify-content: center;
            border-radius: 30px;
            width: max-content;
            cursor: pointer;
            font-style: normal;
            text-decoration: none;
            &:visited{
                color: inherit;
            }
            h2{
                margin: 0 3%;
                font-weight: 400;
                font-size: 20px;
                line-height: 24px;
            }
        }
        /*.menu {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin: 0 15%;
            width: 45%;
            .nav-button {
                white-space: nowrap;
                display: flex;
                justify-content: center;
                width: 33%;
                cursor: pointer;
                font-style: normal;
                text-decoration: none;
                &:visited{
                    color: inherit;
                }
                h2{
                    margin: 0 3%;
                    font-weight: 400;
                    font-size: 20px;
                    line-height: 24px;
                }
            }
        }*/
        .login_button {
            padding: 14px 20px;
            line-height: 10px;
            margin-right: 22px;
            margin-left: -150px;
            color: #483E34;
            cursor: pointer;
        }
        .reg_button {
            padding: 14px 20px;
            font-size: 16px;
            text-align: center;
            line-height: 14px;
            background-color: #ffffff;
            color: #483E34;
            border: 1px solid #483E34;
            border-radius: 10px;
            cursor: pointer;
            
            &:hover{
                background-color: #000000;
                color: #ffffff;
                border: 1px solid; 
            }
            a:hover{
                color: #ffffff;
            }
        }
    }
</style>