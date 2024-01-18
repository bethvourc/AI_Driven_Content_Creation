function generateContent() {
    const contentType = document.getElementById("content-type").value;
    fetch(`/generate/${contentType}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById("result").innerText = data.content;
        })
        .catch(error => console.error('Error:', error));
}
