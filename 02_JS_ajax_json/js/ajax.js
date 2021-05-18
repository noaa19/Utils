// 使用ajax请求读本地json数据
function getAjax() {
	$.ajax({
		type: "GET",
		url: "resource/ajax.json",
		dataType: "json",
		success: function(data) {
			console.log(data);
			console.log(data.data_1);
			console.log(data.data_1[0].name);
		}
	});
}
