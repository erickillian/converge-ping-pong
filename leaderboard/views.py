from django.shortcuts import render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from leaderboard.models import Match, Player, PlayerRating
from leaderboard.forms import MatchForm, PlayerForm

import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers


def home_page(request):
    """Render view for home page."""
    recent_matches = Match.get_recent_matches(num_matches=20)
    rated_players = PlayerRating.objects.all().order_by('-rating')
    ranked_players = [player for player in rated_players if player.games_played >= 5]
    unranked_players = [player for player in rated_players if player.games_played < 5]
    num_ranked_players = len(ranked_players)
    match_form = MatchForm()
    player_form = PlayerForm()
    if request.method == 'POST':
        if 'winner' in request.POST:  # only occurs for match submissions
            match_form = MatchForm(request.POST)
            if match_form.is_valid():
                match_form.save()
                return redirect('/')
        elif 'first_name' in request.POST:  # only occurs for player submissions
            player_form = PlayerForm(request.POST)
            if player_form.is_valid():
                player_form.save()
                return redirect('/')

    if num_ranked_players >= 3:
        top_three_names = [player.player.full_name for player in ranked_players[:3]]
        top_three_scores = [player.rating for player in ranked_players[:3]]
    else:
        top_three_names = None
        top_three_scores = None


    names = [player.player.full_name for player in ranked_players]
    scores = [player.rating for player in ranked_players]
        
    return render(
        request,
        'home.html',
        context={
            'recent_matches': recent_matches,
            'match_form': match_form,
            'player_form': player_form,
            'ranked_players': ranked_players,
            'unranked_players': unranked_players,
            'num_ranked_players': num_ranked_players,
            'top_three_names': top_three_names,
            'top_three_scores': top_three_scores,
            'names': names,
            'scores': scores,
        }
    )


def add_match(request):
    match_form = MatchForm()

    if request.method == 'POST':
        if 'winner' in request.POST:  # only occurs for match submissions
            match_form = MatchForm(request.POST)
            if match_form.is_valid():
                match_form.save()
                return redirect('/')
        elif 'first_name' in request.POST:  # only occurs for player submissions
            player_form = PlayerForm(request.POST)
            if player_form.is_valid():
                player_form.save()
                return redirect('/')

    return render(
        request,
        'add_match.html',
        context={
            'match_form': match_form,
        }
    )

def add_player(request):
    player_form = PlayerForm()

    if request.method == 'POST':
        if 'winner' in request.POST:  # only occurs for match submissions
            match_form = MatchForm(request.POST)
            if match_form.is_valid():
                match_form.save()
                return redirect('/')
        elif 'first_name' in request.POST:  # only occurs for player submissions
            player_form = PlayerForm(request.POST)
            if player_form.is_valid():
                player_form.save()
                return redirect('/')


    return render(
        request,
        'add_player.html',
        context={
            'player_form': player_form,
        }
    )


def all_matches(request):
    """Render page to view all matches."""
    all_matches = Match.objects.all().order_by('-datetime')
    paginator = Paginator(all_matches, per_page=50)
    page = request.GET.get('page')
    try:
        matches = paginator.page(page)
    except PageNotAnInteger:  # occurs when no page is passed through
        matches = paginator.page(1)
    except EmptyPage:  # occurs when page is out of range
        matches = paginator.page(paginator.num_pages)  # deliver last page of results
    return render(
        request,
        'all_matches.html',
        context={
            'matches': matches
        }
    )

def view_player(request, pk):
    """Render an individual player view"""
    player = Player.objects.get(pk=pk)
    player_rating = PlayerRating.objects.get(player=player)

    return render(
        request,
        'view_player.html',
        context={
            'player': player,
            'player_rating': player_rating,
        }
    )
