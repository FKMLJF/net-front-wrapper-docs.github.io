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

In your website, send a postMessage to the wrapper application with the command using the following code:
```javascript
window.ReactNativeWebView.postMessage('FUNCTION_NAME');
```
other way to call these functions is using the <b>SDK</b> located in [/sdk/nfw-sdk.js](https://github.com/FKMLJF/net-front-wrapper/blob/main/netFrontWrapper/sdk/nfw-sdk.js)

<h3>Getting Response from Wrapper</h3>

In your website, listen for messages from the wrapper application using the following code:
```javascript
document.addEventListener('message', (message) => {
    //console.log(message?.data);
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
For error response this DTO format:
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
To retrieve information about the phone's bluetooth state using the wrapper application, follow one of these:

* In your website, call <b>bluetoothIsEnabled</b> function from the [SDK](#communication-setup)
* or send a postMessage to the wrapper application with the command using the following code:
```javascript
window.ReactNativeWebView.postMessage('BLUETOOTH_ENABLED');
```
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
To retrieve a list of available Bluetooth devices using the wrapper application, follow one of these:

* In your website, call <b>allAvailableBlueToothDevice</b> function from the [SDK](#communication-setup)
* or send a postMessage to the wrapper application with the command using the following code:
```javascript
window.ReactNativeWebView.postMessage('ALL_AVAILABLE_BLUETOOTH_DEVICE');
```
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
To retrieve information about the connected (paired, not live connect!) printer using the wrapper application, follow one of these:

* In your website, call <b>getConnectedDevice</b> function from the [SDK](#communication-setup)
* or send a postMessage to the wrapper application with the command using the following code:
```javascript
window.ReactNativeWebView.postMessage('GET_CONNECTED_DEVICE_INFO');
```
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
