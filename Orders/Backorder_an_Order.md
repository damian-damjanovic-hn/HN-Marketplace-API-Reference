# Backorder an Order
**Method:** POST

**Description:** Mark an order as backordered.

## Parameters
<!-- Add parameters here -->

## Request Example
```json
{
    "url": "/orders/backorder",
    "headers": {
        "Authorization": "Bearer <token>",
        "Content-Type": "application/json"
    },
    "body": {
        "order_id": "12345"
    }
}
```

## Response
```json
{
    "status": 200,
    "body": {
        "message": "Order marked as backordered."
    }
}
```
