#imports
import sqlite3
#constants and varibles
DATABASE = "valorant_pros.db"

#functions
def print_all_info():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = """SELECT player.player_name, player.player_age, player.player_nationality, player.player_edpi, player.player_prize_money, team.team_name, region.region_name 
    FROM player
    INNER JOIN team ON player.team_id=team.team_id
    INNER JOIN region ON team.region_id = region.region_id
    ORDER BY player.player_id
    """
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Name       Age Nationality  Edpi USD Won Team  Region")
    for player in results:
        print(f"{player[0]:<11}{player[1]:<4}{player[2]:<13}{player[3]:<5}{player[4]:<8}{player[5]:<6}{player[6]}")
    db.close()

def print_all_team_info():
    team = input("What team's info would you like to see? \n")
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = """SELECT player.player_name, player.player_age, player.player_nationality, player.player_edpi, player.player_prize_money, team.team_name, region.region_name 
    FROM player
    INNER JOIN team ON player.team_id=team.team_id
    INNER JOIN region ON team.region_id = region.region_id
    WHERE team.team_name = ?
    ORDER BY player.player_id
    """
    cursor.execute(sql,(team,))
    results = cursor.fetchall()
    print("Name       Age Nationality  Edpi USD Won Team  Region")
    for player in results:
        print(f"{player[0]:<11}{player[1]:<4}{player[2]:<13}{player[3]:<5}{player[4]:<8}{player[5]:<6}{player[6]}")
    db.close()

def print_all_region_info():
    region = input("What regions's info would you like to see? \n")
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = """SELECT player.player_name, player.player_age, player.player_nationality, player.player_edpi, player.player_prize_money, team.team_name, region.region_name 
    FROM player
    INNER JOIN team ON player.team_id=team.team_id
    INNER JOIN region ON team.region_id = region.region_id
    WHERE region.region_name = ?
    ORDER BY player.player_id
    """
    cursor.execute(sql,(region,))
    results = cursor.fetchall()
    print(f"\nHere is the info for {region}\nName       Age Nationality  Edpi USD Won Team  Region")
    for player in results:
        print(f"{player[0]:<11}{player[1]:<4}{player[2]:<13}{player[3]:<5}{player[4]:<8}{player[5]:<6}{player[6]}")
    db.close()

#main code
while True:
    user_input = input("\nWhat would you like to do?\n1. Press 1 to print all data\n2. Chose a team to see their info\n3. Chose a region to see their info\n")
    if user_input == "exit":
        break
    elif user_input == "1":
        print_all_info()
    elif user_input == "2":
        print_all_team_info()
    elif user_input == "3":
        print_all_region_info()
    else:
        print("You have not chosen an option\n")