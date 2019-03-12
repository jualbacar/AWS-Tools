#!/bin/bash

keys=$(aws ec2 describe-tags --filters "Name=resource-id,Values=$2" --profile=$1 | jq -r '.[]|.[].Key')

echo "$keys" | while read -r key
do
    if [ "$key" != "Name" ]
    then
        value=$(aws ec2 describe-tags --filters "Name=resource-id,Values=$2" "Name=key,Values=$key" --profile=$1|jq -r '.[]|.[].Value')
        aws ec2 create-tags --resource $3 --tags Key="$key",Value="'$value'" --profile=$1
        echo "Writing tag " "$key" "$value"
    fi
done
