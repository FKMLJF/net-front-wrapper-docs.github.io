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

<h3>Getting Response from Wrapper</h3>

In your website, listen for messages from the wrapper application using the following code:
```javascript
document.addEventListener('message', (message) => {
    // console.log(message?.data);
    // Handle the received message from the wrapper application
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
To retrieve information about the phone's bluetooth state using the wrapper application, follow these steps:

* In your website, send a postMessage to the wrapper application with the command using the following code:
```javascript
window.ReactNativeWebView.postMessage('BLUETOOTH_ENABLED');
```
