window.onload = function() {

    $('#subadd').click(function () {
        var num_val = document.getElementById("num").value;
        if (num_val == ""){
            alert("请输入组成量！！！")
        }else{
            var sid_val = document.getElementById("sid").value;
            var sna_val = document.getElementById("sna").value ;
            var sun_val = document.getElementById("sun").value;
            var cate_val = document.getElementById("cate").value;
            var num_valu = document.getElementById("num").value;
            var tab_str = "<tr><td width='30px'><input type='checkbox' name='ckb'/><td class='ssid'>"+sid_val+"</td><td class='ssna'>"+sna_val+"</td><td class='ssun'>"+sun_val+"</td><td class='sscate'>"+cate_val+"</td><td class='ssnum'>"+num_valu+"</td></tr>";
            $("#bom_relation").append(tab_str);
            document.getElementById("sid").value = "";
            document.getElementById("sna").value = "";
            document.getElementById("sun").value = "";
            document.getElementById("cate").value = "";
            document.getElementById("num").value = "";
        }
    });

    $('#main_query_name').click(function () {
        var main_sel_num = document.getElementById("main_sel").value;
        var query_val = document.getElementById("main_query_text").value;
        if (query_val ==""){
            alert("请输入要查询的内容！")
        }else {
            var params = {
                "m_page": "1",
                "query_sel":main_sel_num,
                "query_text":query_val,
                "query_key": "产成品"
            };
            $.ajax({
                url: "/onebaseinputquery",
                type: "post",
                headers: {
                    "X-CSRFToken": getCookie("csrf_token")
                },
                data: JSON.stringify(params),
                contentType: "application/json",
                success: function (resp) {
                    var tableDict = resp.data.boms_dict;
                    var mainStrHtml = '<tbody id="bommain">';
                    for (i = 0; i < tableDict.length; i++) {
                        mainStrHtml += '<tr><td class="mid">' + tableDict[i].main_id +
                            '</td><td class="mna">' + tableDict[i].main_name + '</td><td class="mun">' +
                            tableDict[i].unit + '</td><td class="mca">' + tableDict[i].cate +
                            '</td><td class="main_choice">选择</td></tr>'
                    }
                    mainStrHtml += '</tbody>';
                    document.getElementById("bommain").innerHTML =mainStrHtml;
                    document.getElementById("maincurr").innerText=resp.data.current_page;
                    var mainBomHtml = '<tr id="mainbom"><td>第<span id="maincurr">'+
                        resp.data.current_page+ '</span>页共<span id="maintota">'+
                        resp.data.total_page+'</span>页</td><td><a class="mainpage">'
                        +'首页</a></td><td><a class="mainpage">上一页</a></td>';
                    for (i = 1; i <= resp.data.total_page; i++) {
                        mainBomHtml += '<td><a class="mainpage">' + i + '</a></td>';
                    }
                    mainBomHtml +='<td><a class="mainpage">下一页</a></td><td><a class="mainpage">末页</a></td> </tr>';
                    document.getElementById("mainbom").innerHTML = mainBomHtml;
                }
            });
        }
    });

    $('.mainpage').click(function (){
        var current_page = $("#maincurr").text();
        var total_page = $("#maintota").text();
        var main_sel_num = document.getElementById("main_sel").value;
        var query_val = document.getElementById("main_query_text").value;
        var pageStr = $(this).text();
        if (pageStr == "首页"){
            page = 1
        }else if(pageStr == "上一页"){
            page = parseInt(current_page)-1
        }else if(pageStr == "下一页"){
            page = parseInt(current_page)+1
        }else if(pageStr == "末页"){
            page = total_page
        }else{
            page = pageStr
        }
         var params = {
            "m_page": page,
            "query_sel":main_sel_num,
            "query_text":query_val,
            "query_key": "产成品"
        };
        $.ajax({
            url: "/onebaseinputquery",
            type: "post",
            headers: {
                "X-CSRFToken": getCookie("csrf_token")
            },
            data: JSON.stringify(params),
            contentType: "application/json",
            success: function (resp) {
                var tableDict = resp.data.boms_dict;
                var mainStrHtml = '<tbody id="bommain">';
                for(i=0;i<tableDict.length;i++){
                     mainStrHtml+='<tr><td class="mid">'+tableDict[i].main_id+
                         '</td><td class="mna">'+tableDict[i].main_name+'</td><td class="mun">'+
                         tableDict[i].unit+'</td><td class="mca">'+tableDict[i].cate+
                         '</td><td class="main_choice">选择</td></tr>'
                }
                mainStrHtml += '</tbody>';
                document.getElementById("bommain").innerHTML =mainStrHtml;
                document.getElementById("maincurr").innerText=resp.data.current_page;
                var mainBomHtml = '<tr id="mainbom"><td>第<span id="maincurr1">'+
                        resp.data.current_page+ '</span>页共<span id="maintota1">'+
                        resp.data.total_page+'</span>页</td><td><a class="mainpage">'
                        +'首页</a></td><td><a class="mainpage">上一页</a></td>';
                for (i = 1; i <= resp.data.total_page; i++) {
                    mainBomHtml += '<td><a class="mainpage">' + i + '</a></td>'
                }
                mainBomHtml +='<td><a class="mainpage">下一页</a></td><td><a class="mainpage">末页</a></td> </tr>';
                document.getElementById("mainbom").innerHTML = mainBomHtml;
            }
        });
    });

    //输入商品名称
    $('#son_query_name').click(function () {
        var main_sel_num = document.getElementById("son_sel").value;
        var query_val = document.getElementById("son_query_text").value;
        if (query_val ==""){
            alert("请输入要查询的内容！")
        }else {
            var params = {
                "m_page": "1",
                "query_sel":main_sel_num,
                "query_text":query_val,
                "query_key": "原材料"
            };
            $.ajax({
                url: "/onebaseinputquery",
                type: "post",
                headers: {
                    "X-CSRFToken": getCookie("csrf_token")
                },
                data: JSON.stringify(params),
                contentType: "application/json",
                success: function (resp) {
                    var tableDict = resp.data.boms_dict;
                    var mainStrHtml = '<tbody id="bomson">';
                    for (i = 0; i < tableDict.length; i++) {
                        mainStrHtml += '<tr><td class="sid">' + tableDict[i].main_id +
                            '</td><td class="sna">' + tableDict[i].main_name + '</td><td class="sun">' +
                            tableDict[i].unit + '</td><td class="sca">' + tableDict[i].cate +
                            '</td><td class="son_choice">选择</td></tr>'
                    }
                    mainStrHtml += '</tbody>';
                    document.getElementById("bomson").innerHTML = mainStrHtml;
                    document.getElementById("soncurr").innerText=resp.data.current_page;
                    var sonBomHtml = '<tr id="sonbom"><td>第<span id="soncurr">'+
                        resp.data.current_page+ '</span>页共<span id="sontota">'+
                        resp.data.total_page+'</span>页</td><td><a class="sonpage">'
                        +'首页</a></td><td><a class="sonpage">上一页</a></td>';
                    for (i = 1; i <= resp.data.total_page; i++) {
                        sonBomHtml += '<td><a class="sonpage">' + i + '</a></td>'
                    }
                    sonBomHtml +='<td><a class="sonpage">下一页</a></td><td><a class="sonpage">末页</a></td> </tr>';
                    document.getElementById("sonbom").innerHTML = sonBomHtml;
                }
            });
        }
    });

    $('.sonpage').click(function (){
        var current_page = $("#soncurr").text();
        var total_page = $("#sontota").text();
        var main_sel_num = document.getElementById("son_sel").value;
        var query_val = document.getElementById("son_query_text").value;
        var pageStr = $(this).text();
        if (pageStr == "首页"){
            page = 1
        }else if(pageStr == "上一页"){
            page = parseInt(current_page)-1
        }else if(pageStr == "下一页"){
            page = parseInt(current_page)+1
        }else if(pageStr == "末页"){
            page = total_page
        }else{
            page = pageStr
        }
         var params = {
            "m_page": page,
            "query_sel":main_sel_num,
            "query_text":query_val,
            "query_key": "原材料"
        };
        $.ajax({
            url: "/onebaseinputquery",
            type: "post",
            headers: {
                "X-CSRFToken": getCookie("csrf_token")
            },
            data: JSON.stringify(params),
            contentType: "application/json",
            success: function (resp) {
                var tableDict = resp.data.boms_dict;
                var sonStrHtml = '<tbody id="bomson">';
                for(i=0;i<tableDict.length;i++){
                     sonStrHtml+='<tr><td class="sid">'+tableDict[i].main_id+
                         '</td><td class="sna">'+tableDict[i].main_name+'</td><td class="sun">'+
                         tableDict[i].unit+'</td><td class="sca">'+tableDict[i].cate+
                         '</td><td class="son_choice">选择</td></tr>'
                }
                sonStrHtml += '</tbody>';
                document.getElementById("bomson").innerHTML =sonStrHtml;
                document.getElementById("soncurr").innerText=resp.data.current_page;
                var sonBomHtml = '<tr id="sonbom"><td>第<span id="soncurr">'+
                        resp.data.current_page+ '</span>页共<span id="sontota">'+
                        resp.data.total_page+'</span>页</td><td><a class="sonpage">'
                        +'首页</a></td><td><a class="sonpage">上一页</a></td>';
                for (i = 1; i <= resp.data.total_page; i++) {
                    sonBomHtml += '<td><a class="sonpage">' + i + '</a></td>'
                }
                sonBomHtml +='<td><a class="sonpage">下一页</a></td><td><a class="sonpage">末页</a></td></tr>';
                document.getElementById("sonbom").innerHTML = sonBomHtml;
            }
        });
    });

    $("#bommain").on('click','.main_choice',function () {
        var mid_text = $(this).prevAll(".mid").text();
        var mna_text = $(this).prevAll(".mna").text();
        var mun_text = $(this).prevAll(".mun").text();
        var bom_rel = $("#bom_relation").children();
        bom_rel.each(function() {
            $(this).remove();
        });
        document.getElementById("mid").value = mid_text;
        document.getElementById("mna").value = mna_text;
        document.getElementById("mun").value = mun_text;
    });

    $("#bomson").on('click','.son_choice',function () {
        var mid_text = $(this).prevAll(".sid").text();
        var mna_text = $(this).prevAll(".sna").text();
        var mun_text = $(this).prevAll(".sun").text();
        var sca_text = $(this).prevAll(".sca").text();
        document.getElementById("sid").value = mid_text;
        document.getElementById("sna").value = mna_text;
        document.getElementById("sun").value = mun_text;
        document.getElementById("cate").value = sca_text;
    });


};
//获取cookie
function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

function delTr2(){//获取选中的复选框，然后循环遍历删除
     var ckb = "ckb";
     var ckbs=$("input[name="+ckb+"]:checked");
     if(ckbs.size()==0){
        alert("要删除指定行，需选中要删除的行！");
        return;
     }
       ckbs.each(function(){
          $(this).parent().parent().remove();
       });
  }

function storeRel() {
    var main_id = document.getElementById("mid").value;
    var main_name = document.getElementById("mna").value;
    var bom_rel = $("#bom_relation").children();
    bom_rel.each(function() {
        var son_id = $(this).children(".ssid").text();
        var son_num = $(this).children(".ssnum").text();
        var params = {
            "main_id":main_id,
            "main_name":main_name,
            "son_id":son_id,
            "son_num":son_num,
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
