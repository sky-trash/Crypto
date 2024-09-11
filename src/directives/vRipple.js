const handleRipple = (element, binding, ev) => {
  const applyRippleStyle = () => {
    const elementCoordinates = element.getBoundingClientRect()
    const offsetY = ev.clientY - elementCoordinates.y
    const offsetX = ev.clientX - elementCoordinates.x

    rippleElement.style.position = 'absolute'
    rippleElement.style.height = '5px'
    rippleElement.style.width = '5px'
    rippleElement.style.borderRadius = '100%'
    rippleElement.style.backgroundColor = '#f2f2f2'
    rippleElement.style.left = `${offsetX}px`
    rippleElement.style.top = `${offsetY}px`
    ev.target.appendChild(rippleElement)
  }

  const animateRippleSpread = () => {
    const maximalDiameter = +binding.value || 50
    if (currentDiameter <= maximalDiameter) {
      currentDiameter++
      currentOpacity -= 0.65 / maximalDiameter
      rippleElement.style.transform = `scale(${currentDiameter})`
      rippleElement.style.opacity = `${currentOpacity}`
    } else {
      rippleElement.remove()
      clearInterval(animationHandler)
    }
  }

  const rippleElement = document.createElement('span')
  let currentDiameter = 1
  let currentOpacity = 0.65
  const animationHandler = setInterval(animateRippleSpread, 5)
  applyRippleStyle()
}

const vRipple = {
  mounted: (el, binding) => {
    el.addEventListener('click', (ev) => handleRipple(el, binding, ev))
  },
}

export default vRipple
