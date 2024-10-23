from csv import DictReader

import mysql.connector


conn = mysql.connector.connect(
    host="127.0.0.1", # localhost
    user='root',
    password='', #rašot savo
    database="dma_users"#rašot savo
)

c = conn.cursor()
##### Jeigu reikia, kad sukurtų lentelę duomenų bazėje. Duomenų bazę kuriame patys#####
c.execute('''CREATE TABLE IF NOT EXISTS users (
    id BIGINT(20) AUTO_INCREMENT PRIMARY KEY,
    User VARCHAR(255),
    Email VARCHAR(255),
    Phone VARCHAR(8) CHECK (LENGTH(Phone) = 8),
    Country VARCHAR(255),
    Active TINYINT(1)
)''')
conn.commit()



print("============= opt 3 =====================")
with open("./data/dmo dma data.csv") as file:
    data = DictReader(file)
    for user in data:
        editedPhoNo = user['Phone Number'][-8:]
        if len(editedPhoNo) != 8 or editedPhoNo[0] != '6':
            print(user['Phone Number'], editedPhoNo, "bad")
            with open("data/badEntries.txt", 'a') as failas:
                failas.write(f'{user['User']},{user['Email']},{user['Phone Number']},{user['Country']},{user['Active']}\n')
        else:
            print(user['Phone Number'], editedPhoNo, 'good')
            query = ("INSERT INTO `users`(`User`, `Email`, `Phone`, `Country`, `Active`) VALUES ( %s, %s, %s, %s, %s)")
            c.execute(
                query, (
                    user['User'],
                    user['Email'],
                    editedPhoNo,
                    user['Country'],
                    True if user['Active'] == "TRUE" else False
                )
            )
            conn.commit()