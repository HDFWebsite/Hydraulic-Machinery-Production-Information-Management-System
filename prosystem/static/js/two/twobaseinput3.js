window.onload = function() {
    //输入商品名称
    $('#input3_mquery_text').mouseleave(function () {
        var main_sel_num = document.getElementById("input3_msel").value;
        var query_val = document.getElementById("input3_mquery_text").value;
        var query = document.getElementById("input3_mall");
        var query_str = query+"&m_sel="+main_sel_num+"&m_qstr="+query_val;
        $('#input3_mquery_name').attr('href',query_str);
    });
    //输入商品名称
    $('#input3_squery_text').mouseleave(function () {
        var son_sel_num = document.getElementById("input3_ssel").value;
        var query_val = document.getElementById("input3_squery_text").value;
        var query = document.getElementById("input3_sall");
        var query_str = query+"&s_sel="+son_sel_num+"&s_qstr="+query_val;
        $('#input3_squery_name').attr('href',query_str);
    });
    $('.input3_choice').click(function () {
        var mid_text = $(this).prevAll(".input3_id").text();
        var mna_text = $(this).prevAll(".input3_name").text();
        var mun_text = $(this).prevAll(".input3_unit").text();
        document.getElementById("input3_sid").value = mid_text;
        document.getElementById("input3_sna").value = mna_text;
        document.getElementById("input3_sun").value = mun_text;

    });
    $('#input3_in').click(function () {
        var num_val = document.getElementById("input3_spr").value;
        if (num_val == ""){
            alert("请输入价格！！！")
        }else{
            var sid_val = document.getElementById("input3_sid").value;
            var pr_val = document.getElementById("input3_spr").value;
            var params = {
            "main_id":sid_val,
            "price":pr_val
            };
        $.ajax({
            url: "/twomaterialinput3add",
            type: "post",
            headers: {
                "X-CSRFToken": getCookie("csrf_token")
            },
            data: JSON.stringify(params),
            contentType: "application/json",
            success: function (resp) {
                document.location.reload()
            }
        });

        }
    });
    $('#input3_mv').click(function () {
        document.getElementById("input3_sid").value = "";
        document.getElementById("input3_sna").value = "";
        document.getElementById("input3_sun").value = "";
        document.getElementById("input3_spr").value = "";
    });

    $('.input3_del').click(function () {
        var main_id = $(this).prevAll(".input3_sid").text();
        var params = {
        "main_id":main_id
        };
        $.ajax({
            url: "/twomaterialinput3del",
            type: "post",
            headers: {
                "X-CSRFToken": getCookie("csrf_token")
            },
            data: JSON.stringify(params),
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
