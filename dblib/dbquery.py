import MySQLdb
import os


class DB:
    def __init__(self):
        # get connected with the db
        self.connection = MySQLdb.connect(
            host="imdb.ciankffgrtkz.us-east-1.rds.amazonaws.com",
            user="admin",
            passwd=os.environ["PROJ5_DB_PASS"],
            db="proj5",
        )
        # get the cursor of the connection
        self.cursor = self.connection.cursor()

    # the followings are three queries
    '''
    query1: return all the names of movies directed by a specified director
    '''
    def query1(self, director_name):
        sql1 = 'SELECT TITLE FROM MOVIE WHERE DIRECTOR = "' + director_name + '"'
    
    '''
    query2: return the names of movies that have ratings higher than 9
    '''
    def query2(self):
        sql2 = 'SELECT TITLE FROM MOVIE WHERE RATING > 9'

    '''
    query3: return the top 10 highest grossing movies
    '''
    def query3(self):
        sql3 = 'SELECT TITLE FROM MOVIE ORDER BY RATING DESC LIMIT 10'