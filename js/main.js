$(function () {
    $('[data-toggle="tooltip"]').tooltip()
})

$('#legendModal').on('shown.bs.modal', function () {
    $('#legend').trigger('focus')
  })

  function donateBtc() {
    /* Get the text field */
    var copyText = "1GafZ243XHrpteRJ4gNkm91xZHnmYUR96L"
  
  
    /* Copy the text inside the text field */
    document.execCommand("copy");
  
    /* Alert the copied text */
    alert("Copied the text: " + copyText.value);
  }

(function ($) {
    "use strict";
})(jQuery);