<script setup>
import { onMounted, ref } from 'vue'
import { useStateStore } from '@/store/stateStore.js'
import { useRouter } from 'vue-router'
import VInput from '@/components/VInput.vue'
import VDropdown from '@/components/VDropdown.vue'
import useFormatByte from '../utils/useFormatByte.js'

const router = useRouter()
const store = useStateStore()

const activeTeam = ref({})
const data = ref({
  name: '',
  dateBirth: '',
  year: '',
  passportWho: '',
  passportDetail: '',
  passportAddress: '',
  addressIndex: '',
  floorCount: '',
  passportAddressOld: '',
  placeBirth: '',
  address: '',
  addressPeople: '',
  bankNumberNow: '',
  bankNumberPast: '',
  bankEmail: '',
  education: '',
  bankCredit: '',
  bankClientAt: '',
  BankCardCity: '',
  bankPersonVisit: '',
  bankDeposit: '',
  bankGadget: '',
  bankGadgetPast: '',
  ATMaddress: '',
  salary: '',
  busPrice: '',
  metroPrice: '',
  job: '',
  transferWho: '',
  tenPayments: '',
  cardDetail: '',
  code: '',
  images: [],
  status_id: 1,
  team_id: 0,
})

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
  data.value.team_id = activeTeam.value.id
}

const changeDate = (e) => {
  data.value.dateBirth = e.target.value
  dateBirthError.value = false
}

const uploadImages = () => {
  const fileImages = document.getElementById('file')
  const uploadedFiles = Array.from(fileImages.files)
  uploadedFiles.forEach((file) => {
    data.value.images.push(file)
  })
}

const deleteMaterial = (index) => {
  data.value.images.splice(index, 1)
}

const toHome = () => {
  router.push('/home')
}

const addForm = async () => {
  if (
    data.value.name &&
    data.value.dateBirth.length === 10 &&
    data.value.year &&
    data.value.passportWho &&
    data.value.passportDetail &&
    data.value.passportAddress &&
    data.value.addressIndex &&
    data.value.floorCount &&
    data.value.passportAddressOld &&
    data.value.placeBirth &&
    data.value.address &&
    data.value.addressPeople &&
    data.value.bankNumberNow &&
    data.value.bankNumberPast &&
    data.value.bankEmail &&
    data.value.education &&
    data.value.bankCredit &&
    data.value.bankClientAt &&
    data.value.BankCardCity &&
    data.value.bankPersonVisit &&
    data.value.bankDeposit &&
    data.value.bankGadget &&
    data.value.bankGadgetPast &&
    data.value.ATMaddress &&
    data.value.salary &&
    data.value.busPrice &&
    data.value.metroPrice &&
    data.value.job &&
    data.value.transferWho &&
    data.value.tenPayments &&
    data.value.cardDetail &&
    data.value.code &&
    data.value.images.length
  ) {
    await store.addForm(data.value).then(() => router.push('/home'))
  } else {
    if (!data.value.name) nameError.value = true
    if (data.value.dateBirth.length !== 10) dateBirthError.value = true
    if (!data.value.year) yearError.value = true
    if (!data.value.passportWho) passportWhoError.value = true
    if (!data.value.passportDetail) passportDetailError.value = true
    if (!data.value.passportAddress) passportAddressError.value = true
    if (!data.value.addressIndex) addressIndexError.value = true
    if (!data.value.floorCount) floorCountError.value = true
    if (!data.value.passportAddressOld) passportAddressOldError.value = true
    if (!data.value.placeBirth) placeBirthError.value = true
    if (!data.value.address) addressError.value = true
    if (!data.value.addressPeople) addressPeopleError.value = true
    if (!data.value.bankNumberNow) bankNumberNowError.value = true
    if (!data.value.bankNumberPast) bankNumberPastError.value = true
    if (!data.value.bankEmail) bankEmailError.value = true
    if (!data.value.education) educationError.value = true
    if (!data.value.bankCredit) bankCreditError.value = true
    if (!data.value.bankClientAt) bankClientAtError.value = true
    if (!data.value.BankCardCity) BankCardCityError.value = true
    if (!data.value.bankPersonVisit) bankPersonVisitError.value = true
    if (!data.value.bankDeposit) bankDepositError.value = true
    if (!data.value.bankGadget) bankGadgetError.value = true
    if (!data.value.bankGadgetPast) bankGadgetPastError.value = true
    if (!data.value.ATMaddress) ATMaddressError.value = true
    if (!data.value.salary) salaryError.value = true
    if (!data.value.busPrice) busPriceError.value = true
    if (!data.value.metroPrice) metroPriceError.value = true
    if (!data.value.job) jobError.value = true
    if (!data.value.transferWho) transferWhoError.value = true
    if (!data.value.tenPayments) tenPaymentsError.value = true
    if (!data.value.cardDetail) cardDetailError.value = true
    if (!data.value.code) codeError.value = true
    if (!data.value.images.length) imagesError.value = true
  }
}

