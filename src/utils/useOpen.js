import { ref } from 'vue'
export const useOpen = () => {
  const isOpen = ref(false)

  const toggle = () => {
    isOpen.value = !isOpen.value
  }
  const close = () => {
    isOpen.value = false
  }
  return { isOpen, close, toggle }
}
