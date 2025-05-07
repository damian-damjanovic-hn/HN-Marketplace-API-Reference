# HN Marketplace API Reference

## Introduction
The HN Marketplace API enables developers to automate and streamline various processes associated with order management and product inventory. This includes the ability to process orders, create new products and manage stock levels. Each endpoint is equipped with the necessary parameters and responses to ensure a smooth integration experience.

## Orders
The Orders section of the API allows you to manage customer orders effectively. Here are the key endpoints available for order management:

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

This API reference aims to provide all the necessary information for developers to integrate with the HN Marketplace efficiently. Each endpoint is documented with the required parameters, example requests, and responses to help you get started quickly.

## Collections:
### Orders
- **GET** List Orders
- **POST** Acknowledge an order
- **GET** View Order details
- **POST** Backorder an order
- **GET** List carriers
- **POST** Dispatch an order
- **POST** Acknowledge a cancellation

### Products
- **POST** create_product
- **GET** list_products
- **PATCH** stock_update

## License

This project is licensed for internal use. Contact the repository owner for more information.
