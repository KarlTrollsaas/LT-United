#! /usr/bin/env bash
# comment: use command ./LT-Install.sh

# Install a foreign function interface, so code written in one language can call code made in other languages.
echo "*************************"
echo "* Installing libffi-dev *"
echo "*************************"
sudo apt-get install libffi-dev
echo

# Install a spesific crypthography version for compatibility reasons.
echo "*****************************************"
echo "* Installing cryptography version 2.1.4 *"
echo "*****************************************"
sudo pip install cryptography==2.1.4
echo

# Install an extention to use for voice interface to Alexa.
echo "************************"
echo "* Installing flask-ask *"
echo "************************"
sudo pip install flask-ask
echo

echo "Installation of dependencies finished!"
echo "Download ARM 32-bit version from: https://ngrok.com/download"
echo "Remember to always update the Alexa endpoint with new url from Ngrok!"
