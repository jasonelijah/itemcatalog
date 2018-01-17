#Overview
This is a Video Game Item Catalog application made with Flask. It includes a few of my favorite studios. The user can add their favorite games to these studios in the front end of the application.

#Components Needed
- Virtual Box
- Vagrant
- Import Flask
- Import SQLAlchemy for database functions
- and understanding of Routes and JSON
- Uses Google Login ( ouath ) and fb connect
    - Once authenticated, user can make updates to DB via the GUI
- Front end uses Bootstrap 3.X.X for front end display


# To run the application:

1. Clone the [fullstack-nanodegree-vm repository](https://github.com/udacity/fullstack-nanodegree-vm).

2. Look for the *catalog* folder and replace it with the contents of this respository.
   (https://github.com/jasonelijah/fullstack-nanodegree-vm/tree/master/vagrant/catalog)

## Usage

Launch the Vagrant VM from inside the *vagrant* folder with:

`vagrant up`

Then access the shell with:

`vagrant ssh`

Then move inside the catalog folder:

`cd /vagrant/catalog`

To set up the database run:
`python database_setup.py`

To populate the database run:
`python lotsofgames.py`

Then run the application:

`python application.py`

Upon successful completion of the aforementioned steps you can navigate to the front end here:
`http://localhost:5000/`


Enjoy!

# License
Project is released under the [MIT License](http://opensource.org/licenses/MIT).
