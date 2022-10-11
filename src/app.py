import json
import requests
import bcrypt
import boto3

BUCKET_NAME="awsmadeeasy-demo-sam-connector-bucket"

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    ## Load input if we get it
    in_body = {}
    if 'body' in event.keys():
        in_body = json.loads(event['body'])

    ## Echo the input back
    print(in_body)
    res = {}
    res['input'] = in_body


    ## Connect to S3
    client = boto3.client('s3')

    ## If we have an input, add it to the bucket
    status_code = 200
    if 'contents' in in_body.keys() and 'fname' in in_body.keys():
        client.put_object(
            Bucket=BUCKET_NAME,
            Key=in_body['fname'],
            Body=in_body['contents'].encode('utf-8')
        )
        ## We created something, so it's a 201
        status_code = 201

    ## List the contents of the bucket in the return
    bucket_contents = client.list_objects_v2(Bucket=BUCKET_NAME)
    res["bucket_contents"] = bucket_contents['Contents']

    return {
        "statusCode": status_code,
        "body": json.dumps(res, default=str)
    }
