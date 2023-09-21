from fastapi import APIRouter, HTTPException
from Homework_6.db import database, products
from Homework_6.models.product import Product, ProductIn

router = APIRouter()


@router.post("/product", response_model=Product)
async def create_product(product: ProductIn):
    query = products.insert().values(name=product.name,
                                     description=product.description,
                                     price=product.price)
    last_record_id = await database.execute(query)
    return {**product.dict(), "id": last_record_id}


@router.get("/products/", response_model=list[Product])
async def read_product():
    query = products.select()
    return await database.fetch_all(query)


@router.get("/products/{product_id}", response_model=Product)
async def read_product(product_id: int):
    query = products.select().where(products.c.id == product_id)
    return await database.fetch_one(query)


@router.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: int, new_product: Product):
    query = products.update().where(products.c.id == product_id).values(**new_product.dict())
    await database.execute(query)
    return {**new_product.dict(), "id": product_id}


@router.delete("/products/{product_id}")
async def delete_product(user_id: int):
    query = products.delete().where(products.c.id == user_id)
    await database.execute(query)
    return {'message': 'Product deleted'}
