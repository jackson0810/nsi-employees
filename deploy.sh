#!/bin/bash

WORKDIR="/home/nsishell/"
HOMEDIR="employees.navalsystemsinc.com/"
PROJECT="nsi-employees"

cd ${WORKDIR}${HOMEDIR}

echo "Switching to the source directory for the external site..."
cd ${WORKDIR}${HOMEDIR}${PROJECT}
git pull
echo

echo "Available local and remote branches:"
git branch -a
echo

echo "Enter the branch you wish to deploy: "
read  BRANCH_NAME

if [ "${BRANCH_NAME}" == "" ]; then
    echo "No branch specified. Using master..."
    BRANCH_NAME='master'
fi

echo "Checking out ${BRANCH_NAME} ..."
git checkout ${BRANCH_NAME}
git pull
echo

echo "About to deploy the external site..."

echo "Collect static ..."
${WORKDIR}${HOMEDIR}env/bin/python3 manage.py collectstatic --noinput --settings=nsi.settings.production

echo "Installing requirements ..."
${WORKDIR}${HOMEDIR}env/bin/pip3 install -r requirements.txt

echo "Moving passenger script"
cp passenger_wsgi.py ${WORKDIR}${HOMEDIR}

echo "Restarting external site..."
touch ${WORKDIR}${HOMEDIR}tmp/restart.txt

echo "Finished deploying the external site..."

echo "Done"
