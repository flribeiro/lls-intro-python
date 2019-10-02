# sudo chmod +x generate_secret_key.py
# python generate_secret_key.py
import random
import string
print(''.join([random.SystemRandom().choice("{}{}{}".format(string.ascii_letters, string.digits, string.punctuation)) for i in range(50)]))
