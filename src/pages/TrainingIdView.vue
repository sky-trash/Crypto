<script setup>
import { onBeforeUnmount, onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useStateStore } from '../store/stateStore'
import useFormatByte from '../utils/useFormatByte'
import PopupConfirm from '@/components/PopupConfirm.vue'

const route = useRoute()
const router = useRouter()

const isLoading = ref(true)
const isOpenFolder = ref(false)
const isOpenFile = ref(false)
const isOpenLink = ref(false)

const store = useStateStore()

const addLinkData = ref({
  link: '',
})

const addFileData = ref({
  name: '',
  folder_id: route.params.id || null,
  // route: '',
})

const addFolderData = ref({
  name: '',
  folder_id: route.params.id || null,
})

const menuAddShow = ref(false)
const addLinkVisible = ref(false)
const addLinkValidate = ref(false)
const addFolderVisible = ref(false)
const addFileVisible = ref(false)
const addFolderValidate = ref(false)
const addFileValidate = ref(false)

const topMenu = ref('0px')
const leftMenu = ref('0px')
const openAddMenu = (event) => {
  if (addFolderVisible.value || addFileVisible.value)
    return true

  leftMenu.value = event.offsetX + 'px'
  topMenu.value = event.offsetY + 'px'

  menuAddShow.value = !menuAddShow.value
}

onMounted(async () => {
  await store.getTrainingFolder(route.params.id)
  await store.getTrainingFilesById(route.params.id)
  await store.getTrainingFoldersById(route.params.id)

  isLoading.value = false
})

const uploadImages = () => {
  const fileImages = document.getElementById('file')
  const uploadedFiles = Array.from(fileImages.files)
  uploadedFiles.forEach((file) => {
    data.value.files.push(file)
  })
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
  await store.getTrainingFoldersById(route.params.id)
}

const sendTrainingFolder = async () => {
  if (addFolderData.value.name) {
    await store.addTrainingFolder(addFolderData.value, addFolderData.value.folder_id)

    addFolderValidate.value = false
    addFolderVisible.value = false
    addFolderData.value = {
      name: '',
      folder_id: route.params.id || null,
    }

    await store.getTrainingFolders()
  } else {
    addFolderValidate.value = true
  }
}

// const toTrainingFile = (id) => {
//   router.push({ name: 'training', params: { id: id } })
// }

const deleteFileId = ref()
const deleteTrainingFile = async (id) => {
  deleteFileId.value = id
  isOpenFile.value = true
}

const confirmFile = async () => {
  await store.deleteTrainingFile(deleteFileId.value)

  // Обновление данных
  await store.getTrainingFilesById(route.params.id)
}

const sendTrainingFile = async () => {
  if (addFileData.value.name) {
    console.log(addFileData.value)

    await store.addTrainingFile(addFileData.value, addFileData.value.folder_id)

    addFileValidate.value = false
    addFileVisible.value = false
    addFileData.value = {
      name: '',
      folder_id: route.params.id || null,
      route: '',
    }

    await store.getTrainingFiles()
  } else {
    addFileValidate.value = true
  }
}


// const deleteLinkId = ref()
// const deleteLink = async (link) => {
//   deleteLinkId.value = link
//   isOpenLink.value = true
// }

// const confirmLink = async () => {
//   await store.deleteLink(deleteLinkId.value)

//   // Обновление данных
//   await store.getLink()
// }

// const sendLink = async () => {
//   if (addLinkData.value.title) {
//     await store.addLink(addLinkData.value)

//     addLinkValidate.value = false
//     addLinkVisible.value = false
//     addLinkData.value = {
//       link: '',
//     }

//     await store.getLinks()
//   } else {
//     addLinkValidate.value = true
//   }
// }
</script>

<template>
  <div class="page" @mousedown.right="openAddMenu($event)" @contextmenu.prevent>
    <PopupConfirm @good="confirmLink" v-model="isOpenLink" />
    <PopupConfirm @good="confirmFile" v-model="isOpenFile" />
    <PopupConfirm @good="confirmFolder" v-model="isOpenFolder" />
    <div class="training_top">
      <div class="breadcrumbs">
        <a href="/training">Правила и обучение</a> /
        <a :href="`/training/${route.params.id}`">{{ store.training_folder.name }}</a>
      </div>

      <div v-if="!isEdit" class="subtitle">
        {{ store.training_folder.name }}
      </div>

      <!-- <div class="form__block-document">
        <img src="/img/icons/doc.svg" alt="" />
        <div class="document-info">
          {{ doc.name }}
          <span>{{ useFormatByte(doc.size, 2, 'MB') }}</span>
        </div>
      </div>
      <div @click="deleteMaterial(index)" class="btn delete">
        <img src="/img/icons/plus.svg" alt="" />Удалить
      </div> -->
    </div>
  <div class="folder_container">
    <div
      class="folder_container"
    >
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
          v-if="store.user.role?.id === 1 && !isEdit"
          @click="deleteTrainingFolder(item.id)"
          class="folder_content_close"
        >
          <img src="/img/icons/cross.svg" alt="" />
        </div>
        <div class="folder_content_text" @click="toTrainingFolder(item.id)">
          <span>{{ item.name }}</span>
        </div>
      </div>
      <!-- Файлы -->
      <div
        v-for="item in store.training_files"
        :key="item"
        class="file_content"
      >
        <div class="file_content_directory">
          <img src="/img/icons/file.svg" alt="" />
        </div>
        <div
          v-if="store.user.role?.id === 1 && !isEdit"
          @click="deleteTrainingFile(item.id)"
          class="file_content_close"
        >
          <img src="/img/icons/cross.svg" alt="" />
        </div>
        <div class="file_content_text">
          <span>{{ item.name }}</span>
        </div>
      </div>
    </div>
    <div class="training_bottom">
      <!-- Ссылка -->
