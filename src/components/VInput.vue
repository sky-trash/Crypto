<script setup>
import { onUpdated } from 'vue'

const props = defineProps({
  type: {
    type: String,
    default: 'text',
  },
  placeholder: {
    type: String,
  },
  modelValue: {
    type: String,
    default: '',
  },
  color: {
    type: String,
    default: '#474747',
  },
  error: {
    type: Boolean,
    default: false,
  },
})
const emits = defineEmits(['update:modelValue', 'click', 'update:error'])

const onInput = (e) => {
  emits('click')
  emits('update:modelValue', e.target.value)
  emits('update:error', false)
}

// onUpdated(() => {
//   if (props.type === 'date') {
//     const date = new Date()
//     const year = date.getFullYear()
//     const [d, m, y] = props.modelValue.split('.')
//     if (+d > 31 || +m > 12 || +y < 1900 || +y > year) {
//       emits('error', true)
//     } else {
//       emits('error', false)
//     }
//   }
// })
</script>

<template>
  <input
    @input="onInput"
    :type="type"
    :placeholder="placeholder"
    :value="modelValue"
    :class="[{ error: error }]"
  />
</template>

<style scoped lang="scss">
input {
  border-bottom: 1px solid #000;
  padding: 4px 12px 4px 0;
  width: 100%;
  height: 36px;
  font-weight: 500;
  font-size: 14px;
  color: v-bind(color);

  &:-webkit-autofill {
    transition: background-color 5000s ease-in-out 0s;
  }

  &.error {
    border-bottom: 1px solid red;
  }
}
</style>
