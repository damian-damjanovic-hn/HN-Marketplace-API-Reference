# List Products

**Method:** GET

**Description:** Retrieve a list of one or all products.

## Parameters
<!-- Add parameters here -->
part_number

## Request Example

```http
GET /api/v4/products?part_number=SKU-123456 HTTP/1.1
Host: api.virtualstock.com
```

***Status Code: 200***

## Response

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "url": "https://api.virtualstock.com/api/v4/products/180822488/",
            "part_number": "SKU-123456",
            "category": "https://api.virtualstock.com/api/v4/categories/1055865/",
            "client": "https://api.virtualstock.com/api/v4/clients/245/",
            "supplier": "https://api.virtualstock.com/api/v4/suppliers/7469/",
            "data": {
                "rrp": "1500",
                "image": "https://www.segway.com.au/cdn/shop/files/08.LeftView45.png",
                "model": "E2 Pro",
                "barcode": "8720254406763",
                "image_2": "https://www.segway.com.au/cdn/shop/files/12.RightSide.png?v=1715231738&width=600",
                "image_3": "",
                "image_4": "",
                "image_5": "",
                "image_6": "",
                "image_7": "",
                "image_8": "",
                "image_9": "",
                "gcc_code": "GADGETS & GIFTWARE DROPSHIP|GIFTS BY RECIPIENT|FAMILY GIFTS|01125WRSGIFFAM",
                "image_10": "",
                "description": "Featuring innovative functions, the Segway-Ninebot E2 Pro Electric Scooter delivers optimum performance and safety. Powered by top-tier technology and designed with a durable and portable body, this scooter is the ultimate urban ride.",
                "open_orders": "",
                "other_brand": "Segway",
                "part_number": "SKU-123456",
                "hn_buy_price": "1150",
                "link_youtube": "",
                "tax_class_id": "10% GST",
                "warranty_type": "REPAIR",
                "sap_article_ID": "",
                "stock_updated_at": "2025-05-08T02:26:23",
                "low_inv_threshold": "1",
                "short_description": "Segway-Ninebot E2 Pro Electric Scooter",
                "supplier_comments": "More product info be found on the website https://www.segway.com.au/products/segway-ninebot-electric-kickscooter-e2-pro",
                "def_general_packcontents": "",
                "def_warranty_manufacture": "12",
                "second_line_short_description": ""
            },
            "back_in_stock_date": null
        }
    ]
}
```
