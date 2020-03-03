#!/bin/bash

# ATTENTION! this script deletes EC2 stuff!!!

# Get the instances with tag 'Description = Retiring'
instances=$(aws ec2 describe-instances --filters "Name=tag:Description,Values=Retiring" | jq -r .Reservations[].Instances[].InstanceId)

for instance in $instances
do  
    # Terminate
    echo "Terminating instance: $instance"
    aws ec2 terminate-instances --instance-ids $instance
done
