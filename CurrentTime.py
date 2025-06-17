# # This script defines a function to get the current time in a specific format.
def get_current_time():
    from datetime import datetime
    return datetime.now().strftime("%d %B %I:%M:%S %p")

print(get_current_time())