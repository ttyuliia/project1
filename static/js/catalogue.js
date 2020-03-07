'use strict';

$(window).load(function () {

    $('.buy').click(function () {

        let good_id = $(this).parent().next().val();
        alert('Good_Id = ' + good_id);

        $.ajax({
            url: '/catalogue/ajax_cart',
            data: 'gid=' + good_id,
            success: function (result) {
                alert(result.mess);
            }
        });

    });

});