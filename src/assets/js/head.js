;(function () {
        const savedThemePreference = localStorage.getItem('theme')
        if (savedThemePreference) {
          document.documentElement.setAttribute('data-bs-theme', savedThemePreference)
        }
      })()
