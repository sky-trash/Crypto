import { ref } from 'vue'

export const useOnlineStatus = () => {
  const isOnline = ref(true)

  const updateOnlineStatus = () => {
    isOnline.value = navigator.onLine
  }

  window.addEventListener('online', updateOnlineStatus)
  window.addEventListener('offline', updateOnlineStatus)

  return {
    isOnline,
  }
}
