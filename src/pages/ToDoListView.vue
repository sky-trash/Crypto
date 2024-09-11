<script setup>
import { computed, onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useStateStore } from '@/store/stateStore.js'
import VSearch from '@/components/VSearch.vue'
import VInput from '@/components/VInput.vue'
import VDropdown from '@/components/VDropdown.vue'
import PopupConfirm from '@/components/PopupConfirm.vue'
import VTable from '@/components/VTable.vue'

const store = useStateStore()

const searchValue = ref('')

await store.getUser()
await store.getDrops()
</script>
<template>
  <div class="page">
    <header class="header">
      <div class="left">
        <div class="subtitle">Список дел</div>
        <!-- <VSearch v-model="searchValue" /> -->
      </div>
    </header>
    <div class="page__content">
      <div class="page__content-list">
        <TransitionGroup name="slide">
          <VTable />
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
  .droppable {
    padding: 15px;
    border-radius: 5px;
    background: #2c3e50;
    margin-bottom: 10px;
  }

  .droppable h4 {
    color: white;
  }

  .draggable {
    background: white;
    padding: 5px;
    border-radius: 5px;
    margin-bottom: 5px;
  }

  .draggable h5 {
    margin: 0;
  }
}
</style>
