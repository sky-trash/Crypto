<script setup>
const props = defineProps({
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
</script>

<template>
  <textarea
    @input="onInput"
    :placeholder="placeholder"
    :value="modelValue"
    :class="[{ error: error }]"
  ></textarea>
</template>

<style scoped lang="scss">
textarea {
  border: 1px solid black;
  width: 100%;
  height: 200px;
  outline: none;
  padding: 10px;
  font-size: 14px;
  &.error {
    border: 1px solid red;
  }
}
</style>
