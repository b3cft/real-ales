from brewery.models import Brewery
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render_to_response, get_object_or_404

def search(request, phrase, startswith):
    q = request.GET.get('q', phrase)
    if startswith:
        if q == '-':
            found_breweries = Brewery.objects.filter(name__regex=r'^[^a-zA-Z]').order_by('name')
        else:
            found_breweries = Brewery.objects.filter(name__istartswith=q).order_by('name')
    else:
        found_breweries = Brewery.objects.filter(name__contains=q).order_by('name')

    paginator = Paginator(found_breweries, 25)

    page = request.GET.get('page')
    try:
        breweries = paginator.page(page)
    except TypeError:
        breweries = paginator.page(1)
    except EmptyPage:
        breweries = paginator.page(paginator.num_pages)

    return render_to_response('brewery/list.html', {"breweries": breweries}, context_instance=RequestContext(request))


def detail(request, pk, name):
    brewery = get_object_or_404(Brewery, pk=pk)
    return render_to_response('brewery/detail.html', {'brewery': brewery}, context_instance=RequestContext(request))
