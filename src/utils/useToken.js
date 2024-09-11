import { ref } from 'vue'
import { useLocalStorage } from '@/utils/useLocalStorage.js'

export const useToken = () => {
  const { setStorageItem, removeStorageItem, getStorageItem } =
    useLocalStorage()

  const tokenStorage = getStorageItem('token') || null
  const token = ref(tokenStorage)
  const tokenExpireStorage = getStorageItem('tokenExpire') || null
  const tokenExpire = ref(tokenExpireStorage)

  const setToken = (tokenAuth) => {
    token.value = tokenAuth
    setStorageItem('token', tokenAuth)
    decodeJwt()
  }

  const clearToken = () => {
    token.value = null
    removeStorageItem('token')
  }
  const decodeJwt = () => {
    // расшивроквка токена, запись даты окончания в локалтсорейдж и переменную
    const base64Url = token.value.split('.')[1]
    const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/')
    const jsonPayload = decodeURIComponent(
      window
        .atob(base64)
        .split('')
        .map(function (c) {
          return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2)
        })
        .join('')
    )
    const expire = +JSON.parse(jsonPayload).exp * 1000
    tokenExpire.value = expire
    setStorageItem('tokenExpire', expire)
  }
  return { token, setToken, clearToken, tokenExpire }
}
