import { ref } from 'vue'
import axios from 'axios'
import { useStateStore } from '@/store/stateStore.js'

export const useAxios = (url, options) => {
  const stateStore = useStateStore()
  const response = ref()
  const error = ref()

  const request = async () => {
    stateStore.isLoading = true
    try {
      const res = await axios({
        baseURL: window.API + url,
        ...options,
      })
      response.value = res.data
    } catch (e) {
      error.value = e
    } finally {
      stateStore.isLoading = false
    }
  }
  return { response, request, error }
}
