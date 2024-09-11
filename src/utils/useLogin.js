import { ref } from 'vue'
import { useLocalStorage } from '@/utils/useLocalStorage.js'
import { useToken } from '@/utils/useToken.js'
import { useRouter } from 'vue-router'

export const useLogin = () => {
  const { setStorageItem, clearStorage, getStorageItem } = useLocalStorage()
  const { clearToken } = useToken()
  const isAuth = ref(getStorageItem('isAuth')) || false
  const router = useRouter()

  const login = async () => {
    isAuth.value = true
    setStorageItem('isAuth', true, true)
  }

  const logout = async () => {
    clearToken()
    clearStorage()
    isAuth.value = false
  }

  return { login, logout, isAuth }
}
