window.addEventListener('DOMContentLoaded', function() {

    // Adding default beer image to reviews

    const beerImages = document.querySelectorAll('.beer-image'),
        defaultBeerImageSrc = document.querySelector('img.hide').getAttribute('src');
    if (beerImages) {
        beerImages.forEach((image) => {
            if (image.getAttribute('src') == '') {
                image.src = defaultBeerImageSrc;
            }
        });
    }


    //Toggle Dark/Light Modes

    const switchBtn = document.querySelector('#switch'),
        body = document.querySelector(".body"),
        currentTheme = localStorage.getItem('theme'),
        modeIconDark = document.querySelector('#mode-icon-1'),
        modeIconLight = document.querySelector('#mode-icon-2');

    // Initiating localStorage data abouth current theme
    if (!currentTheme) {
        localStorage.setItem('theme', 'light');
    }

    // Listen for a click on the button
    switchBtn.addEventListener('click', function() {
        if (switchBtn.checked) {
            body.classList.add('dark-mode');
            localStorage.setItem('theme', 'dark');
            modeIconDark.classList.remove('hide');
            modeIconLight.classList.add('hide');
        } else {
            body.classList.remove('dark-mode');
            localStorage.setItem('theme', 'light');
            modeIconDark.classList.add('hide');
            modeIconLight.classList.remove('hide');
        }
    });

    //Setting theme according to localStorage preference
    if (currentTheme == "dark") {
        body.classList.add('dark-mode');
        localStorage.setItem('theme', 'dark');
        modeIconDark.classList.remove('hide');
        modeIconLight.classList.add('hide');
        switchBtn.checked = 'True';
    }

    if (currentTheme == "light") {
        body.classList.remove('dark-mode');
        localStorage.setItem('theme', 'light');
        modeIconDark.classList.add('hide');
        modeIconLight.classList.remove('hide');
        switchBtn.removeAttribute('checked');
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