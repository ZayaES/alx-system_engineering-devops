#!/usr/bin/bash
# prints only the size of the file

curl -s -o /dev/null -w %{size_download} "$1"
echo
