<script setup>
import { onErrorCaptured, onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useStateStore } from '@/store/stateStore.js'
import VInput from '@/components/VInput.vue'
import VDropdown from '@/components/VDropdown.vue'

const router = useRouter()
const store = useStateStore()

const formActive = ref(false)

const data = ref({
  title: '',
  color: '#435fe5',
})

const toTeam = (id) => {
  router.push({ name: 'team', params: { id: id } })
}

const addTeam = () => {
  formActive.value = true
}

const closeForm = () => {
  formActive.value = false
}

const sendTeam = async () => {
  await store.addTeam(data.value)
  formActive.value = false
  data.value = {
    title: '',
    color: '#435fe5',
  }
  await store.getTeams()
}

await store.getUser()
await store.getTeams()

onMounted(() => {
  if (store.user.role.id !== 1) router.push('/home')
})
</script>
<template>
  <div class="page">
    <header class="header">
      <div class="left">
        <div class="subtitle">Команды</div>
      </div>
      <div class="right">
        <form v-if="formActive" class="form">
          <div class="form__block">
            <VInput placeholder="Название" v-model="data.title" />
          </div>
          <div class="form__block color">
            <span>Цвет:</span>
            <input type="color" v-model="data.color" />
          </div>
        </form>
        <div
          v-if="store.user.role.id === 1 && !formActive"
          @click="addTeam"
          class="btn-add"
        >
          <img src="/img/icons/plus.svg" alt="" /> Добавить команду
        </div>
        <div v-if="formActive" @click="sendTeam" class="btn success">
          <img src="/img/icons/plus.svg" alt="" />Добавить
        </div>
        <div v-if="formActive" @click="closeForm" class="btn delete">
          <img src="/img/icons/plus.svg" alt="" />Отмена
        </div>
      </div>
    </header>
    <div class="page__content">
      <div class="page__content-list">
        <div
          v-for="item in store.teams"
          :key="item"
          @click="toTeam(item.id)"
          class="item bg-item"
        >
          <span :style="[{ color: item.color }]">{{ item.title }}</span>
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

    &-teams {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 30px;

      @media (max-width: $md2 + px) {
        grid-template-columns: repeat(2, 1fr);
      }

      @media (max-width: $md3 + px) {
        grid-template-columns: repeat(1, 1fr);
      }

      &::-webkit-scrollbar {
        display: none;
      }

      .team {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 320px;
        background-color: #fff;
        border-radius: 30px;
        transition: all 0.3s ease;
        cursor: pointer;
        font-weight: 700;
        font-size: 24px;

        @media (max-width: $md3 + px) {
          height: 220px;
        }

        &:hover {
          box-shadow: inset 0 0 10px 0 rgba(0, 0, 0, 0.2);
        }
      }
    }
  }

  &__header {
  }
}
</style>
