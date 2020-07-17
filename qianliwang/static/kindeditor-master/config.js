/**
 * Created by 14903 on 2020/6/14.
 */
KindEditor.ready(function (k) {
    window.editor = k.create('textarea[name="content"]',{
        resizeType:1,
        allowPreviewEmoticons : false,
        allowImageRemote : false,
        'uploadJson':'/admin/upload/kindeditor',
        height:'1000px',
        width:'1000px'

    });
})
