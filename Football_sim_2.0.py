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



positions = ['Striker' , 'Midfielder' , 'Defender']
position_stats = {
    "Striker":    {"Shooting": 13, "Passing": 8, "Dribbling": 9, "Physical": 8, "Defending": 6},
    "Midfielder": {"Shooting": 8,  "Passing": 13, "Dribbling": 10, "Physical": 7, "Defending": 7},
    "Defender":   {"Shooting": 7,  "Passing": 8,  "Dribbling": 6, "Physical": 10, "Defending": 13}
}
for i , position in enumerate(positions , start = 1):
    print(f'{i}. {position}')
position_choices = int(input('Pick a Position: '))
new_pos = positions[position_choices -1]

match_days_played = 0
club = 'Amakiri FC'
stamina =10
money = 0
salary = 50  
ovr = 0

class Player:
    def __init__(self, name, stamina):
        self.name = name
        self.stats = position_stats[new_pos]
        self.position= new_pos
        self.stamina = stamina
        self.club = club
        self.ovr = ovr
        self.salary = salary
        self.money= money
    def show_stats(self):
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        for stat, value in self.stats.items():
            print(f"{stat}: {value}")
    def train(self):
        
        self.stamina -= 2
        if self.stamina <=0:
            self.stamina = 0
            print(f'You Cannot Train Stamina is {self.stamina}')
        elif self.stamina >0:
            print("\nWhich skill do you want to upgrade?")
            stat_keys = list(self.stats.keys())
            for i, stat in enumerate(stat_keys, start=1):
                print(f"{i}. {stat} ({self.stats[stat]})")

            
            choice = input("\nType the number of the skill This Skill is Upgraded By 5 Points: ")
            choice2 = input("Type the number of the skill This Skill is Upgraded By 2 Points: ")
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(stat_keys):
                    chosen_stat = stat_keys[choice - 1]
                    self.stats[chosen_stat] += 5 
                    
                    print(f"\n{chosen_stat} upgraded! New value: {self.stats[chosen_stat]}")
                else:
                    print("Invalid number choice.")
            else:
                print("Please type a number.")
            if choice2.isdigit():
                choice2 = int(choice2)
                if 1 <= choice2 <= len(stat_keys):
                    chosen_stat2 = stat_keys[choice2 - 1]
                    self.stats[chosen_stat2] += 2  
                    print(f"{chosen_stat2} upgraded! New value: {self.stats[chosen_stat2]}")
                else:
                    print("Invalid number choice.")
            else:
                print("Please type a number.")
            print(f'Your Stamina is Now {self.stamina}')
            self.ovr = round((sum(self.stats.values())/ len(position_stats[new_pos].values()))*1.5)
            print(f'Player Overall Rating: {self.ovr}')
            

 

    def play_match(self):
        global match_days_played
        self.money = self.money +self.salary
        match_days_played += 1
        rating = 6.0  
        print("\n⚽ Match Day!")

        
        actions = {
            "Shoot":        {"stat": "Shooting",    "Striker": 3.0, "Midfielder": 1.5, "Defender": 0.5},
            "Pass":         {"stat": "Passing",     "Striker": 1.5, "Midfielder": 3.0, "Defender": 1.0},
            "Dribble":      {"stat": "Dribbling",   "Striker": 3.0, "Midfielder": 2.3, "Defender": 1.5},
            "Tackle":       {"stat": "Defending",   "Striker": 1.0, "Midfielder": 1.5, "Defender": 3.0},
            "Cross":        {"stat": "Passing",     "Striker": 0.8, "Midfielder": 2.0, "Defender": 0.5},
            "Long Pass":    {"stat": "Passing",     "Striker": 1.5, "Midfielder": 2.5, "Defender": 1.5},
            'Freekick': {"stat":'Shooting' , "Striker": 1.5, "Midfielder": 2.5, "Defender": 0.5}       
        }

        
        if self.position == "Striker":
            available = ["Shoot", "Pass", "Dribble", "Cross"]
        elif self.position == "Midfielder":
            available = ["Shoot", "Pass", "Dribble", "Long Pass", "Tackle"]
        else: 
            available = ["Pass", "Dribble", "Tackle", "Long Pass"]

        print("\nYou have the ball. Choose your action:")
        for i, act in enumerate(available, start=1):
            print(f"{i}. {act}")

        choice_num = input("Type the number of your action: ")

        if not choice_num.isdigit() or int(choice_num) < 1 or int(choice_num) > len(available):
            print("Invalid choice! You hesitated and lost the ball.")
            rating -= 0.5
        else:
            action = available[int(choice_num)-1]
            stat = actions[action]["stat"]
            multiplier = actions[action][self.position]
            success_chance = self.stats[stat] * multiplier
            roll = random.randint(1,100)

            if roll <= success_chance:
                
                if action == "Shoot":
                    print("⚽ GOAL! Amazing shot!")
                    rating += 2
                elif action in ["Pass", "Cross", "Long Pass"]:
                    print("🎯 Perfect pass! Teammate is in position!")
                    rating += 1.5
                elif action == "Dribble":
                    print("🔥 Fantastic dribble past the defender!")
                    rating += 1
                elif action == "Tackle":
                    print("🛡️ Excellent tackle! You stopped the attack!")
                    rating += 1
            else:
                # 
                if action == "Shoot":
                    print("❌ Shot missed or blocked!")
                    rating -= 0.5
                elif action in ["Pass", "Cross", "Long Pass"]:
                    print("❌ Pass intercepted!")
                    rating -= 0.5
                elif action == "Dribble":
                    print("❌ You lost the ball while dribbling!")
                    rating -= 0.5
                elif action == "Tackle":
                    print("❌ Tackle failed, attacker got past you!")
                    rating -= 0.5

                
        if match_days_played  == 7:
            pass
        print(f"\nMatch Rating: {round(rating,1)}")
        print(f"Matches Played: {match_days_played}")
        print(f'Money: {self.money}')
        
    def show_clubs(self):
        pass
    def rest(self):
        self.stamina +=5
        if self.stamina >10:
            self.stamina = 10
        if self.stamina == 10:
            print('You Have max Stamina')
        else:
            print(f'\nStamina has increased to {self.stamina}')

            
pl = Player(name, stamina)
pl.show_stats()

time ={
    'day': 1 ,
    'week': 1 ,
    'year': 2026
}
def advance_time():
    global time
    time['day']+=1
    if time['day'] > 7:
        time['day'] = 1
        time['week']+=1
    if time['week'] >52:
        time['week']=1
        time['year']+=1



while True:
    
    print(f'Day {time["day"]} | Weeks {time["week"]} | Year  {time["year"]}')
    print(f'Club: {pl.club}')
    if time['day'] ==  7:
        pl.play_match()
    else:
        choice = input('Would you like to A. Train B. Rest ').upper()
        if choice== 'A':
            pl.train()
        else:
            pl.rest()
    
    advance_time()