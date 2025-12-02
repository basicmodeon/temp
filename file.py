import pyodbc
import tkinter 
conn=pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'Trusted_Connection=yes;'
)
cursor=conn.cursor()
cursor.execute('''
               IF OBJECT_ID('students','U') IS NULL
               CREATE TABLE students(
               id INT IDENTITY(1,1) PRIMARY KEY,
               name NVARCHAR(50),
               age INT,
               grade NVARCHAR(10)
               )''')
conn.commit()
print("Table 'students' checked/created successfully!")


window=tkinter.Tk()
window.geometry("400x600")

# Input
idLabel=tkinter.Label(window,text="ID (Only for Update/Delete)")
idLabel.pack()
idInput=tkinter.Entry(window)
idInput.pack()

name=tkinter.Label(window,text="Name")
name.pack()
nameInput=tkinter.Entry(window)
nameInput.pack()

age=tkinter.Label(window,text="Age")
age.pack()
ageInput=tkinter.Entry(window)
ageInput.pack()

grade=tkinter.Label(window,text="Grade")
grade.pack()
gradeInput=tkinter.Entry(window)
gradeInput.pack()


# Functions
def add_student():
    n = nameInput.get()
    a = ageInput.get()
    g = gradeInput.get()

    cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (n, a, g))
    conn.commit()

def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    win = tkinter.Toplevel(window)
    text = tkinter.Text(win, width=50, height=20)
    text.pack()

    for r in rows:
        text.insert("end", f"{r.id} - {r.name} - {r.age} - {r.grade}\n")

def update_student():
    sid = idInput.get()
    n = nameInput.get()
    a = ageInput.get()
    g = gradeInput.get()

    cursor.execute("UPDATE students SET name=?, age=?, grade=? WHERE id=?",
                   (n, a, g, sid))
    conn.commit()

def delete_student():
    sid = idInput.get()
    cursor.execute("DELETE FROM students WHERE id=?", (sid,))
    conn.commit()


# Button

addBtn=tkinter.Button(window,text="Add Button", command=add_student)
addBtn.pack()

viewBtn=tkinter.Button(window,text="View Button", command=view_students)
viewBtn.pack()

updateBtn=tkinter.Button(window,text="Update Button", command=update_student)
updateBtn.pack()

deleteBtn=tkinter.Button(window,text="Delete Button", command=delete_student)
deleteBtn.pack()

window.mainloop()


