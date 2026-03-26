import random

name = input('Type Your Name: ')
print(f"⚽ Welcome {name} to Football Career Simulator 2.0! ⚽\n")

print("You are about to start your journey as a professional football player.")
print("Your decisions on the pitch, your training, and your stamina will shape your career.\n")
print("Key Tips:")
print("- Choose your position wisely: Striker, Midfielder, or Defender.")
print("- Train your skills to improve your stats.")
print("- Manage your stamina — if it drops too low, you won’t perform well in matches.")
print("- Play matches every week, make key decisions on the ball, and earn match ratings.")
print("- Earn money and move to bigger clubs with higher salaries as you grow.\n")
print("Your journey starts now. Will you rise to football stardom or struggle in the lower leagues?")
print("Good luck!\n")

positions = ['Striker', 'Midfielder', 'Defender']
position_stats = {
    "Striker": {"Shooting": 13, "Passing": 7, "Dribbling": 7, "Physical": 10, "Defending": 6},
    "Midfielder": {"Shooting": 8, "Passing": 13, "Dribbling": 10, "Physical": 5, "Defending": 6},
    "Defender": {"Shooting": 6, "Passing": 7, "Dribbling": 5, "Physical": 10, "Defending": 13}
}

for i, position in enumerate(positions, start=1):
    print(f'{i}. {position}')
position_choice = int(input('Pick a Position: '))
new_pos = positions[position_choice - 1]

match_days_played = 0
club = 'Amakiri FC'
stamina = 5
money = 0
salary = 50
ovr = 0
goals = 0
assist = 0

club_offer = {
    "Amakiri FC": {"salary": 50, "ovr_req": 0},
    "Lagos United": {"salary": 100, "ovr_req": 15},
    "Delta Warriors": {"salary": 150, "ovr_req": 20},
    "Dragon FC": {"salary": 200, "ovr_req": 25},
    "Eagle Rangers": {"salary": 250, "ovr_req": 30},
    "Capital City FC": {"salary": 300, "ovr_req": 35},
    "Thunder Hawks": {"salary": 350, "ovr_req": 40},
    "Silver Lions": {"salary": 400, "ovr_req": 45},
    "Golden Eagles": {"salary": 500, "ovr_req": 55},
    "Royal Titans": {"salary": 600, "ovr_req": 65},
    "Premier Legends": {"salary": 750, "ovr_req": 75},
    "World Stars FC": {"salary": 1000, "ovr_req": 85}
}

