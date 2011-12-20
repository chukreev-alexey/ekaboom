function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
$(document).ready(function() {
    $.ajaxSetup({
        cache: false,
        type: 'POST',
        dataType: 'html',
        beforeSend: function(xhr, settings) {
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    });
    /*Rotator*/
    $("#Rotator").rotator({
		'items': '.RotatorItem',
		'prev': '#RotatorPrevLink',
		'next': '#RotatorNextLink',
		'visibleCount': 4,
		'changeCount': 2,
		'keyboardNavigation': true
	});
    
    /*Cart*/
    $(".ToCart").click(function(){
        var event_object = $(this);
        product = $(this).attr('itemid');
        if (!product) {
            return false;
        }
        $.ajax({
            url: '/cart/add/',
            data: {product: product},
            dataType: 'html',
            type: "POST",
            error: function(){
                alert('ошибка');
            },
            success: function(data){
                data = eval('('+data+')');
                if (data.count > 0) {
                    $("#ShopingCart").html(data.cart_text);
                    $("#ShopingCart").show();
                    event_object.effect('transfer',{to: '#ShopingCart'}, 1000);
                }
                else {
                     $("#ShopingCart").hide();
                }
            }
        });
        return false;
    });
});