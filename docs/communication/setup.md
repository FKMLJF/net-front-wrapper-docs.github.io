---
layout: default
title: Communication Setup
nav_order: 2
---

Communication Setup
=

Calling a function
-

In your website, call the functions which you want ot use using the <b>SDK</b> located in [/sdk/nfw-sdk.js](https://github.com/FKMLJF/net-front-wrapper/blob/main/netFrontWrapper/sdk/nfw-sdk.js)

Getting Response from Wrapper
-

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
