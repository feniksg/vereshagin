<template>
    <section class="text">
        <div class="text-container">
            <div class="text-image-container">
                <img class="text-image" src="@/assets/img/landing/img/text/text-1.png" alt="Text">
            </div>
            <div class="text-inform">
                <div class="title-text">
                    <h1 class="title">Детство и отрочество художника В.В. Верещагина </h1>
                    <h2 class="subtitle">Верещагин В.В., Том 1, 1895. — 315 с.</h2>
                </div>
                <img class="button-inform" @click="toggleDrawer" src="@/assets/img/landing/svg/arr-right.svg" alt="More" @contextmenu.prevent />
            </div>
        </div>
    </section>
    <section class="text-full-info">
        <transition name="drawer">
            <div v-if="isOpen" class="text-full-info-drawer">
                <img class="bg-drawer" src="@/assets/img/landing/img/bg-info-picture.png" alt="BgInfo" @contextmenu.prevent/>
                <div class="text-full-info-container">
                    <div class="text-full-info-text">
                        <p>«Из впечатлений самых первых годов не осталось у меня ничего сознательного; говорили, что я всегда просил у няни: «папки-кокс!» папки – хлеб; кокс – кости, глодать которые я очень любил. Мне рассказывали также, что очень маленького меня полушутя, полусерьезно мамаша иногда посекала, и чтобы не оставалось во мне сердитого чувства, после экзекуции заставляла кричать: кукуреку! – в горе, в слезах, я исполнял приказание, но, к счастию, совсем не помню об этом.</p>
                        <p>Смутно у меня впечатление волков, попадающихся на дороге, когда мы едем в усадьбу тетки. Ильмовик; ясное впечатление стука молотов о наковальни в длинном ряду кузниц, по обрыву горы, на которой стоит наша усадьба – то наши крестьяне ковали гвозди для скупщика Головинского, поставлявшего им железо и отправлявшего потом выработанные гвозди даже в Англию, так как дешевизна рабочих рук зимою была тогда баснословною в России. Не ясно помнится постройка барок для сплава леса, также спуск их на воду с молебствием и угощением...»</p>
                    </div>
                    <a href="#" class="button-source-link">
                        <button type="button" class="button-source">ИСТОЧНИК</button>
                    </a>
                </div>
            </div>
        </transition>
    </section>
    <section class="contact-info">
        <div class="contact-info-item">
            <h2 class="title">Череповецкое Музейное Объединение</h2>
            <a class="contact-container" href="https://www.xn--e1aogg7a.xn--p1ai/">
                <img class="contact-image" src="@/assets/img/landing/img/chermo.png" alt="Chermo">
                <div class="contacts">
                    <p class="address">г. Череповец, Советский пр., 30 А</p>
                    <p class="phone">8 (8202) 49-33-06</p>
                    <p class="email">cherepovets-museum@yandex.ru</p>
                </div>
            </a>
        </div>
        <div class="contact-info-item">
            <h2 class="title">Череповецкий Государственный Университет </h2>
            <a class="contact-container" href="https://www.chsu.ru/">
                <img class="contact-image" src="@/assets/img/landing/img/chsu.png" alt="Chsu">
                <div class="contacts">
                    <p class="address">Пр-т Луначарского, д. 5, г. Череповец, Вологодская обл., Россия</p>
                    <p class="phone">8 (8202) 55-65-97</p>
                    <p class="email">chsu@chsu.ru</p>
                </div>
            </a>
        </div>
    </section>
</template>

<script setup>
    import { ref } from 'vue';

    const isOpen = ref(false);

    const toggleDriver = () => {
    isOpen.value = !isOpen.value;
    };
</script>

<style lang="scss" scoped>
    .text-container {
        display: flex;
        justify-content: center;
        gap: 120px;
        padding: 100px 150px;
        margin-bottom: 50px;
        .text-image-container {
            width: 450px;
            height: 550px;
            overflow: hidden;
            position: relative;

            .text-image {
                width: auto;
                height: auto;
                position: absolute;
                top: 50%;
                left: 50%;
                max-height: 550px;
                transform: translate(-50%, -50%);
            }
        }
        .text-inform {
            display: flex;
            flex-direction: column;
            gap: 100px;
            width: 50%;
            align-items: flex-end;
            .title-text {
                display: flex;
                flex-direction: column;
                gap: 30px;
            }
            .title {
                font-weight: 400;
            }
            .subtitle {
                font-weight: 500;
            }
            .button-inform {
                width: 50px;
                cursor: pointer;
                border: black 1px solid;
                border-radius: 10px;
                &:hover {
                    background-color: #E3E3E2;
                }
            }
        }
    }
    .contact-info {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 30px;
        .contact-info-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 30px;

            .title {
                font-weight: 500;
                align-content: center;
            }

            .contact-container {
                display: flex;
                flex-direction: column;
                gap: 26px;
                cursor: pointer;
                .contact-image {
                    border-radius: 10px;
                }
                .contacts {
                    display: flex;
                    flex-direction: column;
                    gap: 10px;
                    p {
                        margin: 0;
                    }
                }
                &:hover {
                    transform: scale(1.05);
                }
            }
            
        }
    }
    .drawer {
        position: absolute;
        left: 0;
        top: 50px;
    }
    .text-full-info {
        position: relative;
        width: 50%;
        .bg-drawer {
            height: 100%;
            object-fit: cover;
        }
        .text-full-info-container {
            display: flex;
            flex-direction: column;
            gap: 30px;
            position: absolute;
            top: 50%;
            left: 40%;
            transform: translate(-50%, -50%);
            .text-full-info-text {
                margin: 0 auto;
            }
            .button-source-link {
                display: flex;
                justify-content: center;
                align-items: center;
                gap: 30px;
                .button-source {
                    border: black 1px solid;
                    border-radius: 10px;
                    background-color: transparent;
                    cursor: pointer;
                    padding: 16px 20px;
                    font-size: 14px;
                    &:hover {
                        transform: scale(1.05);
                    }
                }
            }
        }
    }
    // .slide-enter-active, .slide-leave-active {
    //     transition: transform 0.3s ease;
    //     }

    // .slide-enter, .slide-leave-to /* .slide-leave-active в <2.1.8 */ {
    //     transform: translateX(-100%); /* Сдвиг влево при появлении/исчезновении */
    // }
    
</style>