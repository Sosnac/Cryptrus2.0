const express = require('express');
const https = require('https');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = 3443;

// 1. Read the newly forged SSL certificates
const sslOptions = {
    key: fs.readFileSync(path.join(__dirname, 'server.key')),
    cert: fs.readFileSync(path.join(__dirname, 'server.cert'))
};

// 2. Serve the CryPTrus 2.0 public HTML file
app.use(express.static(path.join(__dirname, 'public')));

// 3. Launch the Secure HTTPS Server
https.createServer(sslOptions, app).listen(PORT, () => {
    console.log('\n=============================================');
    console.log('🛡️  CryPTrus 2.0 SECURE SERVER INITIATED 🛡️');
    console.log(`🌐 ACCESS VAULT AT: https://localhost:${PORT}`);
    console.log('=============================================\n');
});
