import os
from nick import create_nick


def user_exist(nickname):
    # should raise error if user exist


    # testa
    try:
        with open('usernicks.csv') as usernicksfile:
            for row in usernicksfile.readlines():
                # split line on ","
                user = row.strip().split(',')
                if user[2] == nickname:
                    return True
    except IOError as err:  # if no usernicksfile, generates error

        return False

    return False


def adduser(firstname,lastname,nickname):

    # TODO change to adduser in some computer

    #check if user is in usernicksfile

    if user_exist(nickname):
        message = 'user exist ' + nickname + ' on adding ' + firstname + ' ' + lastname
        raise StandardError(message)
    else:

        # write user and nickname to file, a is append
        with open('usernicks.csv', 'a') as usernicksfile:
            # create the line, '\n' is newline
            line = firstname + ',' + lastname + ',' + nickname + '\n'
            usernicksfile.write(line)




# remove usernicks.csv if it exist

try:
    os.remove('usernicks.csv')
except:
    pass # do nothing



# adding user from file
# open user csv file
with open('users.csv') as userfile:
    # read the lines
    for row in userfile.readlines():
        # split line on ","
        user = row.strip().split(',')
        # assign values
        firstname = user[0]
        lastname = user[1]

        # call create_nick to build a username
        nickname = create_nick(firstname, lastname)

        try:
            adduser(firstname,lastname,nickname)
        except Exception as err:
            # try to add a number on nickname
            print err






