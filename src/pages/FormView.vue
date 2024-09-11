<script setup>
import { onMounted, ref } from 'vue'
import { useStateStore } from '@/store/stateStore.js'
import { useRoute, useRouter } from 'vue-router'
import PopupConfirm from '@/components/PopupConfirm.vue'
import VInput from '@/components/VInput.vue'
import VDropdown from '@/components/VDropdown.vue'
import PopupPhoto from '@/components/PopupPhoto.vue'
import useFormatByte from '@/utils/useFormatByte.js'

const API = window.API
const route = useRoute()
const router = useRouter()
const store = useStateStore()

const tab = ref('info')
const isOpen = ref(false)
const isOpenDeleteImage = ref(false)
const isOpenPhoto = ref(false)
const initialSlide = ref(0)
const isEdit = ref(false)

const activeTeam = ref({})

const nameError = ref(false)
const dateBirthError = ref(false)
const yearError = ref(false)
const passportWhoError = ref(false)
const passportDetailError = ref(false)
const passportAddressError = ref(false)
const addressIndexError = ref(false)
const floorCountError = ref(false)
const passportAddressOldError = ref(false)
const placeBirthError = ref(false)
const addressError = ref(false)
const addressPeopleError = ref(false)
const bankNumberNowError = ref(false)
const bankNumberPastError = ref(false)
const bankEmailError = ref(false)
const educationError = ref(false)
const bankCreditError = ref(false)
const bankClientAtError = ref(false)
const BankCardCityError = ref(false)
const bankPersonVisitError = ref(false)
const bankDepositError = ref(false)
const bankGadgetError = ref(false)
const bankGadgetPastError = ref(false)
const ATMaddressError = ref(false)
const salaryError = ref(false)
const busPriceError = ref(false)
const metroPriceError = ref(false)
const jobError = ref(false)
const transferWhoError = ref(false)
const tenPaymentsError = ref(false)
const cardDetailError = ref(false)
const codeError = ref(false)
const imagesError = ref(false)

const changeTeam = () => {
  store.form.team = activeTeam.value
}

const closeForm = async () => {
  isEdit.value = false
  nameError.value = false
  dateBirthError.value = false
  yearError.value = false
  passportWhoError.value = false
  passportDetailError.value = false
  passportAddressError.value = false
  addressIndexError.value = false
  floorCountError.value = false
  passportAddressOldError.value = false
  placeBirthError.value = false
  addressError.value = false
  addressPeopleError.value = false
  bankNumberNowError.value = false
  bankNumberPastError.value = false
  bankEmailError.value = false
  educationError.value = false
  bankCreditError.value = false
  bankClientAtError.value = false
  BankCardCityError.value = false
  bankPersonVisitError.value = false
  bankDepositError.value = false
  bankGadgetError.value = false
  bankGadgetPastError.value = false
  ATMaddressError.value = false
  salaryError.value = false
  busPriceError.value = false
  metroPriceError.value = false
  jobError.value = false
  transferWhoError.value = false
  tenPaymentsError.value = false
  cardDetailError.value = false
  codeError.value = false
  imagesError.value = false
  await store.getForm(route.params.id)
}

