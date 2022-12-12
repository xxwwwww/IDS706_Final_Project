import MySQLdb
import os

class DB:
    def __init__(self):
        # get connected with the db
        self.connection = MySQLdb.connect(
            host="http://imdb.ciankffgrtkz.us-east-1.rds.amazonaws.com",
            user="admin",
            passwd=os.environ["PROJ5_DB_PASS"],
            db="proj5",
        )
        # get the cursor of the connection
        self.cursor = self.connection.cursor()

    # the followings are three queries
    def query1(self,  ):
        sql = (
            
        )
    
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        
        result = {};
        result['id'] = []
        result['title'] = []
        result['subject'] = []
        result['rating'] = []
        
        for row in data:
            result['id'].append(str(row[0]))
            result['title'].append(str(row[1]))
            result['subject'].append(str(row[2]))
            result['rating'].append(str(row[3]))
        return result;

