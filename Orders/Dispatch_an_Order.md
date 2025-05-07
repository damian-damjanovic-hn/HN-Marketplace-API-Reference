# Dispatch an Order
**Method:** <span style="color: yellow;">POST</span>

**Description:** Dispatch an order to the customer.

## Request Example
```json
{
    "items": [
        {
            "part_number": "SKU123",
            "line_ref": "11996227",
            "quantity": 1,
            "supplier_dispatch_date": "2024-08-10",
            "supplier_delivery_date": "2024-08-12",
            "tracking_number": "abc-12345",
            "carrier": "fastway-au"
        }
    ]
}
```

## Response
```json
{
    "status_code": 200
}
```
