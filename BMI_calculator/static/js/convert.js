function convertFeetToMeters() {
    const feetInput = document.getElementById('feet').value;
    const feet = parseFloat(feetInput);
    const resultElement = document.getElementById('conversionResult');

    if (!isNaN(feet)) {
        const meters = (feet * 0.3048).toFixed(2);
        resultElement.textContent = `${feet} feet is approximately ${meters} meters.`;
    } else {
        resultElement.textContent = feetInput.trim() === "" 
            ? ""  // Clear the message if input is empty
            : "Please enter a valid number.";
    }
}