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
    if(confirm('是否确认退出？')) {
        $.get("/logout", function (resp) {
            window.location.href = '/'
        })
    }
}

// 管理员退出
function logoff(){
    if(confirm('是否确认注销？')) {
        $.get("/logoff", function (resp) {
            window.location.href = '/'
        })
    }
}

