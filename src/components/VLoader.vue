<script setup></script>

<template>
  <div class="loader">
    <div class="loader__content">
      <img src="/img/gif/loader.gif" alt="" />
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import '@/assets/scss/variables';
.loader {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0, 0, 0, 0.4);

  &__content {
    width: 150px;
    height: 100px;
    background-color: #fff;
    border-radius: 10px;
    box-shadow: 0 4px 20px 0 rgba(0, 0, 0, 0.3);

    img {
      width: 100%;
    }
  }
}
</style>
