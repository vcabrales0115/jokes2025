
username= input("Please enter a username:")
print(f"Hello,{username}!")

def play_jokes():
    
    joke = input("Do you want to hear a joke? : ").lower()
    
    if joke == "no":
        print("Okay, suit yourself!")
        return

   
    while joke == "yes":
        topics = ["robbers", "tanks", "pencils"]
        print(f"Available topics: {topics}")
        
        choice = input("Pick a topic: ").lower()

        if choice == "robbers":
            input("Knock Knock")
            input("Calder")
            print("Calder police - I've been robbed!")
        elif choice == "tanks":
            input("Knock Knock")
            input("Tank")
            print("You're welcome!")
        elif choice == "pencils":
            input("Knock Knock")
            input("Broken pencil")
            print("Nevermind, it's pointless!")
        else:
            print("That topic isn't in the list!")

        joke = input("Do you want to hear another joke or are you finished? : ").lower()

    # Feedback section
    if joke == "finished":
        try:
            rate = int(input("Please rate our game 1-10: "))
            final_score = rate * 10
            print(f"{final_score}% satisfaction rate!")
        except ValueError:
            print("Thanks for playing!")

        friend = input("Would you recommend this game to a friend? : ").lower()
        if friend == "yes" or friend == "maybe":
            print("Thanks, we appreciate it!")
        else:
            print("Sorry you didn't enjoy it.")


play_jokes()


