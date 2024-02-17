while True:
    a = (input("Enter a number: "))
    if a =="q":
        break
    try:
        a=int(a)
        if a > 6:
            print("You have entered a number greater than 6")
    except Exception as e:
        print(f"Your input resulted in an error: {e}")
print("Thanks for playing this game")
