import os
import boto3
import logging
from botocore.exceptions import ClientError
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%d-%m-%y_%T")

logging.basicConfig(level=logging.INFO)

try:
    s3_resource = boto3.resource(
        's3',
        endpoint_url='https://s3.ir-thr-at1.arvanstorage.com',
        aws_access_key_id='...',
        aws_secret_access_key='...'
    )
except Exception as exc:
    logging.error(exc)
else:
    try:
        bucket = s3_resource.Bucket('k8s-etcd-backup')
        file_path = '/home/ubuntu/backup-file.tar.gz'
        object_name = current_time

        with open(file_path, "rb") as file:
            bucket.put_object(
                ACL='private',
                Body=file,
                Key=object_name
            )
    except ClientError as e:
        logging.error(e)