import pandas as pd
import numpy as np
import json


ipl_matches = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRy2DUdUbaKx_Co9F0FSnIlyS-8kp4aKv_I0-qzNeghiZHAI_hw94gKG22XTxNJHMFnFVKsO4xWOdIs/pub?gid=1655759976&single=true&output=csv"
matches = pd.read_csv(ipl_matches)


def teamAPI():
    teams = set(list(matches["Team1"]) + list(matches["Team2"]))
    return json.dumps({"toal teams": str(teams)}, indent=6, sort_keys=True)


def teamVteamAPI(team1, team2):
    team_df = matches[
        ((matches["Team1"] == team1) & (matches["Team2"] == team2))
        | ((matches["Team1"] == team2) & (matches["Team2"] == team1))
    ]
    total = team_df.shape[0]
    try:
        matches_won_team1 = team_df["WinningTeam"].value_counts()[team1]
        matches_won_team2 = team_df["WinningTeam"].value_counts()[team2]
        draw = total - (matches_won_team1 + matches_won_team2)
        response = {
            "total_matches": str(total),
            team1: str(matches_won_team1),
            team2: str(matches_won_team2),
            "draws": str(draw),
        }
        return json.dumps(response)
    except KeyError:
        return {"message": "No match have been played between these two teams"}


def allRecord(team):
    df = matches[(matches["Team1"] == team) | (matches["Team2"] == team)]
    mp = df.shape[0]
    won = df[df.WinningTeam == team].shape[0]
    nr = df[df.WinningTeam.isnull()].shape[0]
    loss = mp - won - nr
    nt = df[(df.MatchNumber == "Final") & (df.WinningTeam == team)].shape[0]
    return json.dumps({"matchesplayed": mp, "won": won, "loss": loss, "noResult": nr, "title": nt})
