from beer.models import Beer
from brewery.models import Brewery
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render_to_response, get_object_or_404

def search(request, phrase, startswith):
    if startswith:
        found_breweries = Brewery.objects.filter(name__startswith=request.GET.get('q', phrase)).order_by('name')
    else:
        found_breweries = Brewery.objects.filter(name__contains=request.GET.get('q', phrase)).order_by('name')

    paginator = Paginator(found_breweries, 25)

    page = request.GET.get('page')
    try:
        breweries = paginator.page(page)
    except TypeError:
        breweries = paginator.page(1)
    except EmptyPage:
        breweries = paginator.page(paginator.num_pages)

    return render_to_response('brewery/list.html', {"breweries": breweries}, context_instance=RequestContext(request))


def detail(request, brewery_id):
    brewery = get_object_or_404(Brewery, pk=brewery_id)
    return render_to_response('brewery/detail.html', {'brewery': brewery}, context_instance=RequestContext(request))
