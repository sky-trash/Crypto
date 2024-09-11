<script setup>
import { computed, onMounted, ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useStateStore } from '@/store/stateStore.js'
import VSearch from '@/components/VSearch.vue'
import VInput from '@/components/VInput.vue'
import VDropdown from '@/components/VDropdown.vue'
import PopupConfirm from '@/components/PopupConfirm.vue'
import { vOnClickOutside } from '@vueuse/components'

const router = useRouter()
const route = useRoute()
const store = useStateStore()

const formActive = ref(false)
const menuAddShow = ref(false)

const isOpenFolder = ref(false)
const isOpenFile = ref(false)

const addFileData = ref({
  name: '',
  // route: [],
})

const addFolderData = ref({
  name: '',
})

await store.getUser()
await store.getTrainingFolders()
await store.getTrainingFiles()

onMounted(() => {
  if (store.user.role.id !== 1) router.push('/home')
})

const addFolderVisible = ref(false)
const addFileVisible = ref(false)
const addFolderValidate = ref(false)
const addFileValidate = ref(false)

const topMenu = ref('0px')
const leftMenu = ref('0px')
const openAddMenu = (event) => {
  if (addFolderVisible.value) return true
  if (addFileVisible.value) return true

  leftMenu.value = event.offsetX + 'px'
  topMenu.value = event.offsetY + 'px'

  menuAddShow.value = !menuAddShow.value
}

const toTrainingFolder = (id) => {
  router.push({ name: 'training', params: { id: id } })
}

const deleteFolderId = ref()
const deleteTrainingFolder = async (id) => {
  deleteFolderId.value = id
  isOpenFolder.value = true
}
const confirmFolder = async () => {
  await store.deleteTrainingFolder(deleteFolderId.value)

  // Обновление данных
  await store.getTrainingFolders()
}

const sendTrainingFolder = async () => {
  if (addFolderData.value.name) {
    await store.addTrainingFolder(addFolderData.value)

    addFolderValidate.value = false
    addFolderVisible.value = false
    addFolderData.value = {
      name: '',
    }

    await store.getTrainingFolders()
  } else {
    addFolderValidate.value = true
  }
}

// const toTrainingFile = (id) => {
//   router.push({ name: 'training', params: { id: id } })
// }


// const uploadFiles = () => {
//   const file = document.getElementById('route')
//   const uploadedFiles = Array.from(file.route)
//   uploadedFiles.forEach((route) => {
//     addFileData.value.files.push(route)
//   })
// }

const deleteFileId = ref()
const deleteTrainingFile = async (id) => {
  deleteFileId.value = id
  isOpenFile.value = true
}

const confirmFile = async () => {
  await store.deleteTrainingFile(deleteFileId.value)

  // Обновление данных
  await store.getTrainingFiles()
}

