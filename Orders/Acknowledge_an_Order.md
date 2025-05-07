# Acknowledge an Order
**Method:** POST

**Description:** Acknowledge the receipt of a new customer order.

## Parameters
<!-- Add parameters here -->

## Request Example
```http
POST /v4/orders/uri/acknowledge/ HTTP/1.1
Host: api.virtualstock.comrestapi
Content-Length: 498

{
"items":
	[
	{
	"part_number": "EXAMPLE-SKU-1",
	"line_ref": "12332544",
	"quantity": 1,
	"sub_status": "Pending",
	"supplier_dispatch_date": "2024-08-08T12:00:00",
	"supplier_delivery_date":"2024-08-10T12:00:00",
	"comment": "Line acknowledged"
	},
    	{
	"part_number": "EXAMPLE-SKU-2",
	"line_ref": "12332599",
	"quantity": 2,
	"sub_status": "Pending",
	"supplier_dispatch_date": "2024-08-08T12:00:00",
	"supplier_delivery_date":"2024-08-10T12:00:00",
	"comment": "Line acknowledged"
	}
	]
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
