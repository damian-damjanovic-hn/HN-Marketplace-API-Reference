# Acknowledge a Cancellation
**Method:** POST

**Description:** Acknowledge the cancellation of an order.

## Parameters
<!-- Add parameters here -->

## Request Example
```json
{
    "url": "/orders/cancel",
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
        "message": "Order cancellation acknowledged."
    }
}
```
