#imports
import sqlite3

#constants and varibles
DATABASE = "valorant_pros.db"

#the base sql statement that i will use to save space 
base_statement = """FROM player
    INNER JOIN team ON player.team_id=team.team_id
    INNER JOIN region ON team.region_id = region.region_id
    """

#my first function to print all of the info in my database
def print_all_info():
    #getting all of the info from the database
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = f"""SELECT player.player_name, player.player_age, player.player_nationality, player.player_edpi, player.player_prize_money, team.team_name, region.region_name
    {base_statement} ORDER BY player.player_id"""
    cursor.execute(sql)
    results = cursor.fetchall()
    #printing all the need info for the user
    print("\nHere is all of the information in my database\nName       Age Nationality  Edpi USD Won Team  Region")
    for player in results:
        print(f"{player[0]:<11}{player[1]:<4}{player[2]:<13}{player[3]:<5}{player[4]:<8}{player[5]:<6}{player[6]}")
    print("You can exit the program by typing exit\n")
    db.close()


#this function prints all of the info from a chosen team
def print_all_team_info():
    #try helps stop the function if the user has inputted an option unavalible
    try:
        #displaying the options of teams to choose
        team_input = int(input("What team's info would you like to see? \n1.  G2\n2.  Sentinels\n3.  MIBR\n4.  Rex Regum Qeon\n5.  Gen.G\n6.  Paper Rex\n7.  Xi Lai Gaming\n8.  Bilibili Gaming\n9.  Wolves Esports\n10. fnatic\n11. Team Heretics\n12. Team Liquid\n"))
        if team_input < 1 or team_input > 12:
            print('you have not chosen an option')
            return
        #the elifs turn the user input into a value that tells the program which information to print
        elif team_input == 1:
            team = '"G2"'
        elif team_input == 2:
            team = '"SEN"'
        elif team_input == 3:
            team = '"MIBR"'
        elif team_input == 4:
            team = '"RRQ"'
        elif team_input == 5:
            team = '"GEN"'
        elif team_input == 6:
            team = '"PRX"'
        elif team_input == 7:
            team = '"XLG"'
        elif team_input == 8:
            team = '"BLG"'
        elif team_input == 9:
            team = '"WOL"'
        elif team_input == 10:
            team = '"FNC"'
        elif team_input == 11:
            team = '"TH"'
        elif team_input == 12:
            team = '"TL"'
        #getting all of the info chosen from the database
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        sql = f"""SELECT player.player_name, player.player_age, player.player_nationality, player.player_edpi, player.player_prize_money, region.region_name
        {base_statement} WHERE team.team_name = {team} ORDER BY player.player_id"""
        cursor.execute(sql)
        results = cursor.fetchall()
        #printing all the need info for the user
        print(f"\nHere is the info for {team}\nName       Age Nationality  Edpi USD Won Region")
        for player in results:
            print(f"{player[0]:<11}{player[1]:<4}{player[2]:<13}{player[3]:<5}{player[4]:<8}{player[5]:<6}")
        print("You can exit the program by typing exit\n")
    except team_input <= 0 or team_input > 12 or ValueError:
        print("You have not chosen an option\n")
        return
    db.close()

#this function prints all of the info from a chosen region
def print_all_region_info():
    #try helps stop the function if the user has inputted an option unavalible
    try:
        region_input = int(input("What regions's info would you like to see? \n1. AMERICAS\n2. PACIFIC\n3. CHINA\n4. EMEA\n"))
        if region_input < 1 or region_input > 4:
            print('you have not chosen an option')
            return
        #the elifs turn the user input into a value that tells the program which information to print
        elif region_input == 1:
            region = '"AMERICAS"'
        elif region_input == 2:
            region = '"PACIFIC"'
        elif region_input == 3:
            region = '"CHINA"'
        elif region_input == 4:
            region = '"EMEA"'
        #getting all of the info chosen from the database
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        sql = f"""SELECT player.player_name, player.player_age, player.player_nationality, player.player_edpi, player.player_prize_money, team.team_name
        {base_statement} WHERE region.region_name = {region} ORDER BY player.player_id"""
        cursor.execute(sql)
        results = cursor.fetchall()
        #printing all the need info for the user
        print(f"\nHere is the info for {region} region\nName       Age Nationality  Edpi USD Won Team")
        for player in results:
            print(f"{player[0]:<11}{player[1]:<4}{player[2]:<13}{player[3]:<5}{player[4]:<8}{player[5]:<6}")
        print("You can exit the program by typing exit\n")
    except region_input <= 0 or region_input > 12 or ValueError:
        print("You have not chosen an option\n")
    db.close()

#this is the best function where you can 
def print_all_info_ordered():
    #try helps stop the function if the user has inputted an option unavalible
    try:
        order_input = int(input("What would you like to order the data by? \n1. Name\n2. Age\n3. Nationality\n4. Edpi\n5. Prize Money\n"))
        if order_input < 1 or order_input > 6:
            print('you have not chosen an option')
            return
        elif order_input == 1:
            order = "player.player_name"
        elif order_input == 2:
            order = "player.player_age"
        elif order_input == 3:
            order = "player.player_nationality"
        elif order_input == 4:
            order = "player.player_edpi"
        elif order_input == 5:
            order = "player.player_prize_money"
        else:
            print("You have not chosen an option\n")
        #getting all of the info chosen from the database
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        sql = f"""SELECT player.player_name, player.player_age, player.player_nationality, player.player_edpi, player.player_prize_money, team.team_name, region.region_name
        {base_statement} ORDER BY {order} ASC"""
        cursor.execute(sql)
        results = cursor.fetchall()
        #printing all the need info for the user
        print("\nName       Age Nationality  Edpi USD Won Team  Region")
        for player in results:
            print(f"{player[0]:<11}{player[1]:<4}{player[2]:<13}{player[3]:<5}{player[4]:<8}{player[5]:<6}{player[6]}")
        print("You can exit the program by typing exit\n")
    except order_input <= 0 or order_input > 12 or ValueError:
        print("You have not chosen an option\n")
    db.close()

#title and introduction
print("\nI have chosen to make my database about various statistics from the top pro valorant players\nIn my database I have gathered this information from the top 3 teams in the world from each region (all of the teams qualifed to the upcoming masters Toront event)\nYou have 4 options")
#menu options
while True:
    user_input = input("What would you like to do?\n1. Press 1 to print all data\n2. Choose a team to see their info\n3. Choose a region to see their info\n4. Choose a peice of data to order by\n")
#code for the menu and calling the chosen functions
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