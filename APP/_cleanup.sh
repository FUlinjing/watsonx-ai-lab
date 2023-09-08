#!/bin/bash

CURDIR=`pwd`

cd ./API.en
./03-cleanup.sh

cd $CURDIR

cd ./GUI
./03-cleanup.sh

cd $CURDIR
