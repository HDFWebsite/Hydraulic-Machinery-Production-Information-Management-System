window.onload = function() {
    //输入商品名称
    $('#main_query_text').mouseleave(function () {
        var main_sel_num = document.getElementById("main_sel").value;
        var query_val = document.getElementById("main_query_text").value;
        var query_str = "/onebaseinput?m_sel="+main_sel_num+"&m_qstr="+query_val;
        $('#main_query_name').attr('href',query_str);
    });
    //输入商品名称
    $('#son_query_text').mouseleave(function () {
        var son_sel_num = document.getElementById("son_sel").value;
        var query_val = document.getElementById("son_query_text").value;
        var query_str = "/onebaseinput?s_sel="+son_sel_num+"&s_qstr="+query_val;
        $('#son_query_name').attr('href',query_str);
    });

    $('.main_choice').click(function () {
        var bom_rel = $("#bom_relation").children();
        bom_rel.each(function() {
            $(this).remove();
        });
        var mid_text = $(this).prevAll(".mid").text();
        var mna_text = $(this).prevAll(".mna").text();
        var mun_text = $(this).prevAll(".mun").text();
        document.getElementById("mid").value = mid_text;
        document.getElementById("mna").value = mna_text;
        document.getElementById("mun").value = mun_text;

    });
    $('.son_choice').click(function () {
        var mid_text = $(this).prevAll(".sid").text();
        var mna_text = $(this).prevAll(".sna").text();
        var mun_text = $(this).prevAll(".sun").text();
        document.getElementById("sid").value = mid_text;
        document.getElementById("sna").value = mna_text;
        document.getElementById("sun").value = mun_text;

    });
    $('#subadd').click(function () {
        var num_val = document.getElementById("num").value;
        if (num_val == ""){
            alert("请输入组成量！！！")
        }else{
            var sid_val = document.getElementById("sid").value;
            var sna_val = document.getElementById("sna").value ;
            var sun_val = document.getElementById("sun").value;
            var num_valu = document.getElementById("num").value;
            var tab_str = "<tr><td width='30px'><input type='checkbox' name='ckb'/><td class='ssid'>"+sid_val+"</td><td class='ssna'>"+sna_val+"</td><td class='ssun'>"+sun_val+"</td><td class='ssnum'>"+num_valu+"</td></tr>";
            $("#bom_relation").append(tab_str);
            document.getElementById("sid").value = "";
            document.getElementById("sna").value = "";
            document.getElementById("sun").value = "";
            document.getElementById("num").value = "";
        }
    });

};
//获取cookie
function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

function delTr(ckb){//获取选中的复选框，然后循环遍历删除
     var ckbs=$("input[name="+ckb+"]:checked");
     if(ckbs.size()==0){
        alert("要删除指定行，需选中要删除的行！");
        return;
     }
       ckbs.each(function(){
          $(this).parent().parent().remove();
       });
  }

function delTr2(){
     delTr('ckb');
}

function storeRel() {
    var main_id = document.getElementById("mid").value;
    var main_name = document.getElementById("mna").value;
    var bom_rel = $("#bom_relation").children();
    bom_rel.each(function() {
        var son_id = $(this).children(".ssid").text();
        var son_name = $(this).children(".ssna").text();
        var son_num = $(this).children(".ssnum").text();
        var son_unit = $(this).children(".ssun").text();
        var params = {
            "main_id":main_id,
            "main_name":main_name,
            "son_id":son_id,
            "son_name":son_name,
            "son_num":son_num,
            "son_unit":son_unit
        };
        $.ajax({
            url: "/onebaseinputadd",
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
}
