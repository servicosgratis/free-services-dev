//Low light switcher
const mode = document.getElementById('mode');
const logo = document.getElementById('sidebar-logo');

const isEnglish = document.documentElement.lang === "en";

function updateLogo() {
    const isDarkMode = document.documentElement.hasAttribute('data-dark-mode');
    logo.src = isDarkMode 
        ? (isEnglish ? logo.dataset.logoEnWhite : logo.dataset.logoPtWhite)
        : (isEnglish ? logo.dataset.logoEnColor : logo.dataset.logoPtColor);
}

if (mode !== null) {
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', event => {
        if (event.matches) {
            localStorage.setItem('theme', 'dark');
            document.documentElement.setAttribute('data-dark-mode', '');

        } else {
            localStorage.setItem('theme', 'light');
            document.documentElement.removeAttribute('data-dark-mode');
        }
        updateLogo();
    })
    mode.addEventListener('click', () => {
        document.documentElement.toggleAttribute('data-dark-mode');
        localStorage.setItem('theme', document.documentElement.hasAttribute('data-dark-mode') ? 'dark' : 'light');
        updateLogo();
    });
    if (localStorage.getItem('theme') === 'dark') {
        document.documentElement.setAttribute('data-dark-mode', '');
    } else {
        document.documentElement.removeAttribute('data-dark-mode');
    }
    updateLogo();
}