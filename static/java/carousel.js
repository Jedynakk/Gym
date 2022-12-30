const buttons = document.querySelector("[data-carousel-selector]")

buttons.forEach(button => {
    button.addEventListener("click", () => {
        const offset = button.dataset.carouselButton === "next" ? 1 : -1
        const slides = button.closest("[data-carousel]").querySelector("[data-slides]")

        const activeSlides = slides.querySelector("[data-active]")
        let newIndex = [...slides.childern].indexOf(activeSlides) + offset
        if (newIndex < 0) newIndex = slides.children.length - 1
        if (newIndex >= slides.children.length) newIndex = 0
        slides.children[newIndex].dataset.active = true
        delete activeSlides.dataset.active

    })

})