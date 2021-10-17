$(document).ready(function () {
    $(".main_nav li a, .scrollBtn").on("click", function (event) {
        //отменяем стандартную обработку нажатия по ссылке
        event.preventDefault();
        //забираем идентификатор бока с атрибута href
        var id  = $(this).attr('href'),
            //узнаем высоту от начала страницы до блока на который ссылается якорь
            top = $(id).offset().top;

        top = top - 60;

        //анимируем переход на расстояние - top за 1500 мс
        $('body,html').animate({scrollTop: top}, 500);

        $('.xs_menu').removeClass('active');
        $('body').css('overflow','auto');
    });

    $(function () {
        setInterval(function()
        {
            $('.blink_btn').addClass('blink_on');
            setTimeout(function(){$('.blink_btn').removeClass('blink_on')},2500);
        },4000);
    });

    $(function()
    {
        $("input[type=tel]").mask("9 (999) 999-9999");
    });

    $(function () {
        // new WOW().init();

        // AOS.init({
        //     offset: 0
        // });
    });

    function parallax(layer, container, x, y) {
        var $layer_1 = layer,
            $container = container,
            container_w = $container.width(),
            container_h = $container.height();

        $(window).on('mousemove.parallax', function(event) {
            var pos_x = event.clientX,
                pos_y = event.clientY,
                left  = 0,
                top = 0;

            left = container_w / 2 - pos_x;
            top  = container_h / 2 - pos_y;

            TweenMax.to(
                $layer_1,
                1,
                {
                    css: {
                        transform: 'translateX(' + left / x + 'px) translateY(' + top / y + 'px)'
                    },
                    ease:Expo.easeOut,
                    overwrite: 'all'
                });
        });

    }

    $(function () {
        parallax($('.offer_bg'), $('.offer_block'), -50, -50);
        parallax($('.repair_is_no_longer_your_headache_img'), $('.repair_is_no_longer_your_headache'), -50, -50);
        parallax($('.decor_bg, .dots'), $('.in_addition_models_on_site'), -50, -50);
    });

    $(function () {
        var rellax = new Rellax('.rellax');
    });

    $(function () {
        $(window).scroll(function(){
            if ($(this).scrollTop() > 100) {
                $('.scrollup').addClass('active');
            } else {
                $('.scrollup').removeClass('active');
            }
        });

        $('.scrollup').click(function(){
            $("html, body").animate({ scrollTop: 0 }, 600);
            return false;
        });
    });

    $(function () {
        $('.o_xs_menu').click(function () {
            $('body').css('overflow','hidden');
            $('.xs_menu').addClass('active');
        });

        $('.c_xs_menu').click(function () {
            $('body').css('overflow','auto');
            $('.xs_menu').removeClass('active');
        });
    });

    $(function () {
        $('.order_btn').click(function () {
            var val = $(this).val();
            $('#what').val(val);
            $.fancybox.open($('#order_modal'));
        });
    });

    $(function () {
        $('.benefits_slider').owlCarousel({
            loop:true,
            nav:false,
            dots:true,
            items: 3,
            autoplay:false,
            // navText: [$('.prev_btn'),$('.next_btn')],
            // navText : ["<i class=\"fas fa-arrow-left fas_icon\"></i>","<i class=\"fas fa-arrow-right fas_icon\"></i>"],
            autoplayTimeout:3000,
            autoplayHoverPause:true,
            center: true,
            margin: 30,
            responsive : {
                // breakpoint from 0 up
                0 : {
                    items: 1,
                    margin: 0
                },
                576 : {
                    items: 2,
                    margin: 20,
                    center: false
                },
                800 : {
                    items: 3,
                    margin: 20,
                    center: false
                },
            }
        });
    });

    $(function () {
        $('ul.tabs__caption').on('click', 'li:not(.active)', function() {
            $(this)
                .addClass('active').siblings().removeClass('active')
                .closest('div.tabs').find('div.tabs__content').removeClass('active').eq($(this).index()).addClass('active');
        });
    });

    if((/iPhone|iPad|iPod|Android/i.test(navigator.userAgent) && $(document).width() < 991) || $(document).width() < 991)
    {
        $(function () {
            $('.services_slider').addClass('owl-carousel');
            $('.services_slider').owlCarousel({
                loop:true,
                nav:true,
                dots: false,
                items: 1,
                autoplay:false,
                autoplayTimeout:5000,
                autoplayHoverPause:true,
                responsive : {
                    // breakpoint from 0 up
                    0 : {
                        items: 1,
                    },
                    768 : {
                        items: 2,
                        margin: 20,
                    },
                }
            });
        });
    }
});



window.onscroll = function() {myFunction()};

var header = document.getElementById("header");

var sticky = header.offsetTop;

function myFunction() {
    if (window.pageYOffset >= sticky) {
        header.classList.add("sticky");
    } else {
        header.classList.remove("sticky");
    }

    if (window.pageYOffset == 0) {
        header.classList.remove("sticky");
    }
}



$(function () {
    var bLazy = new Blazy({
        breakpoints: [{
            width: 420 // Max-width
            , src: 'data-src-small'
        }]
        , success: function(element){
            setTimeout(function(){
                // We want to remove the loader gif now.
                // First we find the parent container
                // then we remove the "loading" class which holds the loader image
                var parent = element.parentNode;
                parent.className = parent.className.replace(/\bloading\b/,'');
            }, 200);
        }
    });
});
// <img class="b-lazy" src="images/placeholder.svg"
// data-src="images/whatsapp.svg"
// data-src-small="images/whatsapp.svg"
// alt="whatsapp">
