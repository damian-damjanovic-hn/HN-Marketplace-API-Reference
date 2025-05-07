# List Products
**Method:** GET

**Description:** Retrieve a list of one or all products.

## Parameters
<!-- Add parameters here -->

## Request Example
```json
{
    "url": "/products",
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
            "product_id": "67890",
            "name": "New Product"
        }
    ]
}
```
