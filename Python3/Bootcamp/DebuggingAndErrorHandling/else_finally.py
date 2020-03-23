while True:
    try:
        num = int(input("please enter a number: "))
    except ValueError:
        print("That is not a number!")
    else:
        print("Good job, you entered a number!")
        break
    finally:
        print("RUNS NO MATTER WHAT!")
print("REST OF GAME LOGIC RUNS!")