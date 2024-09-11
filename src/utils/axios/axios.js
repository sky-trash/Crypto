import axios from 'axios'

const API = window.API
export const axiosInstance = axios.create({
  baseURL: API,
})
