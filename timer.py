import time

def countdown_timer(minutes):
    """
    A countdown timer that takes the specified number of minutes and counts down to zero.

    Args:
    minutes (int): The number of minutes for the countdown timer.
    """
    # Convert minutes to total seconds
    total_time = minutes * 60
    elapsed_time = 0

    # Loop until the elapsed time exceeds the total time
    while elapsed_time <= total_time:
        # Calculate remaining time
        remaining_time = total_time - elapsed_time
        # Convert remaining time to minutes and seconds
        mins, secs = divmod(remaining_time, 60)
        # Format the timer string
        timer = '{:02d}:{:02d}'.format(mins, secs)

        # Print the timer, keeping the output on the same line
        print(f"\rStay Focused 🌿 | Timer: {timer}", end="")

        # Wait for one second
        time.sleep(1)
        # Increment the elapsed time by one second
        elapsed_time += 1

    # Print a message when the timer reaches zero
    print("\rStay Focused 🌿 | Timer: 00:00 | Time's up! 🎉")
