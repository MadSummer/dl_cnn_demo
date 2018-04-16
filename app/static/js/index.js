$().ready(function () {
  $('#go').on('click', function () {
    var url = $('#url').val().trim();
    if (!url) return alert('请输入图片地址');
    $.post('./getImage', {
      url: url
    }, function (res) {
      if (res.status != 200) return alert('处理出错，请重试！');
      $('#original_image').attr('src', res.orginal_path);
      $('#processed_image').attr('src', res.processed_path);
    });
  });
});
