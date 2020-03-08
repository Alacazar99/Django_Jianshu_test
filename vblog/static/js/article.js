$(function(){
   function save_article(){
        var title = $("#blog_title ").val()
        var content = CKEDITOR.instances["blog_content"].getData();
        var category_id = $("#wenji_list li.active_blog").attr("data_id");

        var article_id = $("#article_id").val()
        $.post("/blog/article",{blog_title:title, blog_content: content, category_id:category_id, article_id:article_id},function(data){

            if(data.status == 200){
                $("#article_id").val(data.data.article_id)
                article_id = data.data.article_id

                if (article_id){
                    alert("文章保存成功！")
                }else{
                    alert("文章修改成功..")
                }
            } else {
                alert(data.status)
                    }
        })

   }

    CKEDITOR.instances["blog_content"].on("instanceReady",function(){
        this.addCommand('save',{
					exec:function(editor){
						save_article();
					}
		})
    })
});