import sqlite3  
  
conn = sqlite3.connect('db/resources.db')

c = conn.cursor()
  
c.execute('''  
    CREATE TABLE IF NOT EXISTS table01 (  
        id INTEGER PRIMARY KEY,  
        name TEXT,  
        latitude REAL,  
        longitude REAL,
        painkillers INTEGER,
        bandages INTEGER,
        oxygen INTEGER,
        population INTEGER
        )  
''')  


data = [  
    ('Al Amal Hospital', 31.351760977252724, 34.29860339167593, 3500, 5000, 28000000, 426056),  
    ('Dar Al Salam Hospital', 31.3520698710092, 34.32065349350031, 2600, 2000, 35000000, 426056),  
    ('Al Nasser Hospital', 31.347876077834794, 34.293281889093095, 1250, 3000, 55000000, 426056)
]  
  
c.executemany('''  
    INSERT INTO table01 (name, latitude, longitude, painkillers, bandages, oxygen, population)  
    VALUES (?, ?, ?, ?, ?, ?, ?)  
''', data)  


conn.commit()  
conn.close()  

