<script setup lang="ts">
import { computed, onBeforeUnmount, onMounted, ref } from 'vue'
import { useStateStore } from '@/store/stateStore.js'
import VInput from '@/components/VInput.vue'
import PopupConfirm from '@/components/PopupConfirm.vue'
import VDropdownUser from '@/components/VDropdownUser.vue'
import { Value } from 'sass'
import { vOnClickOutside } from '@vueuse/components'
import { da } from 'date-fns/locale'

const store = useStateStore()
await store.getUsers()
const formActive = ref(false)
const menuShow = ref()
const isEdit = ref()
const task = ref()
const dataUser = ref()
const isOpen = ref(false)
const confirmToDoList = ref()
let todolistErorTitle = ''
let todolistErorDescription = ''
let todolistErorUser = ''

const addToDoList = (category) => {
  formActive.value = true
  data.value.category_id = category.id
  isEdit.value = null
  itemDrop.value = null
  todolistErorTitle = ''
  todolistErorDescription = ''
  todolistErorUser = ''
  return (task.value = category.id)
}
const itemUser = ref({
  user_id: '',
})
const itemDrop = ref()
const itemAll = ref({
  id: '',
  title: '',
  description: '',
  user_name: '',
  category_id: '',
  user_id: {},
})
const data = ref({
  title: '',
  description: '',
  user_name: '',
  category_id: '',
  user_id: {},
})

await store.getToDoLists()

const onDragStart = (e: DragEvent, item) => {
  e.dataTransfer.dropEffect = 'move'
  e.dataTransfer.effectAllowed = 'move'
  e.dataTransfer.setData('itemId', item.id.toString())
  return (itemDrop.value = item)
}

const onDrop = (e: DragEvent, category_id) => {
  const itemId = parseInt(e.dataTransfer.getData('itemId'))
  store.todolists = store.todolists.map((x) => {
    if (x.id == itemId) x.category_id = category_id

    return x
  })
  store.editToDoList(itemDrop.value)
  isEdit.value = null
  formActive.value = false
}
const closeForm = () => {
  formActive.value = false
  todolistErorTitle = ''
  todolistErorDescription = ''
  todolistErorUser = ''
}
const sendToDoList = async () => {
  if (data.value.title == '') {
    todolistErorTitle = 'Заполните название'
    todolistErorDescription = ''
    todolistErorUser = ''
    await store.getToDoLists()
    return todolistErorTitle
  }
  if (data.value.description == '') {
    todolistErorDescription = 'Заполните описание'
    todolistErorTitle = ''
    todolistErorUser = ''
    await store.getToDoLists()
    return todolistErorDescription
  }
  if (!itemUser.value.user_id) {
    todolistErorUser = 'Заполните пользователя'
    todolistErorTitle = ''
    todolistErorDescription = ''
    await store.getToDoLists()

    return todolistErorUser
  } else {
    dataUser.value = data.value.user_id
    data.value.user_id = dataUser.value.id
    data.value.user_name = dataUser.value.login
    await store.addToDoList(data.value)
    formActive.value = false
    data.value = {
      title: '',
      description: '',
      user_name: '',
      category_id: '',
      user_id: '',
    }
    todolistErorTitle = ''
    todolistErorDescription = ''
    todolistErorUser = ''
  }
  await store.getToDoLists()
}
const clickedMenu = ref(false)
const openMenu = (id) => {
  clickedMenu.value = true

  if (menuShow.value == id) {
    menuShow.value = null
  } else if (menuShow.value != id) {
    menuShow.value = null
    menuShow.value = id
  } else if (menuShow.value == null) {
    menuShow.value = id
  }

  clickedMenu.value = false
}
const closeMenu = () => {
  if (!clickedMenu.value) menuShow.value = null
}

const openConfirm = (id) => {
  isOpen.value = true
  confirmToDoList.value = id
}
const startEdit = (item, id, category) => {
  isEdit.value = id
  formActive.value = true
  itemAll.value.category_id = category.id
  itemAll.value.id = item.id
  itemAll.value.title = item.title
  itemAll.value.description = item.description
  itemAll.value.user_name = item.user_name
  itemAll.value.user_id = item.user_id
  todolistErorTitle = ''
  todolistErorDescription = ''
  todolistErorUser = ''
  return (task.value = category.id)
}

