import pymysql

class DBHelper:
  def __init__(self):
      try:
          self.mySqlConnection=pymysql.connect(user="root",host="localhost",password="Hritik@1234",database="Training")

          self.cursor=self.mySqlConnection.cursor()

          print("Database connected successfully")
      except Exception as e:
          print("Could'nt connect the databse ")
          print(e)
 