window.onload = function() {

    $('#calRCons').click(function () {
        $.ajax({
            url: "/fourrawmccalculationadd",
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
    $('#RScal').click(function () {
        $.ajax({
            url: "/foursemimccalculationadd",
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
};
//获取cookie
function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}
