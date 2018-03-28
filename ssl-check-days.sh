#!/bin/sh
DATE="/bin/date"
OPENSSL="/usr/bin/openssl"
HOST=$1
PORT=$2
WARNINGDAYS=$3
RED='\033[0;31m'
NC='\033[0m' # No Color


if [ "$HOST" = "" ]; then
echo "hostname is required, yo"
    exit
fi

if [ "$PORT" = "" ]; then
    PORT="443"
fi

if [ "$WARNINGDAYS" = "" ]; then
    WARNINGDAYS="30"
fi

CMD=`echo "" | timeout 5 $OPENSSL s_client -servername $HOST -connect $HOST:$PORT 2>/dev/null | $OPENSSL x509 -enddate -noout 2>/dev/null|  sed 's/notAfter\=//'`

if [ "$CMD" != "" ]; then
    EXPIRE_DATE=`$DATE -d "$CMD" +%s`
    TIME=`$DATE +%s`
    EXPIRE_TIME=`expr $EXPIRE_DATE - $TIME`
    EXPIRE_TIME=`expr $EXPIRE_TIME / 86400`
    if [ $EXPIRE_TIME -lt $WARNINGDAYS ]; then echo "${RED}${EXPIRE_TIME} days : ${HOST}${NC}"; else echo $EXPIRE_TIME days : $HOST; fi
fi
