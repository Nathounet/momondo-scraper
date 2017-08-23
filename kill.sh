#!/bin/sh

pid=`ps aux | grep main.py | grep -v grep | awk '{print $2}'`
kill $pid
