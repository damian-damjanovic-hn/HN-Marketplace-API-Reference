# View Order Details
**Method:** GET

**Description:** View detailed information about a specific order.

## Parameters
<!-- Add parameters here -->

## Request Example
```json
{
    "url": "/orders/{order_id}",
    "headers": {
        "Authorization": "Bearer <token>"
    }
}
```

## Response
```json
{
    "status": 200,
    "body": {
        "order_id": "12345",
        "status": "Processing"
    }
}
```
