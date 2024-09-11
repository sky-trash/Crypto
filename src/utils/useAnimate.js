import { ref } from 'vue'
import { useRouter } from 'vue-router'

export const useAnimate = () => {
  const router = useRouter()
  const scale = ref(1.5)
  const scaleSmall = ref(1.1)
  const opacity = ref(0)
  const sideTop = ref('-1920px')
  const sideLeft = ref('-1920px')
  const delayBig = ref('0.5s')
  const delaySmall = ref('1s')
  const delay2S = ref('2s')
  const leave = ref(false)

  const routerLeave = (path) => {
    leave.value = true
    scale.value = 1.5
    scaleSmall.value = 1.1
    opacity.value = 0
    sideTop.value = '-1080px'
    sideLeft.value = '-1920px'
    delayBig.value = '0s'
    delaySmall.value = '0s'

    delay2S.value = '0s'
    setTimeout(() => {
      router.push(`${path}`)
    }, 1000)
  }

  const initAnimate = () => {
    setTimeout(() => {
      scale.value = 1
      scaleSmall.value = 1
      opacity.value = 1
      sideTop.value = '0px'
      sideLeft.value = '0px'
    }, 300)
  }
  return {
    scale,
    scaleSmall,
    opacity,
    sideTop,
    sideLeft,
    delayBig,
    delaySmall,
    delay2S,
    leave,
    routerLeave,
    initAnimate,
  }
}
