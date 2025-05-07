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
                "body": [
                    {
                        "order_id": "12345",
                        "customer_name": "John Doe",
                        "status": "Processing",
                        "items": [{"product_id": "67890", "quantity": 2}]
                    }
                ]
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
        }
        # Add other Orders endpoints here...
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
                "body": {
                    "name": "New Product",
                    "price": 19.99,
                    "stock": 100
                }
            },
            "response": {
                "status": 201,
                "body": {
                    "product_id": "67890",
                    "name": "New Product",
                    "price": 19.99,
                    "stock": 100
                }
            }
        }
        # Add other Products endpoints here...
    ]
}

# Create directories and markdown files
for category, endpoints in api_docs.items():
    os.makedirs(category, exist_ok=True)
    for ep in endpoints:
        filename = f"{ep['endpoint'].replace(' ', '_')}.md"
        filepath = os.path.join(category, filename)
        with open(filepath, "w") as f:
            f.write(f"# {ep['endpoint']}\n")
            f.write(f"**Method:** {ep['method']}\n\n")
            f.write(f"**Description:** {ep['description']}\n\n")
            f.write("## Parameters\n")
            f.write("<!-- Add parameters here -->\n\n")
            f.write("## Request Example\n")
            f.write("```json\n")
            f.write(json.dumps(ep.get("request", {}), indent=4))
            f.write("\n```\n\n")
            f.write("## Response\n")
            f.write("```json\n")
            f.write(json.dumps(ep.get("response", {}), indent=4))
            f.write("\n```\n")
