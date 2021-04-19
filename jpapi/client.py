'''load resource classes'''
from .post import Post
from .comment import Comment
from .album import Album
from .photo import Photo
from .todo import Todo
from .user import User

class Client:
    '''Class for JSON Placement api client'''
    def __init__(self, entrypoint = "https://jsonplaceholder.typicode.com"):
        self.entrypoint = entrypoint
        self.posts = Post(f"{self.entrypoint}")
        self.comments = Comment(f"{self.entrypoint}")
        self.albums = Album(f"{self.entrypoint}")
        self.photos = Photo(f"{self.entrypoint}")
        self.todos = Todo(f"{self.entrypoint}")
        self.users = User(f"{self.entrypoint}")

    if "__name__" == "__main__":
        print(f"Entrypoint: {self.entrypoint}")
