var ht = window.location.host;
var url = 'ws://' + ht + '/';
var ws = new WebSocket(url);

ws.onmessage = function (e) {
	let data = JSON.parse(e.data);
	console.log('message', data);
	if (data['type'] == 'add') {
		let li = "<li class='notes' data-id='" + data.id + "'><p id='note'><strong>" + data.text + "</strong></p></li>";
		$('ul').append(li);
		$('input[name=note]').val('');
	} else if (data['type'] == 'delete') {
		$('li[data-id=' + data.id + ']').remove()
	}
};

ws.onopen = function (e) {
    console.log('Websocket open');
};

ws.onclose = function (e) {
	console.log('Websocket close')
};