const editToDoList = async () => {
  if (itemAll.value.title == '') {
    todolistErorTitle = 'Заполните название'
    todolistErorDescription = ''
    todolistErorUser = ''
    await store.getToDoLists()
    return todolistErorTitle
  }
  if (itemAll.value.description == '') {
    todolistErorDescription = 'Заполните описание'
    todolistErorTitle = ''
    todolistErorUser = ''
    await store.getToDoLists()
    return todolistErorDescription
  }
  if (!itemAll.value.user_id) {
    todolistErorUser = 'Заполните пользователя'
    todolistErorTitle = ''
    todolistErorDescription = ''
    await store.getToDoLists()

    return todolistErorUser
  } else {
    itemDrop.value = itemAll.value
    store.editToDoList(itemDrop.value)
    isEdit.value = null
    formActive.value = false
    itemDrop.value = null
    todolistErorTitle = ''
    todolistErorDescription = ''
    todolistErorUser = ''
    await store.getToDoLists()
  }
  await store.getToDoLists()
}
const endEdit = () => {
  formActive.value = false
  isEdit.value = null
  todolistErorTitle = ''
  todolistErorDescription = ''
  todolistErorUser = ''
  return (itemDrop.value = '')
}
const deleteToDoList = async () => {
  await store.deleteToDoList(confirmToDoList.value)
  await store.getToDoLists()
  confirmToDoList.value = false
  isEdit.value = null
  itemDrop.value = null
  todolistErorTitle = ''
  todolistErorDescription = ''
  todolistErorUser = ''
}
await store.getToDoCategoryes()
</script>

<template>
  <PopupConfirm @good="deleteToDoList" v-model="isOpen" />
  <div class="column">
    <div
      class="column-card"
      v-for="category in store.todocategoryes"
      :key="category.id"
      @drop="onDrop($event, category.id)"
      @dragover.prevent
      @dragenter.prevent
    >
      <div class="column-card__title">{{ category.title }}</div>
      <div
        class="column-card__add-task"
        v-if="(store.user.role.id === 1 && !formActive) || category.id != task"
        @click="addToDoList(category)"
      >
        Добавить новую задачу
      </div>

      <div v-if="category.id == task">
        <form v-if="formActive" class="form">
          <div v-if="isEdit !== itemDrop">
            <div class="form__block">
              <VInput placeholder="Название" v-model="itemAll.title" />
              <div class="todolistEror">
                {{ todolistErorTitle }}
              </div>
            </div>
            <div class="form__block">
              <VInput placeholder="Описание" v-model="itemAll.description" />
              <div class="todolistEror">
                {{ todolistErorDescription }}
              </div>
              <VInput
                type="hidden"
                :modelValue="itemAll.user_name"
                v-model="itemAll.user_name"
              />
              <VInput
                type="hidden"
                :modelValue="itemAll.user_name"
                v-model="itemAll.user_id"
              />
            </div>
            <VDropdownUser
              :modelValue="{ id: itemAll.user_id }"
              @update:modelValue="
                ($event, $events) => {
                  itemAll.user_id = $event

                  $events = $event.login
                  $event = $event.id
                  return (
                    (itemAll.user_name = $events),
                    (itemAll.user_id = $event),
                    (itemUser.user_id = $event)
                  )
                }
              "
              nonPlaceholder
              :list="store.users"
            />
            <div class="todolistEror">
              {{ todolistErorUser }}
            </div>
          </div>
          <div v-else>
            <div class="form__block">
              <VInput placeholder="Название" v-model="data.title" />
              <div class="todolistEror">
                {{ todolistErorTitle }}
              </div>
            </div>
            <div class="form__block">
              <VInput placeholder="Описание" v-model="data.description" />
              <div class="todolistEror">
                {{ todolistErorDescription }}
              </div>
            </div>
            <VDropdownUser
              :modelValue="data.user_id"
              @update:modelValue="
                ($event) => {
                  data.user_id = $event
                  $event = $event.id
                  return (itemUser.user_id = $event)
                }
              "
              nonPlaceholder
              :list="store.users"
            />
            <div class="todolistEror">
              {{ todolistErorUser }}
            </div>
          </div>
          <!-- select -->
        </form>
        <div v-if="formActive">
          <div
            v-if="isEdit !== itemDrop"
            @click="editToDoList()"
            class="btn success"
          >
            <img src="/img/icons/plus.svg" alt="" />Изменить
          </div>
          <div v-else @click="sendToDoList" class="btn success">
            <img src="/img/icons/plus.svg" alt="" />Добавить
          </div>

          <div v-if="isEdit !== itemDrop" @click="endEdit" class="btn delete">
            <img src="/img/icons/plus.svg" alt="" />Отмена
          </div>
          <div v-else @click="closeForm" class="btn delete">
            <img src="/img/icons/plus.svg" alt="" />Отмена
          </div>
        </div>
      </div>
      <div
        class="column-card__task"
        v-for="item in store.todolists.filter(
          (x) => x.category_id === category.id
        )"
        @dragstart="onDragStart($event, item)"
        draggable="true"
      >
        <div class="column-card__task_title">{{ item.title }}</div>
        <div class="column-card__task_description">
          {{ item.description }}
        </div>
        <div class="column-card__task_who">
          <strong>Назначена</strong>: {{ item.user_name }}
        </div>
        <div class="column-card__task_who">
          <strong>Дата создания</strong>: {{ item.date }}
        </div>

        <div @click="openMenu(item.id)" class="column-card__task_svg">
          <svg
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <circle cx="12" cy="5" r="2" fill="black" />
            <circle cx="12" cy="12" r="2" fill="black" />
            <circle cx="12" cy="19" r="2" fill="black" />
          </svg>
        </div>

        <Transition name="fade">
          <div
            class="column-card__menu"
            :class="{
              'column-card__menu--left': category.title == 'Выполнено',
            }"
            v-on-click-outside="closeMenu"
            v-if="menuShow == item.id"
          >
            <div
              class="column-card__menu_item"
              @click="startEdit(item, item.id, category)"
            >
              Редактировать
            </div>
            <div @click="openConfirm(item.id)" class="column-card__menu_item">
              Удалить
            </div>
          </div>
        </Transition>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
