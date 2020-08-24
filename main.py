# Dianna Xu
# CS110-A 5.2
# Create an ID from a name and ID

def main():
  first_name = input("What is your first name? ")
  last_name = input("What is your last name? ")
  ID = input("What is your your ID? ")
  get_student_login(first_name, last_name, ID)
  print ("Your login is: ", first_name[:3]+last_name[:3]+ID[-3:])

def get_student_login(first_name, last_name, ID):
  return first_name[:3]+last_name[:3]+ID[-3:]

main()
