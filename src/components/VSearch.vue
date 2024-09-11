<script setup>
defineProps({
  modelValue: {
    type: String,
    default: '',
  },
})
const emits = defineEmits(['update:modelValue', 'click'])

const onInput = (e) => {
  emits('click')
  emits('update:modelValue', e.target.value)
}
</script>

<template>
  <div class="search">
    <input
      @input="onInput"
      type="text"
      :value="modelValue"
      class="search__input"
      placeholder="Поиск..."
    />
    <img src="/img/icons/search.svg" alt="" class="search__img" />
  </div>
</template>

<style scoped lang="scss">
@import '@/assets/scss/variables';

.search {
  display: flex;
  align-items: center;
  position: relative;

  @media (max-width: $md4 + px) {
    width: 100%;
  }

  &__input {
    background-color: #fff;
    width: 320px;
    height: 36px;
    padding: 0 12px 0 48px;
    border-radius: 4px;
    //box-shadow: 0 4px 20px 0 rgba(0, 0, 0, 0.15);
    border: 1px solid #dee2e6;
    font-size: 14px;
    @media (max-width: $md1 + px) {
      width: 280px;
    }

    @media (max-width: $md2 + px) {
      width: 250px;
    }

    @media (max-width: $md4 + px) {
      width: 100%;
    }
  }

  &__img {
    position: absolute;
    width: 28px;
    left: 4px;
  }
}
</style>
