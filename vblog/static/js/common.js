$(function(){
	$("#add-ablum-btn").click(function(){
		$("#add-category-form").slideDown('fast');
	});

	$("#add-category-form .btn-cancel").click(function(){
		$("#add-category-form").slideUp('fast');
	});

	$(".update-ablum-btn").click(function(){
		$("#update-ablum-modal").modal("show");
	})


	function show_delete_modal(){
		// 找到文集的名称（id）
		var wenji_name = $(this).parent().parent().parent().parent().children("label.wenji_name").text()
		var wenji_id = $(this).attr("data_id")
		//删除文集
		$("#delete_wenji_id").val(wenji_id)
		//弹出对话框：确定删除文集
		$("#delete-ablum-modal .modal-body strong.wenji_name").text(" 《" + wenji_name + "》 ")
		//文集删除，渲染
		$("#delete-ablum-modal").modal("show");
	}

	$(".delete-ablum-btn").click(show_delete_modal)
	//发送验证码
	$("#send_code_to_email").click(function(e){
		e.preventDefault();
		//获取邮箱地址：
		var email = $("#id_email").val()
		if(!email || email.trim()==""){
			alert("邮箱不能为空")
			return;
		}

		var csrf = $("#register_form input[name='csrfmiddlewaretoken']").val()
		$.post('/user/sendcode',{'email':email,'csrfmiddlewaretoken':csrf},function(data){
			console.info(data)
		})
	})

	// 验证邮箱
	$("#id_email").blur(function(){
		var email = $(this).val()
		$.get('/user/validemail',{'email':email},function(data){
			if(data != "ok") {
				alert("该邮箱已被使用")
			}
		})
	})

	function load_weiji_list(){
		$.get("/blog/category",function(data){
			var html = "";
			//点击新建文集：弹出
			for(var i = 0; i < data.length; i++){
				html += ' <li class="list-group-item" data_id="'+ data[i].pk +'"> <label class="wenji_name">' + data[i].fields.category_name + '</label>'
				html += `
				<div class="btn-group pull-right">
					  <a class="dropdown-toggle ablum-opt-btn" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
						<span class="glyphicon glyphicon-cog" aria-hidden="true"></span>
					  </a>
					  <ul class="dropdown-menu">
						<li><a href="#" class="update-ablum-btn"  data_id="${data[i].pk}"><span class="glyphicon glyphicon-edit" aria-hidden="true"></span> 修改文集</a></li>
						<li role="separator" class="divider"></li>
						<li><a href="#" class="delete-ablum-btn" data_id="${data[i].pk}"><span class="glyphicon glyphicon-trash" aria-hidden="true"></span> 删除文集</a></li>
					  </ul>
					</div>
				  </li>
				`
			}

			$("#wenji_list").html(html)
			// 重新绑定 点击事件
			$(".delete-ablum-btn").click(show_delete_modal)
		})
	}

	$("#weiji_submit_btn").click(function(e){
		e.preventDefault();
		//点击：提交（创建新文集）
		var category_name = $("#create_wenji_form > input").val()
		$.post("/blog/category",{"name":category_name},function(data){
			if(data == "ok") {
				load_weiji_list();
				$(".delete-ablum-btn").click(show_delete_modal)
				$("#create_wenji_form > input").val('')
				$("#add-category-form .btn-cancel").click()
			} else {
				alert(data)
			}
		})
	})

	//点击：删除文集
	$("#confirm_delete_btn").click(function(){
		var wenji_id = $("#delete_wenji_id").val()
		$.post("/blog/category/delete",{cate_id:wenji_id},function(data){
			if(data == "ok") {
				load_weiji_list();
				$("#delete-ablum-modal").modal("hide");
			} else {
				alert(data)
			}
		})
	})


	$("#wenji_list > li").click(function(){
		$("#wenji_list > li").each(function(){
			$(this).removeClass("active_blog")
		})

		$(this).addClass("active_blog")
	})
})