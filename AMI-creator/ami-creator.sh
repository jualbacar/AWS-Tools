#!/bin/bash

# Dump instances' config to be retired
aws ec2 describe-instances --filters "Name=tag:Description,Values=Retiring" > instances_retiring.json

# Get the instances with tag 'Description = Retiring'
instances=$(aws ec2 describe-instances --filters "Name=tag:Description,Values=Retiring" | jq -r .Reservations[].Instances[].InstanceId)

for instance in $instances
do  
    # Get instances' tag Name
    instance_name=$(aws ec2 describe-instances --instance-id $instance --query 'Reservations[].Instances[].Tags[?Key == `Name`].Value' |jq .[][] -r)
    # Create an AMI with Name = instance_id + instance_tag_name
    ami_id=$(aws ec2 create-image --instance-id $instance --name "$instance_name - $instance" | jq .[] -r)
    echo "CREATED AMI $ami_id for --> $instance: $instance_name - $(date "+%Y-%m-%d% - %H:%M:%S")"
done


