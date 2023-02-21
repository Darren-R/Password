from passwordEntropy import PasswordEntropy
import passwordGenerate

def main():
    running = True

    while running:
        print("\n1. Generate new password")
        print("2. Check entropy of existing passwords")
        #print("3. ")
        print("4. Exit\n")

        choice = userChoice()
        if choice == '1':
            generateNew()
        elif choice == '2':
            entropy()
        #elif choice == '3':
        #    print('You input 3\n')
        elif choice == '4':
            print('Bye!\n')
            quit()
        else:
            print('Please input valid choice')

def generateNew():
    len = int(input("Input the max allowed charcter length: "))
    pw_gen = passwordGenerate.Generator(len)
    password = pw_gen.generate_password()
    while pw_gen.check_special_characters(password) == False:
        password = pw_gen.generate_password()
    print("Password is: " + password)
        


def entropy():
    pw = input("Input your password: ")
    password_entropy = PasswordEntropy(pw)
    print("Password entropy is: " + str(round(password_entropy.entropy(), 2)) + " bits\n")

    if password_entropy.entropy() <= 20:
        print("A password with less than 20 bits can be cracked within a second")
    elif password_entropy.entropy() <= 40:
        print("A password with an entropy of 40 bits would take about 1000 years to crack.")
    elif password_entropy.entropy() <= 60:
        print("A password with an entropy of 60 bits would take about 1 billion years to crack.")
    elif password_entropy.entropy() <= 80:
        print("A password with an entropy of 80 bits would take take about 1 quadrillion years to crack.")
    else:
        print("A password with a larger entropy would take over 1 quintillion years to crack")
    print("This number is for a single computer. With various techniques (distributed computing, botnets etc.) \nthe attacker could significantly reduce the time to break the password.")

def userChoice():
    choice = input()
    return choice

if __name__ == "__main__":
    main()