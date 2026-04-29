/* Custom theme toggle: sun/moon direct switch, default light */
(function ($) {
  function updateToggleIcon() {
    var mode = parseInt(localStorage.getItem('dark_mode') || '0');
    if (mode === 1) {
      $('.theme-icon-light').hide();
      $('.theme-icon-dark').show();
    } else {
      $('.theme-icon-light').show();
      $('.theme-icon-dark').hide();
    }
  }

  $(document).ready(function () {
    // Default to light (0) if never set before
    if (localStorage.getItem('dark_mode') === null) {
      localStorage.setItem('dark_mode', '0');
    }

    updateToggleIcon();

    $('.js-toggle-theme').on('click', function (e) {
      e.preventDefault();
      var mode = parseInt(localStorage.getItem('dark_mode') || '0');
      if (mode === 1) {
        // currently dark -> switch to light
        $('.js-set-theme-light').trigger('click');
      } else {
        // currently light (or auto interpreted as light) -> switch to dark
        $('.js-set-theme-dark').trigger('click');
      }
      // Wait a tick for wowchemy.js to update localStorage, then refresh icon
      setTimeout(updateToggleIcon, 0);
    });
  });
})(jQuery);
