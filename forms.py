"""Forms for playlist app."""

from wtforms import SelectField, StringField, TextAreaField
from wtforms.validators import InputRequired, Length
from flask_wtf import FlaskForm


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""
    name = StringField("Name Of Playlist", validators=[InputRequired(), Length(min=1, max=100)])
    
    description = TextAreaField("Playlist Description", validators=[InputRequired(), Length(min=1, max=250)]) 


class SongForm(FlaskForm):
    """Form for adding songs."""
    title = StringField("Song Title", validators=[InputRequired(), Length(min=1, max=100)])
    
    artist = StringField("Artist Name(s)", validators=[InputRequired(), Length(min=1, max=100)])


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int, choices=[])
