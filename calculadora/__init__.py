def create_dict(names,goals,goals_avoided,assists):
    """
    This function creates a dictionary 
    with each name as a key and having for values 
    a tuple with three elements: goals, goals_avoided
    and assists respectively.
    """

    players = {}

    names = names.split()
    for n, g, ga, a in zip(names,goals,goals_avoided, assists):
        players[n] = (g,ga,a)

    return players

def get_scorer(players):
    """
    This function returns a tuple with
    the name of the scorer and his/her number
    of goals 
    """

    scorers_name, goals = max(players.items(), key = lambda x : x[1][0])

    return scorers_name, goals[0]

def best_performance(players):
    """
    This function gets the most influential player
    by creating a list of tuples with each player's name
    and performance score calculated with this values:
    goals = 1.5, goals_avoided = 1.25, assists = 1
    Then it returns the name of the player 
    with the maximum performance value
    """
    performances = [(player, (values[0] * 1.5) + (values[1] * 1.25) + values[2]) for player, values in players.items()]

    top_performer = max(performances, key = lambda x : x[1])

    return top_performer[0]


def goal_average(goals):
    """
    This function returns the average of goals
    per match this season (25 matches played)
    """

    return sum(goals)/25

def get_scorer_average(players):
    """
    This function returns the goal average of the
    scorer, usig the function "get_scorer"
    """

    player = get_scorer(players)

    return player[1]/25



