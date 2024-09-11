import { ref } from 'vue'
import { useStateStore } from '@/store/stateStore'

export const useFetching = (cb) => {
  const stateStore = useStateStore()
  const isLoading = ref(false)
  const error = ref('')

  const fetching = async (args) => {
    try {
      isLoading.value = true
      stateStore.isLoading = true
      return await cb(args)
    } catch (e) {
      error.value = e.message
    } finally {
      isLoading.value = false
      stateStore.isLoading = false
    }
  }
  return {
    isLoading,
    error,
    fetching,
  }
}
