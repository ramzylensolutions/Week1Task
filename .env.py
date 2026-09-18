import os
from dotenv import load_dotenv

load_dotenv()

name = os.getenv("name")
password = os.getenv("passs")

print(name)
print(password)