window.onload = function() {
    //输入商品名称
    $('#input2_mquery_text').mouseleave(function () {
        var main_sel_num = document.getElementById("input2_msel").value;
        var query_val = document.getElementById("input2_mquery_text").value;
        var query = document.getElementById("input2_mall");
        var query_str = query+"&m_sel="+main_sel_num+"&m_qstr="+query_val;
        $('#input2_mquery_name').attr('href',query_str);
    });
    //输入商品名称
    $('#input2_squery_text').mouseleave(function () {
        var son_sel_num = document.getElementById("input2_ssel").value;
        var query_val = document.getElementById("input2_squery_text").value;
        var query = document.getElementById("input2_sall");
        var query_str = query+"&s_sel="+son_sel_num+"&s_qstr="+query_val;
        $('#input2_squery_name').attr('href',query_str);
    });
    $('.input2_choice').click(function () {
        var mid_text = $(this).prevAll(".input2_id").text();
        var mna_text = $(this).prevAll(".input2_name").text();
        var mun_text = $(this).prevAll(".input2_unit").text();
        document.getElementById("input2_sid").value = mid_text;
        document.getElementById("input2_sna").value = mna_text;
        document.getElementById("input2_sun").value = mun_text;

    });
    $('#input2_in').click(function () {
        var num_val = document.getElementById("input2_spr").value;
        if (num_val == ""){
            alert("请输入价格！！！")
        }else{
            var sid_val = document.getElementById("input2_sid").value;
            var pr_val = document.getElementById("input2_spr").value;
            var params = {
            "main_id":sid_val,
            "price":pr_val
            };
        $.ajax({
            url: "/twomaterialinput2add",
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
    $('#input2_mv').click(function () {
        document.getElementById("input2_sid").value = "";
        document.getElementById("input2_sna").value = "";
        document.getElementById("input2_sun").value = "";
        document.getElementById("input2_spr").value = "";
    });

    $('.input2_del').click(function () {
        var main_id = $(this).prevAll(".input2_sid").text();
        var params = {
        "main_id":main_id
        };
        $.ajax({
            url: "/twomaterialinput2del",
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
