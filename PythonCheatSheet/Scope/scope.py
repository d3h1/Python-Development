######## SCOPE ###########
enemies = 1 #! Global

def increase_enemies():
    enemies = 2 #! Local
    print(f'Enemies inside the function: {enemies}')
    
increase_enemies()

print(f'Enemies outside the function: {enemies}')

    