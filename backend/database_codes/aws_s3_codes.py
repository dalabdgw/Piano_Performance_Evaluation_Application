import boto3
from botocore.exceptions import NoCredentialsError
from dotenv import load_dotenv
import os

# .env 파일 불러오기
load_dotenv('./database_codes/db_env.env')
aws_access_key = os.getenv('AWS_ACCESS_KEY')
aws_private_key = os.getenv('AWS_PRIVATE_KEY')
aws_s3_bucket_name = os.getenv('AWS_S3_BUCKET_NAME')

print(aws_s3_bucket_name)

def upload_to_aws(local_file, s3_file_path):
    """
    AWS S3 버킷의 특정 폴더에 파일을 업로드하고, 업로드한 파일의 URL을 반환하는 함수입니다.

    :param local_file: 로컬 시스템에 있는 파일의 경로입니다.
    :param bucket: 업로드할 S3 버킷의 이름입니다.
    :param s3_file_path: S3에 저장될 파일의 경로 및 이름입니다.
    :return: 업로드 성공 여부와 파일 URL을 반환합니다.
    """
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key,
                      aws_secret_access_key=aws_private_key)

    try:
        s3.upload_file(local_file, aws_s3_bucket_name, s3_file_path)
        file_url = f"https://{aws_s3_bucket_name}.s3.amazonaws.com/{s3_file_path}"
        return True, file_url
    except FileNotFoundError:
        return False, None
    except NoCredentialsError:
        return False, None


#uploaded, file_url = upload_to_aws('test.txt', aws_s3_bucket_name, 'test/test.txt')

#if uploaded:
#    print(f"File URL: {file_url}")

