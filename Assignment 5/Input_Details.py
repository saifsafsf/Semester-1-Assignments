def teams_details(teams):
      '''Takes the number of teams.
            Returns list of dictionaries, one for each team.'''   # Documentation

      list_teams = []
      team_num = []
      i = 1

      print('\nEnter the following:')     # Details of each team
      print()

      for counter in range(teams):
            dict_team = {}

            dict_team['Name'] = input(f'Team {i} name: ')
            dict_team['Played'] = int(input('Number of matches played: '))
            dict_team['Won'] = int(input('Number of matches won: '))
            dict_team['Lost'] = int(input('Number of matches lost: '))
            dict_team['World Cups'] = int(input('Number of World Cups won: '))
            dict_team['Avg Runs'] = int(input('Average Runs per match: '))

            team_num.append(counter)      # Storing each dictionary's index to use later

            list_teams.append(dict_team)        # Making a list of dictionaries
            print()

            i += 1      # To print "Match No."

      return list_teams, team_num
