# AWS-Tools

EC2-TAGS-CLONE

This script copy all tags and his values from an origin instance to a destination instance, excep the tag 'Name'. The script should be used with your aws cli credential files, so obviusly you have to have installed the aws cli. The ouput of the script should be the tags with his values.

```./ec2-tags-cloner.sh [profile] [id instancia origen] [id instancia destino]```

Example: ```./ec2-tags-cloner.sh serunion i-039d5bcd4554213b6 i-0a77b6800ce1c6aea```
