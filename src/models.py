import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    password = Column(String(50), nullable=False)
    email = Column(String(250), nullable=False)
    phone = Column(String(15))
    gender = Column(String(250))

    def __repr__(self):
        return '<User %r>' % self.username

class Post(Base):
    __tablename__ = 'posts'
    # Here we define columns for the table posts
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    description = Column(String(30), nullable=False)
    icons = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    def __repr__(self):
        return '<Post %r>' % self.title


class Comment(Base):
    __tablename__ = 'comments'
    # Here we define columns for the table comment
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    comment = Column(String(65535))
    user = relationship(User)
    post = relationship(Post)

    def __repr__(self):
        return '<Comment %r>' % self.comment


class Reaction(Base):
    __tablename__ = 'reaction'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    like_count = Column(Integer, nullable=False)
    dislike_count = Column(Integer, nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id'))
    comment_id = Column(Integer, ForeignKey('comments.id'))
    post = relationship(Post)
    comment = relationship(Comment)

    def __repr__(self):
        return '<Reaction %r>' % self.id


class Follower(Base):
    __tablename__ = 'followers'
    # Here we define columns for the table [ . . . ]
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    follower_user_id = Column(Integer, ForeignKey('user.id'))
    follower = relationship(User)

    def __repr__(self):
        return '<Follower %r>' % self.id


#class Address(Base):
#    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
#    id = Column(Integer, primary_key=True)
#    street_name = Column(String(250))
#    street_number = Column(String(250))
#    post_code = Column(String(250), nullable=False)
#    person_id = Column(Integer, ForeignKey('person.id'))
#    person = relationship(Person)
#
#    def to_dict(self):
#        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
