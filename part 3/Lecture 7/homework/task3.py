class Scoreboard:
    def __init__(self):
        self.team=""
        self.runs=0
        self.wickets=0
    def set_team(self,team):
        if team =="":
            print("Invalid team name")
        else:
            self.team=team
    def get_team(self):
        return self.team
    def get_runs(self):
        return self.runs
    def get_wickets(self):
        return self.wickets
    def add_runs(self,runs):
        if 0<=runs<7:
            self.runs=self.runs+runs
        else:
            print("You need to enter a number between 0 and 6")
    def add_wicket(self):
        self.wickets=self.wickets+1
    def display_score(self):
        print(f"Team:{self.team}")
        print(f"Score:{self.runs}/{self.wickets}")
    
scoreboard = Scoreboard()
scoreboard.set_team("Blue Tigers")
scoreboard.add_runs(4)
scoreboard.add_runs(6)
scoreboard.add_wicket()
scoreboard.add_runs(1)
scoreboard.add_wicket()
scoreboard.display_score()