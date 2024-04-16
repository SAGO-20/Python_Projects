
preference_dict = {}

def generatePreferences(values):
    """
    This function returns a dictionary whose key value represents agents and 
    the values are lists that correspond to the preference orderings of those agents.

    Parameters:
        values: A worksheet corresponding to an xlsx file

    Returns:
        preference_dict: A dictionary where keys are the agents and values are the list corresponding 
                 preference orderings of those agents.
    """
    for row in range(1,values.max_row + 1):
        # Using Nested loops to store the values from the file to the temp_dict
        temporary_dict = {}
        sorting_list = []
        temp_list = []
        temporary_dict[row] = []
        for col in range(1,values.max_column +1):
            temporary_dict[row].append(values.cell(row,col).value)
        for agents,preference_values in enumerate(temporary_dict[row],start = 1):
            sorting_list.append((agents,preference_values))

        #sorting the the agents preferences
        sorting_list.sort(key = lambda x: (x[1],x[0]),reverse = True)
        for y in sorting_list:
            temp_list.append(y[0])
        preference_dict.update({row:temp_list})
    return preference_dict

def dictatorship(preferenceProfile, agent):
    """
    This function will return the winner alternative by dictator rules.

    Parameters:
        preferenceProfile (dict) : A dictionary containing agent number along with their list of preferences.

        agent (int) : agent number

    Returns:
        winner (int) : It returns the winner alternative.
    
    """
    try:
        winner = preferenceProfile[agent][0]
        return winner
    except KeyError:
        print('Please enter a valid agent number')

def TieBreak(preferences,maximum_preference,tieBreak):
    """"
    This function will use in case of tie-break between winning alternatives.

    Parameters:
        preferences (dict): A dictionary containing agent number along with their list of preferences.

        maximum_preference (list) : list of possible winner alternatives

        tieBreak: 'max', 'min' or agent number (an integer between 1 and n)
    
    Raises:
        KeyError: The error will be raised when the wrong agent number is provided

    Returns:
        winner (int) : winner alternative

    """
    if tieBreak == "max":
        # In this case the alternative with highest number will be selected
        winner = max(maximum_preference)
        return winner

    elif tieBreak == "min"  :
        # In this case the alternative with the lowest number will be selected
        winner = min(maximum_preference)
        return winner

    else:
        agent = tieBreak
        # In this case the alternative that agent ranks the highest will be selected
        try:
            agent = tieBreak
            expected_winner_list = preferences[agent]
            for winner in expected_winner_list:
                if winner in maximum_preference:
                    return winner
                    break
        except KeyError:
            # This message will be printed in case the agent number doesn't exist
                print('No agent of that number')

def plurality(preferences,tieBreak):
    """
    This Function will return the alternative that appears the most times in the first position of the agents' preference orderings.
    In the case of tie, tie breaking rules will be used to select the single winner
    
    Parameters:
        preferences (dict) : A dictionary containing agent number along with their list of preferences.

        tieBreak ('max', 'min', integer between 1 and n) : determines the winner in case of tie break
    
    Returns :
        winner (int):  It returns the winner alternative.
    
    """
    test_dict = {}
    count_pref = {}

    for x,y in preferences.items():
        test_dict[x] = y[0]

    for a,b in test_dict.items():
        if b in count_pref.keys():
            count_pref[b] += 1
        else:
            count_pref[b] = 1

    maximum_preference = [key for key,value in count_pref.items() if value == max(count_pref.values())]

    if len(maximum_preference) > 1:
        # In this case the winner is selcted using the tie breaking rule
        winner = TieBreak(preferences,maximum_preference,tieBreak)
    else:
        winner = maximum_preference[0]
    return winner