const sendTrainingFile = async () => {
  if (addFileData.value.name) {
    await store.addTrainingFile(addFileData.value)

    addFileValidate.value = false
    addFileVisible.value = false
    addFileData.value = {
      name: '',
      route: [],
    }

    await store.getTrainingFiles()
  } else {
    addFileValidate.value = true
  }
}
</script>
<template>
  <div class="page" @mousedown.right="openAddMenu($event)" @contextmenu.prevent>
    <PopupConfirm @good="confirmFile" v-model="isOpenFile" />
    <PopupConfirm @good="confirmFolder" v-model="isOpenFolder" />
    <header class="header">
      <div class="left">
        <div class="subtitle">Правила и обучение</div>
      </div>
    </header>
    <div class="folder_container">
      <!-- Папки -->
      <div
        v-for="item in store.training_folders"
        :key="item"
        class="folder_content"
      >
        <div
          class="folder_content_directory"
          @click="toTrainingFolder(item.id)"
        >
          <img src="/img/icons/folder.svg" alt="" />
        </div>
        <div
          v-if="store.user.role.id === 1 && !isEdit"
          @click="deleteTrainingFolder(item.id)"
          class="folder_content_close"
        >
          <img src="/img/icons/cross.svg" alt="" />
        </div>
        <div @click="toTrainingFolder(item.id)" class="folder_content_text">
          <span>{{ item.name }}</span>
        </div>
      </div>
      <!-- Файлы -->
       <!-- <a :src="API + '/' + file" download> -->
      <div
        v-for="item in store.training_files"
        :key="item"
        class="file_content"
      >
        <div class="file_content_directory">
          <img src="/img/icons/file.svg" alt="" />
        </div>
        <div
          v-if="store.user.role.id === 1 && !isEdit"
          @click="deleteTrainingFile(item.id)"
          class="file_content_close"
        >
          <img src="/img/icons/cross.svg" alt="" />
        </div>
        <div class="file_content_text">
          <span>{{ item.name }}</span>
        </div>
      </div>
    <!-- </a> -->
    </div>
    <Transition name="fade">
      <div
        class="menu-add"
        v-if="menuAddShow"
        v-on-click-outside="
          () => {
            menuAddShow = false
          }
        "
      >
        <div
          class="menu-add_item"
          @click="
            () => {
              addFileVisible = !addFileVisible
              menuAddShow = !menuAddShow
            }
          "
          id="add_file"
        >
          Добавить файл
        </div>
        <div
          class="menu-add_item"
          @click="
            () => {
              addFolderVisible = !addFolderVisible
              menuAddShow = !menuAddShow
            }
          "
          id="add_folder"
        >
          Добавить папку
        </div>
      </div>
    </Transition>

    <!-- Модальное окно -->
    <div class="v-popup-overlay" v-if="addFolderVisible"></div>
    <Transition name="fade">
      <div
        class="v-popup"
        @close_add_folder="close_add_folder"
        v-show="addFolderVisible"
      >
        <div class="v-popup_header">
          <div class="v-popup_header_text">
            <h1>Добавить папку</h1>
          </div>
          <div class="v-popup_header_image">
            <img
              @click="addFolderVisible = !addFolderVisible"
              src="/img/icons/cross.svg"
              alt=""
            />
          </div>
        </div>
        <hr />
        <div class="v-popup_content">
          <div class="v-popup_content_text">
            <p>Название папки:</p>
          </div>
          <div class="v-popup_content_input">
            <input v-model="addFolderData.name" type="text" />
          </div>
          <div class="v-popup_content_text_error" v-if="addFolderValidate">
            <p>Введите название папки</p>
          </div>
        </div>
        <div class="v-popup_footer">
          <div @click="sendTrainingFolder" class="btn-add">Добавить</div>
        </div>
      </div>
    </Transition>
    <!-- Модальное окно -->
    <!-- Модальное окно -->
    <div class="v-popup-overlay" v-if="addFileVisible"></div>
    <Transition name="fade">
      <div
        class="v-popup"
        @close_add_file="close_add_file"
        v-show="addFileVisible"
      >
        <div class="v-popup_header">
          <div class="v-popup_header_text">
            <h1>Добавить файл</h1>
          </div>
          <div class="v-popup_header_image">
            <img
              @click="addFileVisible = !addFileVisible"
              src="/img/icons/cross.svg"
              alt=""
            />
          </div>
        </div>
        <hr />
        <div class="v-popup_content">
          <div class="v-popup_content_text">
            <p>Название файла:</p>
          </div>
          <div class="v-popup_content_input">
            <input v-model="addFileData.name" type="text" />
          </div>
          <div class="v-popup_content_text_error" v-if="addFileValidate">
            <p>Введите название файла</p>
          </div>
        </div>
        <div class="v-popup_footer btn-add">
          <input
            @change="uploadFiles"
            type="file"
            name="file"
            id="file"
            class="input-file"
            accept="file/*"
            multiple
          />
        </div>
        <div class="v-popup_footer">
          <div @click="sendTrainingFile" class="btn-add">Добавить</div>
        </div>
      </div>
    </Transition>
    <!-- Модальное окно -->
  </div>
</template>

<style lang="scss">
.page {
  position: relative;
}
.menu-add {
  position: absolute;
  top: v-bind('topMenu');
  left: v-bind('leftMenu');
  z-index: 5;

  background-color: #fff;
  border-radius: 8px;
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
.folder_container {
  display: flex;
  flex-wrap: wrap;
  gap: 50px;

  margin-top: 80px;
  padding: 30px 0 30px 30px;
  @media screen and (max-width: 768px) {
    margin-top: 0px;
  }
}
.folder_content {
  position: relative;
  &_directory {
    img {
      width: 75px;
      height: auto;
    }
  }
  &_close {
    position: absolute;
    top: 0px;
    right: 0px;
    img {
      width: 17px;
      height: auto;
    }
  }
  &_text {
    position: absolute;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    width: 125px;
  }
  &_text:hover {
    white-space: wrap;
  }
}
.file_content {
  &_directory {
    img {
      width: 67px;
      height: auto;
    }
  }
  &_close {
    position: absolute;
    margin: -4.6% 0 0 3.3%;
    img {
      width: 17px;
      height: auto;
    }
  }
  &_text {
    position: absolute;
    margin: 7px 0 0 0;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    width: 125px;
  }
  &_text:hover {
    white-space: wrap;
  }
}
.v-popup_content_text_error p {
  color: red;
}
.v-popup_footer .btn-add {
  padding: 7px 20px;
}
</style>
