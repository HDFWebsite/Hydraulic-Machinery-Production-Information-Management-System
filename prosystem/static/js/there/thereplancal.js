window.onload = function() {

    $('#requireCal').click(function () {
        $.ajax({
            url: "/theremareqcalculationadd",
            type: "post",
            headers: {
                "X-CSRFToken": getCookie("csrf_token")
            },
            data: JSON.stringify({}),
            contentType: "application/json",
            success: function (resp) {
                document.location.reload()
            }
        });

    });

    $('.changeorder').click(function () {
        var id = $(this).prevAll(".changeid").text();
        $.ajax({
            url: "/therepurchaseordergetadd",
            type: "post",
            headers: {
                "X-CSRFToken": getCookie("csrf_token")
            },
            data: JSON.stringify({"id":id}),
            contentType: "application/json",
            success: function (resp) {
                document.location.reload()
            }
        });
    });
    $('.getgoods').click(function () {
        var id = $(this).prevAll(".getid").text();
        $.ajax({
            url: "/thereproarrivalmanageadd",
            type: "post",
            headers: {
                "X-CSRFToken": getCookie("csrf_token")
            },
            data: JSON.stringify({"id":id}),
            contentType: "application/json",
            success: function (resp) {
                document.location.reload()
            }
        });
    });

};
//获取cookie
function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}
