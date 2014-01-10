from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Category, UserScore


def competition_detail(request):
    return render_to_response('leaderboards/competition_detail.html',
                              {'selected_item': "details"},
                              context_instance=RequestContext(request))


def show_leaderboard(request, category):
    category = Category.objects.get(name=category)
    teams = UserScore.objects.filter(category=category)
    teams = sorted(teams, key=lambda t: t.max_score, reverse=True)
    return render_to_response('leaderboards/leaderboard.html',
                              {'teams': teams, 'selected_item': category.name},
                              context_instance=RequestContext(request))
