# 📞 Welcome to Kalab’s Contact Book 📞

# 1. Add Contact
# 2. Show All Contacts
# 3. Search Contact
# 4. Delete Contact
# 5. Save & Quit

# Enter your choice: 1
# Enter name: Sara
# Enter phone: 0911223344
# ✅ Contact added successfully!

# Enter your choice: 1
# Enter name: Robel
# Enter phone: 0988776655
# ✅ Contact added successfully!

# Enter your choice: 2
# 📋 Your contacts:
# 1. Sara - 0911223344
# 2. Robel - 0988776655

# Enter your choice: 3
# Search name: Robel
# 🔍 Found: Robel - 0988776655

# Enter your choice: 5
# 💾 Contacts saved to file.
# 👋 Goodbye!
print("📞 Welcome to Kalab’s Contact Book 📞")
print("1. Add Contact")
print("2. Show All Contacts")
print("3. Search Contact")
print("4. Delete Contact")
print("5. Save & Quit")
my_list=[]
try:
    with open("my_list.txt","r")as file:
        for line in file:
            name, phone =line.strip().split()
            my_list.append((name, phone))
            print(" do ")
except FileNotFoundError:
    print(" you do have file refreash it to see it a gain ")

while True:
    chooce=int(input("Enter your choice: "))
    if chooce==1:

       name=input("enter you contact name: ")
       phone=int(input("enter the phone number: "))
       my_list.append((name,phone))
       print("✅ Contact added successfully!")
    elif chooce==2:
        for i,(name,phone) in enumerate(my_list,1):
            print(f"{i}.{name}-{phone}")
    elif chooce==3:
        search=input("enter the contact name want to find: ")
        found=False
        for name,phone in my_list:
          if name==search:
            print(f"{name}-{phone}")
            found=True
        if not found:
            print(f"we can't find the name that match")
            found=False
    elif chooce==4:
        for i,(name,phone) in enumerate(my_list,1):
            print(f"{i}.{name}-{phone}")
        delet=int(input("enter the witch number you want to delet"))
        my_list.pop(delet-1)
        print(f"dleted secsesfuly")
    elif chooce==5:
        print("💾 Contacts saved to file.")
        print("👋 Goodbye!")
        break