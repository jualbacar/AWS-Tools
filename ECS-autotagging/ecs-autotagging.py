# This lambda should be used with a CW event

import boto3

def lambda_handler(event, context):
    
    # initialization
    ec2           = boto3.resource('ec2', region_name=event['region'])
    instance      = ec2.Instance(event['detail']['instance-id'])
    user_tags     = [ tag for tag in instance.tags if 'aws:' != tag['Key'][:4] ]
    instance_name = [ tag['Value'] for tag in instance.tags if tag['Key'] == 'Name' ][0]

    if 'ECS Instance - EC2ContainerService' in instance_name:

        # add Application tag
        user_tags.append({ 'Key': 'Application', 'Value': 'ECS' })
        
        # add Managed-By-Ansible tag
        user_tags.append({ 'Key': 'Managed-By-Ansible', 'Value': 'True' })

        # add Environment tag
        if 'Dev' in instance_name:
            user_tags.append({ 'Key': 'Environment', 'Value': 'DEV' })

        elif 'SharedServices' in instance_name:
            user_tags.append({ 'Key': 'Environment', 'Value': 'PRO' })

        elif 'Production' in instance_name:
            user_tags.append({ 'Key': 'Environment', 'Value': 'PRO' })

        # update the instance tags
        instance.create_tags(Tags=user_tags)