# Create a Product
**Method:** POST

**Description:** Add a new product.

## Parameters
<!-- Add parameters here -->

## Request Example
```json
{
    "url": "/products",
    "headers": {
        "Authorization": "Bearer <token>",
        "Content-Type": "application/json"
    },
    "body": {
        "name": "New Product",
        "price": 19.99,
        "stock": 100
    }
}
```

## Response
```json
{
    "status": 201,
    "body": {
        "product_id": "67890",
        "name": "New Product"
    }
}
```
