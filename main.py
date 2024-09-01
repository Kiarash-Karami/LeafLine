from timer import countdown_timer

# Display a welcome message to the user
print("Welcome to LeafLine 🌿!")

# Prompt the user to enter the duration of their focus session in minutes
minutes = int(input("How long would you like to focus today? Please enter the time in minutes: "))

# Inform the user that their focus session is starting
print("Awesome! Your focus session is starting now. Let's grow your productivity! 🌱")

# Call the countdown_timer function with the user-provided duration
countdown_timer(minutes)
