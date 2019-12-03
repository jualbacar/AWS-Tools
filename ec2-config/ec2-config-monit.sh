#!/bin/bash

# Get the instances from the Environment = PRO
instances=$(aws ec2 describe-instances --filters "Name=tag:Environment,Values=PRO" | jq -r .Reservations[].Instances[].InstanceId)

for instance in $instances
do  
    # Enable detailed monitoring
    echo $instance
    aws ec2 monitor-instances --instance-id $instance 
done