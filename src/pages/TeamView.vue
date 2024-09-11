<script setup>
import { useRoute, useRouter } from 'vue-router'
import { useStateStore } from '@/store/stateStore.js'
import { computed, onErrorCaptured, onMounted, ref } from 'vue'
import PopupConfirm from '@/components/PopupConfirm.vue'
import VInput from '@/components/VInput.vue'
import VDropdown from '@/components/VDropdown.vue'
import VSearch from '@/components/VSearch.vue'

const router = useRouter()
const route = useRoute()
const store = useStateStore()

const searchValue = ref('')
const isOpen = ref(false)
const isEdit = ref(false)

const deleteTeam = async () => {
  isOpen.value = true
}

const toTeams = () => {
  router.push('/teams')
}

const startEdit = () => {
  isEdit.value = true
}

const closeForm = async () => {
  isEdit.value = false
  await store.getTeam(route.params.id)
}

const sendForm = async () => {
  await store.editTeam(store.team)
  isEdit.value = false
  await store.getTeam(route.params.id)
}

const confirm = async () => {
  await store.deleteTeam(route.params.id).then(() => router.push('/teams'))
}

const toForm = (id) => {
  router.push({ name: 'form', params: { id: id } })
}
const changeStatus = (data) => {
  store.editForm(data)
}

const sortedList = computed(() =>
  store.forms
    .filter(
      (item) =>
        item.team?.title === store.team?.title &&
        item.name?.toLowerCase().includes(searchValue.value?.toLowerCase())
    )
    .sort((a, b) => a.status.id - b.status.id)
)

await store.getUser()
await store.getTeam(route.params.id)
await store.getStatuses()
await store.getForms()

onMounted(() => {
  if (store.user.role.id !== 1) router.push('/home')
})
</script>
<template>
  <div class="page">
    <PopupConfirm @good="confirm" v-model="isOpen" />
    <header class="header">
      <div class="left">
        <img @click="toTeams" src="/img/icons/back.svg" alt="" />
        <div
          v-if="!isEdit"
          class="subtitle"
          :style="[{ color: store.team.color }]"
        >
          {{ store.team.title }}
        </div>
        <VSearch v-if="!isEdit" v-model="searchValue" />
        <div v-if="isEdit" class="form-block">
          <VInput
            v-model="store.team.title"
            placeholder="Название"
            :color="store.team.color"
          />
        </div>
        <div v-if="isEdit" class="form-block">
          <input type="color" v-model="store.team.color" />
        </div>
      </div>
      <div class="right">
        <div
          v-if="store.user.role.id === 1 && !isEdit"
          @click="startEdit"
          class="btn edit"
        >
          <img src="/img/icons/edit.svg" alt="" />
          <span>Изменить</span>
        </div>
        <div v-else @click="sendForm" class="btn success">
          <img src="/img/icons/check.svg" alt="" />
          <span>Сохранить</span>
        </div>
        <div
          v-if="store.user.role.id === 1 && !isEdit"
          @click="deleteTeam"
          class="btn delete"
        >
          <img
            src="/img/icons/trash.svg"
            alt=""
            style="transform: rotate(0deg)"
          />
          <span>Удалить</span>
        </div>
        <div
          v-if="store.user.role.id === 1 && isEdit"
          @click="closeForm"
          class="btn delete"
        >
          <img src="/img/icons/plus.svg" alt="" />
          <span>Отмена</span>
        </div>
      </div>
    </header>
    <div class="page__content">
      <div class="page__content-list">
        <TransitionGroup name="slide">
          <div
            v-for="item in sortedList"
            :key="item"
            @click="toForm(item.id)"
            class="item bg-item"
          >
            <div
              v-if="store.user.role.title === 'ROLE_USER'"
              class="item-status"
              :style="{ color: item.status.color }"
            >
              {{ item.status.title }}
            </div>
            <div v-else class="item-status">
              <div>
                <VDropdown
                  @click.stop
                  @change="changeStatus(item)"
                  :list="store.statuses"
                  v-model="item.status"
                  non-placeholder
                />
              </div>
            </div>
            <div class="item-title">{{ item.name }}</div>
            <div class="item-title">{{ item.bankNumberNow }}</div>
            <div v-if="item.team" class="item-team">
              <span :style="[{ background: item.team.color }]">{{
                item.team.title
              }}</span>
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
  }

  &__header {
  }
}
</style>
