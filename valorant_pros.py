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
    ORDER BY player.player_id ASC
    """
    cursor.execute(sql)
    results = cursor.fetchall()
    for player in results:
        print(f"{player[0]:<11}{player[1]:<4}{player[2]:<13}{player[3]:<5}{player[4]:<8}{player[5]:<6}{player[6]}")
    db.close()

#main code
print_all_info()