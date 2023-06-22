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
In your website, listen for messages from the wrapper application using the following code:

Getting Response from Wrapper
-
For any call the wrapper will send success response in this DTO format:
```json
{
    functionName: ”FUNCTION_NAME”,
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
