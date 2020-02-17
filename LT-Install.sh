#! /usr/bin/env bash
# comment: use command ./LT-Install.sh

echo "*************************"
echo "* Installing libffi-dev *"
echo "*************************"
sudo apt-get install libffi-dev
echo

echo "*****************************************"
echo "* Installing cryptography version 2.1.4 *"
echo "*****************************************"
sudo pip install cryptography==2.1.4
echo

echo "************************"
echo "* Installing flask-ask *"
echo "************************"
sudo pip install flask-ask
echo

echo "Next steps are to start the python program and ngrok at http port 5001"
echo "REMEMBER TO UPDATE THE ALEXA ENDPOINT WITH THE NEW URL!"
