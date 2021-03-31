import boto3

# boto3, python SDK for accessing AWS services
ec2 = boto3.client('ec2')

# starting an ec2 instance
def start_ec2(event, context):
    ec2_instances = get_all_ec2_ids()
    response = ec2.start_instances(
        InstanceIds=ec2_instances,
        DryRun=False
    )
    return response

# stopping an instance
def stop_ec2(event, context):
    ec2_instances = get_all_ec2_ids()
    response = ec2.stop_instances(
        InstanceIds=ec2_instances,
        DryRun=False
    )
    return response


# get the list of all the ec2 instances currently available
def get_all_ec2_ids():
    response = ec2.describe_instances(DryRun=False)
    instances = []
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            # prints the entire Dictionary object
            # This will print will output the value of the Dictionary key 'InstanceId'
            instances.append(instance["InstanceId"])
    return instances
