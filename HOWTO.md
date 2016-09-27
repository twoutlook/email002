

# Email Settings

    Mail Server Username: s1@skyrock-casting.org
    
    Standard (without SSL)
    Incoming Mail Server: mail.skyrock-casting.org
    Supported Ports: 143 (IMAP), 110 (POP3)
    Outgoing Mail Server: mail.skyrock-casting.org
    Supported Port: 26 (server requires authentication)
    
    Private (with SSL)
    Incoming Mail Server: host411.hostmonster.com (SSL)
    Supported Ports: 993 (IMAP), 995 (POP3)
    Outgoing Mail Server: host411.hostmonster.com (SSL)
    Supported Port: 465 (server requires authentication)
    
    Supported Incoming Mail Protocols: POP3, IMAP
    Supported Outgoing Mail Protocols: SMTP 


# Production to backup database

# Push Production to a new Github project

# Create a new c9.io blank project and clone Github project

# Setup c9.io developing envrionment
## install Python 3.5 and venv 

    sudo apt-get -y install python3.5 python3.5-venv

## setup virtual envrionment

    python3.5 -m venv myvenv
    pip freeze
    source myvenv/bin/activate
    pip freeze
    pip install --upgrade pip
    
    pip install django
    pip install django-bootstrap3
    pip install django-import-export
    pip install django-ipware
    
    cd cloud001
    cd mysite
    cp db.sqlite3x09201033 db.sqlite3
    ./manage.py runserver $IP:$PORT
    
# On PRODUCTION, Change view context, need to restart apache
    sudo service apache2 restart


# Steps

# Clone Github project using SSH, no need to input user/pass

    git clone git@github.com:twoutlook/cloud001.git

git clone https://github.com/twoutlook/cloud001.git
Need to input user/pass

# add model Item012
# register model Item012
# migrate db

    
    ./manage.py makemigrations
    ./manage.py migrate

# prepare sample data
ensure  f12 is data format in plain text

# login to admin and import
use item012-raw-6.xls sample data to import, use 48 records, done!

# template
# view
# url






