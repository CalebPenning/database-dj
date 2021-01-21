from models import Playlist, PlaylistSong, Song, db
from app import app 

db.drop_all()
db.create_all()

p1 = Playlist(name="hangin", description="I'm hanging out.")
p2 = Playlist(name="Pumped", description="I'm amped up now.")
p3 = Playlist(name="chillin", description="I'm chillin again.")

s1 = Song(title="Numbers", artist="Young Thug")
s2 = Song(title="Silver", artist="A.G. Cook")
s3 = Song(title="March Madness", artist="Future")

db.session.add_all([p1, p2, p3])
db.session.commit()

db.session.add_all([s1, s2, s3])
db.session.commit()
