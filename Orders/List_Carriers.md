# List Carriers
**Method:** GET

**Description:** Retrieve a list of available carriers for order dispatch.

## Request Example
```http
GET /restapi/v4/order-tracking-carriers/ HTTP/1.1
Host: api.virtualstock.com
Authorization: Basic *****
```

## Response
```json
[
    {
        "id": 124,
        "slug": "australia-post",
        "name": "Australia Post"
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
    }
]
```
