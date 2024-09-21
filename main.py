from timer import start_timer
from db import init_db, add_tree, get_tree_count, get_total_focus_time

def display_forest_stats():
    tree_count = get_tree_count()
    total_focus_time = get_total_focus_time()
    print(f"\nYour forest has {tree_count} trees!")
    print(f"Total focus time: {total_focus_time // 60} minutes")

def main():
    init_db()
    print("Welcome to the Forest Productivity Timer!")
    display_forest_stats()
    minutes = int(input("\nEnter the number of minutes for your focus session: "))
    start_timer(minutes * 60)
    add_tree(minutes * 60)
    print("\nGreat job! A new tree has been added to your forest.")
    display_forest_stats()

if __name__ == "__main__":
    main()
