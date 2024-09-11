import { defineStore } from 'pinia'
import { ref } from 'vue'
import { axiosInstance } from '@/utils/axios/axios.js'

export const useStateStore = defineStore('stateStore', () => {
  const isLoading = ref(false)

  const users = ref([])
  const user = ref({})

  const forms = ref([])
  const form = ref({})

  const teams = ref([])
  const team = ref({})

  const statuses = ref([])
  const history = ref([])

  const roles = ref([])

  const drops = ref([])

  const training_folders = ref([])
  const trainingFoldersAll = ref([])
  const training_folder = ref({})

  const training_files = ref([])
  const trainingFilesAll = ref([])
  const training_file = ref({})

  const todocategoryes = ref([])
  const todocategory = ref({})

  const todolists = ref([])
  const todolistuser = ref([])
  const todolist = ref({})

  const getUser = async () => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: '/users/current',
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'GET',
      })
      user.value = response.data
      await editUserOnline(user.value.id, true)
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const getUsers = async () => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: '/users',
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'GET',
      })
      users.value = response.data
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const getUsersHidden = async () => {
    try {
      const response = await axiosInstance({
        url: '/users',
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'GET',
      })
      users.value = response.data
    } catch (e) {
      throw e
    }
  }

  const editUser = async (data) => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: `/users/${data.id}`,
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'PATCH',
        data: {
          role_id: data.role.id,
          active_team_id: data.active_team?.title
            ? data.active_team.id.toString()
            : null,
        },
      })
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }
  const editUserOnline = async (id, online) => {
    try {
      const response = await axiosInstance({
        url: `/users/${id}/online`,
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'PATCH',
        data: {
          online: online,
        },
      })
    } catch (e) {
      throw e
    }
  }

  const addUser = async (data) => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: `/users`,
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'POST',
        data: {
          login: data.login,
          password: data.password,
          role_id: data.role.id,
        },
      })
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const deleteUser = async (id) => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: `/users/${id}`,
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'DELETE',
      })
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const getForms = async () => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: '/forms',
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'GET',
      })
      forms.value = response.data
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const getForm = async (id) => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: `/forms/${id}`,
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'GET',
      })
      form.value = response.data
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const addForm = async (data) => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: '/forms',
        headers: {
          'Content-Type': 'multipart/form-data',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'POST',
        data: data,
      })
      await addImageToForm(response.data.id, data.images)
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const addImageToForm = async (id, images) => {
    isLoading.value = true
    const formData = new FormData()
    images?.forEach((file) => {
      formData.append('images', file)
    })
    try {
      const response = await axiosInstance({
        url: `forms/add_images/${id}`,
        headers: {
          'Content-Type': 'multipart/form-data',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'PATCH',
        data: formData,
      })
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const deleteImageFromForm = async (id, data) => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: `forms/delete_images/${id}`,
        headers: {
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'PATCH',
        data: data,
      })
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const deleteForm = async (id) => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: `/forms/${id}`,
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'DELETE',
      })
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const editForm = async (data, images) => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: `/forms/${data.id}`,
        headers: {
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'PATCH',
        data: { data, team_id: data?.team?.id },
      })
      if (images.length) {
        await addImageToForm(data.id, images)
      }
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const getTeams = async () => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: '/teams',
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'GET',
      })
      teams.value = response.data
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const getTeam = async (id) => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: `/teams/${id}`,
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'GET',
      })
      team.value = response.data
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const addTeam = async (data) => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: `/teams`,
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'POST',
        data: data,
      })
      team.value = response.data
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const deleteTeam = async (id) => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: `/teams/${id}`,
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'DELETE',
      })
      team.value = response.data
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const editTeam = async (data) => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: `/teams/${data.id}`,
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'PATCH',
        data: {
          title: data.title,
          color: data.color,
        },
      })
      team.value = response.data
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const getStatuses = async () => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: '/statuses',
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'GET',
      })
      statuses.value = response.data
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const addStatus = async (data) => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: '/statuses',
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'POST',
        data,
      })
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const editStatus = async (data) => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: `/statuses/${data.id}`,
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'PATCH',
        data,
      })
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const deleteStatus = async (id) => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: `/statuses/${id}`,
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'DELETE',
      })
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const getHistory = async (id) => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: `/histories/${id}`,
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'GET',
      })
      history.value = response.data
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const getRoles = async () => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: `/roles`,
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'GET',
      })
      roles.value = response.data
      console.log(response.data)
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const getDrops = async () => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: `/drop_managers`,
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'GET',
      })
      drops.value = response.data
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const addDrop = async (data) => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: `/drop_managers`,
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'POST',
        data: data,
      })
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const deleteDrop = async (id) => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: `/drop_managers/${id}`,
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'DELETE',
      })
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const editDrop = async (data) => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: `/drop_managers/${data.id}`,
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'PATCH',
        data,
      })
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const getTrainingFolders = async () => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: '/training_folders',
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'GET',
      })
      training_folders.value = response.data
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const getTrainingFoldersById = async (id) => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: `/training_folders/all/${id}`,
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'GET',
      })
      training_folders.value = response.data
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const getTrainingFolder = async (id) => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: `/training_folders/${id}`,
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'GET',
      })
      training_folder.value = response.data
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const addTrainingFolder = async (data) => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: `/training_folders`,
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'POST',
        data: data,
      })
      training_folder.value = response.data
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const deleteTrainingFolder = async (id) => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: `/training_folders/${id}`,
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'DELETE',
      })
      training_folder.value = response.data
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const editTrainingFolder = async (data) => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: `/training_folders/${data.id}`,
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'PATCH',
        data: {
          title: data.title,
          color: data.color,
        },
      })
      training_folder.value = response.data
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const getTrainingFiles = async () => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: '/training_files',
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'GET',
      })
      training_files.value = response.data
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const getTrainingFilesById = async (id) => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: `/training_files/all/${id}`,
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'GET',
      })
      training_files.value = response.data
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const getTrainingFile = async (id) => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: `/training_files/${id}`,
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'GET',
      })
      training_file.value = response.data
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const addTrainingFile = async (data, folder_id = null) => {
    isLoading.value = true
    try {
      let url = '/training_files'
      if (Number(folder_id)) url += `/${folder_id}`
      const response = await axiosInstance({
        url,
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'POST',
        data: data,
      })
      ;(training_file.value = response.data), data.images
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const deleteTrainingFile = async (id) => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: `/training_files/${id}`,
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'DELETE',
      })
      training_file.value = response.data
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const getToDoCategoryes = async () => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: '/to_do_category',
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'GET',
      })
      todocategoryes.value = response.data
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const getToDoCategory = async (id) => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: `/to_do_category/${id}`,
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'GET',
      })
      todocategory.value = response.data
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const getToDoLists = async () => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: '/to_do_list',
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'GET',
      })
      todolists.value = response.data
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const getToDoList = async (id) => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: `/to_do_list/${id}`,
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'GET',
      })
      todolist.value = response.data
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const getToDoListTask = async (id) => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: `/to_do_list/users/${id}`,
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'GET',
      })
      todolistuser.value = response.data
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const addToDoList = async (data) => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: `/to_do_list`,
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'POST',
        data: data,
      })
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const deleteToDoList = async (id) => {
    isLoading.value = true
    try {
      const response = await axiosInstance({
        url: `/to_do_list/${id}`,
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'DELETE',
      })
    } catch (e) {
      throw e
    } finally {
      isLoading.value = false
    }
  }

  const editToDoList = async (data) => {
    try {
      const response = await axiosInstance({
        url: `/to_do_list/${data.id}`,
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        method: 'PATCH',
        data,
      })
    } catch (e) {
      throw e
    } finally {
    }
  }

  return {
    isLoading,
    users,
    user,
    forms,
    form,
    teams,
    team,
    statuses,
    history,
    roles,
    drops,
    training_folders,
    getTrainingFoldersById,
    training_folder,
    training_files,
    getTrainingFilesById,
    training_file,
    todolists,
    todolistuser,
    todolist,
    todocategoryes,
    todocategory,
    getUsers,
    getUsersHidden,
    getUser,
    editUser,
    editUserOnline,
    addUser,
    deleteUser,
    getForms,
    getForm,
    addForm,
    deleteImageFromForm,
    deleteForm,
    editForm,
    getTeams,
    addTeam,
    getTeam,
    deleteTeam,
    editTeam,
    getStatuses,
    addStatus,
    editStatus,
    deleteStatus,
    getHistory,
    getRoles,
    getDrops,
    addDrop,
    deleteDrop,
    editDrop,
    getTrainingFolders,
    addTrainingFolder,
    getTrainingFolder,
    deleteTrainingFolder,
    editTrainingFolder,
    getTrainingFiles,
    addTrainingFile,
    getTrainingFile,
    deleteTrainingFile,
    getToDoCategoryes,
    getToDoCategory,
    getToDoLists,
    getToDoList,
    getToDoListTask,
    addToDoList,
    deleteToDoList,
    editToDoList,
  }
})
