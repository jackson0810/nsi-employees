#!/usr/bin/env bash
# This script is used to provision a local development vagrant box.

echo "Updating Time Zone to America/New_York"
ln -sf /usr/share/zoneinfo/America/New_York /etc/localtime

echo "Running apt-get update and upgrade..."
apt-get -f install
apt-get update && sudo apt-get upgrade

echo "Installing required Python and other packages ..."
apt-get install -y build-essential unixodbc-dev unixodbc-bin unixodbc supervisor python3-pip python3-dev
apt-get install -y libldap2-dev libssl-dev libsasl2-dev libjpeg8-dev libjpeg62 libtiff4-dev zlib1g-dev libfreetype6-dev
apt-get install -y liblcms2-dev libwebp-dev libaio1 g++ nginx git wget curl vim zip unzip libpq-dev
apt-get install -y libmysqlclient-dev expect openssl

if [ ! -f /vagrant/requirements_installed ]
then
    echo "Installing project-specific Python packages with pip3 ..."
    cd /vagrant
    pip3 install -r requirements.txt
    touch requirements_installed
fi

echo "Installing and upgrading pip and distribute..."
/usr/bin/pip3 install -U distribute
/usr/bin/pip3 install -U pip

echo "Create en_US locale..."
locale-gen en_US
dpkg-reconfigure locales

#export SECRET_KEY='(@7o_g@c)+^$m^*802p5fd@vbe=wpw$j6u_hf^3-5=u+n%6cpx'
#export SECRET_KEY_EMPLOYEES='2s6zo@m4_slqx22q(-sm$b@ko(rho1avnxa=0!t&7j!(vtob^a'
#export DATABASE_NAME='nsilocal'
#export DATABASE_USER='nsilocal'
#export DATABASE_PASSWORD='yOmk%ix5KWy^ISlGl!4'
#export DATABASE_SERVER='localhost'

echo "Provisioning complete."

