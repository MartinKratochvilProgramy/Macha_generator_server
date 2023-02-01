function checkInput() {

    var inputStringField = document.getElementById("inputString");
    var outputLengthField = document.getElementById("length");

    inputStringField.classList.remove("invalid-input");
    outputLengthField.classList.remove("invalid-input");

    if (inputStringField.value.length === 0) {
        inputStringField.classList.add("invalid-input");
        return false;
    }

    if (outputLengthField.value.length === 0) {
        outputLengthField.classList.add("invalid-input");
        return false;
    }

    return true;
}

function getText() {

    if (!checkInput()) return;

    var inputString = document.getElementById("inputString").value;
    var outputLength = document.getElementById("length").value;

    if (inputString.length === 0 || outputLength.length === 0) return;
    if (outputLength > 5000) return;

    document.getElementById("output").innerHTML = "Generuji text...";

    fetch('http://localhost:8000/generate_text/', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "input-string": inputString,
            "length": outputLength,
        })
    })
        .then(response => response.json())
        .then(response => {
            const text = response;
            console.log(text.message);

            printLetterByLetter("output", text.message, 10);
        })
}

function printLetterByLetter(destination, message, speed) {
    document.getElementById(destination).innerText = "";

    var i = 0;
    var interval = setInterval(function () {
        document.getElementById(destination).innerText = message.slice(0, i);
        i++;
        if (i > message.length) {
            clearInterval(interval);
        }
    }, speed);
}

document.addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        document.getElementById("submitButton").click();
    }
});