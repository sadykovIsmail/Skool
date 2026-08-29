import os
import boto3
from botocore.config import Config

def required_environment_variable(name):
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(f"Missing {name}. Set it before running this upload script.")
    return value


# Keep credentials out of source control. Set these values in your shell or a local .env file.
ACCOUNT_ID = required_environment_variable("R2_ACCOUNT_ID")
ACCESS_KEY_ID = required_environment_variable("R2_ACCESS_KEY_ID")
SECRET_ACCESS_KEY = required_environment_variable("R2_SECRET_ACCESS_KEY")
BUCKET_NAME = os.environ.get("R2_BUCKET_NAME", "app-course-videos")

# Initialize S3 client for Cloudflare R2
s3 = boto3.client(
    service_name="s3",
    endpoint_url=f"https://{ACCOUNT_ID}.r2.cloudflarestorage.com",
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=SECRET_ACCESS_KEY,
    config=Config(signature_version="s3v4")
)

folder = "videos"
files = [f for f in os.listdir(folder) if f.endswith('.mp4')]

print(f"Checking and uploading remaining files from '{folder}'...\n")

success = 0
skipped = 0
failed = 0

for file_name in files:
    local_path = os.path.join(folder, file_name)

    # Check if the video is already uploaded to avoid redundant work
    try:
        s3.head_object(Bucket=BUCKET_NAME, Key=file_name)
        print(f"Skipping (already uploaded): {file_name}")
        skipped += 1
    except:
        print(f"Uploading via S3 multipart: {file_name}...")
        try:
            s3.upload_file(local_path, BUCKET_NAME, file_name)
            print(f"SUCCESS: {file_name}\n")
            success += 1
        except Exception as e:
            print(f"FAILED: {file_name} -> {e}\n")
            failed += 1

print("Done!")
print(f"Uploaded: {success} file(s)")
print(f"Skipped: {skipped} file(s)")
print(f"Failed: {failed} file(s)")
