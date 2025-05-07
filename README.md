# HN Marketplace API Documentation

## Introduction

The HN Marketplace API enables developers to automate and streamline various processes associated with order management and product inventory. This includes the ability to process orders, create new products, and manage stock levels. Each endpoint is equipped with the necessary parameters and responses to ensure a smooth integration experience.

## Orders

The Orders section of the API allows you to manage customer orders effectively. Key endpoints include:

- **GET List Orders**: Retrieve a list of all customer orders.
- **POST Acknowledge an Order**: Acknowledge the receipt of a new customer order.
- **GET View Order Details**: View detailed information about a specific order.
- **POST Backorder an Order**: Mark an order as backordered.
- **GET List Carriers**: Retrieve a list of available carriers for order dispatch.
- **POST Dispatch an Order**: Dispatch an order to the customer.
- **POST Acknowledge a Cancellation**: Acknowledge the cancellation of an order.

## Product & Stock Management

- **POST Create a Product**: Add a new product.
- **GET List Products**: Retrieve a list of one or all products.
- **PATCH Update Stock**: Update the stock levels for a specific product.

## Getting Started

To use the API, you will need an API key. Include it in the `Authorization` header of your requests:

```http
Authorization: Bearer <your-api-key>
```

## Collections

### Orders

- `GET /orders`
- `POST /orders/acknowledge`
- `GET /orders/{order_id}`
- `POST /orders/backorder`
- `GET /carriers`
- `POST /orders/dispatch`
- `POST /orders/cancel`

### Products

- `POST /products`
- `GET /products`
- `PATCH /products/{product_id}/stock`

## License

This project is licensed for internal use. Contact the repository owner for more information.