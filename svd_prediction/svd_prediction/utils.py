# coding: utf-8
import numpy as np

class BaseAspectHandler():
    def __init__(self, users_path, movies_path):
        #self.user_aspects_path = users_path
        #self.movies_aspects_path = movies_path

        self._load_aspects(user_aspect_path=users_path, movie_aspect_path=movies_path)

    def _load_aspects(self, user_aspect_path, movie_aspect_path):
        import numpy as np

        self.user_aspect = np.loadtxt(user_aspect_path, delimiter=',')
        self.movie_aspect = np.loadtxt(movie_aspect_path, delimiter=',')

    def get_aspects(self):
        return self.user_aspect, self.movie_aspect


class BaseHandler():
    def __init__(self, base_path):
        self.base = np.loadtxt(base_path, delimiter=',')


    def get_unseen_movies_dict(self):
        unseen = {}
        for i, user in enumerate(self.base):
            user_unseen = []

            for j, movie in enumerate(user):
                if not movie:
                    user_unseen.append(j)

            unseen[i] = user_unseen


        return unseen
