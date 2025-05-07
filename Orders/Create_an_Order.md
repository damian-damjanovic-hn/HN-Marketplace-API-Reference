# Create an Order
**Method:** <span style="color: yellow;">POST</span>

**Description:** Create a new order.

## <span style="color: orange;">Request Example</span>
```http
POST /restapi/v4/orders/ HTTP/1.1
Host: api.virtualstock.com
Content-Length: 1222
```
### Body
```json
{
    "supplier":"https://api.virtualstock.com/restapi/v4/suppliers/7534/",
    "order_reference":"31000200410_995_986450",
    "additional_order_reference":"31000000000",
    "end_user_purchase_order_reference":"31000000000",
    "order_date":"2024-10-30T18:56:09",
    "test_flag": true,
    "currency_code":"AUD",
    "comment":"Test Order - HN - Damian",
    "items":[
        {
            "supplier_sku_reference": "EXAMPLE-SKU-1",
            "retailer_sku_reference": "EXAMPLE-SKU-1",
            "retailer_additional_reference": null,
            "line_reference": "12946636",
            "name": "Oak Electric Standing Desk - 150cm",
            "description": "Spot check line item",
            "quantity": 1,
            "unit_cost_price": "150.00",
            "subtotal": "150.00",
            "tax_rate": "10.00",
            "tax": "15.00",
            "total": "165.00",
            "promised_date": "2024-11-20T00:00:00"
        }
    ],
    "shipping_address":{
       "full_name":"Lucy Simonis V",
       "line_1":"Unit 3-4, 145-151 Arthur Street",
       "city":"Homebush West",
       "state":"New South Wales",
       "postal_code":"2140",
       "phone":"0434196629",
       "country":"AU"
    }
}
```

### <span style="color: purple;">Body</span>
```json
{
    "items": [
        {
            "part_number": "EXAMPLE-SKU-1",
            "line_ref": "12332544",
            "quantity": 1,
            "sub_status": "Pending",
            "supplier_dispatch_date": "2024-08-08T12:00:00",
            "supplier_delivery_date": "2024-08-10T12:00:00",
            "comment": "Line item set to backorder"
        },
        {
            "part_number": "EXAMPLE-SKU-2",
            "line_ref": "12332599",
            "quantity": 2,
            "sub_status": "Pending",
            "supplier_dispatch_date": "2024-08-08T12:00:00",
            "supplier_delivery_date": "2024-08-10T12:00:00",
            "comment": "Line item set to backorder"
        }
    ]
}
```

#### Response
```json
{
    "status": 200,
}
```
