# Function to create a badge message for a given name
def badge_maker(name):
    return f"Hello, my name is {name}."

# Function to create a list of badge messages for a list of names
def batch_badge_creator(names):
    return [badge_maker(name) for name in names]

# Function to assign rooms to speakers and create a list of room assignments
def assign_rooms(speakers):
    room_assignments = []
    for i, speaker in enumerate(speakers, start=1):
        room_assignment = f"Hello, {speaker}! You'll be assigned to room {i}!"
        room_assignments.append(room_assignment)
    return room_assignments

# Function to print badge messages and room assignments
def printer(names):
    badges = batch_badge_creator(names)
    room_assignments = assign_rooms(names)
    
    for badge in badges:
        print(badge)
    
    for assignment in room_assignments:
        print(assignment)

# Example usage
speakers = ["Arel", "Carol"]
printer(speakers)
