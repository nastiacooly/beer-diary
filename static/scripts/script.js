window.addEventListener('DOMContentLoaded', function() {

    // Adding default beer image to reviews

    const beerImages = document.querySelectorAll('.beer-image');
    if (beerImages) {
        beerImages.forEach((image) => {
            if (image.getAttribute('src') == '') {
                image.src = '/static/images/beer-default.jpg';
            }
        });
    }


    //Toggle Dark/Light Modes

    const switchBtn = document.querySelector('#switch'),
        theme = document.querySelector("#theme-link"),
        currentTheme = localStorage.getItem('theme'),
        modeIcon = document.querySelector('.mode-icon');

    // Initiating localStorage data abouth current theme
    if (!currentTheme) {
        localStorage.setItem('theme', 'light');
    }

    // Listen for a click on the button
    switchBtn.addEventListener('click', function() {
        if (switchBtn.checked) {
            theme.href = "/static/css/dark-theme.css";
            localStorage.setItem('theme', 'dark');
            modeIcon.src = "/static/icons/night.svg";
        } else {
            theme.href = "/static/css/light-theme.css";
            localStorage.setItem('theme', 'light');
            modeIcon.src = "/static/icons/sun.svg";
        }
    });

    //Setting theme according to localStorage preference
    if (currentTheme == "dark") {
        theme.href = "/static/css/dark-theme.css";
        switchBtn.setAttribute('checked', 'true');
        modeIcon.src = "/static/icons/night.svg";
    }

    if (currentTheme == "light") {
        theme.href = "/static/css/light-theme.css";
        switchBtn.removeAttribute('checked');
        modeIcon.src = "/static/icons/sun.svg";
    }


    // Filter-form - disabling certain inputs in order not to double filter request

    const filterForm = document.querySelector('#filter-form');

    if (filterForm) {
        const beerTypeInput = filterForm.querySelector('#id_beer_type'),
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
    }


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

});





