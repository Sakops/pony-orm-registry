from pony.orm import Database, PrimaryKey, Required, db_session
from text import commands

db = Database(provider='sqlite', filename='database.db', create_db=True)


class Post(db.Entity):
    _table_ = "Posts"
    id = PrimaryKey(int, auto=True)
    header = Required(str)
    content = Required(str)


db.generate_mapping(create_tables=True)

while True:
    c = input(commands)
    if c == "c":
        header = input("enter header: ")
        content = input("enter content: ")
        with db_session:
            post = Post(header=header, content=content)
            db.commit()
            print(Post[post.id].id)
            print(Post[post.id].header)
            print(Post[post.id].content)
    elif c == "ro":
        id = int(input("enter id: "))
        with db_session:
            print(Post[id].to_dict())
    elif c == "ra":
        with db_session:
            posts = Post.select()
            for post in posts:
                print(post.to_dict())
    elif c == "d":
        id = int(input("enter id: "))
        with db_session:
            Post[id].delete()
    elif c == "u":
        id = int(input("enter id: "))
        header = input("enter header: ")
        content = input("enter content: ")
        with db_session:
            post = Post[id]
            post.header = header
            post.content = content
            db.commit()
            print(post.to_dict())
    elif c == "q":
        break

# with db_session:
#     post = Post(header="Python", content="Some text about Python")
#     db.commit()
