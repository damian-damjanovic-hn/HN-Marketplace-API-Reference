# List Carriers
**Method:** GET

**Description:** Retrieve a list of available carriers for order dispatch.

## Parameters
<!-- Add parameters here -->

## Request Example
```http
GET /restapi/v4/order-tracking-carriers/ HTTP/1.1
Host: api.virtualstock.com
Authorization: Basic *****
```

## Response
```json
{
    "status": 200,
    "body": [
    {
        "id": 124,
        "slug": "australia-post",
        "name": "Australia Post"
    },
    {
        "id": 964,
        "slug": "dhl-supply-chain-au",
        "name": "DHL Australia"
    },
    {
        "id": 114,
        "slug": "tnt-au",
        "name": "TNT Australia"
    },
    {
        "id": 184,
        "slug": "fastway-au",
        "name": "Aramex Australia"
    },
]
}
```
