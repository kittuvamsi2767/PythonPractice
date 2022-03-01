# 5. write a program to read file from s3 bucket and write it to another bucket without changes?
import boto3
# Scenario 1. Display the objects in the S3 bucket
'''
pref = input("Enter S3 Object name to search in bucket vamsi-own-bucket: ")
 s3 = boto3.resource('s3')
 my_bucket = s3.Bucket('vamsi-own-bucket')
 for object_summary in my_bucket.objects.filter(Prefix=pref):
    print(object_summary.key)
'''

# Scenario 2. Create a Object in the given bucket
'''
new_file_name = input("Enter S3 Object name to be created : ")
bucket_name = input("Please provide the object where you want to create the new object: ")
s3 = boto3.resource('s3')

txt_data = b'Vamsi and Hareesh are working on Python programs given by Veera Shekar'
object = s3.Object(bucket_name,new_file_name)
result = object.put(Body=txt_data)
'''

# Scenario 3. Read an object from one bucket and write it to another S3 bucket without any changes
s3 = boto3.resource('s3')
old_bucket_name = input("Enter the Old Bucket Name: ")
my_old_bucket = s3.Bucket(old_bucket_name)
old_object_name = input("Enter the old object Name: ")
s3_object  = s3.get_object(Bucket=old_bucket_name, Key=old_object_name)
print(s3_object.read())


# Scenario 4. Read an object from one bucket and write it to another S3 bucket by making some changes

