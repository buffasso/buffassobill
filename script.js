$( document ).ready(function() {
    $(".head").height($( window ).height());
    $(".button-collapse").sideNav();
    /*$(".mycarousel").slick({
        infinite: true,
        autoplay: true,
        autoplaySpeed: 2000,
        slidesToShow: 6,
        slidesToScroll: 1,
        responsive: [
            {
                breakpoint: 750,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 1,
                    infinite: true
                }
            }
        ],
        appendArrows : $(".arrows"),
        prevArrow : '<button class="waves-effect waves-light btn red prev"><i class="fa fa-arrow-left" aria-hidden="true"></i> Précédent</button>',
        nextArrow : '<button class="waves-effect waves-light btn red">Suivant <i class="fa fa-arrow-right" aria-hidden="true"></i> </button>'

    })*/
});

function scrollDown(){
    $('html, body').animate({
        scrollTop: $("#navbar").offset().top
    }, 1000);
}