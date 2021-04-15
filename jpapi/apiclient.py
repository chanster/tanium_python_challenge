from .post import Post
from .comment import Comment
from .album import Album

class ApiClient:

    def __init__(self, entrypoint = "https://jsonplaceholder.typicode.com"):
        self.entrypoint = entrypoint
        self.posts = Post(f"{self.entrypoint}")
        self.comments = Comment(f"{self.entrypoint}")
        self.albums = Album(f"{self.entrypoint}")
    
    if "__name__" == "__main__":
        print(f"Entrypoint: {entrypoint}")
