# Products REST API

A simple REST API built with **FastAPI** to practice core HTTP methods — GET, POST, PUT, and DELETE. This is a learning project focused on understanding path parameters, query parameters, and request body handling.

---

## What I Learned

- Building REST APIs with FastAPI
- Using **path parameters** for fetching specific resources
- Using **query parameters** for filtering data
- Handling **request bodies** with `Body()` for POST and PUT
- Performing **CRUD operations** on an in-memory dataset

---

## Getting Started

### Prerequisites

- Python 3.8+
- FastAPI
- Uvicorn

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/products-rest-api.git
cd products-rest-api

# Install dependencies
pip install fastapi uvicorn

# Run the server
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

> FastAPI auto-generates interactive docs at `http://127.0.0.1:8000/docs`

---

##  Data Structure

Each product has the following fields:

| Field      | Type    | Description                        |
|------------|---------|------------------------------------|
| `id`       | int     | Unique identifier                  |
| `name`     | string  | Product name                       |
| `brand`    | string  | Brand name                         |
| `category` | string  | Category (electronics, sports etc) |
| `price`    | float   | Price in USD                       |
| `stock`    | int     | Available quantity                 |

---

##  API Endpoints

### GET

| Method | Endpoint                        | Description                        |
|--------|---------------------------------|------------------------------------|
| GET    | `/allproducts`                  | Fetch all products                 |
| GET    | `/products/{product_id}`        | Fetch a single product by ID       |
| GET    | `/productCategory?category=`    | Filter products by category        |
| GET    | `/productBrand?brand=`          | Filter products by brand           |
| GET    | `/productPrice?price=`          | Filter products by exact price     |

### POST

| Method | Endpoint        | Description          |
|--------|-----------------|----------------------|
| POST   | `/addProducts`  | Add a new product    |

**Request body example:**
```json
{
  "id": 21,
  "name": "Wireless Earbuds",
  "brand": "SoundMax",
  "category": "electronics",
  "price": 49.99,
  "stock": 60
}
```

### PUT

| Method | Endpoint          | Description                      |
|--------|-------------------|----------------------------------|
| PUT    | `/updateproducts` | Update an existing product by ID |

**Request body example:**
```json
{
  "id": 5,
  "name": "Leather Wallet",
  "brand": "UrbanEdge",
  "category": "accessories",
  "price": 45.00,
  "stock": 60
}
```

### DELETE

| Method | Endpoint                          | Description                  |
|--------|-----------------------------------|------------------------------|
| DELETE | `/deleteproduct/{product_id}`     | Delete a product by ID       |

---

## 📁 Project Structure

```
products-rest-api/
│
├── main.py        # All API routes and logic
└── README.md      # Project documentation
```

---

##  Built With

- [FastAPI](https://fastapi.tiangolo.com/) — Web framework
- [Uvicorn](https://www.uvicorn.org/) — ASGI server

---

##  Notes

This project uses an **in-memory list** to store data, meaning all changes reset when the server restarts. It is intended purely for learning purposes.

---

##  Future Improvements

- [ ] Add Pydantic models for request validation
- [ ] Connect to a real database (PostgreSQL / SQLite)
- [ ] Add proper 404 error handling with `HTTPException`
- [ ] Add price range filtering (`min_price` / `max_price`)
- [ ] Follow consistent URL naming conventions

---

*Built while learning FastAPI — inspired by a Books API tutorial.*
