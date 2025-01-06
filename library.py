import pandas as pd
import os
user_name = []
user_password = []

# Function to create a new user
def create_user(name, password):
    user_name.append(name)
    user_password.append(password)
    user_diction = {"Name": user_name, "Password": user_password}
    user_df = pd.DataFrame(user_diction)
    if os.path.exists("users.csv"):
        user_df.to_csv("users.csv", index=False, mode="a", header=False)
    else:
      user_df.to_csv("users.csv", index=False)
    return "Account created successfully"

# Function to log in
def login(name, password):
    user_df = pd.read_csv("users.csv")
    if name in user_df['Name'].to_list():
        user_index = user_df[user_df['Name'] == name].index[0]
        if password == user_df.loc[user_index, 'Password']:
            return "Login successful"
        else:
            return "Incorrect password"
    else:
        return "User not found"

