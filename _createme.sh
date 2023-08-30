#!/bin/bash

CURDIR=`pwd`

./_verify.sh
if [[ .$?. != .0. ]]; then
	exit 1
fi


cd API
./01-buildimage.sh
./02-runcontainer.sh

cd $CURDIR

cd GUI
./01-buildimage.sh
./02-runcontainer.sh

cd $CURDIR

