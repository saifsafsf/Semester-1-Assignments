import random
def schedule(j, rem_teams, team_num, team_num2, list_teams):
      '''Takes the list of teams & chooses randomly for a round
            Also, stores teams\' indices rearranged to their sequence in tournament'''
      print(f'\t\t\tROUND - {j}')         # Starting a round

      for i in range(1, int(rem_teams/2)+1):
            index = random.choice(team_num)
            team_num.remove(index)        # Randomly choosing the players

            team_num2.append(index)
            first_team = list_teams[index]
            # Also removing them from original list

            index = random.choice(team_num)
            team_num.remove(index)

            team_num2.append(index)
            second_team = list_teams[index]

            print(f'\t\t\t Match {i}\n\t\t    {first_team["Name"]} VS {second_team["Name"]}\n')

            win_rate_1 = (first_team['Won']/first_team['Played'])*100
            win_rate_2 = (second_team['Won']/second_team['Played'])*100

            win_chance_1 = (win_rate_1/(win_rate_1+win_rate_2))*100
            first_team['Winning Rate'] = win_rate_1
            # Calculating win chances & win rates of teams

            print(f'Winning Chance for {first_team["Name"]}: {win_chance_1:.2f}')

            win_chance_2 = (win_rate_2/(win_rate_1+win_rate_2))*100
            second_team['Winning Rate'] = win_rate_2

            print(f'Winning Chance for {second_team["Name"]}: {win_chance_2:.2f}\n')

      return team_num, team_num2
