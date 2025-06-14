;(function () {
        const togglers = document.querySelectorAll('.js-theme-toggler')
        Array.from(togglers).forEach(function (toggler) {
          toggler.addEventListener('click', function () {
            const theme = document.documentElement.getAttribute('data-bs-theme')
            const newTheme = theme == 'light' ? 'dark' : 'light'
            document.documentElement.setAttribute('data-bs-theme', newTheme)
            localStorage.setItem('theme', newTheme)
          })
        })
      })()