const sendForm = async () => {
  if (
    store.form.name &&
    store.form?.dateBirth?.length === 10 &&
    store.form.year &&
    store.form.passportWho &&
    store.form.passportDetail &&
    store.form.passportAddress &&
    store.form.addressIndex &&
    store.form.floorCount &&
    store.form.passportAddressOld &&
    store.form.placeBirth &&
    store.form.address &&
    store.form.addressPeople &&
    store.form.bankNumberNow &&
    store.form.bankNumberPast &&
    store.form.bankEmail &&
    store.form.education &&
    store.form.bankCredit &&
    store.form.bankClientAt &&
    store.form.BankCardCity &&
    store.form.bankPersonVisit &&
    store.form.bankDeposit &&
    store.form.bankGadget &&
    store.form.bankGadgetPast &&
    store.form.ATMaddress &&
    store.form.salary &&
    store.form.busPrice &&
    store.form.metroPrice &&
    store.form.job &&
    store.form.transferWho &&
    store.form.tenPayments &&
    store.form.cardDetail &&
    store.form.code
  ) {
    await store.editForm(store.form, images.value)
    await store.getForm(route.params.id)
    isEdit.value = false
  } else {
    if (!store.form.name) nameError.value = true
    if (store.form?.dateBirth?.length !== 10) dateBirthError.value = true
    if (!store.form.year) yearError.value = true
    if (!store.form.passportWho) passportWhoError.value = true
    if (!store.form.passportDetail) passportDetailError.value = true
    if (!store.form.passportAddress) passportAddressError.value = true
    if (!store.form.addressIndex) addressIndexError.value = true
    if (!store.form.floorCount) floorCountError.value = true
    if (!store.form.passportAddressOld) passportAddressOldError.value = true
    if (!store.form.placeBirth) placeBirthError.value = true
    if (!store.form.address) addressError.value = true
    if (!store.form.addressPeople) addressPeopleError.value = true
    if (!store.form.bankNumberNow) bankNumberNowError.value = true
    if (!store.form.bankNumberPast) bankNumberPastError.value = true
    if (!store.form.bankEmail) bankEmailError.value = true
    if (!store.form.education) educationError.value = true
    if (!store.form.bankCredit) bankCreditError.value = true
    if (!store.form.bankClientAt) bankClientAtError.value = true
    if (!store.form.BankCardCity) BankCardCityError.value = true
    if (!store.form.bankPersonVisit) bankPersonVisitError.value = true
    if (!store.form.bankDeposit) bankDepositError.value = true
    if (!store.form.bankGadget) bankGadgetError.value = true
    if (!store.form.bankGadgetPast) bankGadgetPastError.value = true
    if (!store.form.ATMaddress) ATMaddressError.value = true
    if (!store.form.salary) salaryError.value = true
    if (!store.form.busPrice) busPriceError.value = true
    if (!store.form.metroPrice) metroPriceError.value = true
    if (!store.form.job) jobError.value = true
    if (!store.form.transferWho) transferWhoError.value = true
    if (!store.form.tenPayments) tenPaymentsError.value = true
    if (!store.form.cardDetail) cardDetailError.value = true
    if (!store.form.code) codeError.value = true
  }
}

const deleteForm = async () => {
  isOpen.value = true
}

const changeDate = (e) => {
  store.form.dateBirth = e.target.value
  dateBirthError.value = false
}

const confirm = async () => {
  await store.deleteForm(route.params.id).then(() => router.push('/home'))
}

const edit = () => {
  isEdit.value = true
  // store.editForm(store.form)
}

const changeTab = (tabName) => {
  tab.value = tabName
}

const photoForDelete = ref({ images: [] })
const deletePhoto = (img) => {
  photoForDelete.value.images.push(img)
  isOpenDeleteImage.value = true
}

const confirmDeleteImage = async () => {
  await store
    .deleteImageFromForm(store.form.id, photoForDelete.value)
    .then(() => {
      photoForDelete.value.images = []
      store.getForm(route.params.id)
      store.getHistory(route.params.id)
    })
}

const openPhoto = (index) => {
  isOpenPhoto.value = true
  initialSlide.value = +index
}

const images = ref([])
const uploadImages = () => {
  const fileImages = document.getElementById('file')
  const uploadedFiles = Array.from(fileImages.files)
  uploadedFiles.forEach((file) => {
    images.value.push(file)
  })
}

const deleteMaterial = (index) => {
  images.value.splice(index, 1)
}

const toHome = () => {
  router.push('/home')
}

await store.getUser()
await store.getTeams()
await store.getForm(route.params.id)
await store.getHistory(route.params.id)

