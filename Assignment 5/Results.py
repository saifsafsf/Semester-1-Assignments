def input_results(rem_teams, m, removal, list_teams, team_num2):
      '''Returns the dictionary with updated data
            & the indices of losers of a round to remove them later on.'''    # Documentation

      for i in range(1, int(rem_teams/2)+1):

            index = team_num2[m]
            print(f'Between {list_teams[index]["Name"]}')

            index = team_num2[m+1]        # Index to print Names of teams
            print(f'\tVS\n\t{list_teams[index]["Name"]}')
            print('Who won?')

            winner = int(input(f'Enter 1 for first team OR 2 for second team: '))

            list_teams[index]["Played"] += 1
            list_teams[team_num2[m]]["Played"] += 1
            # Incrementing the number of played matches

            if winner == 1:
                  list_teams[team_num2[m]]["Won"] += 1
                  # Incrementing the number of won & lost matches
                  
                  list_teams[index]["Lost"] += 1
                  removal.append(index)
                  # Storing losers' indices to be removed after the loop

            elif winner == 2:
                  list_teams[index]["Won"] += 1
                  # Incrementing the number of won & lost matches
                  
                  list_teams[team_num2[m]]["Lost"] += 1
                  removal.append(team_num2[m])
                  # Storing losers' indices to be removed after the loop

            print(f'\nStatistics have been updated! Thank You!\n')

            m += 2

      return removal, list_teams
