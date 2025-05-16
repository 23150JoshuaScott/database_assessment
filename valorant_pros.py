import sqlite3

DATABASE = "valorant_pros.db"

def all_info():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT player.player_name, team.team_name, region.region_name FROM player " \
        "INNER JOIN team ON player.team_id=team.team_id " \
        "INNER JOIN region ON team.region_id = region.region_id" \
        "ORDER BY player.player_id ASCS"
        cursor.execute(sql)
        results = cursor.fetchall()

        for thing in results:
        

print("In my database i have ")

if __name__ == "__main__":
    print_all_info()