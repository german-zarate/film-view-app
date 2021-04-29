import csv
from db import db

def count():
    sql = "SELECT COUNT(*) FROM countries"
    result = db.session.execute(sql)
    return result.fetchone()[0]

def create_list():
    sql = "SELECT COUNT(*) FROM continents"
    result = db.session.execute(sql)
    db.session.commit()

    if result.fetchone()[0] > 0:
        return False

    sql = "INSERT INTO continents (name) VALUES " \
          "('Africa'), ('Asia'), ('Europe'), ('North America'), ('South America'), ('Oceania')"
    db.session.execute(sql)
    db.session.commit()

    with open('data/countries.csv') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            name = row[1]
            continent_id = 0
            if row[0] == "AF":
                continent_id = 1
            elif row[0] == "AS":
                continent_id = 2
            elif row[0] == "EU":
                continent_id = 3
            elif row[0] == "NA":
                continent_id = 4
            elif row[0] == "SA":
                continent_id = 5
            elif row[0] == "OC":
                continent_id = 6
            sql = "INSERT INTO countries (name, continent_id) VALUES (:name, :continent_id)"
            db.session.execute(sql, {"name":name, "continent_id":continent_id})
        db.session.commit()

    return True
        
def get_list():
    sql = "SELECT id, name FROM countries"
    result = db.session.execute(sql)
    return result.fetchall()