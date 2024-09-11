export const useRegular = () => {
  const dateRegular = /(0?[1-9]|[12][0-9]|3[01])[/\-.](0?[1-9]|1[012])[ /.-]/
  const emailRegular =
    /^([A-Za-z0-9_\-.])+@([A-Za-z0-9_\-.])+\.([A-Za-z]{2,4})$/

  const dateTest = (date) => dateRegular.test(date)
  const emailTest = (email) => emailRegular.test(email)

  return {
    dateTest,
    emailTest,
  }
}
