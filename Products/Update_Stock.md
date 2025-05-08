# Update Stock

**Method:** PATCH

**Description:** Update stock quantity for a specific product.

## Request Example

```http
PATCH /api/v4/products/55423544/ HTTP/1.1
Host: api.virtualstock.com
Content-Length: 106
```

### Body

```json
{
    "data": {
        "sap_article_ID": 11881027,
        "supplier_free_stock": 52
    }
}
```

## Response

```json
{
    "url": "https://api.virtualstock.com/api/v4/products/55423544/",
    "part_number": "PID-00003-00",
    "category": "https://api.virtualstock.com/api/v4/categories/1055865/",
    "client": "https://api.virtualstock.com/api/v4/clients/245/",
    "supplier": "https://api.virtualstock.com/api/v4/suppliers/5216/",
    "data": {
        "rrp": "649.95",
        "image": "https://clickdepotptyltd.sharepoint.com/:f:/s/ClickDepot/EqIMeB-G6upJrp4KNhtoCh8BvGWgPD4tfYkbjZalRoPnBQ?e=8fgXaF",
        "model": "Adventurer 3",
        "barcode": "",
        "image_2": "",
        "image_3": "",
        "image_4": "",
        "image_5": "",
        "image_6": "",
        "image_7": "",
        "image_8": "",
        "image_9": "",
        "gcc_code": "PRINTING & IMAGING|PRINTERS|SPECIALITY PRINTERS|01062IMAPRNSPE",
        "image_10": "",
        "catalog_id": "",
        "description": "The best choice for your first 3D Printer!\r\nFeatures Include:\r\n• Minimalist design with closed printing chamber – no assembly required!\r\n• Detachable nozzle with buckle design for easy maintenance,\r\n• Removable flexible platform with heating capabilities to 100°C,\r\n• 150x150x150mm print volume,\r\n• Filament detector with automatic loading & unloading,\r\n• Auto-Levelling,\r\n• Supports ABS filament,\r\n• Touch screen operation with 2.8-inch colour screen,\r\n• Supports data transmission via USB, Wi-Fi, ethernet, FlashCloud and PolarCloud,\r\n• 45db ultra-mute printing,\r\n• Built-in camera for monitoring printing progress remotely,\r\n• Filament detection function suspends activity automatically when filament is broken or used up.\r\nSpecifications:\r\n• Extruder Number: 1\r\n• Extruder Diameter: 0.4mm\r\n• Max Set Temp. of Extruder: 240°C\r\n• Max Set Temp. of Platform: 100°C\r\n• Working Environment: 18-30°C\r\n• Print Speed: 10-100mm/s\r\n• Supported Filament: PLA/ABS\r\n• Print Volume: 150x150x150mm\r\n• Layer Resolution: 0.1-0.4mm\r\n• Print Resolution: ±0.2mm\r\n• Input: 100-240VAC, 47-63Hz\r\n• Output: 24V, 6.25A\r\n• Power: 150W\r\n• Spool Hold Diameter: 52mm\r\n• Contain Spool Diameter: 50x52x200mm\r\n• Internal Storage: 8GB\r\n• Software: FlashPrint\r\n• File Output: .gx/.g files\r\n• File Input: .3mf/.stl/.obj/.fpp/.bmp/.png/.jpeg\r\nBox Contents:\r\n• 1x 3D Printer\r\n• 1x Power Cable\r\n• 1x Screwdriver\r\n• 1x Unclogging Pin Tool\r\n• 1x Allen Wrench Key\r\n• 1x Grease\r\n• 1x 250g Spool of Filament\r\n• Quick Start Guide & After-Sales Service Card\r\nCompliance Specifications:\r\n• Do NOT open machine compartments if it is plugged in or switched on.\r\n• Do NOT leave machine unattended while operating.\r\n• Avoid touching the heated print bed and hot-end when operating.\r\n• Adult supervision recommended for users under 18 years when assembling and operating.",
        "other_brand": "",
        "part_number": "PID-00003-00",
        "reorder_qty": "1",
        "contact_name": "Rodney Scheffer",
        "hn_buy_price": "495",
        "last_updated": "Published at: 24/04/2025 14:37",
        "link_youtube": "",
        "publish_date": "Wed Aug  7 00:03:27 2024",
        "tax_class_id": "10% GST",
        "contact_email": "rodney@3dprintersonline.com.au",
        "warranty_type": "REPAIR",
        "contact_number": "(02) 8488 6213",
        "publish_images": "off",
        "sap_article_ID": "11881027",
        "enrolment_status": "Active",
        "stock_updated_at": "2025-05-08T01:41:30",
        "low_inv_threshold": "1",
        "short_description": "FlashForge Adventurer 3 V2 3D Printer",
        "supplier_comments": "",
        "package1_description": "",
        "package2_description": "",
        "package3_description": "",
        "package4_description": "",
        "package5_description": "",
        "package6_description": "",
        "package7_description": "",
        "package8_description": "",
        "package9_description": "",
        "package_gross_weight": "12.5",
        "package10_description": "",
        "package11_description": "",
        "package12_description": "",
        "country_of_manufacture": "China",
        "dropship_team_comments": "",
        "def_dimension_packdepth": "43",
        "def_dimension_packwidth": "48",
        "def_dimension_proddepth": "33",
        "def_dimension_prodwidth": "38",
        "def_dimension_packheight": "53",
        "def_dimension_prodheight": "40",
        "def_general_packcontents": "",
        "def_warranty_manufacture": "12",
        "second_line_short_description": ""
    },
    "back_in_stock_date": null
}
```
