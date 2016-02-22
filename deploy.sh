#!/bin/bash

WORKDIR="/home/nsishell/"
HOMEDIR="navalsystemsinc/"
HOMEDIR_EMPLOYEES="employees.navalsystemsinc.com/"
PROJECT="nsi"
DEPLOY_EXTERNAL='Y'
DEPLOY_INTERNAL='Y'

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

echo "Do you want to deploy the external site: (Y/n)?  The default is Yes"
read DEPLOY_EXTERNAL

echo "Do you ant to deploy the employees site: (Y/n)? The default is Yes"
read DEPLOY_INTERNAL

if [ "${DEPLOY_EXTERNAL}" == "Y" ]; then
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
fi

if [ "${DEPLOY_INTERNAL}" == "Y" ]; then
    echo "About to deploy the employees site..."

    echo "Copying files to the employees site..."
    rm -rf ${WORKDIR}${HOMEDIR_EMPLOYEES}${PROJECT}
    mkdir ${WORKDIR}${HOMEDIR_EMPLOYEES}${PROJECT}
    cp -r ${WORKDIR}/${HOMEDIR}${PROJECT}/* ${WORKDIR}${HOMEDIR_EMPLOYEES}${PROJECT}
    rm -rf ${WORKDIR}${HOMEDIR_EMPLOYEES}${PROJECT}/.git

    echo "Removing the old passenger file..."
    rm passenger_wsgi.py
    mv employees_passenger_wsgi.py passenger_wsgi.py

    echo "Collect static ..."
    ${WORKDIR}${HOMEDIR_EMPLOYEES}env/bin/python3 manage.py collectstatic --noinput --settings=nsi.settings.production_employees

    echo "Installing requirements ..."
    ${WORKDIR}${HOMEDIR_EMPLOYEES}env/bin/pip3 install -r requirements.txt

    echo "Moving passenger script"
    cp passenger_wsgi.py ${WORKDIR}${HOMEDIR_EMPLOYEES}

    echo "Restarting external site..."
    touch ${WORKDIR}${HOMEDIR_EMPLOYEES}tmp/restart.txt

    echo "Finished deploying the employee site..."
fi

echo "Done"
