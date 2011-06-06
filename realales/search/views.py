from beer.models import Beer
from django.db.models import Q
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render_to_response


def search(request, phrase):
    q = request.GET.get('q', phrase)
    found_beers = Beer.objects.filter(
                            Q(brewery__name__icontains=q) |
                            Q(name__icontains=q))
    paginator = Paginator(found_beers, 25)

    page = request.GET.get('page')
    try:
        beers = paginator.page(page)
    except TypeError:
        beers = paginator.page(1)
    except EmptyPage:
        beers = paginator.page(paginator.num_pages)

    return render_to_response('search/results.html', {"beers": beers, "phrase":q}, context_instance=RequestContext(request))