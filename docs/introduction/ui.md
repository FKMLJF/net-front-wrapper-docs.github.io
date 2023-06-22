---
layout: default
title: UI Interface
nav_order: 1
---


#  UI Interface (Android application only)  
![Screenshot 2023-06-22 at 14 49 32](https://github.com/FKMLJF/net-front-wrapper-docs.github.io/assets/24462886/c2f9f861-4590-4d7e-9e84-cedd9099715b)

This is an overview of all Android versions support

| api level | name | api level | name |
| ----------- | ----------- | ----------- | ----------- |
| Level 24 | Nougat | Level 30 | Red Velvet Cake |
| Level 25 | Nougat | Level 31 | Snow Cone |
| Level 26 | Oreo | Level 32 | Snow Cone |
| Level 27 | Oreo | Level 33 | Tiramisu |
| Level 28 | Pie | Level 34 | Upside Down Cake |
| Level 29 | Quince Tart |    |    |

##  UI permission requests
![Screenshot_20230622_145335_Permission controller](https://github.com/FKMLJF/net-front-wrapper-docs.github.io/assets/24462886/643fe90a-924d-4ab7-89b8-132fef2925f2)
![Screenshot_20230622_145420_Permission controller](https://github.com/FKMLJF/net-front-wrapper-docs.github.io/assets/24462886/f7f1104b-4869-406d-a871-c9e66664fcd6)
![Screenshot_20230622_145447_Permission controller](https://github.com/FKMLJF/net-front-wrapper-docs.github.io/assets/24462886/85e70855-7630-4d8f-8459-715fdbb29a16)
![Screenshot_20230622_145517_Permission controller](https://github.com/FKMLJF/net-front-wrapper-docs.github.io/assets/24462886/4c6f5b12-ada0-487b-a04d-95a3dcabc5ef)

##  Set Frontend url
![Screenshot_20230622_145405_eVsr](https://github.com/FKMLJF/net-front-wrapper-docs.github.io/assets/24462886/a37741da-f2d9-4700-8483-934d5e07ed8b)
![Screenshot_20230622_145454_eVsr](https://github.com/FKMLJF/net-front-wrapper-docs.github.io/assets/24462886/3c388293-4c77-495e-9634-d0f506845b0c)
> use a secure website, use ssl!

##  SET printer with BL auto scanner
![Screenshot_20230622_145547_eVsr](https://github.com/FKMLJF/net-front-wrapper-docs.github.io/assets/24462886/98b91bfa-c502-4ed3-8df3-03537de06afc)
![Screenshot_20230622_145555_eVsr](https://github.com/FKMLJF/net-front-wrapper-docs.github.io/assets/24462886/abf51ba0-1e26-4dc6-b32f-71b3584b84a5)

## You can set programically (**Recommended**)
```javascript
setPrinter({
  label: "MP80",
  value: "DC:0D:30:95:35:33"
});
// path netFrontWrapper/sdk/nfw-sdk.js
```

Response receive
```javascript
document.addEventListener(‘message', (message) => { 
// console.log(message?.data);
},false);
```

```json
{
  "functionName": "SET_PRINTER",
  "result": {
    "stored": true,
    "message": {
      "value": "MP80",
      "label": "DC:0D:30:95:35:33"
    }
  },
  "isSuccess": true
}
```

## HIDE HEADER feature (**Recommended**)

```javascript
setPrinter(headerHide());
// path netFrontWrapper/sdk/nfw-sdk.js
```
```json
{
  "functionName": "HEADER_SHOW",
  "result": {
    "isHeaderShow": false
  },
  "isSuccess": true
}
```

[![Screenshot 2023-06-22 at 15 54 17](https://github.com/FKMLJF/net-front-wrapper-docs.github.io/assets/24462886/823015d0-1a3f-458b-aefe-e17c6254a62d)](https://github.com/FKMLJF/net-front-wrapper/blob/00cc204d64411d51e577cb007f42bd112b0bf479/netFrontWrapper/sdk/nfw-sdk.js)
