from beer.models import Beer
from brewery.models import Brewery
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render_to_response, get_object_or_404

def list(request):
    if request.GET.get('q'):
        all_breweries = Brewery.objects.filter(name__contains=request.GET.get('q'))
    else:
        all_breweries = Brewery.objects.all()
        
    paginator = Paginator(all_breweries, 25)

    page = request.GET.get('page')
    try:
        breweries = paginator.page(page)
    except TypeError:
        breweries = paginator.page(1)
    except EmptyPage:
        breweries = paginator.page(paginator.num_pages)

    return render_to_response('brewery/list.html', {"breweries": breweries})

def search(request):
    found_breweries = Brewery.objects.filter(name__contains=request.GET.get('q'))
    paginator = Paginator(found_breweries, 25)

    page = request.GET.get('page')
    try:
        breweries = paginator.page(page)
    except TypeError:
        breweries = paginator.page(1)
    except EmptyPage:
        breweries = paginator.page(paginator.num_pages)

    return render_to_response('brewery/list.html', {"breweries": breweries})


def detail(request, brewery_id):
    brewery = get_object_or_404(Brewery, pk=brewery_id)
    return render_to_response('brewery/detail.html', {'brewery': brewery})
