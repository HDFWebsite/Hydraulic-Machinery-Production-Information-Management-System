window.onload = function(){
    $('.left span').click(function(){
        if($(this).siblings().attr('class')=='hidden1'){
            $(this).siblings().removeClass('hidden1')
        }else{
            $(this).siblings().addClass('hidden1')
        }
    })
}

// 管理员退出
function logout(){
    $.get("/logout",function(resp){
        window.location.href = '/'
    })
}


