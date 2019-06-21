#!/usr/bin/env python

####################################################
##  Hooky script to find any classic ELBs across  ##
##  every region in your AWS account, and spit    ##
##  out commands that can be used to update said  ##
##  classic ELBs from ye olde TLS ciphers to the  ##
##  more up to date set which should only have    ##
##  TLS 1.2, because we don't need to support     ##
##  IE6 anymore - use at own risk, obviously      ##
####################################################

import boto3
import time
import re

ec2 = boto3.client('ec2')
regionlist = ec2.describe_regions()
for region in regionlist["Regions"]:
    print '#',region.get("RegionName")

    session = boto3.Session(profile_name="default", region_name=region.get("RegionName"))
    elb = session.client("elb")
    elbs = elb.describe_load_balancers()
    r = re.compile("AWSConsole-SSLNegotiationPolicy-*")

    for instance in elbs["LoadBalancerDescriptions"]:
        for listener in instance["ListenerDescriptions"]:
            if (not filter(r.match,listener.get("PolicyNames"))) and listener.get("Listener").get("Protocol") == "HTTPS":
 #               print "Probably using ye olde TLS policy?"
                print "#",instance["LoadBalancerName"] ,listener.get("Listener").get("LoadBalancerPort") , listener.get("PolicyNames")
                newPolicyName = ("MatCreated-SSLNegotiationPolicy-{}-{}".format(instance["LoadBalancerName"],str(int(time.time()))))
 #               print newPolicyName
                print "aws elb create-load-balancer-policy --load-balancer-name ", instance["LoadBalancerName"] ," --policy-name ",newPolicyName ," --policy-type-name SSLNegotiationPolicyType --policy-attributes AttributeName=Reference-Security-Policy,AttributeValue=ELBSecurityPolicy-TLS-1-2-2017-01  --region ",region.get("RegionName")
                print "aws elb set-load-balancer-policies-of-listener --load-balancer-name ", instance["LoadBalancerName"] ," --load-balancer-port ", listener.get("Listener").get("LoadBalancerPort") ," --policy-names ", newPolicyName, " --region ",region.get("RegionName")
 #               print "********************************\n\n"

