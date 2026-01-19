while True:
    print("\n------ PASSWORD GENERATOR ------")
    print("1. Generate Password")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "2":
        print("Program exited!")
        break

    if choice == "1":
        length = int(input("Enter password length: "))

        print("\nSelect password complexity:")
        print("1. Letters only")
        print("2. Letters and numbers")
        print("3. Letters, numbers, and symbols")

        complexity = input("Enter password complexity choice: ")

        if complexity == "1":
            characters = string.ascii_letters
        elif complexity == "2":
            characters = string.ascii_letters + string.digits
        elif complexity == "3":
            characters = string.ascii_letters + string.digits + string.punctuation
        else:
            print("Invalid complexity choice entered!")
            continue

        password = ""
        for i in range(length):
            password += random.choice(characters)

        print("\nGenerated Password is:", password)

    else:
        print("Invalid option! Please try again.")
