#!/bin/bash

WORKDIR="/home/nsishell/"
HOMEDIR="employees.navalsystemsinc.com/"
PROJECT="nsi-employees"
ENV_ABBR="staging"

echo "Deploy environment (Type 1=Staging or 2=Production.): "
read ENVIRONMENT

if ["${ENVIRONMENT}" == 2]; then
    HOMEDIR="n-s-i/"
    ENV_ABBR="production"
fi

cd ${WORKDIR}${HOMEDIR}

echo "Switching to the source directory for the internal site..."
cd ${WORKDIR}${HOMEDIR}${PROJECT}
git pull
echo

echo "Available local and remote branches..."
git branch -a
echo

echo "Enter the branch you wish to deploy: (Leave blank to deploy master)..."
read  BRANCH_NAME

if [ "${BRANCH_NAME}" == "" ]; then
    echo "No branch specified. Using master..."
    BRANCH_NAME='master'
fi

echo "Checking out ${BRANCH_NAME} ..."
git checkout ${BRANCH_NAME}
git pull
echo

echo "Collect static ..."
${WORKDIR}${HOMEDIR}env/bin/python3 manage.py collectstatic --noinput --settings=nsi.settings.${ENV_ABBR}

echo "Installing requirements ..."
${WORKDIR}${HOMEDIR}env/bin/pip3 install -r requirements.txt

echo "Copying ${ENV_ABBR} passenger script to ${WORKDIR}${HOMEDIR}"
cp passenger_wsgi_${ENV_ABBR}.py ${WORKDIR}${HOMEDIR}

echo "Renaming the script passenger_wsgi_${ENV_ABBR}.py to passenger_wsgi.py"
rm ${WORKDIR}${HOMEDIR}passenger_wsgi.py
mv ${WORKDIR}${HOMEDIR}passenger_wsgi_${ENV_ABBR}.py ${WORKDIR}${HOMEDIR}passenger_wsgi.py

echo "Restarting internal site..."
touch ${WORKDIR}${HOMEDIR}tmp/restart.txt

echo "Done"
