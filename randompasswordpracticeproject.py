import random
import string

def password(n):
   chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
   return ''.join(random.choice(chars) for _ in range(n))
print(password(10))