---
layout: default
title: Communication with wrapper
nav_order: 1
---

Net-Front Wrapper App Communication Documentation
=

Introduction
-
This part of the documentation explains how to establish communication between the website and the wrapper using a postMessage bridge.

Communication Setup
-

<h3>Calling a function</h3>


In your website, call the functions which you want ot use using the <b>SDK</b> located in [/sdk/nfw-sdk.js](https://github.com/FKMLJF/net-front-wrapper/blob/main/netFrontWrapper/sdk/nfw-sdk.js)

<h3>Getting Response from Wrapper</h3>

In your website, listen for messages from the wrapper application using the following code:
```javascript
document.addEventListener('message', (message) => {
    //console.log(JSON.stringify(message?.data));
    //Handle the received message from the wrapper application
}, false);
```

For any call the wrapper will send success response in this DTO format:
```json
{
    functionName: 'FUNCTION_NAME',
    result: 
        {
          Object differs according to the given function
        },
    isSuccess: true;
}
```
For error response is this DTO format:
```json
{
    functionName: ”FUNCTION_NAME”,
    result: 
        {
          Object differs according to the given function
        },
    isSuccess: false,
}
```

Available Functions
-

<h3>Checking if Bluetooth enabled</h3>
To retrieve information about the phone's bluetooth state using the wrapper application:

* In your website, call `bluetoothIsEnabled()` function from the [SDK](#communication-setup)

Response will look like this:
```json
{
    "functionName": "BLUETOOTH_ENABLED",
    "result":
        {
            "bluetooth":false
        },
    "isSuccess": true
}
```

<h3>Getting Available Bluetooth Devices</h3>
To retrieve a list of available Bluetooth devices using the wrapper application:

* In your website, call `allAvailableBlueToothDevice()` function from the [SDK](#communication-setup)

Response will look like this:
```json
{
    "functionName": "ALL_AVAILABLE_BLUETOOTH_DEVICE",
    "result": {
      "devices": {
        "paired": [
          {
            "name": "MP80",
            "address": "DC:0D:30:95:35:33"
          },
          {
            "name": "DPP-350",
            "address": "68:AA:D2:0F:B1:BA"
          }
        ],
        "found": [
          {
            "name": "BMW 47775",
            "address": "9C:DF:03:41:91:63"
          },
          {
            "address": "57:19:BB:98:09:2B"
          }
        ]
      },
      "executionTime": "12836 ms"
    },
    "isSuccess": true
}
```

<h3>Getting Connected Printer Info</h3>
To retrieve information about the connected (paired, not live connect!) printer using the wrapper application:

* In your website, call `getConnectedDevice()` function from the [SDK](#communication-setup)

Response will look like this:
```json
{
    "functionName": "GET_CONNECTED_DEVICE_INFO",
    "result": {
      "label": "MP80",
      "value": "DC:0D:30:95:35:33"
    },
    "isSuccess": true
}
```

<h3>Connect to a Printer</h3>
To make a connection with a device which can be used for printing later:

* In your website, call `setPrinter()` function from the [SDK](#communication-setup) with a <b>PrinterDto</b> type param:
  
PrinterDTO:

| name: |  value:  | 
|:------|:--------:|
| label | `string` |
| value | `string` |

Response will look like this:
```json
{
    "functionName": "SET_PRINTER",
    "result": {
      "stored" :true,
      "message": {
        "value": "MP80",
        "label": "DC:0D:30:95:35:33"
      }
    },
    "isSuccess": true
}
```

<h3>Get Printer Settings</h3>
To get the settings of the connected printer:

* In your website, call `getPrinterSettings()` function from the [SDK](#communication-setup)

Response will look like this:
```json
{
    "functionName": "GET_PRINTER_SETTINGS",
    "result": {
      "width": "576",
      "leftPadding": "0"
    },
    "isSuccess": true
}
```

<h3>Set Printer Settings</h3>
After successfully connected to a device, set it's setting on the printing:

* In your website, call `setPrinterSettings()` function from the [SDK](#communication-setup) with a <b>PrintingSettingsDto</b> type param:

PrintingSettingsDto:

| name:       |  value:  |
|:------------|:--------:|
| width       | `string` |
| leftPadding | `string` |

Response will look like this:
```json
{
    "functionName": "SET_PRINTER_SETTINGS",
    "result": {
      "width": "576",
      "leftPadding": "0"
    },
    "isSuccess": true
}
```

<h3>Print image</h3>
After successfully connected to a device, to print an image:

* In your website, call `printImage()` function from the [SDK](#communication-setup) with a <b>PrintImageDto</b> type param:

PrintImageDto:

| name:       |  value:  | required |
|:------------|:--------:|:--------:|
| base64PDF   | `string` |  `true`  |
| imageWidth  | `number` | `false`  |
| leftPadding | `number` | `false`  |

Response will look like this **POLPOS PRINTER**:
```json
{
  "functionName": "PRINT_IMAGE",
  "result": {
    "printingTime": "UNKNOWN",
    "printingStart": true,
    "message": [
      {
        "code": "12"
      },
      {
        "code": "12"
      },
      {
        "code": "12"
      },
      {
        "code": "12"
      }
    ]
  },
  "isSuccess": true
}
```

Response will look like this **DATECS PRINTER**:
```json
{
  "functionName": "PRINT_IMAGE",
  "result": {
    "printingTime": "19287 ms",
    "printed": true,
    "message": ""
  },
  "isSuccess": true
}
```

<h3>Scanning QR Code or Barcode</h3>
To start the scan of QR code or barcode using the wrapper application (Note: only receive response after QR or barcode found):

* In your website, call `barcodeReadingStart()` function from the [SDK](#communication-setup)

On successfully reading response will look like this:
```json
{
    "functionName": "BARCODE_READING_START",
    "result": {
      "data": "barcodeDataInString"
    },
    "isSuccess": true
}
```

<h3>Cache clearing</h3>
To clear the cache of the App's webview:

* In your website, call `webviewClearCache()` function from the [SDK](#communication-setup)

Response will look like this:
```json
{
    "functionName": "WEBVIEW_CLEAR_CACHE",
    "result": {
      "message": "cache and history cleared!"
    },
    "isSuccess": true
}
```

<h3>Hiding header in the App</h3>
To hide the top header of the app:

* In your website, call `headerHide()` function from the [SDK](#communication-setup)

Response will look like this:
```json
{
    "functionName": "HEADER_HIDE",
    "result": {
      "isHeaderShow": false
    },
    "isSuccess": true
}
```

<h3>Hiding header in the App</h3>
To hide the top header of the app:

* In your website, call `headerShow()` function from the [SDK](#communication-setup)

Response will look like this:
```json
{
    "functionName": "HEADER_SHOW",
    "result": {
      "isHeaderShow": true
    },
    "isSuccess": true
}
```
