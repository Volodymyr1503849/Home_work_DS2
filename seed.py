import faker
import sqlite3
from random import randint

number_of_users = 10
number_of_status = 3
number_of_task = 40 

def create_fake_data(number_of_users,number_of_task):
    fake_data = faker.Faker()
    fake_users = [fake_data.name() for _ in range(number_of_users)]
    fake_email = [fake_data.email() for _ in range(number_of_users)]
    fake_task = [fake_data.job() for _ in range(number_of_task)]
    fake_descript = [fake_data.text(10) for _ in range(number_of_task)]
    return fake_users, fake_email, fake_task, fake_descript

def prepare_data(fake_users, fake_email, fake_task, fake_descript):
        status_data = [('new',), ('in progress',), ('completed',)]
        users_data = [(usr,email) for usr,email in zip(fake_users,fake_email)]
        task_data = [(task,descript,randint(1,number_of_status), randint(1,number_of_users))for task,descript in zip(fake_task,fake_descript)] 
        return users_data, status_data,task_data

def insert_data_to_db(users_data, status_data, task_data) -> None:
    with sqlite3.connect('tasks.db') as con:
        cur = con.cursor()

        sql_to_users = """INSERT INTO users(fullname, email) VALUES (?, ?)"""
        cur.executemany(sql_to_users, users_data )

        sql_to_status = """INSERT INTO status(name) VALUES (?)"""
        cur.executemany(sql_to_status, status_data)

        sql_to_task = """INSERT INTO tasks(title, description, status_id, users_id) VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_to_task, task_data)

        con.commit()
    
if __name__ == "__main__":
     fake_users, fake_email, fake_task, fake_descript = create_fake_data(number_of_users,number_of_task)
     users_data, status_data, task_data = prepare_data(fake_users, fake_email, fake_task, fake_descript)
     insert_data_to_db(users_data, status_data, task_data)

