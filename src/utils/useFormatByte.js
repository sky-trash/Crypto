export default function useFormatByte(bytes, decimals, only) {
  const K_UNIT = 1024
  const SIZES = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB']

  if (bytes === 0) return '0 Byte'

  if (only === 'MB') {
    if ((bytes / (K_UNIT * K_UNIT)).toFixed(decimals) === '0.00') {
      return '<' + (bytes / (K_UNIT * K_UNIT)).toFixed(decimals) + ' мб'
    } else {
      return (bytes / (K_UNIT * K_UNIT)).toFixed(decimals) + ' мб'
    }
  }

  let i = Math.floor(Math.log(bytes) / Math.log(K_UNIT))
  let resp =
    parseFloat((bytes / Math.pow(K_UNIT, i)).toFixed(decimals)) + ' ' + SIZES[i]

  return resp
}
