# List Carriers
**Method:** GET

**Description:** Retrieve a list of available carriers for order dispatch.

## Parameters
<!-- Add parameters here -->

## Request Example
```json
{
    "url": "/carriers",
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
            "carrier_id": "1",
            "name": "Carrier One"
        }
    ]
}
```
