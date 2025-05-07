# List Orders
**Method:** GET

**Description:** Retrieve a list of all customer orders.

## Parameters
<!-- Add parameters here -->

## Request Example
```json
{
    "url": "/orders",
    "headers": {
        "Authorization": "Bearer <token>"
    }
}
```

## Response
```json
{
    "status": 200,
    "body": [
        {
            "order_id": "12345",
            "status": "Processing"
        }
    ]
}
```
