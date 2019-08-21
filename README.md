# AWS-Tools

Remember, these scripts should be run with your aws cli credential files, so obviusly you have to have installed the aws cli

EC2-TAGS-CLONE

This script copy all tags and his values from an origin instance to a destination instance, excep the tag 'Name'. The ouput of the script should be the tags with his values.

```./ec2-tags-cloner.sh [profile] [id instancia origen] [id instancia destino]```

Example: ```./ec2-tags-cloner.sh serunion i-039d5bcd4554213b6 i-0a77b6800ce1c6aea```


GETBUCKETINFO

This script outputs a summary of all buckets of an account, showing the total size and the lifecycle policy configured.

```./getinfobucket.sh```

Output:

```yourappelb-exported-logs: 0.00826002 GB - The lifecycle configuration does not exist

yourapp-logs: 69.8013 GB
[
  {
    "Rules": [
      {
        "Expiration": {
          "Days": 380
        },
        "ID": "Expire logs",
        "Status": "Enabled"
      }
    ]
  }
]

yourapp-ses: 1.05527 GB - The lifecycle configuration does not exist

yourapp-terraform-state: 1.08616 GB - The lifecycle configuration does not exist
