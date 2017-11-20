$(function () {

   $('.category li').click(function () {
       $(this).animate({ left: 50 * $(this).index()});

       var $prevAll = $(this).prevAll();
       $prevAll.each(function () {
           $(this).animate({ left: 50 * $(this).index() });
       });

       var $nextAll = $(this).nextAll();
       var $li_count = $(this).siblings().length;
       $nextAll.each(function () {
            $(this).animate({ left: (($li_count*50)+600)-50*($li_count-$(this).index()) });
       });

       // event.preventDefault();
       // event.stopPropagation();
   }); 
});