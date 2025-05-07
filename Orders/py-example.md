# Fetch Order Data

## Introduction

The VirtualStock API allows vendors to fetch order data using HTTP authentication. This guide explains how to retrieve orders using Python.

## Installation

Ensure you have Python installed along with the `requests` library:

```bash
pip install requests
```

## Authentication

The API requires basic HTTP authentication using:

- **Username**
    
- **Password**
    

Provide these credentials in your script.

## Fetching Orders

### Functionality

The `get_orders()` function retrieves customer orders using customizable parameters.

### Parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| `limit` | `int` | Number of orders to fetch per request |
| `offset` | `int` | Pagination offset for fetching records |
| `status` | `str` | Status filter (`ORDER`, `ORDER_ACK`, etc.) |

### Example Usage:

```
orders = get_orders(limit=5, offset=0, status="ORDER")
print(orders)
```

### Error Handling

If the request fails, the function captures the exception and prints an error message.
### Script
    ```bash
    Fetch a list of new customer orders from the API.

    Args:
        limit (int): Number of orders to retrieve per request.
        offset (int): Pagination offset (default is 0).
        status (str): Order status filter (default is "ORDER").

    Returns:
        list or None: List of order details or None if an error occurs.
        # Raises an error for bad responses (4xx, 5xx)
    ```

### Python Code:

```python
import requests

API_URL = "https://api.virtualstock.com/restapi/v4/orders/"
API_USERNAME = "your_username"
API_PASSWORD = "your_password"

def get_orders(limit=1, offset=0, status="ORDER"):

    params = {
        "limit": limit,
        "offset": offset,
        "status": status
    }

    headers = {
        "Accept": "application/json"
    }

    try:
        response = requests.get(
            API_URL, 
            params=params,
            auth=HTTPBasicAuth(API_USERNAME, API_PASSWORD),
            headers=headers
        )
        response.raise_for_status()
        orders_data = response.json()

        if orders_data and "orders" in orders_data:
            return orders_data["orders"]
        else:
            print("No orders found.")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching orders: {e}")
        return None

if __name__ == "__main__":
    orders = get_orders(limit=5, offset=0, status="ORDER")
    if orders:
        print("Fetched Orders:", orders)
    else:
        print("Failed to retrieve orders.")
```
