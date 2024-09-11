<script setup>
import { Navigation } from 'swiper/modules'
import { Swiper, SwiperSlide } from 'swiper/vue'
import 'swiper/css'
import 'swiper/css/navigation'

defineProps({
  modelValue: {
    type: Boolean,
    default: false,
  },
  list: {
    type: Array,
    required: true,
  },
  initialSlide: {
    type: Number,
    default: 0,
  },
})
const emits = defineEmits(['update:modelValue'])

const API = window.API

const close = () => {
  emits('update:modelValue', false)
}
</script>

<template>
  <Transition name="fade">
    <div v-if="modelValue" class="popup">
      <div @click="close" class="popup__close">
        <img src="/img/icons/plus.svg" alt="" />
      </div>
      <div class="popup__content">
        <div class="prev">
          <img src="/img/icons/arrow.svg" alt="" />
        </div>
        <div class="next">
          <img src="/img/icons/arrow.svg" alt="" />
        </div>
        <Swiper
          :slidesPerView="1"
          :spaceBetween="30"
          :initial-slide="initialSlide"
          :navigation="{
            prevEl: `.prev`,
            nextEl: `.next`,
          }"
          :modules="[Navigation]"
          class="mySwiper"
        >
          <SwiperSlide v-for="slide in list" :key="list" class="slide">
            <img :src="API + '/' + slide" alt="" />
          </SwiperSlide>
        </Swiper>
      </div>
    </div>
  </Transition>
</template>

<style scoped lang="scss">
@import '@/assets/scss/variables';

.popup {
  position: absolute;
  inset: 0;
  z-index: 6;
  background-color: rgba(0, 0, 0, 0.66);
  display: flex;
  align-items: center;
  justify-content: center;

  &__close {
    position: absolute;
    z-index: 5;
    top: 32px;
    right: 32px;
    transform: rotate(45deg);
    @media (max-width: $md3 + px) {
      top: 24px;
      right: 24px;
    }

    img {
      width: 32px;
      @media (max-width: $md3 + px) {
        width: 24px;
      }
    }
  }

  &__content {
    width: 80%;
    height: 80%;
    display: flex;
    align-items: center;
    position: relative;

    @media (max-width: $md2 + px) {
      width: 90%;
      height: 90%;
    }

    @media (max-width: $md3 + px) {
      width: 100%;
      height: 100%;
    }

    .prev {
      position: absolute;
      z-index: 4;
      left: 32px;
      transform: rotate(180deg);

      img {
        width: 32px;
      }

      @media (max-width: $md3 + px) {
        display: none;
      }
    }

    .next {
      position: absolute;
      z-index: 4;
      right: 32px;

      img {
        width: 32px;
      }

      @media (max-width: $md3 + px) {
        display: none;
      }
    }

    .swiper {
      width: 100%;
      height: 100%;

      .slide {
        width: 100%;
        height: 100%;

        img {
          width: 100%;
          height: 100%;
          object-fit: contain;
        }
      }
    }
  }
}
</style>
