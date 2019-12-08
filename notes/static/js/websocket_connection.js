var ht = window.location.host;
var url = 'ws://' + ht + '/';
var ws = new WebSocket(url);

ws.onmessage = function (e) {
	let data = JSON.parse(e.data);
	if (data['type'] == 'add') {
		let li = "<li><input type='checkbox' id='" + data.id + "' class='notes'><label style='margin-left: 31px' for='" + data.id + "'>" + data.text + "</label></li>";
		$('ul').append(li);
		$('input[name=note]').val('');
	} else if (data['type'] == 'change_status') {
		$('input[id='+data.id+']').prop('checked', data.status)
	}
};