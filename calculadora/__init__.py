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







