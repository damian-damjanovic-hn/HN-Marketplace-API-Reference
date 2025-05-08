## Scenario

As a Harvey Norman Vendor Manager, I want to create new products across 1000 Marketplace Vendors (suppliers) seamlessly, which I can range online.

Here is a workflow example for 1 product “`SKU123`” using supplier “`test-prod-restapi-supplier`”:

### List suppliers

```http
GET /api/v4/suppliers/?limit=1000 HTTP/1.1
Host: api.virtualstock.com
Authorization: Basic =
```

* * *

### Choose supplier

```json
        {
            "url": "https://api.virtualstock.com/api/v4/suppliers/7606/",
            "name": "test-prod-restapi-supplier",
            "uuid": "9442a2e1-6ed1-405c-b8b8-190f13b4cc70",
            "postcode": "RG1 3AR",
            "country": "GB",
            "categories": [],
            "account_id": "24680"
        },
```

* * *

## Create new product

```http
POST /api/v4/products/ HTTP/1.1
Host: api.virtualstock.com
Content-Length: 1200

{
    "part_number": "SKU123",
    "category": "https://api.virtualstock.com/api/v4/categories/1055865/",
    "client": "https://api.virtualstock.com/api/v4/clients/245/",
    "supplier": "https://api.virtualstock.com/api/v4/suppliers/7606/",
    "data": {
        "rrp": "800.00",
        "hn_buy_price": "500.00",
        "tax_class_id": "10% GST",
        "model": "",
        "barcode": "",
        "short_description": "Lenovo IdeaPad 3 14ADA05 14 Inch FHD Laptop - Silver",
        "description": "product copy and specs",
        "other_brand": "Lenovo",
        "warranty_type": "REPAIR",
        "low_inv_threshold": "1",
        "supplier_comments": "",
        "def_warranty_manufacture": "12",
        "supplier_free_stock": 200,
        "link_youtube": "",
        "image": "https://www.gstatic.com/webp/gallery3/1.png",
        "image_2": "https://www.gstatic.com/webp/gallery3/3.png",
        "image_3": "",
        "image_4": "",
        "image_5": "",
        "image_6": "",
        "image_7": "",
        "image_8": "",
        "image_9": "",
        "gcc_code": "GADGETS & GIFTWARE DROPSHIP|GIFTS BY RECIPIENT|FAMILY GIFTS|01125WRSGIFFAM"
    }
    }
```

### Response 201 created

```json
{
    "url": "https://api.virtualstock.com/api/v4/products/171335048/",
    "part_number": "SKU123",
    "category": "https://api.virtualstock.com/api/v4/categories/1055865/",
    "client": "https://api.virtualstock.com/api/v4/clients/245/",
    "supplier": "https://api.virtualstock.com/api/v4/suppliers/7606/",
    "data": {
        "rrp": "800.00",
        "image": "https://www.gstatic.com/webp/gallery3/1.png",
        "model": "",
        "barcode": "",
        "image_2": "https://www.gstatic.com/webp/gallery3/3.png",
        "image_3": "",
        "image_4": "",
        "image_5": "",
        "image_6": "",
        "image_7": "",
        "image_8": "",
        "image_9": "",
        "gcc_code": "GADGETS & GIFTWARE DROPSHIP|GIFTS BY RECIPIENT|FAMILY GIFTS|01125WRSGIFFAM",
        "image_10": "",
        "description": "product copy and specs",
        "other_brand": "Lenovo",
        "part_number": "SKU123",
        "hn_buy_price": "500.00",
        "link_youtube": "",
        "tax_class_id": "10% GST",
        "warranty_type": "REPAIR",
        "sap_article_ID": "",
        "stock_updated_at": "2025-02-04T08:34:46",
        "low_inv_threshold": "1",
        "short_description": "Lenovo IdeaPad 3 14ADA05 14 Inch FHD Laptop - Silver",
        "supplier_comments": "",
        "def_general_packcontents": "",
        "def_warranty_manufacture": "12",
        "second_line_short_description": ""
    },
    "back_in_stock_date": null
}

```

![5ee746b46967fe0184e206c18ad40e56.png](:/13f5267043bf47f6b4c9ab71673df77b)

&nbsp;

* * *

## Using the SKU (`part_number`) get product *REST ID*

```http
GET /api/v4/products/?part_number=SKU123 HTTP/1.1
Host: api.virtualstock.com
Authorization: Basic =
```

