const btn = document.querySelector('#switch-dm_btn'),
    theme = document.querySelector("#theme-link"),
    currentTheme = localStorage.getItem('theme');

//Toggle Dark/Light Modes

// Initiating localStorage data abouth current theme
localStorage.setItem('theme', 'light');

// Listen for a click on the button
btn.addEventListener("click", function() {
    // If the current URL contains "ligh-theme.css"
    if (theme.getAttribute("href") == "/static/css/light-theme.css") {
        // ... then switch it to "dark-theme.css"
        theme.href = "/static/css/dark-theme.css";
        btn.classList.remove("btn-light");
        btn.classList.add("btn-dark");
        btn.innerHTML = 'Switch to Light Mode';
        localStorage.setItem('theme', 'dark');
    // Otherwise...
    } else {
        // ... switch it to "light-theme.css"
        theme.href = "/static/css/light-theme.css";
        btn.classList.add("btn-light");
        btn.classList.remove("btn-dark");
        btn.innerHTML = 'Switch to Dark Mode';
        localStorage.setItem('theme', 'light');
    }
});

// Choosing mode depending on localStorage data
if (currentTheme == "dark") {
    theme.href = "/static/css/dark-theme.css";
    btn.classList.remove("btn-light");
    btn.classList.add("btn-dark");
    btn.innerHTML = 'Switch to Light Mode';
}

if (currentTheme == "light") {
    theme.href = "/static/css/light-theme.css";
    btn.classList.add("btn-light");
    btn.classList.remove("btn-dark");
    btn.innerHTML = 'Switch to Dark Mode';
}

