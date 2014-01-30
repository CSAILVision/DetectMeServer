from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from .models import Category, UserScore, Performance


def competition_detail(request):
    return render_to_response('leaderboards/competition_detail.html',
                              {'selected_item': "details"},
                              context_instance=RequestContext(request))


def show_leaderboard(request, category):
    category = Category.objects.get(name=category)
    teams = UserScore.objects.filter(category=category)
    teams = sorted(teams, key=lambda t: t.best_performance.average_precision, reverse=True)
    return render_to_response('leaderboards/leaderboard.html',
                              {'teams': teams, 'selected_item': category.name},
                              context_instance=RequestContext(request))

@login_required
def submissions(request):
    user = request.user.get_profile()
    performances = Performance.objects.filter(detector_author=user)
    return render_to_response('leaderboards/submissions.html',
                              {'performances': performances, 'selected_item': "submissions"},
                              context_instance=RequestContext(request))

