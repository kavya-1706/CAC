#!/usr/bin/env python
# coding: utf-8

# In[5]:


import csv
def createAccount(email, password):
    lst = [email, password]
    acc_created=False
    with open("EmailDetails.csv", "r", newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)
    for row in rows:
        if len(row) > 0 and email == row[0]:
            print("EMAIL ALREADY EXISTS!")
            return
    with open("EmailDetails.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(lst)
        print("ACCOUNT CREATED")
        acc_created=True
        return acc_created
        
def addToFiles(email): 
    with open("Inbox.csv", "a+", newline="") as f:
        reader = csv.reader(f)
        writer = csv.writer(f)
        rows = list(reader)
        if rows:
            existing_row = rows[0]
            existing_row.append(email)
            f.seek(0)  
            writer.writerow(existing_row)
        else:
            writer.writerow([email])
        f.close()
        
    with open("Outbox.csv", "a+", newline="") as f:
        reader = csv.reader(f)
        writer = csv.writer(f)
        rows = list(reader)
        if rows:
            existing_row = rows[0]
            existing_row.append(email)
            f.seek(0)  
            writer.writerow(existing_row)
        else:
            writer.writerow([email])
        f.close()
        
def addColName():
    with open("EmailDetails.csv", "a+") as f:
        f.seek(0)  
        reader = csv.reader(f)
        rows = list(reader)
        if len(rows) == 0 or (rows[0][0] != "Email" or rows[0][1] != "Password"):
            col_head = ['Email', 'Password']
            f.seek(0)  
            writer = csv.writer(f)
            writer.writerow(col_head)
                
def login(email, password):
    login_successful = False
    with open("EmailDetails.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) >= 2 and row[0] == email and row[1] == password:
                login_successful = True
                break
        f.close()
        return login_successful

def check_email_existence(email):
    a=False
    b=False
    with open("Inbox.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == email:
                a=True

    with open("Outbox.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == email:
                b=True

    if a==True and b==True:
        return True
    else:
        return False


def sendEmail(user, receiver, subject, msg):
    mail = [user, receiver, subject, msg]

    if not check_email_existence(receiver):
        print("EMAIL DOES NOT EXIST")
        return
    rows = []
    with open("Inbox.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == receiver:
                row.append(mail)
            rows.append(row)
    with open("Inbox.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    rows = []
    with open("Outbox.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == user:
                row.append(mail)
            rows.append(row)
    with open("Outbox.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print("EMAIL SENT!")

        
def readInbox(email):
    with open("Inbox.csv","r") as f:
        reader=csv.reader(f)
        c=0
        for row in reader:
            if row[0]==email:
                print("INBOX FOR-",email)
                for i in reversed(range(1,len(row))):
                    c+=1
                    row[i]=eval(row[i])
                    print("**************************")
                    print("From:",row[i][0])
                    print("Subject:",row[i][2])
                    print("Message:",row[i][3])
                    print("**************************")
        if c==0:
            print("NO EMAILS RECEIVED YET!")
            
def readOutbox(email):
    with open("Outbox.csv","r") as f:
        reader=csv.reader(f)
        c=0
        for row in reader:
            if row[0]==email:
                print("Outbox for-",email)
                for i in reversed(range(1,len(row))):
                    c+=1
                    row[i]=eval(row[i])
                    print("**************************")
                    print("To:",row[i][1])
                    print("Subject:",row[i][2])
                    print("Message:",row[i][3])
                    print("**************************")
        if c==0:
            print("NO EMAILS SENT YET!")
                
def logout(): 
    print("LOGGED OUT!")
        
def main():
    print("***EMAIL SYSTEM***")
    with open("Inbox.csv",'a+') as f:
        f.close()
    with open("Outbox.csv",'a+') as f:
        f.close()
    addColName()
    while True:
        print("1. Create a new account")
        print("2. Login")
        print("0. Exit")
        ch = int(input("Choose an option:"))
        if ch == 1:
            print("CREATE A NEW ACCOUNT")
            email = input("Enter Email:")
            password = input("Enter Password:")
            res=createAccount(email, password)
            if res:
                addToFiles(email)
        elif ch == 2:
            print("LOGIN")
            email = input("Enter Email:")
            password = input("Enter Password:")
            login_success=login(email, password)
            if login_success:
                print("LOGGED IN!")
            else:
                print("WRONG EMAIL OR PASSWORD!")
                continue
            while True:
                print("1. Send Email")
                print("2. Open Outbox")
                print("3. Open Inbox")
                print("4. Logout")
                user=email
                ch1=int(input("Enter choice:"))
                if ch1==1:
                    receiver=input("Enter Receiver's Email:")
                    if user==receiver:
                        print("YOU ARE ENTERING YOUR OWN EMAIL ID. INVALID!")
                    else:
                        subject=input("Enter Subject Of The Email:")
                        msg=input("Enter Message Of The Email:")
                        sendEmail(user,receiver,subject,msg)
                elif ch1==2:
                    readOutbox(user)
                elif ch1==3:
                    readInbox(user)
                elif ch1==4:
                    logout()
                    break
                else:
                    print("WRONG CHOICE ENTERED!")
        elif ch == 0:
            print("EXIT")
            break
        else:
            print("WRONG CHOICE ENTERED!")

main()


# In[ ]:





# In[ ]:




