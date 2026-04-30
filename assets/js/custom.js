/* Custom theme toggle: cycle through Light / Dark / Auto with sun/moon icons */
(function ($) {
  function updateToggleIcon(mode) {
    var $btn = $('.js-toggle-theme');
    if (!$btn.length) return;

    // Remove existing icon classes
    $btn.find('i').remove();

    if (mode === 0) {
      // Light mode: show sun
      $btn.append('<i class="fas fa-sun" aria-hidden="true" style="font-size:1em;color:#f39c12;"></i>');
      $btn.attr('title', 'Light mode (click to switch)');
    } else if (mode === 1) {
      // Dark mode: show moon
      $btn.append('<i class="fas fa-moon" aria-hidden="true" style="font-size:1em;color:#9b59b6;"></i>');
      $btn.attr('title', 'Dark mode (click to switch)');
    } else {
      // Auto mode: show sun+moon combo
      $btn.append('<i class="fas fa-sun" aria-hidden="true" style="font-size:0.65em;position:absolute;top:0;left:0;opacity:0.85;color:#f39c12;"></i><i class="fas fa-moon" aria-hidden="true" style="font-size:0.65em;position:absolute;bottom:0;right:0;opacity:0.85;color:#9b59b6;"></i>');
      $btn.attr('title', 'Auto mode (click to switch)');
    }
  }

  $(document).ready(function () {
    // Default to light (0) if never set before
    if (localStorage.getItem('dark_mode') === null) {
      localStorage.setItem('dark_mode', '0');
    }

    var mode = parseInt(localStorage.getItem('dark_mode') || '0');
    updateToggleIcon(mode);

    $('.js-toggle-theme').on('click', function (e) {
      e.preventDefault();
      var mode = parseInt(localStorage.getItem('dark_mode') || '0');
      if (mode === 0) {
        // Light -> Dark
        localStorage.setItem('dark_mode', '1');
        $('.js-set-theme-dark').trigger('click');
        updateToggleIcon(1);
      } else if (mode === 1) {
        // Dark -> Auto
        localStorage.setItem('dark_mode', '2');
        $('.js-set-theme-auto').trigger('click');
        updateToggleIcon(2);
      } else {
        // Auto -> Light
        localStorage.setItem('dark_mode', '0');
        $('.js-set-theme-light').trigger('click');
        updateToggleIcon(0);
      }
    });
  });
})(jQuery);