def veto(preferences,tieBreak):
    """
    This Function will return the winner where every agent assigns 0 points to the alternative that they rank in the last place of their preference orderings, and 1 point to every other alternative.
    The winner is the alternative with the most number of points.
    In the case of a tie, use a tie-breaking rule to select a single winner.

    Parameters:
        preferences (dict): A dictionary containing agent number along with their list of preferences.

        tieBreak ('max', 'min', integer between 1 and n): determines the winner in case of tie break.
    
    Returns:
        winner (int):  It returns the winner alternative.

    """
    possible_winners = []
    winner_count = {}

    for x,y in preferences.items():
        for a in range(len(preferences[x])-1):
            possible_winners.append(preferences[x][a])

    for x in possible_winners:
        if x in winner_count.keys():
            winner_count[x] += 1
        else:
            winner_count[x] = 1

    maximum_preference = [key for key, value in winner_count.items() if value == max(winner_count.values())]

    if len(maximum_preference) > 1:
        # In this case the winner is selcted using the tie breaking rule
        winner = TieBreak(preferences,maximum_preference,tieBreak)
    else:
        winner = maximum_preference[0]
    return winner
    
def borda(preferences,tieBreak):
    """
    This Function will return the winner where every agent assigns a score of  to the their least-preferred alternative (the one at the bottom of the preference ranking),
    a score of  to the second least-preferred alternative, ... , and a score of  to their favourite alternative.
    In other words, the alternative ranked at position j receives a score of m-j.The winner is the alternative with the highest score.
    In the case of a tie, use a tie-breaking rule to select a single winner.

    Parameters:
        preferences (dict): A dictionary containing agent number along with their list of preferences.

        tieBreak ('max', 'min', integer between 1 and n): determines the winner in case of tie break.
    
    Returns:
        winner (int):  It returns the winner alternative.

    """
    possible_winners = {}

    for x in preferences.keys():
        points = 4
        for a in range(len(preferences[x])):
            if preferences[x][a] in possible_winners.keys():
                possible_winners[preferences[x][a]] += points
            else:
                possible_winners[preferences[x][a]] = points
            points -= 1

    maximum_preference = [key for key, value in possible_winners.items() if value == max(possible_winners.values())]

    if len(maximum_preference) > 1:
        # In this case the winner is selcted using the tie breaking rule
        winner = TieBreak(preferences,maximum_preference,tieBreak)
    else:
        winner = maximum_preference[0]
    return winner

def harmonic(preferences,tieBreak):
    """
    This function will return the winner where every agent assigns a score of 1/m to the their least-preferred alternative (the one at the bottom of the preference ranking), 
    a score of 1/(m-1) to the second least-preferred alternative, ... ,and a score of  to their favourite alternative.
    In other words, the alternative ranked at position j receives a score of 1/j .
    The winner is the alternative with the highest score. 
    In the case of a tie, use a tie-breaking rule to select a single winner.

    Parameters:
        preferences (dict): A dictionary containing agent number along with their list of preferences.

        tieBreak ('max', 'min', integer between 1 and n): determines the winner in case of tie break.
    
    Returns:
        winner (int):  It returns the winner alternative.

    """
    possible_winners = {}

    for x in preferences.keys():
        for a in range(len(preferences[x])):
            if preferences[x][a] in possible_winners.keys():
                possible_winners[preferences[x][a]] += 1/(a+1)
            else:
                possible_winners[preferences[x][a]] = 1/(a+1)

    maximum_preference = [key for key, value in possible_winners.items() if value == max(possible_winners.values())]

    if len(maximum_preference) > 1:
        # In this case the winner is selcted using the tie breaking rule
        winner = TieBreak(preferences,maximum_preference,tieBreak)
    else:
        winner = maximum_preference[0]
    return winner

