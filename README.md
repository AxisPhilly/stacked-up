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

The MIT License (MIT)

Copyright (c) 2013 AxisPhilly

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
