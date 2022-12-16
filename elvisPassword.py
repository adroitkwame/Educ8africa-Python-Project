import secrets
import string

numerals = string.digits
alphabets = string.ascii_letters
character_set = string.punctuation

#combining the 3 sets to give a good password
initial_password = alphabets + numerals + character_set

#Password length is 20 to make it harder to crack
password_length = 20

#Checking to make sure password has atleast to punctuation characters
#The password is randomized to improve its security
while True:
  user_password = ''
  for i in range(password_length):
    user_password += ''.join(secrets.choice(initial_password))

  if (any(char in character_set for char in user_password) and 
      sum(char in numerals for char in user_password)>=2):
          break

print("Your Random Password is: " + user_password)
print("Please Do not share your password with anyone")