# List Orders
**Method:** <span style="color: green;">GET</span>

**Description:** Retrieve a list of all customer orders.

## Parameters
&nbsp;
limit
&
offset
&nbsp;
## Request Example
```http
GET /restapi/v4/orders/?limit=1&offset=0 HTTP/1.1
Host: api.virtualstock.com
Authorization: Basic *****
```

## Response
```json
{
    "count": 1,
    "next": "https://api.virtualstock.com/restapi/v4/orders/?limit=1&offset=1",
    "previous": null,
    "results": [
        {
            "url": "https://www.the-edge.io/restapi/v4/orders/51929056/",
            "retailer": "https://www.the-edge.io/restapi/v4/customers/245/",
            "order_reference": "31002057508_737_330866",
            "order_date": "2025-05-08T00:48:15",
            "status": "ORDER_ACK",
            "channel": null,
            "purchase_order_reference": null,
            "end_user_purchase_order_reference": "31002057508",
            "additional_order_reference": "31002057508",
            "comment": "P.O. Box 183 \nCoramba NSW 2450\nAustralia",
            "test_flag": false,
            "supplier": "https://www.the-edge.io/restapi/v4/suppliers/6537/",
            "items": [
                {
                    "url": "https://www.the-edge.io/restapi/v4/items/81225920/",
                    "part_number": "EXAMPLE-SKU-1",
                    "retailer_sku_reference": "EXAMPLE-SKU-1",
                    "supplier_sku_reference": "EXAMPLE-SKU-1",
                    "line_reference": "12482135",
                    "quantity": 1,
                    "name": "Foldable Metal Panel Pet Enclosure",
                    "description": "Bonus Delivery*",
                    "status": "ORDER",
                    "unit_cost_price": "30.90",
                    "subtotal": "30.90",
                    "tax": "3.09",
                    "tax_rate": "10.00",
                    "total": "33.99",
                    "promised_date": "2025-05-16T00:50:17",
                    "retailer_additional_reference": null
                }
            ],
            "currency_code": "AUD",
            "subtotal": "30.90",
            "tax": "3.09",
            "total": "33.99",
            "shipping_address": {
                "country": "AU",
                "line_1": "Unit 3-4, 145-151 Arthur Street",
                "line_2": null,
                "city": "Homebush West",
                "postal_code": "2140",
                "state": "New South Wales",
                "phone": "0434196629",
                "full_name": "Damian Damjanovic",
                "email": null
            },
            "retailer_data": {
                "uuid": "79aadaec-73e1-48eb-8344-10dd07b6495c",
                "name": "Harvey Norman",
                "email": "",
                "phone": "",
                "tax_code": "",
                "address": {
                    "line_1": "",
                    "line_2": "",
                    "city": "",
                    "state": "",
                    "country": "AU",
                    "postal_code": ""
                }
            },
            "delivery_service_code": null
        }
    ]
}
```
