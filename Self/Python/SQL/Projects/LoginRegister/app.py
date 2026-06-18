import sys
from DBHelper import DBHelper


class loginRegister:
  def __init__(self):
    # connect to the database
    self.db=DBHelper()
    self.menu()
    def menu(self):
      user_input= input("""Enter your choice
                        1. Press 1 to Login
                        2. Press 2 to register
                        3. Press anything to exit""")
      
      if user_input=="1":
        self.login()
      elif user_input=="2":
        self.register()
      else:
        sys.exit()
