# Stacked Up

## Do Philly students have the books they need?

Explore the textbook inventory of Philadelphia public schools and see if schools have enough reported books
to teach approved reading and math curriculum.

Note that not all schools use the school district's official system. But for those that are, what's going on in the data?

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

Your app is then accessible on `localhost:8111` (where your vagrant port was setup).

This is how you'll start the app when you want to work on it. You are now in a virtual environment, and should execute any `./manage.py` kinds of commands in here. Open another bash session to use git or other tools outside of your virtual environment.

## Contributors

[Pam Selle](http://github.com/pselle)

[Jeff Frankl](http://github.com/jfrankl)

## Thanks

This project leverages [vagrant-django-template](https://github.com/torchbox/vagrant-django-template) to get up and running quickly.

## License

Stacked Up is a web application that tracks curricula and learning
material inventory for schools and school districts.

Copyright (C) 2013 AxisPhilly

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
