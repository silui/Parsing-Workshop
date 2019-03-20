#!/usr/local/bin/bash
# LAST=$(cat $1 | head -n 1)
LAST=""
cat $1 | while read timevar rest
do
  if [ "$timevar" = "" ]
  then
    echo
    continue
  fi
  if [ "$LAST" = "" ]
  then
    LAST="$timevar $rest"
  else
    echo $LAST | awk -v time="$timevar" '{print $1"-"time" "$2}'
    LAST="$timevar $rest"
  fi
  if [ "$rest" = "End" ]
  then
    echo "$timevar $rest"
    LAST=""
  fi
done
  # echo $LAST | awk -v time="$timevar" '{print $1"-"time" "$2}'
  # LAST=$(echo $timevar $rest)
# cat $1 | tail -n 1
# echo $LAST