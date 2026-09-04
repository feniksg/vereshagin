<template>
    <section class="pictures">
        <!-- Картинка должна быть из БД -->
        <img id="picture" ref="pictureElement" class="picture" src="@/assets/img/landing/img/picture/apotheosis_of_war.png" alt="" @contextmenu.prevent/>
        <!-- Всякая инфа должна быть тоже из БД -->
        <DrawerPictureInfo 
            :height="pictureHeight"
            title="Апофеоз войны"
            year_and_size="1871, 127×197 см"
            text="Работая над самой известной своей картиной, Василий Верещагин держал в уме вполне конкретный исторический контекст – он собирался назвать ее «Торжество Тамерлана». Однако когда работа была закончена, художник понял, что создал универсальный образ, могучее антивоенное высказывание, выходящее за рамки какой-либо исторической эпохи, личности или легенды.

                        Склонный к сарказму, Верещагин нередко снабжал свои полотна посвящениями, названиями или аннотациями, которые нервировали записных патриотов сильнее, чем сами полотна. Можно предположить, что картина, живописующая последствия кровопролитного штурма Плевны, была бы встречена царской семьей куда более благосклонно, если бы художник не собирался назвать ее «Царскими именинами».
                        
                        «Апофеоз войны» не стал исключением: чтобы избежать недопонимания, художник сделал на раме надпись: «Посвящается всем великим завоевателям - прошедшим, настоящим и будущим»." 
        />
    </section>

    <section class="brief_info_picture">
        <div class="text_brief_info">
            <img class="qr_picture" src="@/assets/img/landing/img/picture/aow_qr.png" alt="QR-code"/>
            <h1 class="title_qr">QR-code</h1>
        </div>
        <div class="text_brief_info">
            <p>Открайте для себя захватывающее произведение Василия Верещагина «Апофеоз войны» с помощью QR-кода.
                Картина Верещагина — это не просто изображение войны, это призыв к миру.
                Она напоминает нам о том, что война — это трагедия, которая несет смерть и разрушение.</p>
            <p> После открытия QR-кода наведите камеру своего смартфона на изображение картины и вам откроется дополненная реальность.
                Испытайте силу искусства и позвольте произведению великого художника затронуть ваше сердце.</p>
        </div>
    </section>
</template>

<script setup>
    import { ref, onMounted } from 'vue'
    import DrawerPictureInfo from '~/components/layout/DrawerPictureInfo.vue'

    const pictureElement = ref(null)
    const pictureHeight = ref(0)

    onMounted(() => {
        if (pictureElement.value) {
            pictureHeight.value = pictureElement.value.offsetHeight
        }
    })
</script>

<style scoped>
    .pictures {
        width: 100%;
        position: relative;
        display: inline-block;
    }
    .picture {
        width: 100%;
        position: relative;
        top: -66px;
        z-index: -1;
        max-width: var(--max-width);
        object-fit: cover;
    }
    .title_qr {
        padding-top: 40px;
    }
    .qr_picture {
        filter: grayscale(100%);
    }
    .text_brief_info {
        width: 30%;
        text-align: justify;
    }
    .brief_info_picture {
        position:relative;
        display:flex;
        justify-content: space-evenly;
        align-items: center;
        padding-top: 250px;
        padding-bottom: 150px;
    }
    
</style>