import boto3
import uuid

s3 = boto3.resource("s3")
def upload_backup(s3, file_name, bucket_name, key_name):
    data = open(file_name, 'rb') #reads the data in binary format, cause in when uploading data to an S3 bucket the data is read in binary format
    s3.Bucket(bucket_name).put_object(Key=key_name, Body = data)
    print("Uploaded!")

file_name = "file_to_be_backedup.txt"
bucket_name = "automation-s3-project-bucket"
key_name = "backup " +str(uuid.uuid4()) +".tar.gz"

upload_backup(s3, file_name,bucket_name, key_name)