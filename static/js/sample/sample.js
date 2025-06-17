const socketio = io(window.location.origin, { transports: ['websocket'] });

socketio.on("test", function (response) {
    console.log("Sample Socketio response:", response);
});

$(document).ready(function () {
    $.ajax({
        type: "POST",
        url: "/sample_text",
        data: JSON.stringify({ text: "Sample text" }),
        dataType: "json",
        contentType: "application/json",
        success: function (response) {
            console.log("Sample AJAX response:", response);
        }
    });

    socketio.emit("test", { text: "Sample text"});
});