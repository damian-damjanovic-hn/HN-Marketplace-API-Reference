# Acknowledge an Order
**Method:** POST

**Description:** Acknowledge the receipt of a new customer order.

## Parameters
<!-- Add parameters here -->

## Request Example
```json
{
    "url": "/orders/acknowledge",
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
        "message": "Order acknowledged successfully."
    }
}
```
