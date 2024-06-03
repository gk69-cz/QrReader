const { exec } = require('child_process');
const path = require('path');

function scanQrCode(imagePath) {
    return new Promise((resolve, reject) => {
        console.log('test')
        const pythonScriptPath = path.resolve(__dirname, '../../python/scan_qr.py');
        exec(`python ${pythonScriptPath} ${imagePath}`, { encoding: 'utf8' }, (error, stdout, stderr) => {
            if (error) {
                reject(`Error: ${stderr}`);
            } else {
                resolve(stdout.trim());
            }
        });
    });
}

module.exports = scanQrCode;

// Usage example (uncomment to test directly)
// const imagePath = path.resolve(__dirname, '../example-qr-code.png');
// scanQrCode(imagePath)
//     .then(hexData => {
//         console.log('Hex Representation of QR Code Data:', hexData);
//     })
//     .catch(err => {
//         console.error(err);
//     });
