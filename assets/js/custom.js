/* Custom theme toggle: cycle through Light / Dark / Auto with a sun+moon icon */
(function ($) {
  function updateToggleIcon() {
    // No visual state change needed — the sun+moon combo icon is static.
  }

  $(document).ready(function () {
    // Default to light (0) if never set before
    if (localStorage.getItem('dark_mode') === null) {
      localStorage.setItem('dark_mode', '0');
    }

    $('.js-toggle-theme').on('click', function (e) {
      e.preventDefault();
      var mode = parseInt(localStorage.getItem('dark_mode') || '0');
      if (mode === 0) {
        // Light -> Dark
        $('.js-set-theme-dark').trigger('click');
      } else if (mode === 1) {
        // Dark -> Auto
        $('.js-set-theme-auto').trigger('click');
      } else {
        // Auto (or any other) -> Light
        $('.js-set-theme-light').trigger('click');
      }
    });
  });
})(jQuery);
