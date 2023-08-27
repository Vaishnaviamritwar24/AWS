import boto3

# Replace with your AWS credentials and region
aws_access_key = 'AKIA2TWQFX6ZG7NMH7IW'
aws_secret_key = 'c5kCOFotNFdPivAQcS1sZW3wlUmuVuqCPvNxpOBW'
region = 'ap-south-1'

bucket_name = 'vaishnavi02'  # Replace with your bucket name
file_path = '/Users/vaishnavi/Desktop/AWS/S3/access.log'  # Replace with the local file path
s3_key = 'access.log'  # Replace with the destination key in the bucket

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name=region)

# Upload the file
s3.upload_file(file_path, bucket_name, s3_key)

print(f'{file_path} uploaded to {bucket_name}/{s3_key}')
