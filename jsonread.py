import json
companies={}
try:
    with open("MiniProject/companies.json","r") as files:
        companies = json.load(files)
except json.JSONDecodeError:     #load companieswrongformat.json for checking the exception working
    print("Give the correct formatted JSON file!!")
except FileNotFoundError:
    print("Check for the file or check the JSON File Name!!")
    