<script setup>
import { computed, onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useStateStore } from '@/store/stateStore.js'
import VSearch from '@/components/VSearch.vue'
import VInput from '@/components/VInput.vue'
import VDropdown from '@/components/VDropdown.vue'
import PopupConfirm from '@/components/PopupConfirm.vue'
// import VDropdown from '@/components/VDropdown.vue'

const router = useRouter()
const store = useStateStore()

const formActive = ref(false)
const searchValue = ref('')
const isEdit = ref()
const isOpen = ref(false)
const confirmStatus = ref()

const sortedList = computed(() =>
  store?.drops.filter(
    (item) =>
      item.name?.toLowerCase().includes(searchValue.value?.toLowerCase()) ||
      item.tg_id?.toLowerCase().includes(searchValue.value?.toLowerCase())
  )
)

const data = ref({
  name: '',
  tg_id: '',
})
const addDrop = () => {
  formActive.value = true
}
const closeForm = () => {
  formActive.value = false
}
const sendDrop = async () => {
  await store.addDrop(data.value)
  formActive.value = false
  data.value = {
    name: '',
    tg_id: '',
  }
  await store.getDrops()
}

const toDrop = (id) => {
  router.push({ name: 'home', query: { drop: id } })
}

const copyDrop = (link) => {
  navigator.clipboard.writeText('https://crm-form.vibromatvey.ru/?drop=' + link)
}

const copyTg = (link) => {
  navigator.clipboard.writeText(link)
}

const startEdit = (id) => {
  isEdit.value = id
}

const openConfirm = (id) => {
  isOpen.value = true
  confirmStatus.value = id
}
const editDrop = (data) => {
  store.editDrop(data)
  isEdit.value = null
}
const endEdit = () => {
  isEdit.value = null
}

const deleteDrop = async () => {
  await store.deleteDrop(confirmStatus.value)
  await store.getDrops()
  confirmStatus.value = false
}

await store.getUser()
await store.getDrops()
</script>
<template>
  <div class="page">
    <PopupConfirm @good="deleteDrop" v-model="isOpen" />
    <header class="header">
      <div class="left">
        <div class="subtitle">Дроповоды</div>
        <VSearch v-model="searchValue" />
      </div>
      <div class="right">
        <form v-if="formActive" class="form">
          <div class="form__block">
            <VInput placeholder="Имя" v-model="data.name" />
          </div>
          <div class="form__block">
            <VInput placeholder="@example" v-model="data.tg_id" />
          </div>
        </form>
        <div
          v-if="store.user.role.id === 1 && !formActive"
          @click="addDrop"
          class="btn-add"
        >
          <img src="/img/icons/plus.svg" alt="" /> Добавить дроповода
        </div>
        <div v-if="formActive" @click="sendDrop" class="btn success">
          <img src="/img/icons/plus.svg" alt="" />Добавить
        </div>
        <div v-if="formActive" @click="closeForm" class="btn delete">
          <img src="/img/icons/plus.svg" alt="" />Отмена
        </div>
      </div>
    </header>
    <div class="page__content">
      <div class="page__content-list">
        <TransitionGroup name="slide">
          <div
            v-for="item in sortedList"
            :key="item"
            @click="toDrop(item.id)"
            class="item bg-item"
          >
            <div v-if="isEdit !== item.id" class="item-title">
              {{ item.name }}
            </div>
            <div v-else @click.stop class="inputs">
              <VInput v-model="item.name" />
            </div>
            <div
              v-if="isEdit !== item.id"
              @click.stop
              @click="copyTg(item.tg_id)"
              class="item-title clickable"
            >
              {{ item.tg_id }}
            </div>
            <div v-else @click.stop class="inputs">
              <VInput v-model="item.tg_id" />
            </div>
            <div @click.stop class="item-team">
              <span @click="copyDrop(item.referral)"
                >https://crm-form.vibromatvey.ru/?drop={{ item.referral }}</span
              >
            </div>
            <div @click.stop class="item-actions">
              <div
                v-if="isEdit !== item.id"
                @click="startEdit(item.id)"
                class="btn edit"
              >
                <img src="/img/icons/edit.svg" alt="" />
                Изменить
              </div>
              <div v-else @click="editDrop(item)" class="btn success">
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
        </TransitionGroup>
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
        &-team {
          overflow: hidden;

          span {
            white-space: nowrap;
            text-overflow: ellipsis;
            overflow: hidden;
            color: $primary;

            &:active {
              color: $green;
            }
          }
        }
      }
    }
  }
}
</style>
