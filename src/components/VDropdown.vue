<script setup>
import { computed, ref } from 'vue'

const props = defineProps({
  list: {
    type: Array,
    required: true,
  },
  modelValue: {
    type: Object,
  },
  placeholder: {
    type: String,
    default: 'Не выбрано',
  },
  nonPlaceholder: {
    type: Boolean,
    default: false,
  },
})

const emits = defineEmits(['update:modelValue', 'change'])

const menuPosition = ref('bottom')
const dropdownTitle = ref()

const activeItem = computed(
  () =>
    props.list[props.list.findIndex((item) => item.id === props.modelValue?.id)]
)
const isOpen = ref(false)

const sortedList = computed(() =>
  props.list.filter((item) => item?.title !== activeItem.value?.title)
)

const toggle = () => {
  const triggerRect = dropdownTitle.value.getBoundingClientRect()
  const spaceBelow = window.innerHeight - triggerRect.bottom
  if (spaceBelow < 200) {
    menuPosition.value = 'top'
  }

  isOpen.value = !isOpen.value
}

const setActive = (item) => {
  isOpen.value = false
  emits('update:modelValue', item)
  emits('change')
}

const close = () => {
  isOpen.value = false
}
</script>

<template>
  <div v-outside="close" class="dropdown">
    <div @click="toggle" ref="dropdownTitle" class="dropdown__title">
      <span :style="{ color: activeItem?.color }">{{
        activeItem?.title ? activeItem?.title : placeholder
      }}</span>
      <img src="/img/icons/back.svg" alt="" :class="{ active: isOpen }" />
    </div>
    <Transition name="slide">
      <div
        v-if="isOpen"
        ref="menu"
        :class="[
          'dropdown__body',
          { top: menuPosition === 'top' },
          { bottom: menuPosition === 'bottom' },
        ]"
      >
        <div class="dropdown__body-list">
          <div
            v-if="activeItem && !nonPlaceholder"
            @click="setActive({})"
            class="dropdown__body-item"
          >
            {{ placeholder }}
          </div>
          <div
            v-for="item in sortedList"
            :key="item"
            @click="setActive(item)"
            class="dropdown__body-item"
            :style="{ color: item?.color }"
          >
            {{ item.title }}
          </div>
        </div>
      </div>
    </Transition>
  </div>
</template>

<style scoped lang="scss">
@import '@/assets/scss/variables';

.dropdown {
  position: relative;
  flex: 0 1 455px;
  cursor: pointer;
  user-select: none;

  &__title {
    position: relative;
    z-index: 1;
    background-color: #fff;
    width: 100%;
    height: 36px;
    padding: 0 8px;
    border-radius: 4px;
    //box-shadow: 0 4px 20px 0 rgba(0, 0, 0, 0.15);
    border: 1px solid #dee2e6;
    display: flex;
    align-items: center;
    justify-content: space-between !important;
    font-size: 14px;
    font-weight: 500;

    span {
      display: block;
      color: $black;
      font-size: 14px !important;
    }

    img {
      width: 8px !important;
      transition: all 0.3s ease;
      transform: rotate(-90deg);

      &.active {
        transform: rotate(90deg);
      }
    }
  }

  &__body {
    position: absolute;
    z-index: 2;
    width: 100%;
    background-color: #fff;
    border-top: none;
    max-height: 320px;
    overflow: auto;
    border-radius: 0 0 4px 4px;
    box-shadow: 0 4px 20px 0 rgba(0, 0, 0, 0.15);
    font-size: 14px;
    font-weight: 500;

    &.top {
      bottom: 100%;
    }

    &.bottom {
      top: 100%;
    }

    &-list {
      display: flex;
      flex-direction: column;
    }

    &-item {
      height: 36px;
      width: 100%;
      border-bottom: 1px solid #00193f60;
      display: flex;
      align-items: center;
      padding: 0 8px;
      color: $black;

      &:last-child {
        border: none;
      }
    }
  }
}
</style>
