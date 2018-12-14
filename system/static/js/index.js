window.onload = function(){
    $('.left span').click(function(){
        if($(this).siblings().attr('class')=='hidden1'){
            $(this).siblings().removeClass('hidden1')
        }else{
            $(this).siblings().addClass('hidden1')
        }
    })
}