import mysql.connector

cnx = mysql.connector.connect(user='root', password='Knitin@sql123',
                              host='127.0.0.1',
                              database='blogmanagementdb')

cursor =  cnx.cursor()

# User Authentication
def register_user(username, password):
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    cnx.commit()
    print('User registered successfully.')

def login_user(username, password):
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    if user:
        print('Login successful.')
        return user
    else:
        print('Invalid credentials.')
        return None

# Blog Post Management
def create_post(title, content, user_id, category_id):
    cursor.execute('INSERT INTO posts (title, content, user_id, category_id) VALUES (?, ?, ?, ?)', (title, content, user_id, category_id))
    cnx.commit()
    print('Post created successfully.')

def view_posts():
    cursor.execute('SELECT * FROM posts')
    posts = cursor.fetchall()
    for post in posts:
        print(f'Title: {post[1]}\nContent: {post[2]}\n')

# Category Management
def create_category(name):
    cursor.execute('INSERT INTO categories (name) VALUES (?)', (name,))
    cnx.commit()
    print('Category created successfully.')

