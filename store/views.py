# from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

from .models import Album, Artist, Contact, Booking


def index(request):
    """
    This function return the 12 albums more recent and available from db
    :param request:
    :return:
    """
    albums = Album.objects.filter(available=True).order_by('-created_at')[:12]
    context = {
        'albums': albums
    }
    return render(request, 'store/index.html', context)


def listing(request):
    albums = Album.objects.filter(available=True)
    context = {
        'albums': albums
    }
    return render(request, 'store/listing.html', context)


def detail(request, album_id):
    id = int(album_id)
    album = get_object_or_404(Album, pk=id)
    artists = [artist.name for artist in album.artists.all()]
    artists_name = " ".join(artists)
    message = "Le nom de l'album est {}. Il a été écrit par {}".format(album.title, artists)
    context = {
        'album_title': album.title,
        'artists_name': artists_name,
        'album_id': album.id,
        'thumbnail': album.picture
    }

    return render(request, 'store/detail.html', context)


def search(request):
    query = request.GET.get('query')
    # hellfest
    if not query:
        albums = Album.objects.all()
    else:
        # title contains the query is and query is not sensitive to case.
        albums = Album.objects.filter(title__icontains=query)
    if not albums.exists():
        albums = Album.objects.filter(artists__name__icontains=query)
    title = "Résultats pour la requête %s"%query
    context = {
        'albums': albums,
        'title': title
    }
    return render(request, 'store/search.html', context)