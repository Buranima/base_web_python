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
});