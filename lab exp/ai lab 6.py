def vacuum_cleaner():
    # 0 represents Clean, 1 represents Dirty
    rooms = {'A': 1, 'B': 1} 
    
    def clean(room):
        if rooms[room] == 1:
            print(f"Room {room} is Dirty. Cleaning...")
            rooms[room] = 0
            print(f"Room {room} is now Clean.")
        else:
            print(f"Room {room} is already Clean.")

    print("Starting Vacuum Agent...")
    
    # Check and clean Room A
    print("\nAgent in Room A:")
    clean('A')
    
    # Move to Room B
    print("\nMoving to Room B:")
    clean('B')
    
    print("\nGoal State reached: All rooms are clean!")

vacuum_cleaner()
