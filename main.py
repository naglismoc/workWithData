from csv import DictReader

'''
atspausdinti kiek yra aktyvių ir neaktyvių vartotojų
nustatyti kokios yra pašto adresų galūnės, ir kiek pašto adresų su kiekviena galūne yra
nustatyti kokia procentinė dalis vartotojų yra iš Europos sąjungos
sukelti visus failo duomenis į duomenų bazės lentelę, ir keliant sutvarkyti telefono numerių formatus. formatas: 
635xxxxx
'''
activeCount = 0
entriesCount = 0
with open("./data/dmo dma data.csv") as file:
    data = DictReader(file)
    for user in data:
        entriesCount += 1
        if user['Active'] == "TRUE":
            activeCount += 1
        print(user)

print(f'{activeCount}/{entriesCount}')


print("============= opt 1 check =====================")

#nustatyti kokios yra pašto adresų galūnės, ir kiek pašto adresų su kiekviena galūne yra
# uniqueEmailDomains = set()
# with open("./data/dmo dma data.csv") as file:
#     data = DictReader(file)
#     for user in data:
#        print(user['Email'].split("@")[1])
#        uniqueEmailDomains.add(user['Email'].split("@")[1])
#
# print(len(uniqueEmailDomains))
# print(uniqueEmailDomains)

print("============= opt 1 count =====================")
emailTypes = {}
with open("./data/dmo dma data.csv") as file:
    data = DictReader(file)
    for user in data:
        userEmail = user["Email"]
        emailDomain = userEmail.split("@")[1]
        if emailDomain in emailTypes:
            emailTypes[emailDomain] = emailTypes[emailDomain] + 1
        else:
            emailTypes[emailDomain] = 1
print(emailTypes)
print("============= opt 2 =====================")

# nustatyti kokia procentinė dalis vartotojų yra iš Europos sąjungos
countries = [
    "Austria", "Belgium", "Bulgaria", "Croatia", "Republic of Cyprus", "Cyprus",
    "Czech Republic", "Denmark", "Estonia", "Finland", "France",
    "Germany", "Greece", "Hungary", "Ireland", "Italy",
    "Latvia", "Lithuania", "Luxembourg", "Malta",
    "Netherlands", "Poland", "Portugal", "Romania",
    "Slovakia", "Slovenia", "Spain", "Sweden"
]
entriesCount = 0
EUCount = 0
with open("./data/dmo dma data.csv") as file:
    data = DictReader(file)
    for user in data:
        entriesCount += 1
        if user['Country'] in countries:
            EUCount += 1
print(f'{EUCount}/{entriesCount} - {round(EUCount * (100 / entriesCount), 2)}% vartotojų yra iš Europos sąjungos')

print("============= opt 3 =====================")
with open("./data/dmo dma data.csv") as file:
    data = DictReader(file)
    for user in data:
        editedPhoNo = user['Phone Number'][-8:]
        if len(editedPhoNo) != 8 or editedPhoNo[0] != '6':
            print(user['Phone Number'], editedPhoNo, "bad")
        else:
            print(user['Phone Number'], editedPhoNo, 'good')

import re
print(re.sub("[ ()\-+]","","+370        ((((((((((6-35) 00000"))