await store.getUser()
await store.getTeams()
await store.getDrops()

onMounted(() => {
  if (store.user.role.title === 'ROLE_USER') router.push('/home')
  // activeTeam.value = store.teams[0]
  data.value.team_id = store.teams[0]?.id
})
</script>
<template>
  <div class="page">
    <header class="header">
      <div class="left">
        <img @click="toHome" src="/img/icons/back.svg" alt="" />
        <div class="subtitle">Добавить анкету</div>
      </div>
    </header>
    <div class="page__content">
      <form class="form">
        <div class="form__blocks">
          <div class="form__block">
            <div :class="['form__label', { error: nameError }]">1. ФИО</div>
            <div class="form__input">
              <VInput
                placeholder="ФИО"
                v-model="data.name"
                v-model:error="nameError"
              />
            </div>
          </div>
          <div class="form__block">
            <div :class="['form__label', { error: dateBirthError }]">
              2. Дата рождения
            </div>
            <div class="form__input">
              <input
                type="date"
                @input="changeDate"
                @change="changeDate"
                v-model="data.dateBirth"
              />
            </div>
          </div>
          <div class="form__block">
            <div :class="['form__label', { error: yearError }]">
              3. Полный возраст:
            </div>
            <div class="form__input">
              <VInput
                placeholder="Полный возраст"
                v-model="data.year"
                v-model:error="yearError"
              />
            </div>
          </div>
          <div class="form__block">
            <div :class="['form__label', { error: passportWhoError }]">
              4. Где, кем и когда выдан паспорт:
            </div>
            <div class="form__input">
              <VInput
                placeholder="Где, кем и когда"
                v-model="data.passportWho"
                v-model:error="passportWhoError"
              />
            </div>
          </div>
          <div class="form__block">
            <div :class="['form__label', { error: passportDetailError }]">
              5. Серия и номер паспорта:
            </div>
            <div class="form__input">
              <VInput
                placeholder="Серия и номер паспорта"
                v-model="data.passportDetail"
                v-model:error="passportDetailError"
              />
            </div>
          </div>
          <div class="form__block">
            <div :class="['form__label', { error: passportAddressError }]">
              6. Адрес прописки по паспорту:
            </div>
            <div class="form__input">
              <VInput
                placeholder="Адрес"
                v-model="data.passportAddress"
                v-model:error="passportAddressError"
              />
            </div>
          </div>
          <div class="form__block">
            <div :class="['form__label', { error: addressIndexError }]">
              7. Индекс по месту прописки:
            </div>
            <div class="form__input">
              <VInput
                placeholder="Индекс по месту прописки"
                v-model="data.addressIndex"
                v-model:error="addressIndexError"
              />
            </div>
          </div>
          <div class="form__block">
            <div :class="['form__label', { error: floorCountError }]">
              8. Сколько этажей по прописке:
            </div>
            <div class="form__input">
              <VInput
                placeholder="Кол-во этажей"
                v-model="data.floorCount"
                v-model:error="floorCountError"
              />
            </div>
          </div>
          <div class="form__block">
            <div :class="['form__label', { error: passportAddressOldError }]">
              9. Адрес предыдущей прописки полностью:
            </div>
            <div class="form__input">
              <VInput
                placeholder="Адрес"
                v-model="data.passportAddressOld"
                v-model:error="passportAddressOldError"
              />
            </div>
          </div>
          <div class="form__block">
            <div :class="['form__label', { error: placeBirthError }]">
              10. Место рождения:
            </div>
            <div class="form__input">
              <VInput
                placeholder="Место рождения"
                v-model="data.placeBirth"
                v-model:error="placeBirthError"
              />
            </div>
          </div>
          <div class="form__block">
            <div :class="['form__label', { error: addressError }]">
              11. Адрес фактического проживания:
            </div>
            <div class="form__input">
              <VInput
                placeholder="Адрес"
                v-model="data.address"
                v-model:error="addressError"
              />
            </div>
          </div>
          <div class="form__block">
            <div :class="['form__label', { error: addressPeopleError }]">
              12. С кем проживаете по адресу:
            </div>
            <div class="form__input">
              <VInput
                placeholder="С кем проживаете по адресу"
                v-model="data.addressPeople"
                v-model:error="addressPeopleError"
              />
            </div>
          </div>
          <div class="form__block">
            <div :class="['form__label', { error: bankNumberNowError }]">
              13. Новый номер телефона:
            </div>
            <div class="form__input">
              <VInput
                placeholder="Новый номер"
                v-model="data.bankNumberNow"
                v-model:error="bankNumberNowError"
              />
            </div>
          </div>
          <div class="form__block">
            <div :class="['form__label', { error: bankNumberPastError }]">
              14. Старый номер телефона:
            </div>
            <div class="form__input">
              <VInput
                placeholder="Старый номер"
                v-model="data.bankNumberPast"
                v-model:error="bankNumberPastError"
              />
            </div>
          </div>
          <div class="form__block">
            <div :class="['form__label', { error: bankEmailError }]">
              15. Электронная почта, указанная в личном кабинете:
            </div>
            <div class="form__input">
              <VInput
                placeholder="email@email.com"
                v-model="data.bankEmail"
                v-model:error="bankEmailError"
              />
            </div>
          </div>
          <div class="form__block">
            <div :class="['form__label', { error: educationError }]">
              16. Какое образование:
            </div>
            <div class="form__input">
              <VInput
                placeholder="Образование"
                v-model="data.education"
                v-model:error="educationError"
              />
            </div>
          </div>
          <div class="form__block">
            <div :class="['form__label', { error: bankCreditError }]">
              17. Брал ли когда-либо кредиты/ипотеку в каком-либо банке:
            </div>
            <div class="form__input">
              <VInput
                placeholder="Да (в каком) / нет"
                v-model="data.bankCredit"
                v-model:error="bankCreditError"
              />
            </div>
          </div>
          <div class="form__block">
            <div :class="['form__label', { error: bankClientAtError }]">
              18. Когда стал клиентом банка:
            </div>
            <div class="form__input">
              <VInput
                placeholder="Когда стал клиентом банка"
                v-model="data.bankClientAt"
                v-model:error="bankClientAtError"
              />
            </div>
          </div>
          <div class="form__block">
            <div :class="['form__label', { error: BankCardCityError }]">
              19. В каком городе открыта карта/карты:
            </div>
            <div class="form__input">
              <VInput
                placeholder="Город"
                v-model="data.BankCardCity"
                v-model:error="BankCardCityError"
              />
            </div>
          </div>
          <div class="form__block">
            <div :class="['form__label', { error: bankPersonVisitError }]">
              20. Дата, причина и адрес отделения последнего посещения банка:
            </div>
            <div class="form__input">
              <VInput
                placeholder="Дата, причина и адрес"
                v-model="data.bankPersonVisit"
                v-model:error="bankPersonVisitError"
              />
            </div>
          </div>
          <div class="form__block">
            <div :class="['form__label', { error: bankDepositError }]">
              21. Есть ли вклад в Сбере:
            </div>
            <div class="form__input">
              <VInput
                placeholder="Да (какой) / Нет"
                v-model="data.bankDeposit"
                v-model:error="bankDepositError"
              />
            </div>
          </div>
          <div class="form__block">
            <div :class="['form__label', { error: bankGadgetError }]">
              22. С какого устройства и когда была сделана последняя регистрация
              в приложении банка:
            </div>
            <div class="form__input">
              <VInput
                placeholder="Устройство, время"
                v-model="data.bankGadget"
                v-model:error="bankGadgetError"
              />
            </div>
          </div>
          <div class="form__block">
            <div :class="['form__label', { error: bankGadgetPastError }]">
              23. С каких моделей телефона заходил раньше в приложение Сбера:
            </div>
            <div class="form__input">
              <VInput
                placeholder="Модели"
                v-model="data.bankGadgetPast"
                v-model:error="bankGadgetPastError"
              />
            </div>
          </div>
          <div class="form__block">
            <div :class="['form__label', { error: ATMaddressError }]">
              24. Где в последний раз снимали наличные:
            </div>
            <div class="form__input">
              <VInput
                placeholder="Место"
                v-model="data.ATMaddress"
                v-model:error="ATMaddressError"
              />
            </div>
          </div>
          <div class="form__block">
            <div :class="['form__label', { error: salaryError }]">
              25. Есть ли какие-то ежемесячные поступления? пособия, заработная
              плата и т.д.:
            </div>
            <div class="form__input">
              <VInput
                placeholder="Ежемесячные поступления"
                v-model="data.salary"
                v-model:error="salaryError"
              />
            </div>
          </div>
          <div class="form__block">
            <div :class="['form__label', { error: busPriceError }]">
              26. Сколько стоит проезд на автобусе в городе:
            </div>
            <div class="form__input">
              <VInput
                placeholder="Цена проезда"
                v-model="data.busPrice"
                v-model:error="busPriceError"
              />
            </div>
          </div>
          <div class="form__block">
            <div :class="['form__label', { error: metroPriceError }]">
              27. Сколько стоит проезд на метро в городе:
            </div>
            <div class="form__input">
              <VInput
                placeholder="Цена проезда"
                v-model="data.metroPrice"
                v-model:error="metroPriceError"
              />
            </div>
          </div>
          <div class="form__block">
            <div :class="['form__label', { error: jobError }]">
              28. Место работы:
            </div>
            <div class="form__input">
              <VInput
                placeholder="Место работы"
                v-model="data.job"
                v-model:error="jobError"
              />
            </div>
          </div>
          <div class="form__block">
            <div :class="['form__label', { error: transferWhoError }]">
              29. Кому были частые переводы:
            </div>
            <div class="form__input">
              <VInput
                placeholder="Частые переводы"
                v-model="data.transferWho"
                v-model:error="transferWhoError"
              />
            </div>
          </div>
          <div class="form__block">
            <div :class="['form__label', { error: tenPaymentsError }]">
              30. Последние 10 платежей по карте:
            </div>
            <div class="form__input">
              <VInput
                placeholder="Последние 10 платежей"
                v-model="data.tenPayments"
                v-model:error="tenPaymentsError"
              />
            </div>
          </div>
          <div class="form__block">
            <div :class="['form__label', { error: cardDetailError }]">
              31. Реквизиты карты:
            </div>
            <div class="form__input">
              <VInput
                placeholder="Реквизиты"
                v-model="data.cardDetail"
                v-model:error="cardDetailError"
              />
            </div>
          </div>
          <div class="form__block">
            <div :class="['form__label', { error: codeError }]">
              32. Кодовое слово:
            </div>
            <div class="form__input">
              <VInput
                placeholder="Кодовое слово"
                v-model="data.code"
                v-model:error="codeError"
              />
            </div>
          </div>
          <div class="form__block">
            <div class="form__label">Выберите команду</div>
            <div class="form__input">
              <VDropdown
                @change="changeTeam"
                :list="store.teams"
                v-model="activeTeam"
              />
            </div>
          </div>
        </div>
        <div class="form__block file">
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
          v-for="(doc, index) in data.images"
          :key="index"
          class="form__block file"
        >
          <div class="form__block-document">
            <img src="/img/icons/doc.svg" alt="" />
            <div class="document-info">
              {{ doc.name }}
              <span>{{ useFormatByte(doc.size, 2, 'MB') }}</span>
            </div>
          </div>
          <div @click="deleteMaterial(index)" class="btn delete">
            <img src="/img/icons/plus.svg" alt="" />Удалить
          </div>
        </div>
        <div @click="addForm" class="btn-add">
          <img src="/img/icons/plus.svg" alt="" /> Добавить анкету
        </div>
      </form>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import '@/assets/scss/variables';
.page {
  display: flex;

  &__content {
    display: flex;
    flex-direction: column;
    width: 100%;

    .form {
      background-color: #fff;
      flex: 1 1 100%;
      display: flex;
      flex-direction: column;
      overflow: auto;
      border-radius: 4px;
      padding: 30px;
      gap: 30px;

      @media (max-width: $md1 + px) {
        gap: 20px;
        padding: 20px;
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
          margin-bottom: 20px;
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
          margin-bottom: 10px;
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
    }
  }

  &__header {
  }

  .btn-add {
    flex: 0 0 40px;
    width: 50%;
    margin: 0 auto;
    display: flex;
    align-items: center;
    padding: 0 12px;
    background-color: $primary;
    border-radius: 4px;
    color: #fff;
    justify-content: center;
    gap: 20px;
    font-weight: 600;
    box-shadow: 0 4px 20px 0 rgba(0, 0, 0, 0.1);
    cursor: pointer;

    &:hover {
      box-shadow: 0 4px 20px 0 rgba(0, 0, 0, 0.2);
    }

    img {
      width: 18px;
    }
  }
}
</style>
