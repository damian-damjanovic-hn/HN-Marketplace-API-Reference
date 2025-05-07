# Dispatch an Order
**Method:** POST

**Description:** Dispatch an order to the customer.

## Parameters
<!-- Add parameters here -->

## Request Example
```json
{
    "url": "/orders/dispatch",
    "headers": {
        "Authorization": "Bearer <token>",
        "Content-Type": "application/json"
    },
    "body": {
        "order_id": "12345",
        "carrier_id": "1"
    }
}
```

## Response
```json
{
    "status": 200,
    "body": {
        "message": "Order dispatched successfully."
    }
}
```
