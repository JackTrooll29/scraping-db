import boto3

client = boto3.client(
    service_name='s3',
    aws_access_key_id='AKIA4QPKVP5PIINEHETW',
    aws_secret_access_key='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',
    region_name='eu-west-2'
)

# client.create_bucket(
#     ACL='public',
#     Bucket='arqemojis', # altere para um nome qualquer
#     CreateBucketConfiguration={
#         'LocationConstraint': 'eu-west-1'
#     },
# )

client.upload_file("https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/apple/325/grinning-face_1f600.png", "emojiurl", "al2.png")
# client.download_file("imgurlemoji", "hello-s3", "downloaded-hello-s3.txt")
