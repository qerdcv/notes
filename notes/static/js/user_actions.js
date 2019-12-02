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
$('ul').on("click", "li.notes", function () {
    let id = $(this).attr('data-id');
    data = {
        type: "delete",
        id: id,
    };
    ws.send(JSON.stringify(data))
});
addEventListener('keydown', function (key) {
    if (key.keyCode == 13) {
        if ($('input[name=note]').val().length != 0) {
            $('#Click').click();
        }
    }
})
