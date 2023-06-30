from models import Pet, Story, db

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add stories
whiskey = Pet(name='Whiskey', species="dog")
bowser = Pet(name='Bowser', species="dog", hunger=10)
spike = Pet(name='Spike', species="porcupine")

# Add stories
momo = Story(title='momomo')
kin = Story(title='kintaro')
ura = Story(title='urashima')

# Add new objects to session, so they'll persist
db.session.add(whiskey)
db.session.add(bowser)
db.session.add(spike)

db.session.add(momo)
db.session.add(kin)
db.session.add(ura)

# Commit--otherwise, this never gets saved!
db.session.commit()