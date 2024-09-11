<script setup>
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useStateStore } from '@/store/stateStore.js'
import VInput from '@/components/VInput.vue'
import PopupConfirm from '@/components/PopupConfirm.vue'

const router = useRouter()
const store = useStateStore()

const formActive = ref(false)
const isEdit = ref()
const isOpen = ref(false)
const confirmStatus = ref()

const data = ref({
  title: '',
  color: '#435fe5',
})

const openConfirm = (id) => {
  isOpen.value = true
  confirmStatus.value = id
}

const addStatus = () => {
  formActive.value = true
}

const closeForm = () => {
  formActive.value = false
}

const sendForm = async () => {
  await store.addStatus(data.value)
  await store.getStatuses()
  data.value = {
    title: '',
    color: '#435fe5',
  }
  formActive.value = false
}

const editStatus = (data) => {
  store.editStatus(data)
  isEdit.value = null
}

const startEdit = (id) => {
  isEdit.value = id
}

const endEdit = () => {
  isEdit.value = null
}

const deleteStatus = async () => {
  await store.deleteStatus(confirmStatus.value)
  await store.getStatuses()
  confirmStatus.value = false
}

await store.getUser()
await store.getStatuses()

onMounted(() => {
  if (store.user.role.id !== 1) router.push('/home')
})
</script>
<template>
  <div class="page">
    <PopupConfirm @good="deleteStatus" v-model="isOpen" />
    <header class="header">
      <div class="left">
        <div class="subtitle">Статусы</div>
      </div>
      <div class="right">
        <form v-if="formActive" class="form">
          <div class="form__block">
            <VInput
              placeholder="Название"
              v-model="data.title"
              :color="data.color"
            />
          </div>
          <div class="form__block color">
            <span>Цвет:</span>
            <input type="color" v-model="data.color" />
          </div>
        </form>
        <div
          v-if="store.user.role.id === 1 && !formActive"
          @click="addStatus"
          class="btn-add"
        >
          <img src="/img/icons/plus.svg" alt="" /> Добавить статус
        </div>
        <div v-if="formActive" @click="sendForm" class="btn success">
          <img src="/img/icons/plus.svg" alt="" />Добавть статус
        </div>
        <div v-if="formActive" @click="closeForm" class="btn delete">
          <img src="/img/icons/plus.svg" alt="" />Отмена
        </div>
      </div>
    </header>
    <div class="page__content">
      <div class="page__content-list">
        <div v-for="item in store.statuses" :key="item" class="item bg-item">
          <span v-if="isEdit !== item.id" :style="[{ color: item.color }]">{{
            item.title
          }}</span>
          <div v-else class="inputs">
            <VInput v-model="item.title" :color="item.color" />
            <input type="color" v-model="item.color" />
          </div>
          <div class="item-actions">
            <div
              v-if="isEdit !== item.id"
              @click="startEdit(item.id)"
              class="btn edit"
            >
              <img src="/img/icons/edit.svg" alt="" />
              Изменить
            </div>
            <div v-else @click="editStatus(item)" class="btn success">
              <img src="/img/icons/check.svg" alt="" />
              Сохранить
            </div>
            <div
              v-if="isEdit !== item.id"
              @click="openConfirm(item.id)"
              class="btn delete"
            >
              <img
                src="/img/icons/trash.svg"
                alt=""
                style="transform: rotate(0deg)"
              />
              Удалить
            </div>
            <div v-else @click="endEdit" class="btn delete">
              <img src="/img/icons/plus.svg" alt="" />
              Отмена
            </div>
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

    &-list {
      .item {
        justify-content: space-between;
      }
    }
  }

  .header {
  }
}
</style>
