Just a collection (yeah, ok, only one so far, shhh) of useful scripts that I want to keep hold of

ssl-check-days.sh
tells you how many days left on an SSL cert for a host
usage: 
ssl-check-days.sh hostname \[port\] \[warning days\]

port - optional - which port to check

warning days - optional - if days left > this number, the output turns red

I use it like this to check all records in an AWS Route53 zone

for I in \`aws route53 list-resource-record-sets --hosted-zone-id EXAMPLEZONEID | jq '.ResourceRecordSets | .[] | .Name' | sort | uniq | sed -e 's/\.\"//' | sed -e 's/\"//' \`; do ssl-check-days.sh ${I}; done

NB: These scripts will be crufty as hell. Probably also riddled with bugs and vulns. Feel free to use them at your own risk, but if they break shit, it's not my fault, ok?
