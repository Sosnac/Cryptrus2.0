const express = require('express');
const CryptoJS = require('crypto-js');
const app = express();
const PORT = 3000;

// 1. Your Secret Key (Keep this very safe in a real app!)
const SECRET_KEY = "my-ultra-secure-key-123";

// 2. Encryption Function
const encryptData = (text) => {
    return CryptoJS.AES.encrypt(text, SECRET_KEY).toString();
};

// 3. Decryption Function
const decryptData = (ciphertext) => {
    const bytes = CryptoJS.AES.decrypt(ciphertext, SECRET_KEY);
    return bytes.toString(CryptoJS.enc.Utf8);
};

// --- Demonstration ---
const originalMessage = "Hello, this is a secure message from CryPTrus 2.0!";
const encrypted = encryptData(originalMessage);
const decrypted = decryptData(encrypted);

console.log("--- CryPTrus 2.0 Logic Check ---");
console.log("Original:", originalMessage);
console.log("Encrypted (Ciphertext):", encrypted);
console.log("Decrypted (Plaintext):", decrypted);
console.log("---------------------------------");

// 4. Basic Route
app.get('/', (req, res) => {
    res.send(`
        <h1>CryPTrus 2.0 is Running!</h1>
        <p><b>Original:</b> ${originalMessage}</p>
        <p><b>Encrypted:</b> ${encrypted}</p>
        <p><b>Decrypted:</b> ${decrypted}</p>
    `);
});

app.listen(PORT, () => {
    console.log(`Server is sprinting on http://localhost:${PORT}`);
});
