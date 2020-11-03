import boto3
kinesis = boto3.client("kinesis")

def handler(event, context):
    try:
        data = kinesis.describe_stream(
            StreamName="kdemo"
        )
        print(data)
    except BaseException as e:
        print(e)
        raise(e)
    
    return {"message": "Successfully executed"}
