import os

# Define the API documentation structure
api_docs = {
    "Orders": [
        {"method": "GET", "endpoint": "List Orders", "description": "Retrieve a list of all customer orders."},
        {"method": "POST", "endpoint": "Acknowledge an Order", "description": "Acknowledge the receipt of a new customer order."},
        {"method": "GET", "endpoint": "View Order Details", "description": "View detailed information about a specific order."},
        {"method": "POST", "endpoint": "Backorder an Order", "description": "Mark an order as backordered."},
        {"method": "GET", "endpoint": "List Carriers", "description": "Retrieve a list of available carriers for order dispatch."},
        {"method": "POST", "endpoint": "Dispatch an Order", "description": "Dispatch an order to the customer."},
        {"method": "POST", "endpoint": "Acknowledge a Cancellation", "description": "Acknowledge the cancellation of an order."}
    ],
    "Products": [
        {"method": "POST", "endpoint": "Create a Product", "description": "Add a new product."},
        {"method": "GET", "endpoint": "List Products", "description": "Retrieve a list of one or all products."},
        {"method": "PATCH", "endpoint": "Update Stock", "description": "Update the stock levels for a specific product."}
    ]
}

# Create directories and files for each API request
for category, requests in api_docs.items():
    os.makedirs(category, exist_ok=True)
    
    for request in requests:
        filename = f"{request['endpoint'].replace(' ', '_')}.md"
        filepath = os.path.join(category, filename)
        with open(filepath, 'w') as f:
            f.write(f"# {request['endpoint']}\n")
            f.write(f"**Method:** {request['method']}\n\n")
            f.write(f"**Description:** {request['description']}\n\n")
            f.write("## Parameters\n")
            f.write("<!-- Add parameters here -->\n\n")
            f.write("## Request Example\n")
            f.write("<!-- Add request example here -->\n\n")
            f.write("## Response\n")
            f.write("<!-- Add response here -->\n")
