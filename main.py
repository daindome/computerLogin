# This project has been created to design an interactive computer login system where the user is prompted to create a
# username and a password to login to a computer system

#1. The system will prompt the user to create a username, The username will be required to meet certain criteria.
#2. Once a suitable username has been entered, the system will then prompt the user to enter a password that meets a set
#criteria.
#3. Once completed, the system will prompt the user to re-enter the password to ensure it is correct.
#4. Once the password has been confirmed, the system will prompt the user to login using the newly created username
# and password. An option to receive an email with the user's username or an email with a link to reset the password or
#will be provided if either are forgotten. If the incorrect password is entered 3 times, the account will be locked.

#Password must contain at least 1 capital letter, 1 number & 1 special character

username = input("Please enter a username between 5 & 20 characters. Your username must start with a letter.\n")

while len(username) <5 or len(username) >20 or not username[0].isalpha() or username.lower() == "username":
 username = input("Please enter a username between 5 & 20 characters. Your username must start with a letter.\n")
 if len(username) <5:
  print("Your username is too short")
 elif len(username) >20:
  print("Your username is too long")
 elif not username[0].isalpha():
  print("Your username must start with a letter")
 elif username.lower() == "username":
  print('"username" is an invalid name')
 else:
  break

print(f'Thanks, your username is {username}')

password = "Please enter a password. It must contain at least 1 capital letter, 1 number & 1 special character.\n"
while len(password) < 7 or len(password) >30 or (not password.islower() and not password.isupper()) \
 or ("[" not in password and "@" not in password and "_" not in password and "!" not in password and "#" not in password\
 and "$" not in password and "%" not in password and "^" not in password and "&" not in password and "*" not in password\
 and "(" not in password and ")" not in password and "<" not in password and ">" not in password and "?" not in password\
 and "/" not in password and "\\" not in password and "|" not in password and "{" not in password and "}" not in password\
 and "~" not in password and ":" not in password and "]" not in password and "0" not in password and "1" not in password\
 and "3" not in password and "4" not in password and "5" not in password and "6" not in password and "7" not in password\
 and "8" not in password and "9" not in password):
 password = input("please enter a password. It must contain a mix of upper & lower case letters, 1 number & 1 special character.\n")
 if len(password) <7:
  print("Your password is too short")
 elif len(password) >30:
  print("Your password is too long")
 elif password.islower() or password.isupper():
  print("Your password must contain a mix of upper and lower characters")
 elif "0" not in password and "1" not in password and "2" not in password and "3" not in password and "4" not in password\
  and "5" not in password and "6" not in password and "7" not in password and "8" not in password and "9" not in password\
  and "10" not in password:
  print("Your password must contain at least 1 number")
 elif "[" not in password and "@" not in password and "_" not in password and "!" not in password and "#" not in password\
 and "$" not in password and "%" not in password and "^" not in password and "&" not in password and "*" not in password\
 and "(" not in password and ")" not in password and "<" not in password and ">" not in password and "?" not in password\
 and "/" not in password and "\\" not in password and "|" not in password and "{" not in password and "}" not in password\
 and "~" not in password and ":" not in password and "]" not in password:
  print("Your password must contain at least 1 character")
 else:
  break

passwordConifrmation = "Please re-enter your password\n"
while passwordConifrmation != password:
 passwordConifrmation = input("Please re-enter your password\n")
 if passwordConifrmation != password:
  print("Your passwords do not match, please try again")
 else:
  break

print("Your passwords match! Your Username & Password have successfully been created.")





        



