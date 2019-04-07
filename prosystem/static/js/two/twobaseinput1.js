window.onload = function() {
    //输入商品名称
    $('#input1_mquery_text').mouseleave(function () {
        var main_sel_num = document.getElementById("input1_msel").value;
        var query_val = document.getElementById("input1_mquery_text").value;
        var query = document.getElementById("input1_mall");
        var query_str = query+"&m_sel="+main_sel_num+"&m_qstr="+query_val;
        $('#input1_mquery_name').attr('href',query_str);
    });
    //输入商品名称
    $('#input1_squery_text').mouseleave(function () {
        var son_sel_num = document.getElementById("input1_ssel").value;
        var query_val = document.getElementById("input1_squery_text").value;
        var query = document.getElementById("input1_sall");
        var query_str = query+"&s_sel="+son_sel_num+"&s_qstr="+query_val;
        $('#input1_squery_name').attr('href',query_str);
    });
    $('.input1_choice').click(function () {
        var mid_text = $(this).prevAll(".input1_id").text();
        var mna_text = $(this).prevAll(".input1_name").text();
        var mun_text = $(this).prevAll(".input1_unit").text();
        document.getElementById("input1_sid").value = mid_text;
        document.getElementById("input1_sna").value = mna_text;
        document.getElementById("input1_sun").value = mun_text;

    });
    $('#input1_in').click(function () {
        var num_val = document.getElementById("input1_spr").value;
        if (num_val == ""){
            alert("请输入价格！！！")
        }else{
            var sid_val = document.getElementById("input1_sid").value;
            var pr_val = document.getElementById("input1_spr").value;
            var params = {
            "main_id":sid_val,
            "price":pr_val
            };
        $.ajax({
            url: "/twomaterialinput1add",
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
    $('#input1_mv').click(function () {
        document.getElementById("input1_sid").value = "";
        document.getElementById("input1_sna").value = "";
        document.getElementById("input1_sun").value = "";
        document.getElementById("input1_spr").value = "";
    });

    $('.input1_del').click(function () {
        var main_id = $(this).prevAll(".input1_sid").text();
        var params = {
        "main_id":main_id
        };
        $.ajax({
            url: "/twomaterialinput1del",
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
