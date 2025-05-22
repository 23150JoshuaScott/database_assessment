#imports
import sqlite3

#constants and varibles
DATABASE = "valorant_pros.db"

#the base sql statement that i will use to save space 
base_statement = """SELECT player.player_name, player.player_age, player.player_nationality, player.player_edpi, player.player_prize_money, team.team_name, region.region_name 
    FROM player
    INNER JOIN team ON player.team_id=team.team_id
    INNER JOIN region ON team.region_id = region.region_id
    """

#my first function to print all of the info in my database
def print_all_info():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = f"{base_statement} ORDER BY player.player_id"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Name       Age Nationality  Edpi USD Won Team  Region")
    for player in results:
        print(f"{player[0]:<11}{player[1]:<4}{player[2]:<13}{player[3]:<5}{player[4]:<8}{player[5]:<6}{player[6]}")
    db.close()

#this function prints all of the info from a chosen team
def print_all_team_info():
    team = input("What team's info would you like to see? \n")
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = f"{base_statement} WHERE team.team_name = ? ORDER BY player.player_id"
    cursor.execute(sql,(team,))
    results = cursor.fetchall()
    print(f"\nHere is the info for {team}\nName       Age Nationality  Edpi USD Won Team  Region")
    for player in results:
        print(f"{player[0]:<11}{player[1]:<4}{player[2]:<13}{player[3]:<5}{player[4]:<8}{player[5]:<6}{player[6]}")
    db.close()

#this function prints all of the info from a chosen region
def print_all_region_info():
    region = input("What regions's info would you like to see? \n")
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = f"{base_statement} WHERE region.region_name = ? ORDER BY player.player_id"
    cursor.execute(sql,(region,))
    results = cursor.fetchall()
    print(f"\nHere is the info for {region}\nName       Age Nationality  Edpi USD Won Team  Region")
    for player in results:
        print(f"{player[0]:<11}{player[1]:<4}{player[2]:<13}{player[3]:<5}{player[4]:<8}{player[5]:<6}{player[6]}")
    db.close()

#this is the best function where you can 
def print_all_info_ordered():
    order_input = input("What would you like to order the data by? \n1. Name\n2. Age\n3. Nationality\n4. Edpi\n5. Prize Money\n")
    if order_input == "1":
        order = "player.player_name"
    elif order_input == "2":
        order = "player.player_age"
    elif order_input == "3":
        order = "player.player_nationality"
    elif order_input == "4":
        order = "player.player_edpi"
    elif order_input == "5":
        order = "player.player_prize_money"
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = f"{base_statement} ORDER BY {order} DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("\nName       Age Nationality  Edpi USD Won Team  Region")
    for player in results:
        print(f"{player[0]:<11}{player[1]:<4}{player[2]:<13}{player[3]:<5}{player[4]:<8}{player[5]:<6}{player[6]}")
    db.close()

#menu options
while True:
    user_input = input("\nWhat would you like to do?\n1. Press 1 to print all data\n2. Chose a team to see their info\n3. Chose a region to see their info\n4. Chose a peice of data to order by\n")
#code for the menu and calling the functions
    if user_input == "exit":
        break
    elif user_input == "1":
        print_all_info()
    elif user_input == "2":
        print_all_team_info()
    elif user_input == "3":
        print_all_region_info()
    elif user_input == "4":
        print_all_info_ordered()
    else:
        print("You have not chosen an option\n")