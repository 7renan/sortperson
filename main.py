import commands
from controllers.participant_controller import route as participants_routes

run = True

while run:
    command = input('Comando: .. ')
    if command in commands.EXIT:
        run = False
    elif command.split(' ')[0] in commands.PARTICIPANTS:
        participants_routes(command.split(' ')[1])


