#!/bin/bash

CURDIR=`pwd`

cd API
./01-buildimage.sh
./02-runcontainer.sh

cd $CURDIR

cd GUI
./01-buildimage.sh
./02-runcontainer.sh

cd $CURDIR

