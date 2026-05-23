from fastapi import Body, FastAPI
app = FastAPI()

PRODUCTS = [
    {"id": 1, "name": "Wireless Headphones", "brand": "SoundMax", "category": "electronics", "price": 89.99, "stock": 45},
    {"id": 2, "name": "Running Shoes", "brand": "SwiftStep", "category": "footwear", "price": 120.00, "stock": 30},
    {"id": 3, "name": "Yoga Mat", "brand": "FlexFit", "category": "sports", "price": 35.50, "stock": 100},
    {"id": 4, "name": "Bluetooth Speaker", "brand": "SoundMax", "category": "electronics", "price": 55.00, "stock": 60},
    {"id": 5, "name": "Leather Wallet", "brand": "UrbanEdge", "category": "accessories", "price": 40.00, "stock": 75},
    {"id": 6, "name": "Stainless Water Bottle", "brand": "HydroLife", "category": "sports", "price": 25.00, "stock": 200},
    {"id": 7, "name": "Mechanical Keyboard", "brand": "TypePro", "category": "electronics", "price": 149.99, "stock": 20},
    {"id": 8, "name": "Sunglasses", "brand": "UrbanEdge", "category": "accessories", "price": 65.00, "stock": 50},
    {"id": 9, "name": "Basketball", "brand": "CourtKing", "category": "sports", "price": 45.00, "stock": 80},
    {"id": 10, "name": "Casual Sneakers", "brand": "SwiftStep", "category": "footwear", "price": 85.00, "stock": 40},
    {"id": 11, "name": "Desk Lamp", "brand": "BrightSpace", "category": "home", "price": 30.00, "stock": 90},
    {"id": 12, "name": "Backpack", "brand": "TrailBlaze", "category": "accessories", "price": 70.00, "stock": 55},
    {"id": 13, "name": "Gaming Mouse", "brand": "TypePro", "category": "electronics", "price": 59.99, "stock": 35},
    {"id": 14, "name": "Ceramic Coffee Mug", "brand": "BrightSpace", "category": "home", "price": 15.00, "stock": 150},
    {"id": 15, "name": "Formal Shoes", "brand": "SwiftStep", "category": "footwear", "price": 110.00, "stock": 25},
    {"id": 16, "name": "Dumbbells Set", "brand": "FlexFit", "category": "sports", "price": 95.00, "stock": 40},
    {"id": 17, "name": "Throw Blanket", "brand": "CozyNest", "category": "home", "price": 42.00, "stock": 70},
    {"id": 18, "name": "Smartwatch", "brand": "SoundMax", "category": "electronics", "price": 199.99, "stock": 15},
    {"id": 19, "name": "Canvas Tote Bag", "brand": "UrbanEdge", "category": "accessories", "price": 22.00, "stock": 120},
    {"id": 20, "name": "Hiking Boots", "brand": "TrailBlaze", "category": "footwear", "price": 135.00, "stock": 18},
]

@app.get("/allproducts")
async def FetchAllProducts():
    return PRODUCTS

#get product by id
@app.get("/products/id/{product_id}")     #used path parameter
async def FetchProductById(product_id: int):
    for item in PRODUCTS:
        if item.get("id") == product_id:
            return item
#get product by product name
@app.get("/products/name/{product_name}")     #used path parameter
async def FetchAllProducts(product_name: str):
    for item in PRODUCTS:
        if item.get("name").casefold() == product_name.casefold():
            return item
        
@app.get("/productCategory")       #used query parameter
async def FetchProductWithCategory(category:str):
    products_to_return = []
    for product in PRODUCTS:
        if product.get("category").casefold() == category.casefold():
            products_to_return.append(product)
    return products_to_return


@app.get("/productBrand")       #used query parameter
async def FetchProductWithbrand(brand:str):
    products_to_return = []
    for product in PRODUCTS:
        if product.get("brand").casefold() == brand.casefold():
            products_to_return.append(product)
    return products_to_return


@app.get("/productPrice")       #used query parameter
async def FetchProductWithPrice(min_price: float, max_price: float):
    return [p for p in PRODUCTS if min_price <= p.get("price") <= max_price]



#POST


@app.post("/addProducts")
async def createProducts(new_product = Body()):
    PRODUCTS.append(new_product)


#update products by id
@app.put("/updateproducts")
async def updateProduct(updated_product = Body()):

    for product in PRODUCTS:

        if product.get("id") == updated_product.get("id"):

            product.update(updated_product)

            return {"message": "Product updated successfully"}

    return {"message": "Product not found"}


@app.delete("/deleteproduct/{product_id}")
async def deleteProduct(product_id:int):
    for product in PRODUCTS:
        if product.get("id") == product_id:
            PRODUCTS.remove(product)
            break








