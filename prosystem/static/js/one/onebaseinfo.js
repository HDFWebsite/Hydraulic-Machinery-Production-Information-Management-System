window.onload = function() {
    $('#page_num').change(function () {
        window.location = this.value;
    });
    //输入商品名称
    $('#query_text').mouseleave(function () {
        var query_val = document.getElementById("query_text").value;
        var query_str = "/onebaseinfo?query_str="+query_val;
        $('#query_name').attr('href',query_str);
    });
    //增加bom
    $('.add_bt').click(function () {
        if ($('#add_list').attr('class') == 'hidden') {
            $('#add_list').removeClass('hidden');
            $('.add_bt a').text("取消");
        } else {
            $('#add_list').addClass('hidden');
            $('.add_bt a').text("增加");
        }
    });
    //保存bom
    $('.keep_bt').click(function () {
        var food_num = $('#food_num').val();
        var food_name = $('#food_name').val();
        var food_spec = $('#food_spec').val();
        var food_cate = $('#food_cate').val();
        var food_unit = $('#food_unit').val();
        var food_company = $('#food_company').val();
        if ($('#add_list').attr('class') == 'hidden') {
            alert("请先点击增加！");
            return
        } else {
            if (food_num == '') {
                alert("货品编号不能为空！");
                return;
            }
            if (food_name == '') {
                alert("货品名称不能为空！");
                return;
            }
            if (food_spec == '') {
                alert("规格不能为空！");
                return;
            }
            if (food_cate == '') {
                alert("货品类别不能为空！");
                return;
            }
            if (food_unit == '') {
                alert("单位不能为空！");
                return;
            }
            if (food_company == '') {
                alert("供应商不能为空！");
                return;
            }
        }
        var params = {
                "food_num": food_num,
                "food_name": food_name,
                "food_spec": food_spec,
                "food_cate": food_cate,
                "food_unit": food_unit,
                "food_company": food_company
         };
        $.ajax({
            url: "/onebaseinfoadd",
            type: "post",
            headers: {
                "X-CSRFToken": getCookie("csrf_token")
            },
            data: JSON.stringify(params),
            contentType: "application/json",
            success: function (resp) {
                if(resp.errno == "200"){
                   alert("保存数据成功！！！")
                }else{
                    alert("保存数据失败！！！")
                }
                document.location.reload()
            }
        });
    });
    //删除bom
    $('.del_bt').click(function () {
        var obj = document.getElementsByName("check_box");
        for(var k=1;k<=obj.length;k++){
            if(obj[k].checked){
               $.get("/onebaseinfodel", {'main_id':obj[k].value},
                  function(resp){
                   if(resp.errno=="200"){
                       alert("数据删除成功！！！");
                       document.location.reload();
                   }else{
                       alert(resp.errmsg);
                       document.location.reload();
                   }

                });
            }
        }
    });

};
//获取cookie
function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}
