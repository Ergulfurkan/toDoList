import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    #consturactor
    def __init__(self):
        print("start")

    def write_in_file(self, file_name, write_to_in_file):
        with open(file_name, "a") as file:
            write_to_in_file = write_to_in_file + "\n"
            file.write(write_to_in_file)

    def read_from_file(self, file_name):
        with open(file_name, "r") as file:
            tasks = file.readlines()
            return tasks

    def delete_all_written(self, file_name):
        with open(file_name, "w") as file:
            file.write("")

    def add_completed_status_to_line(self, line_number):
        with open("tasks.txt", "r") as file:
            lines = file.readlines()

        if 1 <= line_number <= len(lines):
            lines[line_number - 1] = lines[line_number - 1].rstrip('\n') + " -TAMAMLANDI\n"

            with open("tasks.txt", "w") as file:
                file.writelines(lines)
            print(f"{line_number}. satırın sonuna 'tamamlandı' eklendi.")
        else:
            print("Belirtilen satır numarası geçerli değil.")

#list içine dosyayı yazar
def update_listbox():
    tasks_content = deneme.read_from_file("tasks.txt")
    liste.delete(0, tk.END)
    for task in tasks_content:
        liste.insert(tk.END, task.strip())

deneme = ToDoListApp()

interface = tk.Tk()
interface.title("TO DO LIST")
interface.geometry("550x600")

interface.configure(bg="#43766C")

liste = tk.Listbox(interface, width=30, height=20, bg="#F8FAE5")
liste.place(x=200, y=200)

text = tk.Entry(interface, width=30)
text.place(x=200, y=160)

addButton = tk.Button(interface, text="Add Task", command=lambda: on_add_task(), bg="#B19470", width=15)
addButton.place(x=200, y=20)

registerButton = tk.Button(interface, text="Completed Task", command=lambda: on_register_task(), bg="#B19470", width=15)
registerButton.place(x=200, y=70)

deleteButton = tk.Button(interface, text="Delete All Tasks", command=lambda: on_delete_all_tasks(), bg="#76453B", width=15)
deleteButton.place(x=200, y=120)

lbl = tk.Label(interface, text="Yapılacaklar", bg="#43766C", fg="white")
lbl.place(x=200, y=180)
#"tasks.txt" içine girilen görevi yazar
def on_add_task():
    task_text = text.get()
    if task_text:
        deneme.write_in_file("tasks.txt", task_text)
        update_listbox()
        text.delete(0, tk.END)
    else:
        messagebox.showwarning("Uyarı", "Görev boş olamaz!")
#tıklanan görevin sonuna -TAMAMLANDI yazısı ekletir
def on_register_task():
    selected_task_index = liste.curselection()
    if selected_task_index:
        deneme.add_completed_status_to_line(selected_task_index[0] + 1)
        update_listbox()
    else:
        messagebox.showwarning("Uyarı", "Lütfen bir görev seçin!")

#tek tıklamayla kayıtlı görevlerin hepsini siler
def on_delete_all_tasks():
    deneme.delete_all_written("tasks.txt")
    update_listbox()

update_listbox()
interface.mainloop()
