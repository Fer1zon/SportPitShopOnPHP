from app.database.database import new_session
from app.schemas.products import SNewProduct
from sqlalchemy import select
from app.database.models import Product





class Products():
    @classmethod
    async def create_product(self, new_product : SNewProduct):
        async with new_session() as session:
            new_product_obj = new_product.model_dump()
            new_product_ = Product(**new_product_obj)

            session.add(new_product_)
            await session.flush()
            await session.commit()

            return new_product_
        
    async def get_product(self, product_id : int):
        async with new_session() as session:
            product = await session.scalar(select(Product).where(Product.id == product_id))
            return product