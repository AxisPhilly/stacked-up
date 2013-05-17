# Stacked Up

## Do Philly students have enough books?

Explore the textbook inventory of Philadelphia public schools and see if schools have enough reported books
to teach approved reading and math curriculum.

## Running locally

Getting started:

1. Download and install [VirtualBox](https://www.virtualbox.org/)
2. Download and install [Vagrant](http://www.vagrantup.com/)
3. `cd` to this repository
4. Follow the startup procedure:

        vagrant up # this will take a while your first time

        vagrant ssh # ssh into the virtual machine
        
        # then, within the SSH session:

        pip install -r requirements.txt # install the requirements, you should only have to do this the first time
          
        pg_restore -U postgres -d sdp_curricula sdp_curricula.dump # load all the datas

        ./manage.py runserver 0.0.0.0:8000 # or sdprun for a shortcut

Your app is then accessible on `localhost:8111` (where your vagrant port was setup, note that it will not be on 8000).

This is how you'll start the app when you want to work on it. You are now in a virtual environment, and should execute any `./manage.py` kinds of commands in here. Open another bash session to use git or other tools outside of your virtual environment.

## Contributors

[Pam Selle](http://github.com/pselle)

[Jeff Frankl](http://github.com/jfrankl)

## Thanks

This project leverages [vagrant-django-template](https://github.com/torchbox/vagrant-django-template) to get up and running quickly.