@import '@/assets/scss/variables';
:deep(.dropdown__body-item) {
  transition: ease 0.3s;
  &:hover {
    background-color: #e9e9e9;
  }
}
.column {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;

  position: relative;
  text-align: center;

  width: 100%;
  @media screen and (max-width: $md4 + px) {
    grid-template-columns: 1fr;
  }
  &-card {
    position: relative;
    background-color: #fff;
    text-align: left;
    border-radius: 5px;
    padding: 20px;
    border: 1px solid #dee2e6;
    width: 100%;
    height: 100%;
    @media (max-width: 768px) {
      max-width: 100%;
      min-width: 250px;
      width: 100%;
      height: fit-content;
    }
    &__title {
      text-align: center;
      font-size: 20px;
      font-weight: 700;
      margin-bottom: 10px;
      background-color: #5696ff;
      color: #fff;
      padding: 10px 40px;
      border-radius: 5px;
    }
    &__add-task {
      cursor: pointer;
      text-align: center;
      padding: 10px;
      margin: 0 0 30px;
      background-color: #9ecb45;
      font-size: 18px;
      font-weight: 600;
      color: #fff;
      border-radius: 5px;
      &:hover {
        background-color: #8ecb66;
      }
    }
    &__task {
      cursor: grab;
      padding: 10px;
      background-color: #e9e9e9;
      border-radius: 5px;
      transition: ease 0.3s;
      position: relative;
      &_who {
        margin-top: 5px;
        padding: 7px 0;
        line-height: 15px;
        font-size: 14px;
      }
      &_svg {
        position: absolute;
        top: 8px;
        right: 4px;
        width: 24px;
        height: 24px;
        cursor: pointer;
      }
      &:hover {
        background-color: #a5aeb4;
      }
      &:not(:last-child) {
        margin-bottom: 10px;
      }
      &_title {
        font-size: 20px;
        font-weight: 700;
        margin-bottom: 10px;
      }
      &_description {
      }
    }
    &__menu {
      position: absolute;
      top: 0px;
      right: -150px;

      background-color: #fff;
      border-radius: 8px;
      z-index: 3;
      box-shadow: 0px 5px 10px 2px rgba(0, 0, 0, 0.2);
      @media screen and (max-width: $md4 + px) {
        right: 40px;
      }
      &--left {
        top: 34px;
        right: 0px;
      }
      &_item {
        padding: 12px;

        cursor: pointer;
        transition: ease 0.3s;
        &:first-child {
          border-radius: 8px 8px 0px 0px;
        }
        &:last-child {
          border-radius: 0px 0px 8px 8px;
        }
        &:hover {
          background-color: #e9e9e9;
        }
      }
    }
  }
}
.form {
  .dropdown {
    margin-bottom: 10px;
  }
  &__block {
    margin-bottom: 10px;
  }
}
.success {
  width: 100%;
}
.delete {
  width: 100%;
  margin: 5px 0 30px;
}
.todolistEror {
  color: #ea3c41;
  margin-top: 2px;
  font-size: 13px;
  font-weight: 600;
  text-align: start;
}
</style>

