import math
import Options
import Input_Details as ID          # Importing Modules
import Teams_Info as TI 
import Schedule
import Results

option = None

while option != 'x':
      option = Options.options(option)    # Selecting an option

      if option == 'x':
            print('Program exited successfully.')
            break
      elif option != 'g':
            print('First, give teams\' details please.\n')

      teams = 3         # To enter while loop

      while (math.log(teams, 2).is_integer()) == False:     # If input is 2**n
            teams = int(input('Enter number of teams: '))
            
      list_teams, team_num = ID.teams_details(teams)        # Entering details of teams

      option = None
      option = Options.options(option)

      if option == 'x':
            print('Program exited successfully.')           # Again providing menu if you want to exit
            break
      elif option == 'v':
            TI.teams_info(list_teams)           # To check the teams' details

      rem_teams = teams       # To avoid changing the value of orginal list

      team_num2 = []          # Containing indices of teams according to their sequence in tournament

      j = 1

      while rem_teams > 1:
            team_num, team_num2 = Schedule.schedule(j, rem_teams, team_num, team_num2, list_teams)
            # To show the schedule of the tournament
            m = 0
            index = 0
            removal = []

            removal, list_teams = Results.input_results(rem_teams, m, removal, list_teams, team_num2)
            # To enter the results of each round
            for r in removal:
                  team_num2.remove(r)     # Eliminating the losers for next round

            rem_teams /= 2

            team_num = team_num2

            team_num2 = []    # Changing values for next loop

            j += 1

            option = None
