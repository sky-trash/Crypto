<script setup>
import { computed, onMounted, ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useStateStore } from '@/store/stateStore.js'
import VSearch from '@/components/VSearch.vue'
import VDropdown from '@/components/VDropdown.vue'

const router = useRouter()
const route = useRoute()
const store = useStateStore()

const searchValue = ref('')
const activeTeam = ref({})
const forms = ref()

const sortedList = computed(() => {
  if (store.user.role.title === 'ROLE_USER') {
    if (activeTeam.value?.title) {
      return forms.value
        .filter((item) => item.team?.title === activeTeam.value?.title)
        .filter(
          (item) =>
            item.name
              ?.toLowerCase()
              .includes(searchValue.value?.toLowerCase()) ||
            item.bankNumberNow
              ?.toLowerCase()
              .includes(searchValue.value?.toLowerCase())
        )
        .filter((item) => item?.status !== null)
        .sort((a, b) => {
          if (a?.status?.id === 1 && b?.status?.id !== 1) {
            return -1
          } else if (a?.status?.id !== 1 && b?.status?.id === 1) {
            return 1
          } else {
            return 0
          }
        })
    } else
      return forms.value
        .filter(
          (item) =>
            item.name
              ?.toLowerCase()
              .includes(searchValue.value?.toLowerCase()) ||
            item.bankNumberNow
              ?.toLowerCase()
              .includes(searchValue.value?.toLowerCase())
        )
        .filter((item) => item?.status !== null)
        .sort((a, b) => {
          if (a?.status?.id === 1 && b?.status?.id !== 1) {
            return -1
          } else if (a?.status?.id !== 1 && b?.status?.id === 1) {
            return 1
          } else {
            return 0
          }
        })
  } else {
    if (activeTeam.value?.title) {
      return forms.value
        .filter((item) => item.team?.title === activeTeam.value?.title)
        .filter(
          (item) =>
            item.name
              ?.toLowerCase()
              .includes(searchValue.value?.toLowerCase()) ||
            item.bankNumberNow
              ?.toLowerCase()
              .includes(searchValue.value?.toLowerCase())
        )
        .sort((a, b) => {
          if (a?.status?.id === 1 && b?.status?.id !== 1) {
            return -1
          } else if (a?.status?.id !== 1 && b?.status?.id === 1) {
            return 1
          } else {
            return 0
          }
        })
    } else
      return forms.value
        .filter(
          (item) =>
            item.name
              ?.toLowerCase()
              .includes(searchValue.value?.toLowerCase()) ||
            item.bankNumberNow
              ?.toLowerCase()
              .includes(searchValue.value?.toLowerCase())
        )
        .sort((a, b) => {
          if (a?.status?.id === 1 && b?.status?.id !== 1) {
            return -1
          } else if (a?.status?.id !== 1 && b?.status?.id === 1) {
            return 1
          } else {
            return 0
          }
        })
  }
})

const toForm = (id) => {
  router.push({ name: 'form', params: { id: id } })
}

const addForm = () => {
  router.push('/form-add')
}

const changeStatus = (data) => {
  store.editForm(data)
}

await store.getUser()
await store.getTeams()
await store.getForms().then(() => (forms.value = store.forms))
await store.getStatuses()
await store.getDrops()

onMounted(() => {
  if (route.query.drop) {
    forms.value = store.forms.filter(
      (item) => item?.drop_manager?.id === +route.query.drop
    )
  }
})
</script>
<template>
  <div class="page">
    <header class="header">
      <div class="left">
        <div class="subtitle">
          Анкеты
          {{ route.query.drop ? 'дроповода ' : '' }}
          <span v-if="route.query.drop">
            {{
              store.drops[
                store.drops.findIndex((item) => item.id === +route.query.drop)
              ].name
            }}
          </span>
        </div>
        <VSearch v-model="searchValue" />
        <div class="dropdown-block">
          <VDropdown :list="store.teams" v-model="activeTeam" />
        </div>
      </div>
      <div class="right">
        <div
          v-if="store?.user?.role?.id === 1"
          @click="addForm"
          class="btn-add"
        >
          <img src="/img/icons/plus.svg" alt="" /> Добавить анкету
        </div>
      </div>
    </header>
    <div class="page__content">
      <div
        v-if="
          (store.user.role.title === 'ROLE_USER' &&
            store.user.active_team?.title) ||
          store.user.role.title === 'ROLE_ADMIN'
        "
        class="page__content-list"
      >
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
            <div class="item-team">
              <span
                v-if="item.team"
                :style="[{ background: item.team.color }]"
                >{{ item.team.title }}</span
              >
            </div>
          </div>
        </TransitionGroup>
      </div>
      <div class="subtitle" v-else>Для просмотра анкет выберите команду</div>
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
