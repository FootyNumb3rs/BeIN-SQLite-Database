import sqlite3
import pandas as pd

path = "C:\\Users\Tande\Desktop\sqll\scraper_base.sqlite"
conn = sqlite3.connect(path)
c = conn.cursor()

## Creating BEIN table
table_columns = ['pos','name','gp','team','stat',
				 'statname','league','abbr','crest']
bein_sql = """ 
CREATE TABLE bein (
	id integer PRIMARY KEY,
	pos integer NOT NULL,
	name text NOT NULL, 
	gp text NOT NULL,
	team text NOT NULL, 
	stat text NOT NULL,
	statname text NOT NULL, 
	league text NOT NULL,
	abbr text NOT NULL, 
	crest text NOT NULL
) """


create_label = """
INSERT INTO bein ({}) VALUES ({})
""".format(','.join(table_columns),
		  ','.join(['?' for i in range(len(table_columns))]))



# Importing dataset
df = pd.read_csv('super_table5.csv',header=0)


#c.execute(bein_sql)

for i in df.as_matrix():
	c.execute(create_label,i)

conn.commit()
conn.close()
















