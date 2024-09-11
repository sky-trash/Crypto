import { ref } from 'vue'
import { useAxios } from '@/utils/useAxios.js'
import { useStateStore } from '@/store/stateStore.js'

export const useAuth = async (data) => {
  const stateStore = useStateStore()
  const { response, request, error } = useAxios('/token', {
    method: 'POST',
    headers: {
      accept: 'application/json',
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    data,
  })

  if (!stateStore.isLoading.value) {
    await request()
  }

  return { response, error }
}
