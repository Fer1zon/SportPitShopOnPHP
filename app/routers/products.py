from fastapi import APIRouter, File, Form, Body
from app.schemas.products import SNewProduct, SProduct as ProductSchema
from fastapi import UploadFile, Depends
from pathlib import Path
from app.database.working_with_db import Products
# from app.utils.S3 import S3Client
router = APIRouter(prefix="/api/products", tags = ["Товары 📦"])

# S3Client_ = S3Client(
#     access_key="LT1J1P0Y9UMGF09UI18K",
#     secret_key="wltW7untnNmVfkjJCghxzfSY1iiCqymwjdzs7xHE",
#     endpoint_url="https://s3.ru1.storage.beget.cloud",
#     bucket_name="d3870b7926fa-sport-pit-storag"
# )

@router.post("/new_product")
async def new_product(new_product : SNewProduct = Body(...), img : UploadFile = File(...)) -> ProductSchema:
    
    image_path = Path("static","img","product_img",img.filename)
    with open(image_path, "wb") as buffer:
        buffer.write(await img.read())
    print(img)
    # await S3Client_.upload_file(img, "SSSS.jpg")
    
    product_with_img_path = new_product
    product_with_img_path.img_path = str(image_path)
    new_product_ = await Products.create_product(product_with_img_path)

    return new_product_


@router.get("{product_id}")
async def get_product(product_id : int) -> ProductSchema:
    pass




    

        


