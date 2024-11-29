function copy(target) {
    let output = target.innerText;
    navigator.clipboard.writeText(output).then(function() {
        alert("Copied to clipboard!");
    });
}