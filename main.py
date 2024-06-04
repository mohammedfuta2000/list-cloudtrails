import boto3
import os
import sys
from dotenv import load_dotenv

def main(region):
    load_dotenv()  # Load environment variables from a .env file if it exists

    # Retrieve AWS credentials from environment variables
    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    
    if not aws_access_key_id or not aws_secret_access_key:
        print("AWS credentials not found in environment variables.")
        sys.exit(1)

    # Create a boto3 client for CloudTrail
    client = boto3.client(
        'cloudtrail',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=region
    )
    
    # Call the describe_trails method
    response = client.describe_trails()

    # Print trail names and ARNs
    print("CloudTrail information:")
    print(f"{'Name':<20} {'ARN':<60}")
    print("="*80)
    for trail in response['trailList']:
        name = trail.get('Name', 'N/A')
        arn = trail.get('TrailARN', 'N/A')
        print(f"{name:<20} {arn:<60}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <region>")
        sys.exit(1)

    region = sys.argv[1]
    main(region)
