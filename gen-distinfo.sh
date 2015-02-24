#!/bin/sh

md5 $1
sha256 $1
sha1 $1
echo  "SIZE ($1) = `ls -l $1 | awk '{print $5}'`"

