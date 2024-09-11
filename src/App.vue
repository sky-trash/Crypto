<script setup lang="ts">
import { onBeforeUnmount, onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useStateStore } from '@/store/stateStore'

import { useLogin } from '@/utils/useLogin.js'
import VLoader from '@/components/VLoader.vue'
import VAside from '@/components/VAside.vue'
import { useToast } from 'vue-toastification'

const route = useRoute()
const router = useRouter()
const store = useStateStore()
const stateStore = useStateStore()
const { isAuth } = useLogin()
const theme = ref(false)
const timer = ref(0)

// onMounted(() => {
//   if (!localStorage.getItem('theme')) {
//     localStorage.setItem(
//       'theme',
//       window.matchMedia('(prefers-color-scheme: dark)').matches
//         ? 'dark'
//         : 'light'
//     )
//     theme.value = localStorage.getItem('theme')
//   } else {
//     theme.value = localStorage.getItem('theme')
//   }
//   console.log(theme.value)
// })

const inactivityTime = () => {
  const resetTimer = () => {
    timer.value = 0
  }
  setInterval(() => {
    timer.value++
    if (timer.value >= 300) {
      resetTimer()
      store.editUserOnline(store.user.id, false)
    }
  }, 1000)
  // сюда можно добавить любой ивент.
  document.addEventListener('mousemove', resetTimer)
  document.addEventListener('keypress', resetTimer)
  document.addEventListener('touch', resetTimer)
}

const toast = useToast()
const showNotification = async () => {
  const userOnlines = store.user
  await store.getToDoListTask(userOnlines.id)
  const task = store.todolistuser.length
  toast.info(`У вас новых задач - ${task}`, {
    position: 'bottom-right',
    timeout: false,
    closeOnClick: true,
    pauseOnFocusLoss: true,
    pauseOnHover: true,
    draggable: true,
    draggablePercent: 0.6,
    showCloseButtonOnHover: false,
    hideProgressBar: true,
    closeButton: 'button',
    icon: true,
    rtl: false,
  })
}

let timerId
let timeLeft = 3600000 // 2 минуты в миллисекундах
let lastTimeChecked = Date.now()

const startNotificationTimer = () => {
  timerId = setTimeout(() => {
    showNotification()
    timeLeft = 3600000 // Сбрасываем оставшееся время после уведомления
    startNotificationTimer()
  }, timeLeft)
}

const pauseNotificationTimer = () => {
  if (timerId) {
    clearTimeout(timerId)
    timeLeft -= Date.now() - lastTimeChecked
  }
}

const resumeNotificationTimer = () => {
  lastTimeChecked = Date.now()
  startNotificationTimer()
}

const handleVisibilityChange = () => {
  if (document.hidden) {
    pauseNotificationTimer()
  } else {
    resumeNotificationTimer()
  }
}

onMounted(() => {
  showNotification
  startNotificationTimer()
  document.addEventListener('visibilitychange', handleVisibilityChange)
})

onBeforeUnmount(() => {
  if (timerId) {
    clearTimeout(timerId)
  }
  document.removeEventListener('visibilitychange', handleVisibilityChange)
})
</script>

<template>
  <main :class="['main', { light: !theme }, { dark: theme }]">
    <VAside v-if="route.path !== '/'" />
    <div class="main__content">
      <RouterView v-slot="{ Component }">
        <template v-if="Component">
          <transition name="fade-page" mode="out-in">
            <suspense>
              <component :is="Component" :key="route.fullPath"></component>
            </suspense>
          </transition>
        </template>
      </RouterView>
    </div>
    <VLoader v-if="stateStore.isLoading" />
  </main>
</template>

<style lang="scss" scoped>
@import '@/assets/scss/variables';
.main {
  &__content {
    width: 100%;
    display: flex;
    flex-direction: column;
    background-color: #edf2f6;
  }
}
</style>
