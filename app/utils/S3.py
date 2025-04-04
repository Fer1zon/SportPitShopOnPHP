# from aiobotocore.session import get_session
# from contextlib import asynccontextmanager
# import asyncio
# from fastapi import UploadFile
# from pathlib import Path
# class S3Client:
#     def __init__(
#             self,
#             access_key: str,
#             secret_key: str,
#             endpoint_url: str,
#             bucket_name: str):
#         self.config = {
#             "aws_access_key_id": access_key,
#             "aws_secret_access_key": secret_key,
#             "endpoint_url": endpoint_url,
#             "use_ssl" : False, 
#             "verify" : False


            
#         }
#         self.bucket_name = bucket_name
#         self.session = get_session()

#     @asynccontextmanager
#     async def get_client(self):
#         async with self.session.create_client("s3", **self.config) as client:
#             yield client

#     # async def upload_file(
#     #         self,
#     #         file : UploadFile,
#     #         file_name: str,
#     # ):
        
        
#     #     async with self.get_client() as client:
#     #         file = await file.read()
#     #         s = await client.put_object(
#     #                 Bucket=self.bucket_name,
#     #                 Key=file_name,
#     #                 Body=file,
#     #             )
        
#     #         print(s)
#     async def upload_file(
#             self,
#             file_path: str,
#     ):
#         object_name = "i.jpg"  # /users/artem/cat.jpg

#         async with self.get_client() as client:
#             with open(file_path, "rb") as file:
#                 file_content = file.read()
#                 await client.put_object(
#                     Bucket=self.bucket_name,
#                     Key=object_name,
#                     Body=file_content,
#                 )
            
# S3Client_ = S3Client(
#     access_key="LT1J1P0Y9UMGF09UI18K",
#     secret_key="wltW7untnNmVfkjJCghxzfSY1iiCqymwjdzs7xHE",
#     endpoint_url="https://s3.ru1.storage.beget.cloud",
#     bucket_name="d3870b7926fa-sport-pit-storag"
# )

# async def main():
#     await S3Client_.upload_file(Path("app", "utils","i.jpg"))


# asyncio.run(main())