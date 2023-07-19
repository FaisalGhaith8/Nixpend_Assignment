$(document).ready(function () {
    $("#dataForm").submit(function (event) {
        event.preventDefault();

        const formData = new FormData(this);

        fetch("/generate_qr", {
            method: "POST",
            body: formData
        })
        .then(response => response.blob())
        .then(blob => {
            const url = URL.createObjectURL(blob);
            // Open the PDF in a new tab
            window.open(url, "_blank");
        })
        .catch(error => {
            console.error("Error:", error);
        });
    });
});