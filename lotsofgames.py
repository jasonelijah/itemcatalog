from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, CategoryItem, Base, User


engine = create_engine('sqlite:///gamelibrarywithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user to associate inital entries
User1 = User(name="Thomas Anderson", email="neo@thematrix.com",
             picture='https://pbs.twimg.com/profile_images/3175751382/dd31d2dd156204fcf9b6aa1c54455adb_400x400.gif')
session.add(User1)
session.commit()

# Games for 343 Industries
category1 = Category(user_id=1, name="343 Industries")

session.add(category1)
session.commit()

game1 = CategoryItem(user_id=1, name="Halo 4", description="Halo 4's story follows a cybernetically enhanced human supersoldier, Master Chief, and his artificial intelligence construct Cortana, as they encounter unknown threats while exploring an ancient civilization's planet.", category=category1)

session.add(game1)
session.commit()


game2 = CategoryItem(user_id=1, name="Halo 5: Guardians", description="The game's plot follows two fireteams of human supersoldiers: Blue Team, led by Master Chief, and Fireteam Osiris, led by Spartan Locke.", category=category1)

session.add(game2)
session.commit()

game3 = CategoryItem(user_id=1, name="Halo: The Master Chief Collection", description="The collection consists of Halo: Combat Evolved Anniversary, Halo 2: Anniversary, Halo 3, and Halo 4, which were originally released on earlier Xbox platforms", category=category1)

session.add(game3)
session.commit()


# Games for BioWare
category2 = Category(user_id=1, name="BioWare")

session.add(category2)
session.commit()


game1 = CategoryItem(user_id=1, name="Mass Effect", description="Mass Effect is a science fiction action role-playing third-person shooter video game series developed by the Canadian company BioWare", category=category2)

session.add(game1)
session.commit()

game2 = CategoryItem(user_id=1, name="Dragon Age",
                     description="Dragon Age is a high fantasy role-playing video game series created by BioWare.", category=category2)

session.add(game2)
session.commit()


# Games for Ubisoft
category3 = Category(user_id=1, name="Ubisoft")

session.add(category3)
session.commit()

game1 = CategoryItem(user_id=1, name="Splinter Cell Blacklist", description="The protagonist, Sam Fisher, is a highly trained agent of a fictional black-ops sub-division within the NSA, dubbed Third Echelon", category=category3)

session.add(game1)
session.commit()

game2 = CategoryItem(user_id=1, name="Far Cry 4", description="The main story follows Ajay Ghale, a young Kyrati-American, as he is caught in a civil war involving Kyrat's Royal Army, controlled by tyrannical king Pagan Min, and a rebel movement called the Golden Path.", category=category3)

session.add(game2)
session.commit()

category4 = Category(user_id=1, name="EA")
session.add(category4)
session.commit()

print "added Neo's favorite games! EA gets no items because they love lootboxes :p"
