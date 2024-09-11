<script setup>
defineProps({
  modelValue: {
    type: Boolean,
    default: false,
  },
})
const emits = defineEmits(['update:modelValue', 'good'])

const close = () => {
  emits('update:modelValue', false)
}

const good = () => {
  emits('update:modelValue', false)
  emits('good')
}
</script>

<template>
  <Transition name="fade">
    <div v-if="modelValue" @click="close" class="popup">
      <div @click.stop class="popup__content">
        <div class="popup__content-title">Подтвердите действие</div>
        <div class="popup__content-actions">
          <div @click="good" class="btn-add">
            <img src="/img/icons/check.svg" alt="" style="width: 24px" />
            Подвердить
          </div>
          <div @click="close" class="btn delete">
            <img src="/img/icons/plus.svg" alt="" />
            Отмена
          </div>
        </div>
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

  &__content {
    width: 30%;
    height: 200px;
    background-color: #fff;
    border-radius: 30px;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    padding: 30px;
    &-title {
      text-align: center;
      font-size: 24px;
      font-weight: 700;
    }
    @media (max-width: 1260px) {
      width: 50%;
      height: 35%;
      padding: 15px;
    }
    @media (max-width: 768px) {
      width: 75%;
    }
    @media (max-width: 360px) {
      width: 90%;
      &-title {
        font-size: 20px;
      }
    }
    &-actions {
      display: flex;
      justify-content: center;
      gap: 30px;
      @media (max-width: 1260px) {
        gap: 15px;
      }
      div {
        width: calc(50% - 15px);
      }
    }
  }
}
</style>
