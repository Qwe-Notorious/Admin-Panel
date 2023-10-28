import pandas as pd
import numpy as np

# info = input()
# pas = input()

# username = ["Log_in", "Qwe", "Emorty"]
# password = ["6784091Log_in{", "4931058Qwe}", "6783959Emorty>"]


def Beases():

    # usernameDict = {
    #     'username': username,
    #     'password': password
    # }
    #
    # username_df = pd.DataFrame(usernameDict)
    # username_df.index = ['a', 'b', 'c']
    #
    # print(username_df.index)

    # username_df.to_csv('accaunts.csv', index=False)

    userData = pd.read_csv('../accaunts.csv')
    df = pd.DataFrame(userData)

    print('Login Tols\n')
    user = input('Username: ')
    pasw = input('Passwoeds: ')

    matching_creds = (len(df[(df.username == user) & (df.password == pasw)]) > 0)

    if matching_creds:
        print('success')
    else:
        print('\nYour accaunt is not registerad yet!')

obj = Beases()
