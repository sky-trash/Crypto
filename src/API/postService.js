import { axiosInstance } from '@/utils/axios/axios'
const token = localStorage.getItem('token')

export default class PostService {
  static async getForms() {
    try {
      const response = await axiosInstance({
        url: '/forms',
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${token}`,
        },
        method: 'GET',
      })
      return response.data
    } catch (e) {
      throw e
    }
  }
}
