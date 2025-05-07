# Acknowledge a Cancellation
**Method:** POST

**Description:** Acknowledge the cancellation of an order.

## Request Example
```http
POST /restapi/v4/orders/<<ORDER_URI>>/cancel_acknowledge/ HTTP/1.1
Host: api.virtualstock.com
Content-Type: application/json
Authorization: Basic ***
Content-Length: 132
```

### Body (JSON)
```json
{
	"items":
	[
		{
			"part_number": "EXAMPLE-SKU-3",
			"line_ref": "12332599",
			"quantity": 1,
			"comment": "I accept"
		}
	]
}
```

### Response
```json
{
    "status": 200
}
```
