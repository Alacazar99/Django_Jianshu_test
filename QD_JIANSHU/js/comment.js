$(function(){
	$("#add-ablum").click(function(){
		$('#add-category-from').slideDown('normal');
	});
	$('#btn-main,#btn-cancel').click(function(){
		$('#add-category-from').slideUp('fast');
	});
	$('.update-ablum-btn').click(function(){
		$('#update-ablum-modal').modal('show');
	});
	
	
})
