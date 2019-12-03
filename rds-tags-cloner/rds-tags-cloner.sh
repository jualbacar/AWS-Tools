#!/bin/bash

keys=$(aws rds list-tags-for-resource --resource-name $1 | jq -r '.[]|.[].Key')

# Extract tags from DB instance
aws rds list-tags-for-resource --resource-name $1 --generate-cli-skeleton >> tags.json

# Add tags to destination
aws rds add-tags-to-resource --resource-name $2 --cli-input-json file://tags.json

# echo "$keys" | while read -r key
# do
#     if [ "$key" != "Name" ]
#     then
#         value=$(aws ec2 describe-tags --filters "Name=resource-id,Values=$2" "Name=key,Values=$key" --profile=$1|jq -r '.[]|.[].Value')
#         aws ec2 create-tags --resource $3 --tags Key="$key",Value="'$value'" --profile=$1
#         echo "Writing tag " "$key" "$value"
#     fi
# done

