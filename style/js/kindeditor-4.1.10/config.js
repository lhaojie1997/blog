KindEditor.ready(function(K) {
                K.create('textarea[name=content]',{
                //     K.create('#id_content',{
                        width:'800px',
                        height:'200px',
                        uploadJson: '/admin/upload/kindeditor', //新增了这一行
                });
        });