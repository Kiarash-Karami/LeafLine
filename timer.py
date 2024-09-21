import time
import os

def start_timer(duration):
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        remaining_time = max(duration - elapsed_time, 0)
        progress = min(elapsed_time / duration, 1)

        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\rLeafLine 🌿 | Timer: {int(remaining_time)}", end="")

        if remaining_time <= 0:
            break

        time.sleep(1)

    actual_duration = int(time.time() - start_time)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Time's up! Your tree is fully grown.")
    return actual_duration
