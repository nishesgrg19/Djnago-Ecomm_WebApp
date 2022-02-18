$('#slider1, #slider2, #slider3').owlCarousel({
    loop: false,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: false,
            autoplay: true,
        }
    }
})

$('.plus-cart').click(function()
        {
            var id = $(this).attr('pid').toString();
            console.log(id)
            $.ajax({
                type:'GET',
                url:'/pluscart',
                data:{
                    pid:id
                },
                success:function(data){
                    console.log(data)
                    console.log('Success')
                } 
            })
            
        
        }
    )