onMounted(() => {
  activeTeam.value =
    store.teams[
      store.teams.findIndex((item) => item?.id === store.form.team?.id)
    ]
  console.log(store.user)
  if (store.user.active_team === null && store.user.role.title === 'ROLE_USER')
    router.push('/home')
})
</script>
<template>
  <div class="page">
    <PopupConfirm v-model="isOpen" @good="confirm" />
    <PopupConfirm v-model="isOpenDeleteImage" @good="confirmDeleteImage" />
    <PopupPhoto
      v-model="isOpenPhoto"
      :list="store.form?.images"
      :initial-slide="initialSlide"
    />
    <header class="header">
      <div class="left">
        <img @click="toHome" src="/img/icons/back.svg" alt="" />
        <div class="subtitle">
          {{ store.form.name }}
        </div>
      </div>
      <div class="right">
        <div
          v-if="store.user.role.id === 1 && !isEdit"
          @click="edit"
          class="btn edit"
        >
          <img src="/img/icons/edit.svg" alt="" />
          <span>Изменить</span>
        </div>
        <div
          v-if="store.user.role.id === 1 && isEdit"
          @click="sendForm"
          class="btn success"
        >
          <img src="/img/icons/check.svg" alt="" />
          <span>Сохранить</span>
        </div>
        <div
          v-if="store.user.role.id === 1 && !isEdit"
          @click="deleteForm"
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
      <div class="page__content-form">
        <div class="tabs">
          <div
            @click="changeTab('info')"
            :class="['tab', { active: tab === 'info' }]"
          >
            Информация
          </div>
          <div
            v-if="store.user.role.id === 1"
            @click="changeTab('history')"
            :class="['tab', { active: tab === 'history' }]"
          >
            История
          </div>
        </div>
        <div v-if="tab === 'info'" class="tab-content">
          <form class="form">
            <div class="form__blocks">
              <div class="form__block">
                <div :class="['form__label', { error: nameError }]">1. ФИО</div>
                <div class="form__input">
                  <VInput
                    v-if="isEdit"
                    placeholder="ФИО"
                    v-model="store.form.name"
                    v-model:error="nameError"
                  />
                  <span v-else>{{ store.form.name }}</span>
                </div>
              </div>
              <div class="form__block">
                <div :class="['form__label', { error: dateBirthError }]">
                  2. Дата рождения
                </div>
                <div class="form__input">
                  <input
                    v-if="isEdit"
                    type="date"
                    @input="changeDate"
                    @change="changeDate"
                    v-model="store.form.dateBirth"
                  />
                  <span v-else>{{ store.form.dateBirth }}</span>
                </div>
              </div>
              <div class="form__block">
                <div :class="['form__label', { error: yearError }]">
                  3. Полный возраст:
                </div>
                <div class="form__input">
                  <VInput
                    v-if="isEdit"
                    placeholder="Полный возраст"
                    v-model="store.form.year"
                    v-model:error="yearError"
                  />
                  <span v-else>{{ store.form.year }}</span>
                </div>
              </div>
              <div class="form__block">
                <div :class="['form__label', { error: passportWhoError }]">
                  4. Где, кем и когда выдан паспорт:
                </div>
                <div class="form__input">
                  <VInput
                    v-if="isEdit"
                    placeholder="Где, кем и когда"
                    v-model="store.form.passportWho"
                    v-model:error="passportWhoError"
                  />
                  <span v-else>{{ store.form.passportWho }}</span>
                </div>
              </div>
              <div class="form__block">
                <div :class="['form__label', { error: passportDetailError }]">
                  5. Серия и номер паспорта:
                </div>
                <div class="form__input">
                  <VInput
                    v-if="isEdit"
                    placeholder="Серия и номер паспорта"
                    v-model="store.form.passportDetail"
                    v-model:error="passportDetailError"
                  />
                  <span v-else>{{ store.form.passportDetail }}</span>
                </div>
              </div>
              <div class="form__block">
                <div :class="['form__label', { error: passportAddressError }]">
                  6. Адрес прописки по паспорту:
                </div>
                <div class="form__input">
                  <VInput
                    v-if="isEdit"
                    placeholder="Адрес"
                    v-model="store.form.passportAddress"
                    v-model:error="passportAddressError"
                  />
                  <span v-else>{{ store.form.passportAddress }}</span>
                </div>
              </div>
              <div class="form__block">
                <div :class="['form__label', { error: addressIndexError }]">
                  7. Индекс по месту прописки:
                </div>
                <div class="form__input">
                  <VInput
                    v-if="isEdit"
                    placeholder="Индекс по месту прописки"
                    v-model="store.form.addressIndex"
                    v-model:error="addressIndexError"
                  />
                  <span v-else>{{ store.form.addressIndex }}</span>
                </div>
              </div>
              <div class="form__block">
                <div :class="['form__label', { error: floorCountError }]">
                  8. Сколько этажей по прописке:
                </div>
                <div class="form__input">
                  <VInput
                    v-if="isEdit"
                    placeholder="Кол-во этажей"
                    v-model="store.form.floorCount"
                    v-model:error="floorCountError"
                  />
                  <span v-else>{{ store.form.floorCount }}</span>
                </div>
              </div>
              <div class="form__block">
                <div
                  :class="['form__label', { error: passportAddressOldError }]"
                >
                  9. Адрес предыдущей прописки полностью:
                </div>
                <div class="form__input">
                  <VInput
                    v-if="isEdit"
                    placeholder="Адрес"
                    v-model="store.form.passportAddressOld"
                    v-model:error="passportAddressOldError"
                  />
                  <span v-else>{{ store.form.passportAddressOld }}</span>
                </div>
              </div>
              <div class="form__block">
                <div :class="['form__label', { error: placeBirthError }]">
                  10. Место рождения:
                </div>
                <div class="form__input">
                  <VInput
                    v-if="isEdit"
                    placeholder="Место рождения"
                    v-model="store.form.placeBirth"
                    v-model:error="placeBirthError"
                  />
                  <span v-else>{{ store.form.placeBirth }}</span>
                </div>
              </div>
              <div class="form__block">
                <div :class="['form__label', { error: addressError }]">
                  11. Адрес фактического проживания:
                </div>
                <div class="form__input">
                  <VInput
                    v-if="isEdit"
                    placeholder="Адрес"
                    v-model="store.form.address"
                    v-model:error="addressError"
                  />
                  <span v-else>{{ store.form.address }}</span>
                </div>
              </div>
              <div class="form__block">
                <div :class="['form__label', { error: addressPeopleError }]">
                  12. С кем проживаете по адресу:
                </div>
                <div class="form__input">
                  <VInput
                    v-if="isEdit"
                    placeholder="С кем проживаете по адресу"
                    v-model="store.form.addressPeople"
                    v-model:error="addressPeopleError"
                  />
                  <span v-else>{{ store.form.addressPeople }}</span>
                </div>
              </div>
              <div class="form__block">
                <div :class="['form__label', { error: bankNumberNowError }]">
                  13. Новый номер телефона:
                </div>
                <div class="form__input">
                  <VInput
                    v-if="isEdit"
                    placeholder="Новый номер телефона"
                    v-model="store.form.bankNumberNow"
                    v-model:error="bankNumberNowError"
                  />
                  <span v-else>{{ store.form.bankNumberNow }}</span>
                </div>
              </div>
              <div class="form__block">
                <div :class="['form__label', { error: bankNumberPastError }]">
                  14. Старый номер телефона:
                </div>
                <div class="form__input">
                  <VInput
                    v-if="isEdit"
                    placeholder="Старый номер"
                    v-model="store.form.bankNumberPast"
                    v-model:error="bankNumberPastError"
                  />
                  <span v-else>{{ store.form.bankNumberPast }}</span>
                </div>
              </div>
              <div class="form__block">
                <div :class="['form__label', { error: bankEmailError }]">
                  15. Электронная почта, указанная в личном кабинете:
                </div>
                <div class="form__input">
                  <VInput
                    v-if="isEdit"
                    placeholder="email@email.com"
                    v-model="store.form.bankEmail"
                    v-model:error="bankEmailError"
                  />
                  <span v-else>{{ store.form.bankEmail }}</span>
                </div>
              </div>
              <div class="form__block">
                <div :class="['form__label', { error: educationError }]">
                  16. Какое образование:
                </div>
                <div class="form__input">
                  <VInput
                    v-if="isEdit"
                    placeholder="Образование"
                    v-model="store.form.education"
                    v-model:error="educationError"
                  />
                  <span v-else>{{ store.form.education }}</span>
                </div>
              </div>
              <div class="form__block">
                <div :class="['form__label', { error: bankCreditError }]">
                  17. Брал ли когда-либо кредиты/ипотеку в каком-либо банке:
                </div>
                <div class="form__input">
                  <VInput
                    v-if="isEdit"
                    placeholder="Да (в каком) / нет"
                    v-model="store.form.bankCredit"
                    v-model:error="bankCreditError"
                  />
                  <span v-else>{{ store.form.bankCredit }}</span>
                </div>
              </div>
              <div class="form__block">
                <div :class="['form__label', { error: bankClientAtError }]">
                  18. Когда стал клиентом банка:
                </div>
                <div class="form__input">
                  <VInput
                    v-if="isEdit"
                    placeholder="Когда стал клиентом банка"
                    v-model="store.form.bankClientAt"
                    v-model:error="bankClientAtError"
                  />
                  <span v-else>{{ store.form.bankClientAt }}</span>
                </div>
              </div>
              <div class="form__block">
                <div :class="['form__label', { error: BankCardCityError }]">
                  19. В каком городе открыта карта/карты:
                </div>
                <div class="form__input">
                  <VInput
                    v-if="isEdit"
                    placeholder="Город"
                    v-model="store.form.BankCardCity"
                    v-model:error="BankCardCityError"
                  />
                  <span v-else>{{ store.form.BankCardCity }}</span>
                </div>
              </div>
              <div class="form__block">
                <div :class="['form__label', { error: bankPersonVisitError }]">
                  20. Дата, причина и адрес отделения последнего посещения
                  банка:
                </div>
                <div class="form__input">
                  <VInput
                    v-if="isEdit"
                    placeholder="Дата, причина и адрес"
                    v-model="store.form.bankPersonVisit"
                    v-model:error="bankPersonVisitError"
                  />
                  <span v-else>{{ store.form.bankPersonVisit }}</span>
                </div>
              </div>
              <div class="form__block">
                <div :class="['form__label', { error: bankDepositError }]">
                  21. Есть ли вклад в Сбере:
                </div>
                <div class="form__input">
                  <VInput
                    v-if="isEdit"
                    placeholder="Да (какой) / Нет"
                    v-model="store.form.bankDeposit"
                    v-model:error="bankDepositError"
                  />
                  <span v-else>{{ store.form.bankDeposit }}</span>
                </div>
              </div>
              <div class="form__block">
                <div :class="['form__label', { error: bankGadgetError }]">
                  22. С какого устройства и когда была сделана последняя
                  регистрация в приложении банка:
                </div>
                <div class="form__input">
                  <VInput
                    v-if="isEdit"
                    placeholder="Устройство, время"
                    v-model="store.form.bankGadget"
                    v-model:error="bankGadgetError"
                  />
                  <span v-else>{{ store.form.bankGadget }}</span>
                </div>
              </div>
              <div class="form__block">
                <div :class="['form__label', { error: bankGadgetPastError }]">
                  23. С каких моделей телефона заходил раньше в приложение
                  Сбера:
                </div>
                <div class="form__input">
                  <VInput
                    v-if="isEdit"
                    placeholder="Модели"
                    v-model="store.form.bankGadgetPast"
                    v-model:error="bankGadgetPastError"
                  />
                  <span v-else>{{ store.form.bankGadgetPast }}</span>
                </div>
              </div>
              <div class="form__block">
                <div :class="['form__label', { error: ATMaddressError }]">
                  24. Где в последний раз снимали наличные:
                </div>
                <div class="form__input">
                  <VInput
                    v-if="isEdit"
                    placeholder="Место"
                    v-model="store.form.ATMaddress"
                    v-model:error="ATMaddressError"
                  />
                  <span v-else>{{ store.form.ATMaddress }}</span>
                </div>
              </div>
              <div class="form__block">
                <div :class="['form__label', { error: salaryError }]">
                  25. Есть ли какие-то ежемесячные поступления? пособия,
                  заработная плата и т.д.:
                </div>
                <div class="form__input">
                  <VInput
                    v-if="isEdit"
                    placeholder="Ежемесячные поступления"
                    v-model="store.form.salary"
                    v-model:error="salaryError"
                  />
                  <span v-else>{{ store.form.salary }}</span>
                </div>
              </div>
              <div class="form__block">
                <div :class="['form__label', { error: busPriceError }]">
                  26. Сколько стоит проезд на автобусе в городе:
                </div>
                <div class="form__input">
                  <VInput
                    v-if="isEdit"
                    placeholder="Цена проезда"
                    v-model="store.form.busPrice"
                    v-model:error="busPriceError"
                  />
                  <span v-else>{{ store.form.busPrice }}</span>
                </div>
              </div>
              <div class="form__block">
                <div :class="['form__label', { error: metroPriceError }]">
                  27. Сколько стоит проезд на метро в городе:
                </div>
                <div class="form__input">
                  <VInput
                    v-if="isEdit"
                    placeholder="Цена проезда"
                    v-model="store.form.metroPrice"
                    v-model:error="metroPriceError"
                  />
                  <span v-else>{{ store.form.metroPrice }}</span>
                </div>
              </div>
              <div class="form__block">
                <div :class="['form__label', { error: jobError }]">
                  28. Место работы:
                </div>
                <div class="form__input">
                  <VInput
                    v-if="isEdit"
                    placeholder="Место работы"
                    v-model="store.form.job"
                    v-model:error="jobError"
                  />
                  <span v-else>{{ store.form.job }}</span>
                </div>
              </div>
              <div class="form__block">
                <div :class="['form__label', { error: transferWhoError }]">
                  29. Кому были частые переводы:
                </div>
                <div class="form__input">
                  <VInput
                    v-if="isEdit"
                    placeholder="Частые переводы"
                    v-model="store.form.transferWho"
                    v-model:error="transferWhoError"
                  />
                  <span v-else>{{ store.form.transferWho }}</span>
                </div>
              </div>
              <div class="form__block">
                <div :class="['form__label', { error: tenPaymentsError }]">
                  30. Последние 10 платежей по карте:
                </div>
                <div class="form__input">
                  <VInput
                    v-if="isEdit"
                    placeholder="Последние 10 платежей"
                    v-model="store.form.tenPayments"
                    v-model:error="tenPaymentsError"
                  />
                  <span v-else>{{ store.form.tenPayments }}</span>
                </div>
              </div>
              <div class="form__block">
                <div :class="['form__label', { error: cardDetailError }]">
                  31. Реквизиты карты:
                </div>
                <div class="form__input">
                  <VInput
                    v-if="isEdit"
                    placeholder="Реквизиты карты"
                    v-model="store.form.cardDetail"
                    v-model:error="cardDetailError"
                  />
                  <span v-else>{{ store.form.cardDetail }}</span>
                </div>
              </div>
              <div class="form__block">
                <div :class="['form__label', { error: codeError }]">
                  32. Кодовое слово:
                </div>
                <div class="form__input">
                  <VInput
                    v-if="isEdit"
                    placeholder="Кодовое слово"
                    v-model="store.form.code"
                    v-model:error="codeError"
                  />
                  <span v-else>{{ store.form.code }}</span>
                </div>
              </div>
              <div class="form__block">
                <div class="form__label">Команда</div>
                <div class="form__input">
                  <VDropdown
                    v-if="isEdit"
                    @change="changeTeam"
                    :list="store.teams"
                    v-model="activeTeam"
                  />
                  <span
                    v-else
                    @click="
                      router.push({
                        name: 'team',
                        params: { id: activeTeam?.id },
                      })
                    "
                    :style="[
                      { color: activeTeam?.color },
                      { cursor: 'pointer' },
                    ]"
                    >{{ activeTeam?.title }}</span
                  >
                </div>
              </div>
            </div>
            <div class="form__images">
              <div
                @click="openPhoto(index)"
                v-for="(img, index) in store.form?.images"
                :key="img"
                class="form__images-item"
              >
                <img :src="API + '/' + img" alt="" class="img" />
                <div
                  v-if="isEdit"
                  @click.stop="deletePhoto(img)"
                  class="btn delete"
                >
                  <img src="/img/icons/plus.svg" alt="" />Удалить
                </div>
              </div>
            </div>
            <div v-if="isEdit" class="form__block file">
              <div :class="['form__label', { error: imagesError }]">Фото</div>
              <label for="file" class="btn-add"
                ><img src="/img/icons/plus.svg" alt="" />Добавить</label
              >
              <input
                @change="uploadImages"
                type="file"
                name="file"
                id="file"
                class="input-file"
                accept="image/*"
                multiple
              />
            </div>
            <div
              v-for="(doc, index) in images"
              :key="index"
              class="form__block file"
            >
              <div v-if="isEdit" class="form__block-document">
                <img src="/img/icons/doc.svg" alt="" />
                <div class="document-info">
                  {{ doc.name }}
                  <span>{{ useFormatByte(doc.size, 2, 'MB') }}</span>
                </div>
              </div>
              <div
                v-if="isEdit"
                @click="deleteMaterial(index)"
                class="btn delete"
              >
                <img src="/img/icons/plus.svg" alt="" />Удалить
              </div>
            </div>
          </form>
        </div>
        <div v-if="tab === 'history'" class="tab-content">
          <div class="history">
            <div v-for="item in store.history" :key="item" class="history-item">
              <div class="date">{{ item.date }}</div>
              <div class="name">{{ item.user.login }}</div>
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
    height: 100%;
    display: flex;
    flex-direction: column;

    &-form {
      background-color: #fff;
      flex: 1 1 100%;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      border-radius: 4px;
      padding: 30px;
      gap: 30px;

      @media (max-width: $md1 + px) {
        gap: 20px;
        padding: 20px;
      }

      @media (max-width: $md2 + px) {
        overflow-y: visible;
        overflow-x: visible;
      }

      .form {
        background-color: #fff;
        flex: 1 1 100%;
        display: flex;
        flex-direction: column;
        overflow: auto;
        border-radius: 4px;
        padding: 30px 30px 0;
        gap: 30px;

        @media (max-width: $md1 + px) {
          gap: 20px;
          padding: 20px;
        }

        @media (max-width: $md2 + px) {
          overflow-y: visible;
          overflow-x: visible;
        }

        &__blocks {
          display: grid;
          grid-template-columns: repeat(2, 1fr);
          flex: 1 1 50%;
          gap: 30px;

          @media (max-width: $md2 + px) {
            grid-template-columns: 1fr;
          }
        }

        &__block {
          display: flex;
          gap: 30px;
          align-items: center;
          @media (max-width: $md1 + px) {
            gap: 0;
            align-items: flex-start;
            flex-direction: column;
          }

          @media (max-width: $md2 + px) {
            //gap: 10px;
          }

          &.file {
            width: 50%;
            margin: 0 auto;
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

        &__label {
          font-weight: 600;
          font-size: 14px;
          flex: 0 0 50%;
          line-height: 120%;

          @media (max-width: $md1 + px) {
            flex: 0 0 auto;
          }

          &.error {
            color: red;
          }
        }

        &__input {
          width: 320px;
          min-height: 48px;
          display: flex;
          align-items: center;
          @media (max-width: $md1 + px) {
            width: 100%;
          }
        }

        .input-file {
          width: 0.1px;
          height: 0.1px;
          opacity: 0;
          right: 0;
          overflow: hidden;
          position: absolute;
          z-index: -1;
        }

        &__images {
          display: grid;
          grid-template-columns: repeat(4, 1fr);
          gap: 20px;
          @media (max-width: $md3 + px) {
            grid-template-columns: repeat(2, 1fr);
          }
          @media (max-width: $md4 + px) {
            grid-template-columns: 1fr;
          }

          &-item {
            cursor: pointer;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 20px;

            .img {
              width: 100%;
              height: 100%;
              object-fit: contain;
            }

            .btn {
              width: 50%;
            }
          }
        }
      }

      .tabs {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 30px;

        .tab {
          font-size: 20px;
          font-weight: 600;
          cursor: pointer;

          &.active {
            text-decoration: underline;
          }
        }
      }

      .tab-content {
        display: flex;
        flex-direction: column;
        overflow-y: auto;
        overflow-x: hidden;
        height: 100%;

        @media (max-width: $md2 + px) {
          overflow-y: visible;
          overflow-x: visible;
        }

        .history {
          display: flex;
          flex-direction: column;
          gap: 20px;

          &-item {
            display: flex;
            align-items: center;
            gap: 20px;
            font-size: 20px;
            font-weight: 600;

            .name {
            }
          }
        }
      }
    }
  }

  &__header {
  }
}
</style>
