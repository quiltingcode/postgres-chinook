from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# link python file to chinook db, through
# # an engine
db = create_engine("postgresql:///chinook")

# Create a metadata class variable
meta = MetaData(db)

# Create variable to build tables
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer)
)

# Make the connection
with db.connect() as connection: