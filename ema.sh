#!/bin/bash
DOWNLOAD_DIRECTORY="/home/ema90/Escritorio/Git"
TAR_FILE="Git.tar.gz"
DATE=`date +"%d_%m_%Y"`
OTHER_DEVICE="/home/ema90/Escritorio/datos git/"

cd /home/ema90/Escritorio/

tar -czvf $DATE$TAR_FILE $DOWNLOAD_DIRECTORY
mv $DATE$TAR_FILE $OTHER_DEVICE

