import psycopg2
import os

from dotenv import load_dotenv
from choices import df

load_dotenv()

if __name__ == '__main__':
    conn = psycopg2.connect(
        host="localhost",
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD')
    )
    with conn.cursor() as cur:
        # Run users.sql
        with open('users.sql') as db_file:
            cur.execute(db_file.read())
        # Run produce.sql
        with open('produce.sql') as db_file:
            cur.execute(db_file.read())

        # Import all produce from the dataset
        all_produce = list(
            map(lambda x: tuple(x),
                df[['name','goals_scored','assists','total_points','goals_conceded','creativity','influence','threat','bonus','bps','ict_index','clean_sheets','red_cards','yellow_cards','position','GW','total_goals','all_points','total_assists','team']].to_records(index=False))
        )
        args_str = ','.join(
    cur.mogrify("(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s)", tuple(str(x) for x in i)).decode('utf-8')
    for i in all_produce
)
        cur.execute("INSERT INTO Produce (full_name,goals_scored,assists,total_points,goals_conceded,creativity,influence,threat,bonus,bps,ict_index,clean_sheets,red_cards,yellow_cards,position,gw,total_goals,all_points,total_assists,team) VALUES " + args_str)

        # Dummy farmer 1 sells all produce
        dummy_sales = [(1, i) for i in range(1, len(all_produce) + 1)]
        args_str = ','.join(cur.mogrify("(%s, %s)", i).decode('utf-8') for i in dummy_sales)
        cur.execute("INSERT INTO Sell (farmer_pk, produce_pk) VALUES " + args_str)

        conn.commit()

    conn.close()
