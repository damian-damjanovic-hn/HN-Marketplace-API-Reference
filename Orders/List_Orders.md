# List Orders

**Method:** <span style="color: green;">GET</span>

**Description:** Retrieve a list of all new customer orders one at a time by using `status`, `limit` and `offset` parameters.

## Parameters

- status
- limit
- offset

## Request Example

```http
GET /restapi/v4/orders/?limit=1&offset=1&status=ORDER HTTP/1.1
Host: api.virtualstock.com
Authorization: Basic *****
```

## Response

```json
{
    "count": 168473,
    "next": "https://api.virtualstock.com/restapi/v4/orders/?limit=1&offset=2&status=ORDER",
    "previous": "https://api.virtualstock.com/restapi/v4/orders/?limit=1&status=ORDER",
    "results": [
        {
            "url": "https://www.the-edge.io/restapi/v4/orders/51928973/",
            "retailer": "https://www.the-edge.io/restapi/v4/customers/245/",
            "order_reference": "31002057505_624_330865",
            "order_date": "2025-05-08T00:42:32",
            "status": "ORDER",
            "channel": null,
            "purchase_order_reference": null,
            "end_user_purchase_order_reference": "31002057505",
            "additional_order_reference": "31002057505",
            "comment": "",
            "test_flag": false,
            "supplier": "https://www.the-edge.io/restapi/v4/suppliers/1234/",
            "items": [
                {
                    "url": "https://www.the-edge.io/restapi/v4/items/81225828/",
                    "part_number": "A-OCH-MLD-WH",
                    "retailer_sku_reference": "A-OCH-MLD-WH",
                    "supplier_sku_reference": "A-OCH-MLD-WH",
                    "line_reference": "11996227",
                    "quantity": 1,
                    "name": "Gaming Chair with 8-Point Massage - Black & White",
                    "description": "",
                    "status": "ORDER",
                    "unit_cost_price": "147.79",
                    "subtotal": "147.79",
                    "tax": "14.78",
                    "tax_rate": "10.00",
                    "total": "162.57",
                    "promised_date": "2025-05-21T00:44:14",
                    "retailer_additional_reference": null
                }
            ],
            "currency_code": "AUD",
            "subtotal": "147.79",
            "tax": "14.78",
            "total": "162.57",
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
