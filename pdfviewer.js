function scaleimgs() {
    $('.container').find('img').each(function() {
        var imgClass = (this.width / this.height > .1) ? 'wide' : 'tall';
        $(this).addClass(imgClass);
    })
}


var appendNumber = 10;
var prependNumber = 1;
var swiper = new Swiper('.swiper-container', {
    slidesPerView: 3,
    centeredSlides: true,
    spaceBetween: 30,
    pagination: {
        el: '.swiper-pagination',
        type: 'fraction',
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    virtual: {
        slides: (function() {
            var slides = [];
            for (var i = 0; i < 600; i += 1) {
                slides.push(
                    '<div class="container"><img src="./img_files/pdf_page_' + i + '.png"/>'
                );
            }
            return slides;
        }()),
    },
});
document.querySelector('.slide-1').addEventListener('click', function(e) {
    e.preventDefault();
    swiper.slideTo(0, 0);
});

$(window).on('load', function() {
    scaleimgs();
})


swiper.on('transitionEnd', function() {
    scaleimgs();
});