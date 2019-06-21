#!/bin/bash

## loop through all subnets which give a public IPv4 address to new instances, and update that setting to not do that.
## script works across all regions, because that's the way I wrote it.

for region in `aws ec2 describe-regions --output text | cut -f3` ; do aws ec2 describe-subnets --region ${region} | jq -r '.Subnets[] | select(.MapPublicIpOnLaunch==true) | .SubnetId = "aws ec2 modify-subnet-attribute --subnet-id \(.SubnetId) --no-map-public-ip-on-launch --region=\(.AvailabilityZone[:-1])" | .SubnetId' ; done

