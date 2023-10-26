---
layout: default
title: Communication with wrapper
nav_order: 3
---


Available Functions
=

Checking if Bluetooth enabled
-
To retrieve information about the phone's bluetooth state using the wrapper application:

* In your website, call `bluetoothIsEnabled()` function from the [SDK](setup.md#calling-a-function)

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

Getting Available Bluetooth Devices
-
To retrieve a list of available Bluetooth devices using the wrapper application:

* In your website, call `allAvailableBlueToothDevice()` function from the [SDK](setup.md#calling-a-function)

Successful response will look like this:
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

Response if Bluetooth turned off:
```json
{
    "functionName": "ALL_AVAILABLE_BLUETOOTH_DEVICE",
    "result": {
      "message": "NOT_STARTED",
      "executionTime": "5 ms"
    },
    "isSuccess": false
}
```

Getting Connected Printer Info
-
To retrieve information about the connected (paired, not live connect!) printer using the wrapper application:

* In your website, call `getConnectedDevice()` function from the [SDK](setup.md#calling-a-function)

Successful response will look like this:
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

Response if Bluetooth turned off:
```json
{
    "functionName": "GET_CONNECTED_DEVICE_INFO",
    "result": {
      "message": "NOT_STARTED",
      "executionTime": "5 ms"
    },
    "isSuccess": false
}
```

Set selected Printer
-
To select a device which can be used for printing later:

**_NOTE:_** selection will succeed even if stored printer not available

* In your website, call `setPrinter()` function from the [SDK](setup.md#calling-a-function) with a <b>PrinterDto</b> type param:

PrinterDTO:

| name: |  value:  | 
|:------|:--------:|
| label | `string` |
| value | `string` |

Successful response will look like this:
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

Response on selecting error:
```json
{
    "functionName": "SET_PRINTER",
    "result": {
      "stored" : false,
      "message": "NOT_FOUND"
    },
    "isSuccess": false
}
```

Get Printer Settings
-
To get the settings of the connected printer:

* In your website, call `getPrinterSettings()` function from the [SDK](setup.md#calling-a-function)

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

Response without printer selected:
```json
{
    "functionName": "GET_PRINTER_SETTINGS",
    "result": {
      "message": "NOT_FOUND"
    },
    "isSuccess": false
}
```

Set Printer Settings
-
After successfully connected to a device, set it's setting on the printing:

* In your website, call `setPrinterSettings()` function from the [SDK](setup.md#calling-a-function) with a <b>PrintingSettingsDto</b> type param:

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

Response without printer selected:
```json
{
    "functionName": "GET_PRINTER_SETTINGS",
    "result": {
      "stored": false,
      "message": "NOT_FOUND"
    },
    "isSuccess": false
}
```

Print image
-
After successfully connected to a device, to print an image:

* In your website, call `printImage()` function from the [SDK](setup.md#calling-a-function) with a <b>PrintImageDto</b> type param:

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
  "isSuccess": false
}
```
* Is success false because the print status is unknown, it is the operator's responsibility to check it.

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

if, it has error:
```json
{
   "functionName":"PRINT_IMAGE",
   "result":{
      "printingTime":"628 ms",
      "printed":false,
      "message":{
         "printerStatus":4
      }
   },
   "isSuccess":false
}
```
* The printer does not print when the red LED lights up

Scanning QR Code or Barcode
-
To start the scan of QR code or barcode using the wrapper application (Note: only receive response after QR or barcode found):

* In your website, call `barcodeReadingStart()` function from the [SDK](setup.md#calling-a-function)

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
**_NOTE:_** canceling the reading generates no response

Cache clearing
-
To clear the cache of the App's webview:

* In your website, call `webviewClearCache()` function from the [SDK](setup.md#calling-a-function)

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

Hiding header in the App
-
To hide the top header of the app:

* In your website, call `headerHide()` function from the [SDK](setup.md#calling-a-function)

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

Showing header in the App
-
To show the top header of the app:

* In your website, call `headerShow()` function from the [SDK](setup.md#calling-a-function)

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

POLPOS available test (Not recommended, due to extra load)
-
call
```javascript
export function polposTest() {
    const data = {
        command: 'POLPOS_TEST',
    };
    window?.ReactNativeWebView?.postMessage(JSON.stringify(data));
}
```

Response if the printer available:
```json
{
  "functionName": "POLPOS_TEST",
  "result": {
    "printerReady": true,
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

Response if the printer NOT available:
```json
{
  "functionName": "POLPOS_TEST",
  "result": {
    "printerReady": false,
    "message": [
      {
        "code": "-1"
      },
      {
        "code": "-1"
      },
      {
        "code": "-1"
      },
      {
        "code": "-1"
      }
    ]
  },
  "isSuccess": true
}
```
<span style="color:green">If the printer's battery is depleted, malfunctioning, or unavailable for any reason (except in cases of paper shortage or battery charge issues), the request will time out after **10 seconds**. In this scenario, the returned response is the same as in cases of paper shortage or an open lid, but the value of message.code is consistently **-1**. 📗 </span>


POLPOS out of paper
-
call
```javascript
export function polPosOutPaper() {
    const data = {
        command: 'POLPOS_OUT_OF_PAPER',
    };
    window?.ReactNativeWebView?.postMessage(JSON.stringify(data));
}
```

Response if the printer available:
```json
{
  "functionName": "POLPOS_OUT_OF_PAPER",
  "result": {
    "isOk": true,
    "command": "POLPOS_OUT_OF_PAPER"
  },
  "isSuccess": true
}
```
If **isOk** not **true**, then there is something wrong.

POLPOS other error
-

call
```javascript
export function polPosOtherError() {
    const data = {
        command: 'POLPOS_OTHER_ERROR',
    };
    window?.ReactNativeWebView?.postMessage(JSON.stringify(data));
}
```

Response if the printer available:
```json
{
  "functionName": "POLPOS_OTHER_ERROR",
  "result": {
    "isOk": true,
    "command": "POLPOS_OTHER_ERROR"
  },
  "isSuccess": true
}
```
If **isOk** not **true**, then there is something wrong.

POLPOS open cover
-

call
```javascript
export function polPosOpenCover() {
    const data = {
        command: 'POLPOS_OPEN_COVER',
    };
    window?.ReactNativeWebView?.postMessage(JSON.stringify(data));
}
```

Response if the printer available:
```json
{
  "functionName": "POLPOS_OPEN_COVER",
  "result": {
    "isOk": true,
    "command": "POLPOS_OPEN_COVER"
  },
  "isSuccess": true
}
```
If **isOk** not **true**, then there is something wrong.


###### Demo site: [nfw-demo](https://nfw-demo.procats.hu)
###### Build: ![unnamed](https://img.shields.io/badge/4bf756f-Build-red?logo=gnuicecat)

> **DOWNLOAD**
>> [![unnamed](https://img.shields.io/badge/Latest-0.1.59-purple)](https://drive.google.com/file/d/12Q7PwpfIBXH0XuVleceBe-1uUQ2TFIFh/view?usp=sharing)

