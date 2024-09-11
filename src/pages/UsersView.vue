<script setup>
import { computed, onBeforeUnmount, onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useStateStore } from '@/store/stateStore.js'
import VDropdown from '@/components/VDropdown.vue'
import VInput from '@/components/VInput.vue'
import PopupConfirm from '@/components/PopupConfirm.vue'
import VCheckbox from '@/components/VCheckbox.vue'

const router = useRouter()
const store = useStateStore()
const formActive = ref(false)
const isOpen = ref(false)
const deleteId = ref(null)
const onlineChecked = ref(false)
const getUsersInterval = ref(null)

const sortedRoles = computed(() =>
  store.roles
    .map((role) => {
      if (role.title === 'ROLE_ADMIN') {
        return { ...role, title: 'Админ' }
      } else if (role.title === 'ROLE_USER') {
        return { ...role, title: 'Пользователь' }
      }
      return role
    })
    .filter((item) => item.id !== 1)
)

const sortedRolesWithAdmin = computed(() =>
  store.roles.map((role) => {
    if (role.title === 'ROLE_ADMIN') {
      return { ...role, title: 'Админ' }
    } else if (role.title === 'ROLE_USER') {
      return { ...role, title: 'Пользователь' }
    }
    return role
  })
)

const data = ref({
  login: '',
  password: '',
  role: {},
})
const activeRole = ref({})

const updateRole = (data) => {
  store.editUser(data)
}

const addUser = () => {
  formActive.value = true
}

const closeForm = () => {
  formActive.value = false
}

const sendUser = async () => {
  await store.addUser(data.value)
  formActive.value = false
  data.value = {
    login: '',
    password: '',
    role: sortedRoles.value[0],
  }
  await store.getUsers()
}

const deleteUser = (id) => {
  deleteId.value = id
  isOpen.value = true
}

const sendDeleteUser = async () => {
  await store.deleteUser(deleteId.value)
  deleteId.value = null
  isOpen.value = false
  await store.getUsers()
}

await store.getUser()
await store.getUsers()

const sortedUsers = computed(() => {
  const roleOrder = {
    ROLE_ADMIN: 1,
    ROLE_USER: 4,
  }

  if (activeRole.value?.title) {
    if (onlineChecked.value) {
      return store.users
        .filter((item) => item.role.id === activeRole.value.id)
        .filter((item) => item.online === true)
        .sort((a, b) => roleOrder[a.role.title] - roleOrder[b.role.title])
    } else {
      return store.users
        .filter((item) => item.role.id === activeRole.value.id)
        .sort((a, b) => roleOrder[a.role.title] - roleOrder[b.role.title])
    }
  } else {
    if (onlineChecked.value) {
      return store.users
        .filter((item) => item.online === true)
        .sort((a, b) => roleOrder[a.role.title] - roleOrder[b.role.title])
    } else {
      return store.users.sort(
        (a, b) => roleOrder[a.role.title] - roleOrder[b.role.title]
      )
    }
  }
})

await store.getRoles()

onMounted(() => {
  if (store.user.role.id !== 1) router.push('/home')
  data.value.role = sortedRoles.value[0]

  getUsersInterval.value = setInterval(() => {
    store.getUsersHidden()
  }, 10000)
})

onBeforeUnmount(() => {
  clearInterval(getUsersInterval.value)
})
</script>
<template>
  <div class="page">
    <PopupConfirm @good="sendDeleteUser" v-model="isOpen" />
    <header class="header">
      <div class="left">
        <div class="subtitle">Пользователи</div>
        <div v-if="!formActive" class="dropdown-block">
          <VDropdown :list="sortedRolesWithAdmin" v-model="activeRole" />
        </div>
        <VCheckbox
          v-if="!formActive"
          v-model="onlineChecked"
          id="black"
          color="primary"
        >
          <div class="label">Online</div>
        </VCheckbox>
      </div>
      <div class="right">
        <form v-if="formActive" class="form">
          <div class="form__block">
            <VInput placeholder="Логин" v-model="data.login" />
          </div>
          <div class="form__block">
            <VInput placeholder="Пароль" v-model="data.password" />
          </div>
          <div class="form__block">
            <VDropdown
              :list="sortedRolesWithAdmin"
              v-model="data.role"
              non-placeholder
            />
          </div>
        </form>
        <div
          v-if="store.user.role.id === 1 && !formActive"
          @click="addUser"
          class="btn-add"
        >
          <img src="/img/icons/plus.svg" alt="" /> Добавить пользователя
        </div>
        <div v-if="formActive" @click="sendUser" class="btn success">
          <img src="/img/icons/plus.svg" alt="" />Добавить
        </div>
        <div v-if="formActive" @click="closeForm" class="btn delete">
          <img src="/img/icons/plus.svg" alt="" />Отмена
        </div>
      </div>
    </header>
    <div class="page__content">
      <div class="page__content-list">
        <div v-for="item in sortedUsers" :key="item" class="item bg-item">
          <span class="item-title"
            >{{ item.login }}
            <span v-if="item.login === store.user.login"> - вы</span>
          </span>
          <div
            :class="[
              'item-title',
              { online: item.online },
              { offline: !item.online },
            ]"
          >
            {{ item.online ? 'В сети' : 'Не в сети' }}
            <span
              v-if="item.active_team && item.role.title === 'ROLE_USER'"
              :style="[{ color: item?.active_team?.color }]"
              >{{ item?.active_team?.title }}</span
            >
          </div>
          <div v-if="item.role.id !== 1" class="item-role">
            <VDropdown
              :list="sortedRolesWithAdmin"
              v-model="item.role"
              @change="updateRole(item)"
              non-placeholder
            />
          </div>
          <div v-else class="item-role admin">Админ</div>
          <div
            v-if="item.role.id !== 1"
            @click="deleteUser(item.id)"
            class="btn delete"
          >
            <img src="/img/icons/plus.svg" alt="" />Удалить
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import '@/assets/scss/variables';

.page {
  display: flex;

  &__content {
    width: 100%;
    display: flex;
    flex-direction: column;
  }
}
</style>
