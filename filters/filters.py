from typing import Any
def MinimumEmployeeCompany(companies:dict[str:Any])->list[str]:
    list = [company["name"] for company in companies if company["Employees"]<1000]
    return list
def MaximumEmployeeCompany(companies:dict[str:Any])->list[str]:
    list = [company["name"] for company in companies if company["Employees"]>10000]
    return list
def ParticularIndustryFind(companies:dict[str:Any])->list[str]:
    Industry = input("Enter the Industry of the companies you want: ")
    list =  [company["name"] for company in companies if company["industry"]==Industry]
    print(f"The Companies which are all having it's Industry as {Industry} are ",end='')
    return list
def ParticularDomainFind(companies:dict[str:Any])->list[str]:
    Domain = input("Enter the Industry of the companies you want: ")
    list =  [company["name"] for company in companies if company["Domain"]==Domain]
    print(f"The Companies which are all having it's Domain as {Domain} are ",end='')
    return list
if __name__ == "__main__":
    print("This is Filters.py file")
    print("This is branch 1 changes")
