#Prakriti Saldiya
#E22CSEU1610
class FlightTable:
    def _init_(self):
        self.data = [
            {"Match": "Mumbai", "Location": "India", "Team 01": "India", "Team 02": "Sri Lanka", "Timing": "DAY"},
            {"Match": "Delhi", "Location": "England", "Team 01": "England", "Team 02": "Australia", "Timing": "DAY-NIGHT"},
            {"Match": "Chennai", "Location": "India", "Team 01": "India", "Team 02": "South Africa", "Timing": "DAY"},
            {"Match": "Indore", "Location": "England", "Team 01": "England", "Team 02": "Sri Lanka", "Timing": "DAY-NIGHT"},
            {"Match": "Mohali", "Location": "Australia", "Team 01": "Australia", "Team 02": "South Africa", "Timing": "DAY-NIGHT"},
            {"Match": "Delhi", "Location": "India", "Team 01": "India", "Team 02": "Australia", "Timing": "DAY"}
        ]

    def search_by_team(self, team_name):
        matches = [match for match in self.data if team_name in [match["Team 01"], match["Team 02"]]]
        return matches

    def search_by_location(self, location):
        matches = [match for match in self.data if match["Location"] == location]
        return matches

    def search_by_timing(self, timing):
        matches = [match for match in self.data if match["Timing"] == timing]
        return matches

def main():
    flight_table = FlightTable()

    while True:
        print("Choose a search parameter:")
        print("1. List of all the matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            team_name = input("Enter the team name: ")
            matches = flight_table.search_by_team(team_name)
            print("Matches involving", team_name)
            for match in matches:
                print(match)
        elif choice == "2":
            location = input("Enter the location: ")
            matches = flight_table.search_by_location(location)
            print("Matches in", location)
            for match in matches:
                print(match)
        elif choice == "3":
            timing = input("Enter the timing: ")
            matches = flight_table.search_by_timing(timing)
            print("Matches at", timing, "timing")
            for match in matches:
                print(match)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if _name_ == "_main_":
    main()