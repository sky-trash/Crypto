<script setup>
import VIcon from '@/components/icon/VIcon.vue'

const props = defineProps({
  name: {
    type: String,
    default: '',
  },
  id: {
    type: String,
    default: '',
  },
  disabled: {
    type: Boolean,
    default: false,
  },
  modelValue: {
    type: Boolean,
    default: false,
  },
  color: {
    type: String,
    default: 'black',
  },
})
const emits = defineEmits(['update:modelValue', 'change'])

const changeValue = () => {
  emits('update:modelValue', !props.modelValue)
  emits('change', !props.modelValue)
}
</script>

<template>
  <div class="checkbox">
    <input
      type="checkbox"
      :checked="modelValue"
      class="zero-input"
      :id="id"
      :disabled="disabled"
    />
    <div
      @change="changeValue"
      @click="changeValue"
      :class="['checkbox__input', `border-${color}`, { disabled: disabled }]"
      :id="id"
    >
      <div class="checkbox__icon" v-if="modelValue">
        <VIcon icon="check" size="18" :class="`check-${color}`" />
      </div>
    </div>
    <label
      @click="changeValue"
      :for="id"
      :class="['label', { disabled: disabled }]"
    >
      <slot></slot>
    </label>
  </div>
</template>

<style scoped lang="scss">
@import '@/assets/scss/variables';
.checkbox {
  display: flex;
  align-items: center;
  height: 24px;
  gap: 10px;
  &__input {
    padding: 0;
    height: 20px;
    width: 20px;
    cursor: pointer;
  }
  &__icon {
    margin: -1px 0 0 0;
  }
}
.border-gray {
  border: 1px solid $gray;
}
.border-black {
  border: 1px solid $black;
}
.border-primary {
  border: 1px solid $primary;
}
.border-secondary {
  border: 1px solid $secondary;
}
.border-warning {
  border: 1px solid $warning;
}
.border-info {
  border: 1px solid $info;
}
.border-error {
  border: 1px solid $error;
}
.check-gray {
  color: $gray;
}
.check-black {
  color: $black;
}
.check-primary {
  color: $primary;
}
.check-secondary {
  color: $secondary;
}
.check-warning {
  color: $warning;
}
.check-info {
  color: $info;
}
.check-error {
  color: $error;
}
.zero-input {
  height: 20px;
  opacity: 0;
  z-index: -1;
  position: absolute;
}
.disabled {
  opacity: 0.6;
  pointer-events: none;
}
</style>
