apt-get install git
apt-get install python-pip
apt-get install libtiff4-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev

echo "Configure VirutalEnvWrapper? [y/n]"
  pip install virtualenvwrapper
  echo "export WORKON_HOME=~/Envs
mkdir -p $WORKON_HOME
source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
  export WORKON_HOME=~/Envs
  mkdir -p $WORKON_HOME
  source /usr/local/bin/virtualenvwrapper.sh
fi