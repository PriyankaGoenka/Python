username=input("Enter the username: ")
password=input("Enter the password: ")
re_enter_P=input("Re-enter your password: ")
for i in range(3):
    if re_enter_P!=password:
        re_enter_P=input("Re-enter your password: ")
