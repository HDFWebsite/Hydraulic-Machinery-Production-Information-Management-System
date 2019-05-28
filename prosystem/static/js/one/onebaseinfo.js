window.onload = function () {
    $('#page_num').change(function () {
        window.location = this.value;
    });
    //输入商品名称
    $('#query_text').mouseleave(function () {
        var query_val = document.getElementById("query_text").value;
        var query_str = "/onebaseinfo?query_str=" + query_val;
        $('#query_name').attr('href', query_str);
    });

    //取消
    $('.cancel').click(function () {
        $('#add_list').addClass('hidden');
        $('.add_bt a').text("增加");
        $('#upd_list').addClass('hidden');
        $('.upd_bt a').text("更改");
    });

    //删除bom
    $('.del_bt').click(function () {
        if ($("input[name='check_box']:checked").size() == 0) {
            alert("请先选择需要删除的物料！");
            return
        }
        if (confirm("您确认删除吗？")) {
            var obj = document.getElementsByName("check_box");
            for (var k = 1; k <= obj.length; k++) {
                if (obj[k].checked) {
                    $.get("/onebaseinfodel", {'main_id': obj[k].value},
                        function (resp) {
                            if (resp.errno == "200") {
                                alert("数据删除成功！！！");
                                document.location.reload();
                            } else {
                                alert(resp.errmsg);
                                document.location.reload();
                            }
                        });
                }
            }
        }

    });

    //增加bom
    $('.add_bt').click(function () {
        if ($('#add_list').attr('class') == 'hidden') {
            $('#add_list').removeClass('hidden');
            $('.add_bt a').text("确认增加");
        } else {
            var food_num = $('#food_num').val();
            var food_name = $('#food_name').val();
            var food_spec = $('#food_spec').val();
            var food_cate = $('#food_cate').val();
            var food_unit = $('#food_unit').val();
            var food_company = $('#food_company').val();

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
                    if (resp.errno == "200") {
                        alert("保存数据成功！！！")
                    } else {
                        alert("保存数据失败！！！")
                    }
                    document.location.reload()
                }
            });
        }
    });

    //更改bom
    $('.upd_bt').click(function () {
        var obj = document.getElementsByName("check_box");
        if ($('#upd_list').attr('class') == 'hidden') {
            var ckbs = $("input[name='check_box']:checked");
            if (ckbs.size() == 0) {
                alert("请先选择一个需要更改的物料！");
                return;
            }
            ckbs.each(function () {
                $('#upd_list').removeClass('hidden');
                $('.upd_bt a').text("确认更改");
                document.getElementById("update_num").value = $(this).parent().nextAll(".food_num").text();
                document.getElementById("update_name").value = $(this).parent().nextAll(".food_name").text();
                document.getElementById("update_spec").value = $(this).parent().nextAll(".food_spec").text();
                document.getElementById("update_cate").value = $(this).parent().nextAll(".food_cate").text();
                document.getElementById("update_unit").value = $(this).parent().nextAll(".food_unit").text();
                document.getElementById("update_company").value = $(this).parent().nextAll(".food_company").text();
            });

        } else {
            var food_num = $('#update_num').val();
            var food_name = $('#update_name').val();
            var food_spec = $('#update_spec').val();
            var food_cate = $('#update_cate').val();
            var food_unit = $('#update_unit').val();
            var food_company = $('#update_company').val();

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

            var params = {
                "food_num": food_num,
                "food_name": food_name,
                "food_spec": food_spec,
                "food_cate": food_cate,
                "food_unit": food_unit,
                "food_company": food_company
            };
            $.ajax({
                url: "/onebaseinfoupd",
                type: "post",
                headers: {
                    "X-CSRFToken": getCookie("csrf_token")
                },
                data: JSON.stringify(params),
                contentType: "application/json",
                success: function (resp) {
                    if (resp.errno == "200") {
                        alert("更新数据成功！！！")
                    } else {
                        alert("更新数据失败！！！")
                    }
                    document.location.reload()
                }
            });
        }
    });

};
//获取cookie
function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}
