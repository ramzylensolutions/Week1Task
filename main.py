# Inside main.py
from MiniProject.filters.filters import MinimumEmployeeCompany, MaximumEmployeeCompany, ParticularDomainFind, ParticularIndustryFind
from MiniProject.jsonread import companies
print(f"The Companies which is having minimum no of employees are {MinimumEmployeeCompany(companies)}")
print()
print(f"The Companies having maximum no of emplopyees are {MaximumEmployeeCompany(companies)}")
print()
print(ParticularIndustryFind(companies))
print()
print(ParticularDomainFind(companies))
print("This is the changes from branch1")
print("This is from branch2")
name = "Ram Mrithyun Jay"