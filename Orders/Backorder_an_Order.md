# Backorder an Order
**Method:** <span style="color: yellow;">POST</span>

**Description:** Mark an order as backordered.

## <span style="color: purple;">Request Example</span>
```http
```http
POST /restapi/v4/orders/<span style="color: red">{{ORDER_URI}}</span>/backorder/ HTTP/1.1
Host: api.virtualstock.com
Content-Length: 663
```

### <span style="color: purple;">Body</span>
```JSON
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
```JSON
```json
{
    "status": 200,
    "body": {
        "message": "Your order is successfully saved"
    }
}
```
