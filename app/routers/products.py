from fastapi import APIRouter, File, Form, Body
from app.schemas.products import SNewProduct, SProduct as ProductSchema
from fastapi import UploadFile, Depends
from pathlib import Path
from app.database.working_with_db import Products

router = APIRouter(prefix="/products", tags = ["Товары 📦"])


@router.post("/new_product")
async def new_product(new_product : SNewProduct = Body(...), img : UploadFile = File(...)) -> ProductSchema:
    
    image_path = Path("static","img","product_img",img.filename)
    with open(image_path, "wb") as buffer:
        buffer.write(await img.read())
    
    product_with_img_path = new_product
    product_with_img_path.img_path = str(image_path)
    new_product_ = await Products.create_product(product_with_img_path)

    return new_product_


@router.get("{product_id}")
async def get_product(product_id : int) -> ProductSchema:
    pass




    

        


