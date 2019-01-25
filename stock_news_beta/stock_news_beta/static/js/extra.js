$(document).ready(function () {
    
    // 资讯流筛选
    $('.home-news-filter').click(function() { 
        var isChecked = $(this).find('#hudongyi').is(':checked'); 
        isChecked ? $('#hudongyi-news').show() : $('#hudongyi-news').hide(); 

        var isChecked = $(this).find('#e-company').is(':checked'); 
        isChecked ? $('#e-company-news').show() : $('#e-company-news').hide();         
    });
});
