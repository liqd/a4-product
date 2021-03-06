const timeago = require('timeago.js/dist/timeago.min.js')
const $ = require('jquery')

$(function () {
  const $times = $('time.relative')

  $times.each((i, e) => {
    const sevenDays = 60 * 60 * 24 * 7 * 1000
    const datetime = new Date($(e).attr('datetime'))
    const timeagoInstance = timeago()

    if ((new Date() - datetime) < sevenDays) {
      e.textContent = timeagoInstance.format(datetime, document.documentElement.lang)
    }
  })
})
