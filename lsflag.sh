#!/bin/sh

ls -lo $* | awk '{print $10, "\t", $5}'

