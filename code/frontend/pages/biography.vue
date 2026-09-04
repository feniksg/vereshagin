<template>
    <section>
        <div class="title-biography-container">
            <div class="title-biography">
                <img class="bg-header" src="@/assets/img/landing/img/header-biography.png" alt="">
                <h1 class="header-title">Биография</h1>
            </div>
        </div>

        <div class="header-biography">
            <div class="biography-container">
                <div class="image-year-container">
                    <div class="biography-image-container">
                        <img class="biography-image" src="@/assets/img/landing/img/biography/vereshchagin.png" alt="Text">
                    </div>
                    <div class="year-display">
                            <span>{{ startYear }}</span>
                            <div class="border-line"></div>
                            <span>{{ endYear }}</span>
                    </div>
                </div>
                <div class="title-text">
                    <h1 class="title">{{ name }}</h1>
                    <h2 class="subtitle">{{ description}}</h2>
                </div>
            </div>
        </div>

        <div class="text-biography">
            <div class="text-biography-container">
                <BiographyText 
                    title="Детство и отрочество"
                    year="1842-1860гг."
                    text="Василий Верещагин родился в Череповце и в 9 лет родители определили его в кадетский морской корпус. «Корпус терпеть не мог» — вспоминал художник. Ещё во время учебы он посещал рисовальную школу, знакомился с художниками. В 1860 году против воли родителей он поступил в Академию художеств. В это же время пробовал себя в литературном творчестве: предложил свой «Рассказ старого охотника» петербургской газете «Голос»." 
                />
                <BiographyText 
                    title="Картины Туркестанской серии"
                    year="1867-1873гг."
                    text="В 1867 году Верещагин поступил на службу к туркестанскому генерал-губернатору Константину фон Кауфману — штатным художником. Вскоре крепость с русскими войсками оказалась в осаде: восстали местные жители. Верещагин участвовал в битве с бухарцами и получил орден Святого Георгия 4-го класса — за отвагу. 

    Живопись и графику, привезенные из Туркестана, художник представил в 1869 году в столице. Благодаря картинам Верещагина посетители увидели неизвестную им Среднюю Азию: невольничий рынок, нищих опиумоедов и женщин, с головы до ног укрытых одеяниями. Всего в Туркестанскую серию вошли 13 полотен, 81 этюд и 133 рисунка. В 1873 году Верещагин выставил весь цикл в Хрустальном дворце в Лондоне." 
                />
                <div class="centered" style="background-color: white; padding-top: 36px;">
                    <Slider
                        :slideWidth="600"
                        :gapSize="0"
                        class="art-slider"
                        :showStatusBar="false"
                        :horizontalControls="false"
                    >
                        <div class="custom-slide aslis">
                            <div class="image-container">
                                <img src="@/assets/img/landing/img/1.png" alt="">
                            </div>
                            <h2>Апофеоз войны.</h2>  
                        </div>
                        <div class="custom-slide aslis">
                            <div class="image-container">
                                <img src="@/assets/img/landing/img/2.png" alt="">
                            </div>
                            <h2>Тадж Махал.</h2>  
                        </div>
                        <div class="custom-slide aslis">
                            <div class="image-container">
                                <img src="@/assets/img/landing/img/3.png" alt="">
                            </div>
                            <h2>Дядька.</h2>  
                        </div>
                                        
                        
                    </Slider>
                </div>
                <BiographyText 
                    title="Балканский поход и новые батальные полотна"
                    year="1877-1880гг."
                    text="Весть о войне с турками застала Верещагина в Париже, где располагалась его мастерская. Он оставил работу над индийскими полотнами и добровольно отправился на Балканы — в составе действующего подразделения русской. 

    Готовили штурм Плевны. Плевну планировали взять 30 августа, к именинам императора Александра II​. Однако штурм обернулся крупным поражением. Поле брани с сотнями погибших Верещагин изобразил на полотне с провокационным названием «Царские именины». 

    В декабре 1879 года выставка с балканскими работами Верещагина прошла в Париже. На полотнах не было парадных триумфальных сцен. В споре с Павлом Третьяковым, который придерживался традиционных патриотических взглядов на батальную живопись, художник говорил: «…мы с вами расходимся немного в оценке моих работ и очень много в их направлении. Передо мною как художником война, и ее я бью, сколько у меня есть сил...». " 
                />
            </div>
        </div>
    </section>
</template>

<script setup>
import { defineProps } from 'vue';
import BiographyText from '@/components/layout/BiographyText.vue';
import BiographyImage from '@/components/layout/BiographyImage.vue';
const props = defineProps({
    startYear: {
        type: Number,
        default: 1842,
        required: true,
    },
    endYear: {
        type: Number,
        default: 1904,
        required: true,
    },
    name: {
        type: String,
        default: 'Василий Васильевич Верещагин',
        required: true,
    },
    description: {
        type: String,
        default: 'Русский живописец, писатель, один из самых известных баталистов второй половины XIX века',
        required: true,
    }
});

</script>


<style lang="scss" scoped>
    .art-slider {
        width: 600px;
        padding: 0;
        .aslis {
            width: 600px !important;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            .image-container{
                width: 100%;
                height: 100%;
                overflow: hidden;
                margin-bottom: 16px;
                img {
                    width: 100%;
                    height: 100%;
                    object-fit: cover;
                }
            }
            h2 {
                text-align: center;
                margin: 0;
            }
        }
    }
    .title-biography{
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: -70px;
        
        .bg-header{
            width: 100%;
            position: relative;
            z-index: -1;
            max-width: var(--max-width);
            background: #292727;
        }

        .header-title{
            position: absolute;
        }
    }

    .biography-container {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 120px;
        padding-inline: 150px;
        padding-bottom: 100px;
        background: #292727;
        z-index: 0;

        .image-year-container {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            gap: 30px;

            .biography-image-container {
                width: 450px;
                height: 550px;
                overflow: hidden;
                position: relative;

                .biography-image {
                    width: auto;
                    height: 100%;
                    min-height: 100%;
                    object-fit: cover;
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    max-height: 550px;
                    transform: translate(-50%, -50%);
                }
            }
            .year-display {
                width: 60%;
                display: flex;
                align-items: center;
                color: #fff;
                font-weight: 500;
                font-size: 20px;
            }
            .border-line {
                flex-grow: 1;
                height: 0.5px; /* Толщина линии */
                background-color: #fff; /* Цвет линии */
                margin: 0 23px; /* Отступы между годами и линией */
            }
        }
        .title-text {
            width: 40%;
            display: flex;
            flex-direction: column;
            gap: 30px;
            color: #fff;

            .title {
                font-weight: 400;
            }
            .subtitle {
                font-weight: 500;
            }
        }
    }

    .text-biography-container {
        width: 100%;
        height: auto;
        padding: 50px 0;
        background: #EDE9DF;
    }
</style>