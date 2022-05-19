import boto3

class S3Connection:

    def __init__(self):
        self.s3 = boto3.client(service_name='s3', region_name='ap-northeast-2')

    def put_object(self, bucket, filepath, access_key):
        try:
            self.s3.upload_file(filepath, bucket, access_key)
        except Exception as e:
            return False
        return True