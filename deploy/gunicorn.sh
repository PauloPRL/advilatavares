#!/bin/bash
 
NAME="advilatavares" # Name of the application
DJANGODIR=/home/ubuntu/djago_projects/advilatavares # Django project directory
SOCKFILE=//home/ubuntu/djago_projects/advilatavares/deploy/gunicorn.sock # we will communicte using this unix socket
NUM_WORKERS=3 # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=advilatavares.settings # which settings file should Django use
DJANGO_WSGI_MODULE=advilatavares.wsgi # WSGI module name
 
echo "Starting $NAME as `whoami`"
 
# Activate the virtual environment
cd $DJANGODIR
workon advilatavares
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
 
# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR
 
# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
--name $NAME \
--workers $NUM_WORKERS \
--log-level=debug \
--bind=unix:$SOCKFILE