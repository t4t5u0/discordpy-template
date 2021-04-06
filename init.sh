#!/bin/bash

which python >/dev/null 2>&1
if [ $? = 0 ]; then
    echo "ok"
else
    echo "you need to install python3"
    exit 1
fi

which pip >/dev/null 2>&1
if [ $? = 0 ]; then
    echo "ok"
else
    echo "you need to install pip"
    exit 1
fi

pip install -r ./requirements.txt
if [ $? = 0 ]; then
    echo "ok"
else
    echo "you failed `pip install -r requirements.txt`"
    exit 1
fi