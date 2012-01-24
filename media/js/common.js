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
    
    /*Fancybox*/
    $("a[rel=lightbox]").fancybox({
		'transitionIn'		: 'fade',
		'transitionOut'		: 'fade',
		'titlePosition' 	: 'over',
		'titleFormat'		: function(title, currentOpts) {
			return '<span id="fancybox-title-over">' + (title.length ? ' &nbsp; ' + title : '') + '</span>';
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
                    event_object.fadeOut('slow', function() {
                        $(this).fadeIn('slow');
                    });
                    
                    //event_object.effect('transfer',{to: '#ShopingCart'}, 1000);
                }
                else {
                     $("#ShopingCart").hide();
                }
            }
        });
        return false;
    });
    
    /* Изменение количества в корзине */
    $(".OrderItemAmount").focus(function(){
        amount_val = $(this).val();
    });
    $(".ShoppingCartItemAmount > input[object_id]").
    focus(function(){
        amount_val = $(this).val();
    }).
    live('change', function(){
        obj = $(this);
        product = obj.attr("object_id");
        var cval = parseInt(obj.val(), 10);
        if (!cval && obj.val() != '0') {
            obj.val(amount_val);
            return;
        }
        if (cval < 0 || cval > 99) {
            obj.val(amount_val);
            return;
        }
        obj.val(cval);
        $.ajax({
            url: '/cart/update/',
            data: {product: product, amount: cval},
            type: "POST", 
            dataType: 'html',
            success: function(data){
                data = eval('('+data+')');
                if (cval == 0) {
                    obj.parents(".ShoppingCartItem:eq(0)").remove();
                    //obj.parents(".OrderItem:eq(0)").remove();
                }
                else {
                    obj.parents(".ShoppingCartItem:eq(0)").find(".ShoppingCartItemPrice:eq(0)").html(data.one_sum_text);
                }
                if (data.count == 0) {
                    $("#ShopingCart").hide();
                }
                else {
                    $("#ShoppingCartTotal").html('Итого без учета доставки '+data.all_sum_text);
                    $("#ShopingCart").html(data.cart_text);
                    $("#ShopingCart").show();
                }
            }
        });
    });
    
    /*Удаление из корзины*/
    $(".DeleteCartItem").click(function(){
        if (!confirm('Вы уверены, что хотите удалить товар из корзины?')) {
            return false;
        }
        product = $(this).parents(".ShoppingCartItem[object_id]").attr("object_id");
        obj = $(this);
        if (product) {
            $.ajax({
                url: '/cart/delete/'+product+'/',
                type: "POST", 
                dataType: 'html',
                error: function(){
                    alert('Ошибка при удалении товара из корзины');
                },
                success: function(data){
                    data = eval('('+data+')');
                    obj.parents(".ShoppingCartItem").remove();
                    $("#ShoppingCartTotal").html('Итого без учета доставки '+data.all_sum_text);
                    
                    if (data.count > 0) {
                        $("#ShopingCart").html(data.cart_text);
                        $("#ShopingCart").show();
                    }
                    else {
                         $("#ShopingCart").hide();
                    }
                }
            });
        }
        return false;
    });
});