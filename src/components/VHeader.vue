<script setup>
import { useRouter } from 'vue-router'
import { useStateStore } from '@/store/stateStore.js'
import { useLogin } from '@/utils/useLogin.js'

const router = useRouter()
const { logout } = useLogin()
const store = useStateStore()

const exit = () => {
  store.editUserOnline(store.user.id, false)
  logout()
  router.push({ name: 'login' })
}
</script>

<template>
  <header class="header">
    <div class="header__user">{{ store.user.login }}</div>
    <div @click="exit" class="header__logout">
      <img src="/img/icons/exit.svg" alt="" />
    </div>
  </header>
</template>

<style scoped lang="scss">
.header {
  width: calc(100% - 30px);
  background-color: #fff;
  margin-top: 30px;
  padding: 20px;
  border-radius: 0 10px 10px 0;
  box-shadow: 0 4px 20px 0 rgba(0, 0, 0, 0.15);
  display: flex;
  justify-content: flex-end;
  align-items: center;
  gap: 30px;

  &__user {
    font-size: 20px;
    font-weight: 700;
  }

  &__logout {
    width: 32px;
    cursor: pointer;
    img {
      width: 100%;
    }
  }
}
</style>