def STV(preferences,tieBreak):
    """
    In this function the voting rules works in rounds, where in each round the alternatives that appear the least frequently in the first position of agents' rankings are removed, 
    and the process is repeated.When the final set of alternatives is removed (one or possibly more), then this last set is the set of possible winners.
    If there are more than one, a tie-breaking rule is used to select a single winner.

    Parameters:
        preferences (dict): A dictionary containing agent number along with their list of preferences.

        tieBreak ('max', 'min', integer between 1 and n): determines the winner in case of tie break.
    
    Returns:
        winner (int):  It returns the winner alternative.

    """
    first_choice_counter = []

    while len(preferences[1]) > 1:
        no_condidates = len(preferences[1])
    
        for x, y in preferences.items():
            for a in range(0,1):
                first_choice_counter.append(preferences[x][a])

        preference_counter = [(i, first_choice_counter.count(i)) for i in preferences[1]]

        minimum = [x[0] for x in preference_counter if x[1] == min(preference_counter,key = lambda y : y[1])[1]]

        if len(minimum) != no_condidates:
            for y in preferences.values():
                for x in minimum:
                    y.remove(x)
        else:
            break

    winner_candidates = preferences[1]

    if len(winner_candidates) > 1:
        # In this case the winner is selcted using the tie breaking rule
        winner = TieBreak(preferences,winner_candidates,tieBreak)
    else:
        winner = winner_candidates[0]
    return winner

def rangeVoting(values,tieBreak):
    """
    This function return the alternative that has the maximum sum of valuations, i.e., the maximum sum of numerical values in the xlsx file, 
    using the tie-breaking option to distinguish between possible winners.

    Parameters:
        values : A worksheet corresponding to an xlsx file.

        tieBreak ('max', 'min', integer between 1 and n): determines the winner in case of tie break.
    
    Returns:
        winner (int):  It returns the winner alternative.

    """

    temp_dict = {}

    for col in range(1,values.max_column+1):
      total_sum = 0
      temp_dict[col] = []
      for row in range(1,values.max_row + 1):
        total_sum += values.cell(row,col).value
        temp_dict[col] = total_sum

    maximum_alternative = [key for key, value in temp_dict.items() if value == max(temp_dict.values())]

    if len(maximum_alternative) > 1:
        # In this case the winner is selcted using the tie breaking rule
        preferences = generatePreferences(values)
        winner = TieBreak(preferences,maximum_alternative,tieBreak)
    else:
        winner = maximum_alternative[0]
    return winner

def scoringRule(preferences,scoreVector,tieBreak):
  """
  For every agent, the function assigns the highest score in the scoring vector to the most preferred alternative of the agent, 
  the second highest score to the second most preferred alternative of the agent and so on, 
  and the lowest score to the least preferred alternative of the agent. In the end, it returns the alternative with the highest total score, 
  using the tie-breaking option to distinguish between alternatives with the same score.

   Parameters:
        preferences (dict): A dictionary containing agent number along with their list of preferences.

        scoreVector (list): a list of length m containing positive floating alternative

        tieBreak ('max', 'min', integer between 1 and n): determines the winner in case of tie break.
    
    Returns:
        winner (int):  It returns the winner alternative.
  """
  possible_winners = {}

  try:
    for x,y in preferences.items():
      scoreVectorcopy = scoreVector.copy()
      for a in range(len(preferences[x])):
        if len(scoreVector) != len(preferences[x]):
          raise Exception
        else:
          if preferences[x][a] in possible_winners.keys():
            possible_winners[preferences[x][a]] += max(scoreVectorcopy)
          else:
            possible_winners[preferences[x][a]] = max(scoreVectorcopy)
          scoreVectorcopy.remove(max(scoreVectorcopy)) 
   
    maximum_preference = [key for key, value in possible_winners.items() if value == max(possible_winners.values())]

    if len(maximum_preference) > 1:
        # In this case the winner is selcted using the tie breaking rule
        winner = TieBreak(preferences,maximum_preference,tieBreak)
    else:
        winner = maximum_preference[0]
    return winner

  except Exception:
    # The message will be printed in case the length of scoring vector is not m.
    print('Incorrect Input')
    return False






