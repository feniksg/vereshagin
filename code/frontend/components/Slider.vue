<template>
    <div class="slider-container">
        <div class="slider" :style="{transform: `translateX(${currentSlide * (slideWidth + gapSize)}px)`, gap: `${gapSize}px`}">
            <slot />
        </div>
        <div v-if="!horizontalControls" class="slider-controls">
            <div class="slider-control-button" @click="prevSlide()"><img src="@/assets/img/landing/svg/arr-left.svg" alt=""></div>
            <div class="slider-control-status-bar" v-if="totalSlides > 0 && showStatusBar">
                <div class="circle" v-for="index in totalSlides" :key="index" :class="{active:(index-1 - middleSlide)*(-1) == currentSlide}"></div>
            </div>
            <div class="slider-control-button" @click="nextSlide()"><img src="@/assets/img/landing/svg/arr-right.svg" alt=""></div>
        </div>
    </div>
</template>


<script>
import { getCurrentInstance } from 'vue'
export default {
    props: {
        slideWidth: {
            type: Number,
            required: true,
        },
        gapSize: {
            type: Number,
            required: false,
            default: 0,
        },
        slideCount: {
            type: Number,
            required: false,
        },
        showStatusBar: {
            type: Boolean,
            required: false,
            default: false,
        },
        horizontalControls: {
            type: Boolean,
            required: false,
            default: false,
        }

    },
    data() {
        return {
            currentSlide: 0,
            totalSlides: 0,
            instance: getCurrentInstance()
        }
    },
    methods: {
        nextSlide() {
            if (this.currentSlide > this.middleSlide*(-1)) {
                this.currentSlide-= 1;
            }
            else {
                this.currentSlide*=-1;
            }
        },
        prevSlide() {
            if (this.currentSlide < this.middleSlide) {
                this.currentSlide += 1;
            }
            else {
                this.currentSlide*=-1;
            }
        },

    },
    mounted() {
        this.totalSlides = this.$slots.default().length;
        console.log(this.totalSlides)
        console.log(this.props)
        console.log(this.slideCount)
        if (this.slideCount !== undefined) {
            this.totalSlides = this.slideCount;
        }
    },
    computed:{
        middleSlide(){
            return Math.floor(this.totalSlides / 2)
        }
    },
    watch: {
        updateSlidesCount() {
            // this.totalSlides = this.$slots.default().length;
            console.log(this.totalSlides)
        }
    }
}
</script>


<style lang="scss">
.circle {
    border-radius: 50%;
    width: 14px;
    height: 14px;
    background-color: var(--color-saved-text);
}
.active {
    background-color: #525252 !important;
}
.scaled {
    transform: scale(1.2);
}
.slider-container {
    min-width: 300px !important;
    height: 700px;
    width: 1000px;
    overflow: hidden;
    padding: 10px;
    .slider {
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        height: 80%;
        margin-right: 5px;
        margin-bottom: 5px;
        width: 100%;
        padding: 0;
        transition: transform 1.1s ease;
    }
    .slider-controls {
        margin: 0 30%;
        height: 20%;
        display: flex;
        align-items: center;
        justify-content: space-between;
        .slider-control-button {
            padding: 10px;
        }
        .slider-control-status-bar {
            display: flex;
            gap: 5px;
            padding: 10px;
        }
    }
}

    
</style>