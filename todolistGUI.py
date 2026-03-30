import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox as msg
import json


file_name = 'to_do_list.json'



def load_task():
    try:
        with open(file_name , 'r') as file:
            return json.load(file)
            
    except:
       return {'tasks':[]}


def save_task(tasks):
    with open(file_name , 'w') as file:
        return json.dump(tasks , file)

def add(task):
    text = entry.get()
    if text:
        task_list = task['tasks']
        task_list.append({'description': text, 'complete':False})
        lists.delete(0, tk.END)
        view(task)
        entry.delete(0, tk.END)
        save_task(task)
task= load_task()            

def view(tasks):
    task_list = tasks['tasks']
    for i , task in enumerate(task_list):
        task_desc = task_list[i]['description']
        if task_list[i]['complete']== True:
            lists.insert(tk.END,(f'☑ {i+1}. {task_desc}'))
        elif task_list[i]['complete']== False:
            lists.insert(tk.END,(f'☐ {i+1}. {task_desc}'))
            
            
def mark_task_complete(e):
    task_list = task['tasks']
    index = lists.curselection()
    
    if index:
        idx = index[0]
        task_list[idx]['complete']= not task_list[idx]['complete']
        # task_list.pop(idx)
        lists.delete(0, tk.END)
    
    view(task)
    save_task(task)
def delete_task(e):
    
    index = lists.nearest(e.y)
    print(index)
    if index:
        question=msg.askquestion(title='Delete', message='Would you like to delete this task')
        if question== 'yes':
            task['tasks'].pop(index)
            lists.delete(0, tk.END)
            view(task)
        else:
            lists.delete(0, tk.END)
            view(task)      
    
    save_task(task)

def main():
    view(task)
    


#-------------Window Setup------------
window = tk.Tk()
window.title('To Do List')
normal_font = tkFont.Font(family='Arial', size=12)
over_strike = tkFont.Font(family = 'Arial' ,size=12, overstrike=1)
window.title('To Do List')

entry = tk.Entry(window, width=10 , font=('Arial', 10))
entry.grid(row= 0 , column= 0)

add_btn = tk.Button(window , text= 'Add', font=('Arial', 10), command= lambda x=task:add(x))
add_btn.grid(row=0 , column=1)

lists= tk.Listbox(window , bg='#c5feb4',bd=1 , highlightthickness=1,height=10)
lists.bind('<<ListboxSelect>>', mark_task_complete)
lists.grid()
lists.bind("<Button-3>",delete_task)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
main()

window.update()
window_width = 250
window_height =  250

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2)-(window_width/2))
y = int((screen_height/4)- (window_height/4))

window.geometry(f'{ window_width}x{window_height}+{x}+{y}')
window.config(bg='#c5feb4')
window.mainloop()   