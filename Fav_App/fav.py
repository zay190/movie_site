from  MovieFiles.models  import Latest_movie

class Fav():

    def __init__(self,request):
        self.session = request.session

        # Get the current session Key for continuing Users
        user_sesssion = self.session.get("session_key")

        # Generating Session Key For New Users
        if "session_key" not in request.session:
            user_sesssion = self.session["session_key"] = {}

        self.user_session = user_sesssion
        
    def add(self,movie_id):
        fav_id = str(movie_id.id)

        # Get session
        update = self.user_session
        update[fav_id] = True
        self.session.modified = True
    
    def get_fav(self):
        mov_id = self.user_session.keys()

        # Use id to look up the movie in the database
        movies = Latest_movie.objects.filter(id__in = mov_id)

        return movies
    
    def delete(self,movie):
        movie_del = str(movie)

        # Deleting Id From Fav and session
        if movie_del in self.user_session:
            del self.user_session[movie_del]
            
        self.session.modified = True
