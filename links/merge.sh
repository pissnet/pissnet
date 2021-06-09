#!/bin/sh

for f in `find hubs/ servers/ -name '*.conf'`; do
    cat $f;
    echo "\n";
done
