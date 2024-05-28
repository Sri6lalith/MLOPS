
for km in range(1, 6):
    if km == 5:
        print(f"You have completed {km} km. Congratulations! You finished the race.")
        break
    ans = input(f"You have completed {km} km. Are you tired? (yes/no): ").strip().lower()
    if ans == "yes":
        print("You didn't finish the race.")
        break
    elif ans == "no":
        continue
    else:
        print("Invalid input. Please reply with 'yes' or 'no'.")