class Player:
    def __init__(self, name, stamina):
        self.name = name
        self.stats = position_stats[new_pos].copy()
        self.position = new_pos
        self.stamina = stamina
        self.club = club
        self.ovr = ovr
        self.salary = salary
        self.money = money
        self.goals = goals
        self.assist = assist

    def show_stats(self):
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        for stat, value in self.stats.items():
            print(f"{stat}: {value}")

    def train(self):
        self.stamina -= 0.5
        if self.stamina <= 0:
            self.stamina = 0
            print(f'You Cannot Train. Stamina is {self.stamina}')
            

        print("\nWhich skill do you want to upgrade?")
        stat_keys = list(self.stats.keys())
        for i, stat in enumerate(stat_keys, start=1):
            print(f"{i}. {stat} ({self.stats[stat]})")

        choice1 = input("Type number of skill to upgrade by 5 points: ")
        choice2 = input("Type number of skill to upgrade by 2 points: ")

        if choice1.isdigit() and 1 <= int(choice1) <= len(stat_keys):
            self.stats[stat_keys[int(choice1)-1]] += 5
        if choice2.isdigit() and 1 <= int(choice2) <= len(stat_keys):
            self.stats[stat_keys[int(choice2)-1]] += 2

        print(f'Your Stamina is Now {self.stamina}')
        self.ovr = round((sum(self.stats.values()) / len(self.stats)) )
    def show_ovr(self):
        print(f'Player OVR is {self.ovr}')
    def play_match(self):
        global match_days_played
        match_days_played += 1
        self.money += self.salary
        rating = 6.0

        events_this_match = random.randint(3,5)
        events = ["Attacking Chance", "Counter Attack", "Midfield Play", "Defensive Situation", "Wing Play", 'Freekick', 'Penalty']
        actions = {
            "Shoot": "Shooting", "Pass": "Passing", "Dribble": "Dribbling",
            "Tackle": "Defending", "Cross": "Passing", "Long Pass": "Passing",
            "Clear Ball": "Physical", "Intercept": "Defending"
        }

        for i in range(events_this_match):
            event = random.choice(events)
            print(f"\nEvent {i+1}: {event}")

            if event == "Penalty":
                directions = ["Left", "Right", "Center"]
                for j, d in enumerate(directions, start=1):
                    print(f"{j}. {d}")
                choice = input("Choose direction: ")
                if not choice.isdigit() or int(choice) < 1 or int(choice) > 3:
                    print("❌ You slipped! Penalty missed!")
                    rating -= 1
                    continue
                player_dir = directions[int(choice)-1]
                keeper_dir = random.choice(directions)
                print(f"You shot: {player_dir}")
                print(f"Goalkeeper dove: {keeper_dir}")
                if player_dir == keeper_dir:
                    print("🧤 SAVED! The goalkeeper guessed correctly!")
                    rating -= 0.5
                else:
                    print("⚽ GOAL! You scored the penalty!")
                    rating += 1.5
                continue

            if event in ["Attacking Chance", "Counter Attack"]:
                available = ["Shoot", "Pass", "Dribble"]
            elif event == "Midfield Play":
                available = ["Pass", "Long Pass", "Dribble"]
            elif event == "Defensive Situation":
                available = ["Tackle", "Intercept", "Clear Ball"]
            elif event == "Wing Play":
                available = ["Cross", "Dribble", "Pass"]
            elif event == "Freekick":
                available = ["Shoot", "Cross"]

            for j, act in enumerate(available, start=1):
                print(f"{j}. {act}")
            choice = input("Choose your action: ")
            if not choice.isdigit() or int(choice) < 1 or int(choice) > len(available):
                print("❌ You hesitated and lost the ball!")
                rating -= 0.4
                continue

            action = available[int(choice)-1]
            stat_value = self.stats[actions[action]]
            roll = random.randint(1, 100)
            if roll <= stat_value * self.stamina:
                if action == "Shoot":
                    self.goals += 1
                    print("⚽ GOAL!")
                    rating += 1.5
                elif action in ["Pass", "Long Pass", "Cross"]:
                    self.assist += 1
                    print("🎯 Assist!")
                    rating += 1
                elif action == "Dribble":
                    print("🔥 Dribble Success!")
                    rating += 0.8
                elif action in ["Tackle", "Intercept"]:
                    print("🛡 Defensive Success!")
                    rating += 0.8
                elif action == "Clear Ball":
                    print("💨 Cleared Danger!")
                    rating += 0.5
            else:
                print("❌ Action Failed!")
                rating -= 0.3

        print(f"\n⭐ Match Rating: {round(rating,1)}")
        print(f"Matches Played: {match_days_played}")
        print(f"Money: {self.money}")

        if round(rating,1) >= 7:
            self.ovr += 3
            print(f'Player OVR upgraded to {self.ovr}')
        self.show_club_offer()

    def rest(self):
        self.stamina += 0.5
        if self.stamina > 5: 
            self.stamina = 5
        print(f'Stamina: {self.stamina}')

    def show_club_offer(self):
        offers = []
        if match_days_played ==7:
            for name, data in club_offer.items():
                if self.ovr >= data['ovr_req'] and data['salary'] > self.salary:
                    offers.append((name, data['salary']))
            if not offers:
                print("No new club offers available yet.")
                return
            print("\n📢 Transfer Offers Available:")
            for i, (name, sal) in enumerate(offers, start=1):
                print(f"{i}. {name} - Salary: {sal}")
            choice = input("Pick a club to accept or press Enter to skip: ")
            if choice.isdigit() and 1 <= int(choice) <= len(offers):
                self.club = offers[int(choice)-1][0]
                self.salary = offers[int(choice)-1][1]
                print(f"✅ Transferred to {self.club} with salary {self.salary}\n")
            else:
                print("❌ No club transfer this time.\n")

pl = Player(name, stamina)
pl.show_stats()

time = {'day': 1, 'week': 1, 'year': 2026}
def advance_time():
    global time
    time['day'] += 1
    if time['day'] > 7:
        time['day'] = 1
        time['week'] += 1
    if time['week'] > 52:
        time['week'] = 1
        time['year'] += 1

while True:
    print(f'Day {time["day"]} | Week {time["week"]} | Year {time["year"]}')
    print(f'Club: {pl.club}')
    if time['day'] == 7:
        pl.play_match()
    elif time["day"]==6:
        choice = input('A. Train B. Rest ').upper()
        if choice == 'A':
            pl.train()
        else:
            pl.rest()    
        pl.show_ovr()
    else:
        choice = input('A. Train B. Rest ').upper()
        if choice == 'A':
            pl.train()
        else:
            pl.rest()
    advance_time()