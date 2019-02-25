#!/bin/bash
while read -n 5 line; do
    echo $line
done < "$1"
