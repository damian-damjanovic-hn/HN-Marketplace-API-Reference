import os
import json

# Define the API documentation structure
api_docs = {
    "Orders": [
        {
            "method": "GET",
            "endpoint": "List Orders",
            "description": "Retrieve a list of all customer orders.",
            "request": {
                "url": "/orders",
                "headers": {"Authorization": "Bearer <token>"}
            },
            "response": {
                "status": 200,
                "body": [{"order_id": "12345", "status": "Processing"}]
            }
        },
        {
            "method": "POST",
            "endpoint": "Acknowledge an Order",
            "description": "Acknowledge the receipt of a new customer order.",
            "request": {
                "url": "/orders/acknowledge",
                "headers": {
                    "Authorization": "Bearer <token>",
                    "Content-Type": "application/json"
                },
                "body": {"order_id": "12345"}
            },
            "response": {
                "status": 200,
                "body": {"message": "Order acknowledged successfully."}
            }
        },
        {
            "method": "GET",
            "endpoint": "View Order Details",
            "description": "View detailed information about a specific order.",
            "request": {
                "url": "/orders/{order_id}",
                "headers": {"Authorization": "Bearer <token>"}
            },
            "response": {
                "status": 200,
                "body": {"order_id": "12345", "status": "Processing"}
            }
        },
        {
            "method": "POST",
            "endpoint": "Backorder an Order",
            "description": "Mark an order as backordered.",
            "request": {
                "url": "/orders/backorder",
                "headers": {
                    "Authorization": "Bearer <token>",
                    "Content-Type": "application/json"
                },
                "body": {"order_id": "12345"}
            },
            "response": {
                "status": 200,
                "body": {"message": "Order marked as backordered."}
            }
        },
        {
            "method": "GET",
            "endpoint": "List Carriers",
            "description": "Retrieve a list of available carriers for order dispatch.",
            "request": {
                "url": "/carriers",
                "headers": {"Authorization": "Bearer <token>"}
            },
            "response": {
                "status": 200,
                "body": [{"carrier_id": "1", "name": "Carrier One"}]
            }
        },
        {
            "method": "POST",
            "endpoint": "Dispatch an Order",
            "description": "Dispatch an order to the customer.",
            "request": {
                "url": "/orders/dispatch",
                "headers": {
                    "Authorization": "Bearer <token>",
                    "Content-Type": "application/json"
                },
                "body": {"order_id": "12345", "carrier_id": "1"}
            },
            "response": {
                "status": 200,
                "body": {"message": "Order dispatched successfully."}
            }
        },
        {
            "method": "POST",
            "endpoint": "Acknowledge a Cancellation",
            "description": "Acknowledge the cancellation of an order.",
            "request": {
                "url": "/orders/cancel",
                "headers": {
                    "Authorization": "Bearer <token>",
                    "Content-Type": "application/json"
                },
                "body": {"order_id": "12345"}
            },
            "response": {
                "status": 200,
                "body": {"message": "Order cancellation acknowledged."}
            }
        }
    ],
    "Products": [
        {
            "method": "POST",
            "endpoint": "Create a Product",
            "description": "Add a new product.",
            "request": {
                "url": "/products",
                "headers": {
                    "Authorization": "Bearer <token>",
                    "Content-Type": "application/json"
                },
                "body": {"name": "New Product", "price": 19.99, "stock": 100}
            },
            "response": {
                "status": 201,
                "body": {"product_id": "67890", "name": "New Product"}
            }
        },
        {
            "method": "GET",
            "endpoint": "List Products",
            "description": "Retrieve a list of one or all products.",
            "request": {
                "url": "/products",
                "headers": {"Authorization": "Bearer <token>"}
            },
            "response": {
                "status": 200,
                "body": [{"product_id": "67890", "name": "New Product"}]
            }
        },
        {
            "method": "PATCH",
            "endpoint": "Update Stock",
            "description": "Update the stock levels for a specific product.",
            "request": {
                "url": "/products/{product_id}/stock",
                "headers": {
                    "Authorization": "Bearer <token>",
                    "Content-Type": "application/json"
                },
                "body": {"stock": 150}
            },
            "response": {
                "status": 200,
                "body": {"message": "Stock updated successfully."}
            }
        }
    ]
}

# Create folders and markdown files
for category, endpoints in api_docs.items():
    os.makedirs(category, exist_ok=True)
    for ep in endpoints:
        filename = f"{ep['endpoint'].replace(' ', '_')}.md"
        filepath = os.path.join(category, filename)
        with open(filepath, "w") as f:
            f.write(f"# {ep['endpoint']}\n")
            f.write(f"**Method:** {ep['method']}\n\n")
            f.write(f"**Description:** {ep['description']}\n\n")
            f.write("## Parameters\n<!-- Add parameters here -->\n\n")
            f.write("## Request Example\n```json\n")
            f.write(json.dumps(ep["request"], indent=4))
            f.write("\n```\n\n")
            f.write("## Response\n```json\n")
            f.write(json.dumps(ep["response"], indent=4))
            f.write("\n```\n")
