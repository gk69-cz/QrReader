const scanQrCode = require('./index');
const path = require('path');

const imagePath = path.resolve(__dirname, '../../example-qr.png'); // Replace with the actual path to your QR code image
scanQrCode(imagePath)
    .then(hexData => {
        console.log('Hex Representation of QR Code Data:', hexData);
    })
    .catch(err => {
        console.error(err);
    });
