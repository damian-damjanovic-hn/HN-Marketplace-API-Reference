# Update Stock
**Method:** PATCH

**Description:** Update the stock levels for a specific product.

## Parameters
<!-- Add parameters here -->

## Request Example
```json
{
    "url": "/products/{product_id}/stock",
    "headers": {
        "Authorization": "Bearer <token>",
        "Content-Type": "application/json"
    },
    "body": {
        "stock": 150
    }
}
```

## Response
```json
{
    "status": 200,
    "body": {
        "message": "Stock updated successfully."
    }
}
```
