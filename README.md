## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Built Using](#built_using)

## 🧐 About <a name = "about"></a>

The project has four services:
- auth
- user
- customer
- order
- product

Each service has an api module which defines different routes.

### Auth service
Handles the following operations:
- authentication token creation
- authentication token validation

### User service
Handles the following operations:
- user login
- user creation
- user retrieval

### Customer service
Handles the following operations:
- customer creation
- customer retrieval
- customer validation

### Product service
Handles the following operations:
- product creation
- product retrieval
- image upload for a product - stores the images locally in the `/services/product/assets/{product_id}` directory
- image retrieval for a product - returns the images from the `/services/product/assets/{product_id}` directory
- inventory update
- inventory retrieval

### Order service
Handles the following operations:
- order submission - verifies if there is enough stock for that product, checks if the customer has all account information provided, then it updates the inventory and returns a success message.  

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them.

```
python v3.10 - https://www.python.org/downloads/
docker compose v2.3.3 - https://docs.docker.com/compose/install/
```

### Installing

In order to execute the develompent env on your local machine run the following command in a terminal
```
./entryfile.sh
```
This will run all docker containers from the services.


## 🔧 Running the tests <a name = "tests"></a>

### Unit tests
The unit tests for the auth service can be executed from the `/services/auth` directory as follows:
```
docker compose up tests
```

This will test scenarios for generating and validating the authentication token.

### Automated tests
The automated tests for the user service can be executed from the `/services/user` directory as follows:
```
docker compose up tests
```

This will test scenarios for user creation and user login.


## 🎈 Usage <a name="usage"></a>

The system can be tested in a browser by running the [client](https://github.com/vali-pavel/online-shop-app) application.

A user can login from the `/login` page.  
A user of type customer can create an account from the `/signup` page.  
A user of type merchant can create an account from the `/admin/signup` page.  
A merchant can create a product from the `/admin/products/new` page.  
The customer can update account information in the `/account` page.  
The customer and merchant can see products in the `/products` page.  
The customer and merchant can see details for a specific product by clicking on the product name from the `/products` page, which will then redirect to the `/products/{product_id}` page.  
The customer can submit a 1-click checkout from the `/products` page or from the page of a specific product `/products/{product_id}`. If the account information is incomplete then the 1-click checkout will fail.


## ⛏️ Built Using <a name = "built_using"></a>

- [MySQL](https://www.mysql.com/) - Database
- [FastApi](https://fastapi.tiangolo.com/) - Server Framework
- [ReactJs](https://reactjs.org/) - Web Framework
- [Python](https://www.python.org/) - Server Environment
