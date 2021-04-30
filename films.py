from flask import abort
from db import db

def count():
    sql = "SELECT COUNT(*) FROM films WHERE visible=1"
    result = db.session.execute(sql)
    return result.fetchone()[0]

def exists(id):
    sql = "SELECT COUNT(1) FROM films WHERE id=:id AND visible=1"
    result = db.session.execute(sql, {"id":id})
    if result.fetchone()[0] == 0:
        abort(404)

def visible(id):
    sql = "SELECT visible FROM films WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()[0]

def get_list(visible):
    if visible == 1:
        sql = "SELECT f.id, f.visible, f.name, f.description, f.year, c.name " \
          "FROM films AS f, countries AS c " \
          "WHERE c.id=f.country_id AND visible=1 " \
          "ORDER BY f.name"
        result = db.session.execute(sql)
        return result.fetchall()
    elif visible == 0:
        sql = "SELECT f.id, f.visible, f.name, f.description, f.year, c.name " \
          "FROM films AS f, countries AS c " \
          "WHERE c.id=f.country_id " \
          "ORDER BY f.name"
        result = db.session.execute(sql)
        return result.fetchall()
    else:
        abort(500)

def get_details(id):
    sql = "SELECT f.id, f.name, f.description, f.year, c.name, l.name, g.name, d.name, s.name " \
          "FROM films AS f, countries AS c, languages AS l, genres AS g, directors AS d, screenwriters AS s " \
          "WHERE f.id=:id AND c.id=f.country_id AND l.id=f.language_id " \
          "AND g.id=f.genre_id AND d.id=f.director_id AND s.id=f.screenwriter_id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchall()

def get_name(id):
    sql = "SELECT name FROM films WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()[0]

def send(name, description, year, country_id, language_id, genre_id, director_id, screenwriter_id):
    sql = "INSERT INTO films (visible, name, description, year, country_id, language_id, genre_id, director_id, screenwriter_id) " \
          "VALUES (:visible, :name, :description, :year, :country_id, :language_id, :genre_id, :director_id, :screenwriter_id)"
    visible = 1
    db.session.execute(sql, {"visible":visible, "name":name, "description":description, 
                             "year":year, "country_id":country_id, "language_id":language_id,
                             "genre_id":genre_id, "director_id":director_id, "screenwriter_id":screenwriter_id})
    db.session.commit()
    return True

def delete(id):
    sql = "UPDATE films SET visible=0 WHERE id=:id"
    db.session.execute(sql, {"id":id})
    db.session.commit()
    return True

def restore(id):
    sql = "UPDATE films SET visible=1 WHERE id=:id"
    db.session.execute(sql, {"id":id})
    db.session.commit()
    return True