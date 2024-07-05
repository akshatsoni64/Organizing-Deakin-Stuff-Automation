# I used this script to carve out list of deadline for the tasks. I personally follow my tracker to stay updated on assignment deadlines.

true = True
false = False
null = None

def print_required(data):
    print(data.keys())
    print(*list(f"{task['abbreviation']} - {task['target_date']}" for task in data['task_definitions']), sep='\n')
    print(*list(f"{task['target_date']}" for task in data['task_definitions']), sep='\n')

data = {"TO-DO": "Grab API Response from OnTrack Task List API (3 Digit Number)"}

print_required(data)
