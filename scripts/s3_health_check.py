import boto3

# Create S3 client
s3 = boto3.client('s3')

try:
    # Get list of S3 buckets
    response = s3.list_buckets()

    print("\n===== S3 HEALTH CHECK =====\n")

    buckets = response['Buckets']

    if len(buckets) == 0:
        print("No S3 buckets found.")
    else:
        print(f"Total Buckets: {len(buckets)}\n")

        for bucket in buckets:
            print(f"Bucket Name: {bucket['Name']}")
            print(f"Creation Date: {bucket['CreationDate']}")
            print("-" * 40)

except Exception as e:
    print("Error:", e)