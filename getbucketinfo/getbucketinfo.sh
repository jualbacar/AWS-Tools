#!/bin/bash

nolifecycle="The lifecycle configuration does not exist"

for bucket in $(aws s3 ls | awk '{print $3}')
do
        # get bucket size, it could take a while
        size=$(aws s3 ls s3://$bucket --recursive | grep -v -E "(Bucket: |Prefix: |LastWriteTime|^$|--)" | awk 'BEGIN {total=0}{total+=$3}END{print total/1024/1024/1024" GB"}')

        # get bucket policy
        lifecycle=$(aws s3api get-bucket-lifecycle --bucket $bucket 2> /dev/null)

        # format output with size and lifecyle policies
        if [ -z "$lifecycle" ];
        then
            echo -e "\n\e[4m$bucket\e[0m: $size - $nolifecycle"
        else
            echo -e "\n\e[4m$bucket\e[0m: $size"
            echo $lifecycle | jq -s .
        fi
done
