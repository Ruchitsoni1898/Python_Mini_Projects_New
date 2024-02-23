master_pwd = input("what is the master password?")

def view():
    with open("password.txt", 'r') as f:
     for line in f.readlines():
        data = line.rstrip()
        if "|" in data:
            user, passw = data.split("|")
            print("User:", user, "| Password:", passw)
def add():
    name = input("Account Name:")
    pwd = input("Password:")
    with open("password.txt",'a')as f:
        f.write(name + "|" + pwd + "\n")
    pass
while True:
 mode = input("would you like to add a new password or view existing ones(view,add),press q to quit?".lower())
 if mode == "q":
     break
 if mode == "view":
     view()
 elif mode == "add":
     add()
 else:
    print("Invalid mode.")
    continue

