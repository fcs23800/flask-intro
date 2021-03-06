from project import db
from project.models import BlogPost

# create the database and the db table
db.create_all()

# insert data
db.session.add(BlogPost("Good", "I\'m good."))
db.session.add(BlogPost("Well", "I\'m well."))
db.session.add(BlogPost("Excellent", "I\'m excellent."))
db.session.add(BlogPost("Okay", "I\'m okay."))
db.session.add(BlogPost("Flask", "Go to learningflask.com to see the magic"))
db.session.add(BlogPost("Postgres", "set up new postgresql database discover flask dev locally."))

# commit the changes
db.session.commit()