<!-- <div class="link_content">
        <div class="link_content_logo">
          <span>Ссылки</span>
          <div @click="addLinkVisible = !addLinkVisible" class="btn success">
            <img src="/img/icons/plus.svg" alt="" />Добавить ссылку
          </div>
        </div>
        <div class="link_content_main" v-if="store.training_folder.link">
          <a :href="store.training_folder.link">{{
            store.training_folder.link
          }}</a>
          <div @click="deleteLink" class="btn delete">
            <img src="/img/icons/plus.svg" alt="" />Удалить
          </div>
        </div>
      </div> -->
    </div>
    <!-- Меню при клике правой кнопки мыши -->
    <Transition name="fade">
      <div class="menu-add" v-if="menuAddShow">
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
    <!-- Меню при клике правой кнопки мыши -->

    <!-- Модальное окно - папка -->
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
    <!-- Модальное окно - папка -->

    <!-- Модальное окно - файл -->
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
        <div class="v-popup_footer">
          <input class="btn-add" type="file">
        </div>
        <div class="v-popup_footer">
          <div @click="sendTrainingFile" class="btn-add">Добавить</div>
        </div>
      </div>
    </Transition>
    <!-- Модальное окно - файл -->

    <!-- Модальное  - ссылки -->
    <div
      class="v-popup-overlay"
      v-if="addLinkVisible"
    ></div>
    <Transition name="fade">
      <div
        class="v-popup"
        @close_add_link="close_add_link"
        v-show="addLinkVisible"
      >
        <div class="v-popup_header">
          <div class="v-popup_header_text">
            <h1>Добавить ссылку</h1>
          </div>
          <div class="v-popup_header_image">
            <img
              @click="addLinkVisible = !addLinkVisible"
              src="/img/icons/cross.svg"
              alt=""
            />
          </div>
        </div>
        <hr />
        <div class="v-popup_content">
          <div class="v-popup_content_text">
            <p>Название ссылки:</p>
          </div>
          <div class="v-popup_content_input">
            <input v-model="addLinkData.name" type="text" />
          </div>
          <div class="v-popup_content_text_error" v-if="addLinkValidate">
            <p>Введите название ссылки</p>
          </div>
        </div>
        <div class="v-popup_footer">
          <div @click="sendLink" class="btn-add">Добавить</div>
        </div>
      </div>
    </Transition>
    <!-- Модальное окно - ссылки -->
  </div>
</div>
</template>

<style lang="scss">
@import '@/assets/scss/variables';
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

.training_top {
  display: flex;
  flex-direction: column;
  gap: 20px;
  padding: 0 0 0 40px;

  .breadcrumbs {
    margin-top: 16px;
  }
  .form__block {
    display: flex;
    gap: 30px;
    align-items: center;
    @media (max-width: $md1 + px) {
      gap: 0;
      align-items: flex-start;
      flex-direction: column;
      margin-bottom: 20px;
    }

    @media (max-width: $md2 + px) {
      //gap: 10px;
    }

    &.file {
      width: 50%;
      justify-content: space-between;
      align-items: center;
      position: relative;

      @media (max-width: $md2 + px) {
        width: 100%;
        flex-direction: row;

        .btn {
          width: auto;
        }
        .btn-add {
          width: auto;
          min-width: auto;
        }
      }

      .btn-add {
        margin: 0 0 0 auto;
        gap: 12px;
      }
    }

    &-document {
      display: flex;
      align-items: center;
      gap: 5px;

      img {
        width: 24px;
      }

      .document-info {
        display: flex;
        flex-direction: column;
        gap: 2px;
        font-size: 14px;

        span {
          font-size: 10px;
          font-style: italic;
        }
      }
    }
  }
}
.folder_container {
  display: flex;
  flex-wrap: wrap;
  gap: 40px;
  margin: 0 0 0 0;

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
.training_bottom {
  min-width: 1575px;
  @media screen and (max-width: 1440px) {
    max-width: 1440px;
  }
  @media screen and (max-width: 1024px) {
    max-width: 1024px;
  }
  @media screen and (max-width: 768px) {
    max-width: 768px;
    margin-top: 20px;
  }
  .link_content {
    margin: 0px 30px;
    .btn {
      width: fit-content !important;
    }
    &_logo {
      display: flex;
      align-items: center;
      justify-content: space-between;

      padding: 16px;

      background-color: #ebebeb;
      border: 1px solid #5c5c5c;
      border-radius: 7px 7px 0px 0px;
      span {
      }
      .success {
        background-color: $light-blue;
      }
    }
    &_main {
      display: flex;
      align-items: center;
      justify-content: space-between;

      padding: 16px;

      border-radius: 0 0 7px 7px;
      border: 1px solid #5c5c5c;
      span {
        color: #5696ff;
        text-decoration: underline;

        overflow: hidden;
        text-overflow: ellipsis;
        @media screen and (max-width: 425px) {
          max-width: 150px;
        }
      }
    }
  }
}
.v-popup_content_text_error p {
  color: red;
}
.v-popup_footer .btn-add {
  padding: 7px 20px;
}
</style>
