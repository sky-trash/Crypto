<script setup>
import { computed, onMounted, ref, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useStateStore } from '@/store/stateStore.js'
import { useLogin } from '@/utils/useLogin.js'
import VDropdown from '@/components/VDropdown.vue'

const router = useRouter()
const route = useRoute()
const store = useStateStore()

defineProps({
  theme: {
    type: String,
    default: 'light',
  },
})

const isOpen = ref(false)
const activeTeam = ref({})

const { logout } = useLogin()

const list = [
  { id: 0, title: 'Анкеты', path: '/home', role: 0 },
  { id: 1, title: 'Команды', path: '/teams', role: 1 },
  { id: 2, title: 'Пользователи', path: '/users', role: 1 },
  { id: 3, title: 'Статусы', path: '/statuses', role: 1 },
  { id: 4, title: 'Дроповоды', path: '/drops', role: 1 },
  { id: 5, title: 'Список дел', path: '/todolist', role: 0 },
  { id: 6, title: 'Правила и обучение', path: '/training', role: 1 },
]
const themes = [{ title: 'Тёмная' }, { title: 'Светлая' }]

const clickTimeout = ref(null)
const isRouting = ref(false)

const sortedList = computed(() => {
  if (store?.user?.role?.id === 1) return list
  else if (store?.user?.role?.id === 4)
    return list.filter((item) => item.id === 0 || item.id === 2)
  else return list.filter((item) => item.role !== 1)
})

const setActiveItem = (item) => {
  clickTimeout.value = null
  if (!isRouting.value) {
    isRouting.value = true
    router.push(item.path)
    isOpen.value = false
    clickTimeout.value = setTimeout(() => {
      isRouting.value = false
      clearTimeout(clickTimeout.value)
    }, 1000)
  }
}

const close = () => {
  isOpen.value = false
}

const open = () => {
  isOpen.value = true
}

const exit = () => {
  store.editUserOnline(store.user.id, false)
  store.user.active_team = null
  store.editUser(store.user)
  logout()
  router.push({ name: 'login' })
}

const changeTeam = () => {
  if (!activeTeam.value?.title) {
    store.user.active_team = null
    router.push('/home')
  } else store.user.active_team = activeTeam.value
  store.editUser(store.user)
}

watch(
  () => store.user,
  (user) => {
    if (user.active_team) activeTeam.value = user.active_team
  }
)

onMounted(async () => {
  await store.getTeams()
})
</script>

<template>
  <div @click="open" class="aside-open">
    <img src="/img/icons/burger.svg" alt="" />
  </div>
  <div @click="close" :class="['aside-bg', { active: isOpen }]"></div>
  <aside :class="['aside', { active: isOpen }, { disabled: isRouting }]">
    <div @click="close" class="aside-close">
      <img src="/img/icons/plus.svg" alt="" />
    </div>
    <div class="title">Crypto</div>
    <div class="aside__list">
      <div
        v-for="item in sortedList"
        :key="item"
        @click="setActiveItem(item)"
        :class="['aside__list-item', { active: route.path === item.path }]"
      >
        {{ item.title }}
      </div>
    </div>
    <div class="aside__user">
      <VDropdown
        v-if="store.user?.role?.id === 2"
        @change="changeTeam"
        :list="store.teams"
        v-model="activeTeam"
      />
      <div class="user">
        {{ store.user.login }}
      </div>
      <div @click="exit" class="exit">Выйти</div>
    </div>
  </aside>
</template>

<style scoped lang="scss">
@import '@/assets/scss/variables';

.aside {
  height: 100vh;
  flex: 0 0 280px;
  background-color: $primary;
  display: flex;
  flex-direction: column;
  padding: 30px 0;
  box-shadow: -20px 0px 20px 20px rgba(0, 0, 0, 0.5);
  position: relative;
  z-index: 3;
  transition: all 0.3s ease;

  @media (max-width: $md1 + px) {
    flex: 0 0 280px;
  }

  @media (max-width: $md2 + px) {
    box-shadow: 0 20px 20px 0 rgba(0, 0, 0, 0.5);
    position: absolute;
    width: 280px;
    right: -280px;
    z-index: 3;

    &.active {
      right: 0;
    }
  }

  &.disabled {
    pointer-events: none;
  }

  &-close {
    position: absolute;
    right: 20px;
    transform: rotate(45deg);
    display: none;

    @media (max-width: $md2 + px) {
      display: block;
    }

    img {
      width: 24px;
    }
  }

  &-bg {
    display: block;
    content: '';
    background-color: rgba(0, 0, 0, 0.6);
    position: absolute;
    inset: 0;
    z-index: 3;
    opacity: 0;
    transition: all 0.3s ease;
    pointer-events: none;

    &.active {
      pointer-events: all;
      opacity: 1;
    }
  }

  &-open {
    position: absolute;
    z-index: 3;
    width: 32px;
    right: 20px;
    top: 20px;
    display: none;
    @media (max-width: $md2 + px) {
      display: block;
    }

    img {
      width: 100%;
    }
  }

  .title {
    color: #fff;
  }

  &__list {
    margin-top: 50px;
    display: flex;
    flex-direction: column;

    &-item {
      height: 60px;
      border-bottom: 1px solid #fff;
      display: flex;
      align-items: center;
      color: #fff;
      padding: 0 12px;
      font-size: 14px;
      font-weight: 700;
      cursor: pointer;
      user-select: none;

      &.active {
        background-color: #fff;
        color: $primary;
      }
    }
  }

  &__user {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 20px;
    color: #fff;
    font-weight: 600;
    margin-top: auto;
    padding: 0 20px;

    .user {
      font-size: 20px;
      padding: 0 20px;
    }

    .exit {
      font-size: 14px;
      text-decoration: underline;
      cursor: pointer;
    }

    .dropdown {
      flex: 0 0 auto;
      width: 100%;
    }
  }
}
</style>
