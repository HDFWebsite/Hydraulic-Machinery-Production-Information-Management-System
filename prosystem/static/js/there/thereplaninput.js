window.onload = function() {
    //输入商品名称
    $('#plan_mquery_text').mouseleave(function () {
        var main_sel_num = document.getElementById("plan_msel").value;
        var query_val = document.getElementById("plan_mquery_text").value;
        var query = document.getElementById("plan_mall");
        var query_str = query+"&m_sel="+main_sel_num+"&m_qstr="+query_val;
        $('#plan_mquery_name').attr('href',query_str);
    });
    //输入商品名称
    $('#plan_squery_text').mouseleave(function () {
        var son_sel_num = document.getElementById("plan_ssel").value;
        var query_val = document.getElementById("plan_squery_text").value;
        var query = document.getElementById("plan_sall");
        var query_str = query+"&s_sel="+son_sel_num+"&s_qstr="+query_val;
        $('#plan_squery_name').attr('href',query_str);
    });

    $('.plan_choice').click(function () {
        var mid_text = $(this).prevAll(".plan_mid").text();
        var mna_text = $(this).prevAll(".plan_mna").text();
        var mun_text = $(this).prevAll(".plan_mun").text();
        document.getElementById("plan_id").value = mid_text;
        document.getElementById("plan_na").value = mna_text;
        document.getElementById("plan_un").value = mun_text;

    });
    $('#plan_store').click(function () {
        var num_val = document.getElementById("plan_num").value;
        if (num_val == ""){
            alert("请输入价格！！！")
        }else{
            var sid_val = document.getElementById("plan_id").value;
            var sna_val = document.getElementById("plan_na").value;
            var sun_val = document.getElementById("plan_un").value;
            var pr_val = document.getElementById("plan_num").value;
            var params = {
            "main_id":sid_val,
            "main_name":sna_val,
            "main_unit":sun_val,
            "num":pr_val
            };
        $.ajax({
            url: "/thereproplaninputadd",
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
    $('#plan_quit').click(function () {
        document.getElementById("plan_id").value = "";
        document.getElementById("plan_na").value = "";
        document.getElementById("plan_un").value = "";
        document.getElementById("plan_num").value = "";
    });

    $('.plan_sdel').click(function () {
        var id = $(this).prevAll(".plan_iid").text();
        var params = {
        "id":id
        };
        $.ajax({
            url: "/thereproplaninputdel",
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
