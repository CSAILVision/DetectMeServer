from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Category, UserScore


def competition_detail(request):
    categories = Category.objects.all()
    return render_to_response('leaderboards/competition_detail.html',
                              {"categories": categories},
                              context_instance=RequestContext(request))


def show_leaderboard(request, category):
    categories = Category.objects.all()
    category = Category.objects.get(name=category)
    teams = UserScore.objects.filter(category=category)
    teams = sorted(teams, key=lambda t: t.max_score, reverse=True)
    return render_to_response('leaderboards/leaderboard.html',
                              {"teams": teams, "category": category,
                               "categories": categories},
                              context_instance=RequestContext(request))
