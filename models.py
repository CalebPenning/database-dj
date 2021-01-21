"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""
    __tablename__ = 'playlists'
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    name = db.Column(db.Text,
                     nullable=False,
                     unique=False)
    
    description = db.Column(db.Text,
                            nullable=False,
                            default="No description yet.")
    
    @classmethod
    def create_playlist(cls, form):
        name = form.name.data
        description = form.description.data
        
        new_playlist = cls(name=name, description=description)
        db.session.add(new_playlist)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            form.name.errors.append('Must input a name for your playlist')


class Song(db.Model):
    """Song."""

    __tablename__ = 'songs'
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    title = db.Column(db.Text,
                      nullable=False,
                      unique=False)
    
    artist = db.Column(db.Text,
                       nullable=False,
                       unique=False,
                       default="Unknown")
    
    playlists = db.relationship('Playlist',
                                secondary='playlists_songs',
                                backref='songs')
    
    belongs_to = db.relationship('PlaylistSong',
                                 backref='song')
    
    @classmethod
    def create_song(cls, form):
        title = form.title.data
        artist = form.artist.data
        new_song = cls(title=title,
                       artist=artist)
        db.session.add(new_song)
        try:
            db.session.commit()
            
        except IntegrityError:
            db.session.rollback()
            form.title.errors.append('Must input a title for the song')


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""
    __tablename__ = 'playlists_songs'
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    playlist_id = db.Column(db.Integer,
                            db.ForeignKey('playlists.id')) 
    
    song_id = db.Column(db.Integer,
                        db.ForeignKey('songs.id'))
    
        
    


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
