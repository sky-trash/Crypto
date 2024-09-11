export const useLocalStorage = () => {
  const setStorageItem = (key, value, json = false) =>
    json
      ? localStorage.setItem(key, JSON.stringify(value))
      : localStorage.setItem(key, value)

  const getStorageItem = (key, json = false) =>
    json ? JSON.parse(localStorage.getItem(key)) : localStorage.getItem(key)

  const removeStorageItem = (key) => localStorage.removeItem(key)

  const clearStorage = () => localStorage.clear()

  // setStorageItem('token', '')
  // setStorageItem('tokenExpire', '')
  // setStorageItem('isAuth', false, true)

  return { setStorageItem, getStorageItem, removeStorageItem, clearStorage }
}
