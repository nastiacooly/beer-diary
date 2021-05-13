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


// Filter-form - disabling certain inputs in order not to double filter request

const filterForm = document.querySelector('#filter-form'),
    beerTypeInput = filterForm.querySelector('#id_beer_type'),
    beerTypeFilteredInput = filterForm.querySelector('#id_beer_type_filtered'),
    beerTypeColorInput = filterForm.querySelector('#id_beer_type_color');

beerTypeInput.addEventListener('change', (e) => {
    disableInputsOnChange(e.target, beerTypeFilteredInput, beerTypeColorInput);
});

beerTypeFilteredInput.addEventListener('change', (e) => {
    disableInputsOnChange(e.target, beerTypeInput);
});

beerTypeColorInput.addEventListener('change', (e) => {
    disableInputsOnChange(e.target, beerTypeInput);
});

// Function to disable 1 or 2 inputs if the third input is changed
function disableInputsOnChange(changedInput, inputToDisable1, inputToDisable2) {
    if (inputToDisable2 == undefined) {
        if (changedInput.selectedIndex > 0) {
            inputToDisable1.disabled = 'True';
        } else {
            inputToDisable1.removeAttribute('disabled');
        }
    } else {
        if (changedInput.selectedIndex > 0) {
            inputToDisable1.disabled = 'True';
            inputToDisable2.disabled = 'True';
        } else {
            inputToDisable1.removeAttribute('disabled');
            inputToDisable2.removeAttribute('disabled');
        }
    }
}
