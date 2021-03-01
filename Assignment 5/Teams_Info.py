def teams_info(list_teams):
      '''Prints the details about teams'''      # Documentation

      for k in list_teams:    # Taking one dictionary and displaying the values of all the keys
            print(f'''
Team Names\tMatches Won\tMatches Lost\tWorld Cups Won\t\tAverage Runs per Match

{k["Name"]}\t\t{k["Won"]}\t\t{k["Lost"]}\t\t{k["World Cups"]}\t\t\t{k["Avg Runs"]}

''')
