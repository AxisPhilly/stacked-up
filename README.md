This project uses vagrant-django-template. 

=======================

Getting started:

1. Download and install VirtualBox
2. Download and install Vagrant
3. `cd` to this repository
4. Follow the startup procedure:

	vagrant up # this will take a while your first time

    vagrant ssh # ssh into the virtual machine

    pip install -r requirements.txt # install the requirements, you should only have to do this the first time

    (then, within the SSH session:)
      
    ./manage.py runserver 0.0.0.0:8000

Your app is then accessible on `localhost:8111` (where your vagrant port was setup, note that it will not be on 8000).

This is how you'll start the app when you want to work on it. You are now in a virtual environment, and should execute any `./manage.py` kinds of commands in here. Open a separate tab to use git or other tools outside of your virtual environment.

Restore the database: `pg_restore -U postgres -d sdp_curricula sdp_curricula.dump`
