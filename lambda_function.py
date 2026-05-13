import boto3

ec2 = boto3.client('ec2')

INSTANCE_ID = "i-07a29cd83f1e991a5"

def lambda_handler(event, context):
    action = event.get("action")

    if action == "start":
        ec2.start_instances(InstanceIds=[INSTANCE_ID])
        return {"message": "EC2 starting"}

    elif action == "stop":
        ec2.stop_instances(InstanceIds=[INSTANCE_ID])
        return {"message": "EC2 stopping"}

    return {"message": "Invalid action"}