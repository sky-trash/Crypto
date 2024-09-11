<script setup>
import { computed, ref } from 'vue'
import { useRouter } from 'vue-router'
import VInput from '@/components/VInput.vue'
import { useAuth } from '@/utils/useAuth.js'
import { useToken } from '@/utils/useToken.js'
import { useLogin } from '@/utils/useLogin.js'

const authError = ref(false)
const router = useRouter()
const { setToken } = useToken()
const { login } = useLogin()

const data = ref({
  username: '',
  password: '',
})

const btnDisabled = computed(() => !data.value.username || !data.value.password)

const auth = async () => {
  authError.value = false
  const { response, error } = await useAuth(data.value)

  if (error.value) {
    authError.value = error.value.response.data.message
    return
  }

  setToken(response.value.access_token)
  await login()
  await router.push('/home')
}
</script>

<template>
  <div class="page">
    <form @submit.prevent="auth" class="form">
      <div class="title">Sign in</div>
      <div class="form__input">
        <VInput type="text" placeholder="login" v-model="data.username" />
      </div>
      <div class="form__input">
        <VInput
          type="password"
          placeholder="password"
          v-model="data.password"
        />
      </div>
      <div class="form__input">
        <input
          type="submit"
          value="Войти"
          :class="['form__submit', { disabled: btnDisabled }]"
        />
      </div>
    </form>
  </div>
</template>

<style lang="scss" scoped>
@import '@/assets/scss/variables';

.page {
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(to left, #3494e6, #ec6ead);
  padding: 20px;

  .form {
    display: flex;
    flex-direction: column;
    gap: 30px;
    padding: 30px;
    background-color: #fff;
    border-radius: 30px;
    box-shadow: 0 4px 20px 0 rgb(0, 0, 0, 0.15);
    @media (max-width: $md5 + px) {
      width: 100%;
    }

    &__input {
      width: 320px;

      @media (max-width: $md5 + px) {
        width: 100%;
      }
    }

    &__submit {
      display: flex;
      width: 100%;
      background: linear-gradient(to left, #3494e6, #ec6ead);
      color: #fff;
      font-size: 20px;
      font-weight: 700;
      border-radius: 15px;
      height: 48px;
      align-items: center;
      justify-content: center;
      transition: all 0.3s ease;
      cursor: pointer;

      @media (max-width: $md5 + px) {
        font-size: 18px;
      }

      &:hover {
        box-shadow: 0 4px 10px 0 rgba(0, 0, 0, 0.3);
      }

      &.disabled {
        opacity: 0.6;
        pointer-events: none;
      }
    }
  }
}
</style>
