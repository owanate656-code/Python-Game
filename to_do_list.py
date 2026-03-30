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

def view_task(tasks):
    task_list = tasks['tasks']
    if len(task_list) == 0:
        print('There are no task to view')
    else:
        for i , task in enumerate(task_list):
            if task['complete']== False:
                task['complete'] = 'Pending'
            else:
                task['complete'] = 'Completed'
            print(f'{i+1}. {task['description']} | Status: {task['complete']}')




def create_task(tasks):
    description = input('Enter description of task: ')
    if description:
        tasks['tasks'].append({'description':description, 'complete':False})
        print('Tasks has been created successfully')
    save_task(tasks)

def mark_task_complete(tasks):
    view_task(tasks)
    try :
         task_no = int(input('Which task would you like to complete: '))
         if 1 <= task_no <= len(tasks):
             tasks['tasks'][task_no-1]['complete'] = True
             print('Task Marked Complete')
    except:
        print('Error Invalid number')
    save_task(tasks)
    
def delete_task(tasks):
    view_task(tasks)
    
    task_no = int(input('Which task would you like to delete: '))
    if 1 <= task_no<= len(tasks):
        del tasks['tasks'][task_no-1]
    else:
        print('Error Invalid Number')
    save_task(tasks)
def main():
    tasks =load_task()
    
    
    
    while True:
        print('\n To Do List Managaer')
        print('1. View Tasks')
        print('2. Add Task')
        print('3. Complete Task')
        print('4. Delete Tasks')
        print('5. Exit')

        choice = input('Which action would you like to pick: ')
        if choice == '1':
            view_task(tasks)
        elif choice =='2':
            create_task(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice =='5':
            print('Closing...')
            break
        else:
            print('Type a valid number')

main()