---
layout: default
title: Index
nav_exclude: true
---


# Read The Docs Net-Front Wrapper
![unnamed](https://github.com/FKMLJF/net-front-wrapper-docs.github.io/assets/24462886/c4a09f97-4fe9-447e-befc-044c2d17c587)

![unnamed](https://img.shields.io/badge/Version-0.0.0.2-red)
![unnamed](https://img.shields.io/badge/0.71-React%20Native-69b6e4?logo=react)
![unnamed](https://img.shields.io/badge/7.6-Gradle-21d326?logo=gradle)
![unnamed](https://img.shields.io/badge/4.8.4-typescript-blue?logo=typescript)
## Features
![Screenshot 2023-06-22 at 17 06 53](https://github.com/FKMLJF/net-front-wrapper-docs.github.io/assets/24462886/cee8c00d-c7fe-4e0d-9f9f-725ed2616137)

- Set specify frontend url
- Barcode reading with OCR (aztec, code128, code39, code39mod43, code93, ean13, ean8, pdf417, qr, upce, interleaved2of5 (when available), itf14 (when available), datamatrix (when available))
- PostMessage, OnMessage communication interface
- Set Printer, and printer settings
- Bluetooth manager (limited to android 12+)
- Datecs 350 custom SDK for image printing
- Polpos custom SDK for image printing and get status observable

## Installation
#### (read prerequires site)
Install the dependencies and devDependencies and start.

```sh
git clone https://github.com/FKMLJF/net-front-wrapper.git
cd netFrontWrapper
npm install
npm run build:android
npm run start:android
```

## Plugins

netFrontWrapper is currently extended with the following plugins.
Instructions on how to use them in your own application are linked below.

<div class="table-wrapper" markdown="block">

|PLUGIN | DOCS | SOURCE | 
|:---:|:---: |:---:   |
| DATECS  | [DATECS](https://www.datecs.bg/en/documents)   | netFrontWrapper/android/app/lib/com.datecs.api.jar     | 
| POLPOS  | [POLPOS](http://altcashoffice.hu/letoltes/POLPOS_MP80_SDK/)   | netFrontWrapper/android/app/lib/printer_polpos_library.jar     | 
| PdfiumAndroid  | [PdfiumAndroid](https://github.com/barteksc/PdfiumAndroid/blob/master/README.md)   | [PdfiumAndroid](https://github.com/barteksc/PdfiumAndroid/tree/master)     | 
| zxing  | [zxing](https://github.com/zxing/zxing#readme)   | [zxing](https://github.com/zxing/zxing)      | 

</div>

## Tranformation for better process
<div class="table-wrapper" markdown="block">
  
|PLUGIN | DOCS  | 
|:---:| :---:  |
| DATECS  | ../main/java/com/netfrontwrapper/DatecsDPP350SDKModule.java    |
| POLPOS  | [tp-react-native-bluetooth-printer-for-polpos-mp80](https://github.com/FKMLJF/tp-react-native-bluetooth-printer-for-polpos-mp80.git)    |

</div>

Support and Contact Information ![shape4](https://github.com/FKMLJF/net-front-wrapper-docs.github.io/assets/24462886/e214579c-90c7-4f1e-92de-1a1b70ce18bc)

For any inquiries or technical support, please contact:


Website: **https://procats.hu**

Email: **hello@procats.hu**

![unnamed](https://img.shields.io/badge/Version-0.0.0.2-red)
![unnamed](https://img.shields.io/badge/0.71-React%20Native-69b6e4?logo=react)
![unnamed](https://img.shields.io/badge/7.6-Gradle-21d326?logo=gradle)
![unnamed](https://img.shields.io/badge/4.8.4-typescript-blue?logo=typescript)

