Dear \[Vendor Name\],

Welcome to the Harvey Norman Marketplace! We are thrilled to have you join our platform. Below, you will find the necessary information to get started with our REST API.

**REST API Production Credentials:** Your production credentials will be provided separately. If you require sandbox credentials for testing, we can arrange that upon request.

**Rate Limit:** Please note that our API has a rate limit of **150 requests per minute**. Ensure your integration respects this limit to avoid any disruptions.

**Documentation:**

Please find the relevant API documentation below. You can import these into Postman, save them as a collection, and use them for testing purposes.

1.  **Harvey Norman Marketplace Australia API Reference:** [HN Marketplace API Reference](https://documenter.getpostman.com/view/31507165/2sB2j7dVDF "HN Marketplace API Reference")  
    *(Specific to Harvey Norman Marketplace Australia)*
    
2.  **Virtualstock API Integration Documentation:** [Virtualstock API integration documentation](https://documenter.getpostman.com/view/7011074/SWTABeT1?version=latest "Virtualstock API integration documentation")  
    *(Generic documentation provided by Virtualstock)*
    

**Additional Support:**

Below are three common real-life workflows you should implement, though a few other workflows are covered in the provided documentation.

**Workflow 1: Order Processing**

| Step | Company | Request | Description |
| --- | --- | --- | --- |
| 1   | Harvey Norman | Create new order | Harvey Norman creates a new order and sends it to the vendor. |
| 2   | \[Vendor\] | List your orders | Vendor retrieves the list of new orders using the API. |
| 3   | \[Vendor\] | Acknowledge Order | Vendor acknowledges receipt of the order, confirming they will process it. |
| 4   | \[Vendor\] | List available carriers (optional) | Vendor retrieves a list of available carriers for shipping. |
| 5   | \[Vendor\] | Dispatch Order | Vendor dispatches the order and updates the order status with tracking info. |

**Workflow 2: Order Backordering**

| Step | Company | Request | Description |
| --- | --- | --- | --- |
| 1   | Harvey Norman | Create new order | Harvey Norman creates a new order and sends it to the vendor. |
| 2   | \[Vendor\] | List your orders | Vendor retrieves the list of new orders using the API. |
| 3   | \[Vendor\] | Acknowledge Order | Vendor acknowledges receipt of the order, confirming they will process it. |
| 5   | \[Vendor\] | Backorder an Order | Vendor marks the order as backordered if the item is not immediately available. |
| 4   | \[Vendor\] | List available carriers (optional) | Vendor retrieves a list of available carriers for shipping. |
| 6   | \[Vendor\] | Dispatch Order | Vendor dispatches the order once the item is back in stock and updates the order status with tracking info. |

**Workflow 3: Order Cancellation**

| Step | Company | Request | Description |
| --- | --- | --- | --- |
| 1   | Harvey Norman | Create new order | Harvey Norman creates a new order and sends it to the vendor. |
| 2   | \[Vendor\] | List your orders | Vendor retrieves the list of new orders using the API. |
| 3   | \[Vendor\] | Acknowledge Order | Vendor acknowledges receipt of the order, confirming they will process it. |
| 5   | Harvey Norman | Request Cancellation | Harvey Norman requests cancellation of the order. |
| 4   | \[Vendor\] | Acknowledge Cancellation | Vendor acknowledges the cancellation request. |

**Best Practices:**

- **Error Handling:** Ensure to handle API errors gracefully and implement retry mechanisms where necessary.
- **Data Validation:** Validate all data before sending it to the API to avoid processing delays.
- **Security:** Use environment variables to store and manage API credentials securely. Follow best security practices to protect your credentials.

**Support:**

If you have any questions, need test orders, or require further assistance, please do not hesitate to reach out to me directly.

We look forward to a successful partnership!

Best regards,  
**<span style="color: black;">Damian Damjanovic</span>** <span style="color: black;">|</span> <span style="color: #0065b9;">Implementation Manager</span>  
<span style="color: black;">Harvey Norman Online Marketplace</span>  
**<span style="color: #0065b9;">T :</span>** <span style="color: black;">Direct +61 2 9394 6344</span><span style="color: black;">  
</span>**<span style="color: #0065b9;">E: [damian.damjanovic@au.harveynorman.com](mailto:damian.damjanovic@au.harveynorman.com)</span>**  
The eComm Store ACN 145 985 815  
Address: Unit 3-4, 145-151 Arthur Street, Homebush West, NSW 2140  
Postal: Locked Bag 2 Silverwater BC NSW 1811  
<img border="0" width="329" height="41" src=":/16079cb4243b4062972b2bdc1784c2f6" style="height: .427in; width: 3.427in;" alt="HN-DOM-JM_signature" v:shapes="Picture_x0020_1" class="jop-noMdConv">  
[<span style="color: #595959;">www.harveynorman.com.au</span>](http://www.harveynorman.com.au/) <span style="color: #595959;">II</span> [<span style="color: #595959;">www.domayne.com.au</span>](http://www.domayne.com.au/) <span style="color: #595959;">II</span> [<span style="color: #595959;">www.joycemayne.com.au</span>](http://www.joycemayne.com.au/)  
<br/>**<span style="color: #00b050;">Please consider the environment before printing this email</span>**