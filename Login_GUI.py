import tkinter as tk
import json

file_name = 'login_credentials.json'
def login(users):
    username = user_entry.get()
    password = password_entry.get()

    for user in users['users']:
        if user['username'] == username and user['password'] == password:
            print('Login Successful')
            label.config(text='Login Successful')
            
        user_entry.delete(0,tk.END)
        password_entry.delete(0, tk.END)
        

def create_account(users):
    username = user_entry.get()
    password = password_entry.get()
    
    if (not username and  not password ) or (not username and password) or (username and not password):
        print('Must Hve Both Username and Password')
        label.config(text='Must Have Both Username and Password')
        return
    for user in users['users']:
        if user['username'] == username:
            print("Username already exists")
            label.config(text="Username already exists")
            return

    users['users'].append({
        'username': username,
        'password': password
    })

    save(users)

    user_entry.delete(0, 'end')
    password_entry.delete(0, 'end')

    print("Account created")
    label.config(text='Account created')

def save(users):
    with open(file_name,'w') as file:
        json.dump((users ), file)

def load():
    with open(file_name, 'r') as file:
        return json.load(file)

users = load()

window = tk.Tk()
window.title('Login GUI')

user_label = tk.Label(window , text='Username: ',font=('Helvetica', 20) )
user_label.grid(row = 0 , column= 0)

user_entry = tk.Entry(window, font=('Helvetica', 20))
user_entry.grid(row=0, column=1,columnspan=2)

password_label = tk.Label(window , font=('Helvetica', 20) , text='Password: ')
password_label.grid(row=1 , column= 0)

password_entry = tk.Entry(window, font=('Helvetica', 20))
password_entry.grid(row=1, column=1,columnspan=2)

login_btn = tk.Button(window,text='Login',  font=('Helvetica', 20), fg='#0353d3', 
                      bg='#edfd0d', command=lambda x = users:login(x))
login_btn.grid(row= 2 , column= 0)

createAcc_btn = tk.Button(window, text='Create Account' , font=('Helvetica', 20), command=lambda x = users:create_account(x))
createAcc_btn.grid(row= 2 , column= 1)

label = tk.Label(window ,text='', font=('Helvetica', 20))
label.grid(row= 3 , column=0 , columnspan=2)


window.mainloop()