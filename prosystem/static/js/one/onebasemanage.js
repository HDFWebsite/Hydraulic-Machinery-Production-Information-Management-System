window.onload = function() {
//输入商品名称
    $('#my_query_text').mouseleave(function () {
        var son_sel_num = document.getElementById("my_sel").value;
        var query_val = document.getElementById("my_query_text").value;
        var query_str = "/onebasemanage?my_sel=" + son_sel_num + "&my_qstr=" + query_val;
        $('#my_query_name').attr('href', query_str);
    });

    $('.del_bt').click(function () {
        var main_id = $(this).prevAll(".my_main_id").text();
        $.get("/onebasemanagedel", {'main_id':main_id},
          function(resp){
           if(resp.errno=="200"){
               alert("数据删除成功！！！");
               document.location.replace("/onebasemanage");
           }else{
               alert(resp.errmsg);
               document.location.reload();
           }

        });

    });
}