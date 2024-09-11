<script setup>
defineProps({
  icon: {
    type: String,
    required: true,
  },
  size: {
    type: String,
    default: '20',
  },
  color: {
    type: String,
  },
})
</script>

<template>
  <i
    :class="['icon', `icon-${icon}`]"
    :style="[
      { 'font-size': `${size}px` },
      { color: color },
      { height: `${size}px` },
      { width: `${size}px` },
    ]"
  ></i>
</template>

<style scoped lang="scss">
i {
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
</style>
