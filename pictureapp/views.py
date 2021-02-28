from django.shortcuts import render

from .bigquery import get_pictures


# Create your views here.
def index(request):
    """Index page view

    Args:
        request.GET['search_request'] String: search request from search string.

    Returns:
        Render: "index.html" template with "pictures"
            in context if exists.
    """

    context = {"title": "Picture Search"}
    if 'search_request' in request.GET and request.GET['search_request']:
        pictures = get_pictures(request.GET['search_request'])
        context = {
            "title": "Picture Search",
            "pictures": pictures
        }

    return render(request, 'index.html', context)
