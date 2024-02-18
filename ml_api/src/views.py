from django.shortcuts import render
from django.http import HttpResponse
from . import ipl

# Create your views here.
def home(request):
    return HttpResponse("Hello, world.")

def team(request):
    teams = ipl.teamAPI()
    return HttpResponse(teams)

def teamVteam(request):
    team1 = request.GET["team1"]
    team2 = request.GET["team2"]
    response = ipl.teamVteamAPI(team1, team2)
    return HttpResponse(response)

def allrecords(request):
    team = request.GET["team"]
    response = ipl.allRecord(team)
    return HttpResponse(response)
