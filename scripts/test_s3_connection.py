import boto3
import os
from botocore.client import Config

# 从环境变量读取配置
endpoint = os.getenv('S3_ENDPOINT_URL', 'http://192.168.0.190:9000')
bucket_name = os.getenv('S3_BUCKET', 'edge-to-cloud-robotics-landing-s3')
access_key = os.getenv('AWS_ACCESS_KEY_ID', 'minioadmin')
secret_key = os.getenv('AWS_SECRET_ACCESS_KEY', 'minioadmin')

print(f"📡 正在尝试连接 P620 MinIO: {endpoint}")

# 初始化 S3 客户端
s3 = boto3.resource('s3',
                    endpoint_url=endpoint,
                    aws_access_key_id=access_key,
                    aws_secret_access_key=secret_key,
                    config=Config(signature_version='s3v4'),
                    region_name='us-east-1')

try:
    # 1. 创建一个测试文件
    content = "Hello P620! Data from Pi 4B NVMe SSD. 2026-01-02"
    with open("pi_test.txt", "w") as f:
        f.write(content)
    
    # 2. 上传到 MinIO
    s3.Bucket(bucket_name).upload_file("pi_test.txt", "mission_1/pi_test.txt")
    print(f"✅ 上传成功！请在 P620 的 MinIO 管理界面 (http://192.168.0.190:9001) 查看 {bucket_name} 桶。")

except Exception as e:
    print(f"❌ 出错啦: {e}")
