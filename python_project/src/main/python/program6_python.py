import boto3
import pandas as pd
import os

AWS_S3_BUCKET = os.getenv('vamsi-test-bucket-cli2')
s3_client=boto3.client('s3')
response = s3_client.get_object(Bucket=AWS_S3_BUCKET, Key="admin_accessKeys.csv")
status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")
if status == 200:
    print(f"Successful S3 get_object response. Status - {status}")
    books_df = pd.read_csv(response.get("Body"))
    print(books_df)
else:
    print(f"Unsuccessful S3 get_object response. Status - {status}")
