#First Find
# Author: LT 'syreal' Jones

# Description
# Unzip this archive and find the file named 'uber-secret.txt'
# Download zip file

mkdir tmp
cd tmp
wget https://artifacts.picoctf.net/c/502/files.zip
unzip *
cd files
grep -r 'picoCTF'