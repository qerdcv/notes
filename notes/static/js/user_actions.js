$('.add_button').click(function () {
    let note = $('input[name=note]').val();
    if (note.length > 0){
        let data = {
            type: "add",
            text: note
        };
        ws.send(JSON.stringify(data));
    }else{
      alert("error, empty input")
    }
});

$('ul').on("change",'input', function () {
    let id = $(this).attr('id');
    let done_status = $(this).prop('checked');

    let data = {
        type: "change_status",
        id: id,
        status: done_status,
    };

    ws.send(JSON.stringify(data))
});

addEventListener('keydown', function (key) {
    if (key.keyCode == 13) {
        if ($('input[name=note]').val().length != 0) {
            $('#Click').click();
        }
    }
});
