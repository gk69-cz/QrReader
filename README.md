# QR Code Reader

This project includes a Python script and a Node.js application to read QR code data.

## Structure

- `python/`: Contains the Python script to scan QR codes.
- `nodejs/`: Contains the Node.js application to interface with the Python script.
- `example-qr.png`: An example QR code image for testing.

## Setup

### Python

1. Navigate to the `python/` directory:

    ```bash
    cd python
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Python script to scan a QR code:

    ```bash
    python scan_qr.py ../example-qr-code.png
    ```

### Node.js

1. Navigate to the `nodejs/` directory:

    ```bash
    cd nodejs
    ```

2. Install the required dependencies:

    ```bash
    npm install
    ```

3. Run the Node.js application to scan a QR code:

    ```bash
    npm run scan-qr
    ```

Ensure that the paths to the Python script and the example QR code image are correct.