### Response

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "url": "https://api.virtualstock.com/api/v4/products/171335048/",
            "part_number": "SKU123",
            "category": "https://api.virtualstock.com/api/v4/categories/1055865/",
            "client": "https://api.virtualstock.com/api/v4/clients/245/",
            "supplier": "https://api.virtualstock.com/api/v4/suppliers/7606/",
            "data": {
                "rrp": "800.00",
                "image": "https://www.gstatic.com/webp/gallery3/1.png",
                "model": "",
                "barcode": "",
                "image_2": "https://www.gstatic.com/webp/gallery3/3.png",
                "image_3": "",
                "image_4": "",
                "image_5": "",
                "image_6": "",
                "image_7": "",
                "image_8": "",
                "image_9": "",
                "gcc_code": "GADGETS & GIFTWARE DROPSHIP|GIFTS BY RECIPIENT|FAMILY GIFTS|01125WRSGIFFAM",
                "image_10": "",
                "description": "product copy and specs",
                "other_brand": "Lenovo",
                "part_number": "SKU123",
                "hn_buy_price": "500.00",
                "link_youtube": "",
                "tax_class_id": "10% GST",
                "warranty_type": "REPAIR",
                "sap_article_ID": "",
                "stock_updated_at": "2025-02-04T08:34:46",
                "low_inv_threshold": "1",
                "short_description": "Lenovo IdeaPad 3 14ADA05 14 Inch FHD Laptop - Silver",
                "supplier_comments": "",
                "def_general_packcontents": "",
                "def_warranty_manufacture": "12",
                "second_line_short_description": ""
            },
            "back_in_stock_date": null
        }
    ]
}
```

&nbsp;

* * *

## Send SAP ID

```http
PATCH /api/v4/products/171335048/ HTTP/1.1
Host: api.virtualstock.com
Content-Length: 63

{
    "data": {
         "sap_article_ID": 12861916
    }
}
```

### Response

```json
{
    "url": "https://api.virtualstock.com/api/v4/products/171335048/",
    "part_number": "SKU123",
    "category": "https://api.virtualstock.com/api/v4/categories/1055865/",
    "client": "https://api.virtualstock.com/api/v4/clients/245/",
    "supplier": "https://api.virtualstock.com/api/v4/suppliers/7606/",
    "data": {
        "rrp": "800.00",
        "image": "https://www.gstatic.com/webp/gallery3/1.png",
        "model": "",
        "barcode": "",
        "image_2": "https://www.gstatic.com/webp/gallery3/3.png",
        "image_3": "",
        "image_4": "",
        "image_5": "",
        "image_6": "",
        "image_7": "",
        "image_8": "",
        "image_9": "",
        "gcc_code": "GADGETS & GIFTWARE DROPSHIP|GIFTS BY RECIPIENT|FAMILY GIFTS|01125WRSGIFFAM",
        "image_10": "",
        "description": "product copy and specs",
        "other_brand": "Lenovo",
        "part_number": "SKU123",
        "hn_buy_price": "500.00",
        "link_youtube": "",
        "tax_class_id": "10% GST",
        "warranty_type": "REPAIR",
        "sap_article_ID": "12861916",
        "stock_updated_at": "2025-02-04T08:34:46",
        "low_inv_threshold": "1",
        "short_description": "Lenovo IdeaPad 3 14ADA05 14 Inch FHD Laptop - Silver",
        "supplier_comments": "",
        "def_general_packcontents": "",
        "def_warranty_manufacture": "12",
        "second_line_short_description": ""
    },
    "back_in_stock_date": null
}
```

* * *

&nbsp;

### SAP ID is now in VS

![ca39a68059746b51b49b0fb7df82549f.png](:/48bee718b4dc4f24b8a8247d4fcd1e45)

* * *

## Select product with SAP ID and Publish

![b3e52ed5289b0a11a914e6ea4ceb3b79.png](:/af1c797929834426a4814e2f43c1f088)

![9b90873024a83f09d8b3477352aa3364.png](:/d819eb3a2dd74deab9c05101807a4d96)

&nbsp;

### In the SFTP

![89c651b7c62c585ea4caad170a0c12a3.png](:/fcb88a437d8e4e58897c2a7c4d7bb75e)

files

![b8c9a8fdb5a0b0f2e9fea67bbcaf1ee9.png](:/e0c9c313be0d469c96164808a587e0fe)

CSV content: STOCK 200

![ae8c8a22401514296eee0c8ba9325858.png](:/0a63191401cf483dbdc8ea129a8a0a01)

&nbsp;
