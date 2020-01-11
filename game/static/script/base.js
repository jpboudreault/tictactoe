function setActiveMenu(tag){
    $('.nav-item').removeClass('active');
    $(`.nav-item[data=${tag}]`).addClass('active');
}