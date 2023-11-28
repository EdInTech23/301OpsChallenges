#!/bin/bash

# defining source and destination filenames
src_file="/var/log/syslog"
current=$(date +"%Y-%m-%d-%H:%M:%S")
dest_file="/home/edintech/Desktop/syslog-$current"

# copy syslog file to current working directory with timestamp
cp $src_file $dest_file

echo "Log file copied to: $dest_file"