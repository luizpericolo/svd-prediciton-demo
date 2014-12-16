# coding: utf-8

from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse

from forms import SVDPredictionForm

def home(request):
    form = SVDPredictionForm()
    return TemplateResponse(request, 'index.html', {'form': form})

def prediction_result(request):
    import math
    import cPickle as pickle
    import numpy as np
    from django.conf import settings

    user_id = request.POST.get('user_id', None)

    if user_id:
        user_id = int(user_id)

    unseen_movies = pickle.load(open(settings.UNSEEN_MOVIES_FILE, "rb"))

    movie_names = pickle.load(open(settings.MOVIE_TITLES_FILE, "rb"))

    prediction_matrix = np.loadtxt(settings.PREDICTION_MATRIX_FILE, delimiter=',')

    movie_ids = unseen_movies[user_id-1]

    predictions = []

    for movie_id in movie_ids:
        prediction = {
            'movie_name': movie_names[movie_id-1],
            'user_id': user_id,
        }

        prediction['score'] = math.ceil(prediction_matrix[user_id-1, movie_id-1])

        predictions.append(prediction)
           

    return TemplateResponse(request, 'results.html', {'predictions': predictions})
