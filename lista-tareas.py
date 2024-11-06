import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime #agrego libreria datetime--Kevin

class TaskManager:
    def __init__(self, root):
        # Inicializa la ventana principal y establece su título
        self.root = root
        self.root.title("Lista de Tareas - CRUD")
        self.tasks = []  # Lista para almacenar las tareas

        # Listbox para mostrar tareas
        self.task_listbox = tk.Listbox(self.root, width=50, height=15)
        self.task_listbox.pack(pady=20)  # Empaqueta el listbox con un margen vertical

        # Frame para los botones
        button_frame = tk.Frame(self.root)
        button_frame.pack()  # Empaqueta el frame de botones

        # Botones en el Frame (2 por línea)
        # Botón para agregar una tarea
        self.add_button = tk.Button(button_frame, text="Agregar Tarea", command=self.add_task, width=20)
        self.add_button.grid(row=0, column=0, padx=5, pady=5)  # Coloca el botón en la cuadrícula

        # Botón para actualizar una tarea
        self.update_button = tk.Button(button_frame, text="Actualizar Tarea", command=self.update_task, width=20)
        self.update_button.grid(row=0, column=1, padx=5, pady=5)  # Coloca el botón en la cuadrícula

        # Botón para eliminar una tarea
        self.delete_button = tk.Button(button_frame, text="Eliminar Tarea", command=self.delete_task, width=20)
        self.delete_button.grid(row=1, column=0, padx=5, pady=5)  # Coloca el botón en la cuadrícula

        # Botón para limpiar todas las tareas
        self.clear_button = tk.Button(button_frame, text="Limpiar Tareas", command=self.clear_tasks, width=20)
        self.clear_button.grid(row=1, column=1, padx=5, pady=5)  # Coloca el botón en la cuadrícula

        #Boton de busqueda-- Sara lamprea
        self.search_button = tk.Button(button_frame, text="Buscar Tarea", command=self.search_task, width=20)
        self.search_button.grid(row=2, column=0, padx=5, pady=5)

    def add_task(self):
        task = simpledialog.askstring("Agregar Tarea", "Escribe la tarea:")
        if task:
            date_created = datetime.now().strftime("%d/%m/%Y %H:%M")
            self.tasks.append(f"{task} (creado el {date_created})")
            self.update_task_listbox()
    def update_task(self):
        # Método para actualizar la tarea seleccionada
        try:
            selected_index = self.task_listbox.curselection()[0]  # Obtiene el índice de la tarea seleccionada
            current_task = self.tasks[selected_index]  # Obtiene la tarea actual
            new_task = simpledialog.askstring("Actualizar Tarea", "Edita la tarea:", initialvalue=current_task)  # Solicita la nueva tarea
            if new_task:  # Verifica si se ingresó una nueva tarea
                self.tasks[selected_index] = new_task  # Actualiza la tarea en la lista
                self.update_task_listbox()  # Actualiza el Listbox
        except IndexError:
            # Muestra una advertencia si no hay ninguna tarea seleccionada
            messagebox.showwarning("Advertencia", "Selecciona una tarea para actualizar.")

    def delete_task(self):
        # Método para eliminar la tarea seleccionada
        try:
            selected_index = self.task_listbox.curselection()[0]  # Obtiene el índice de la tarea seleccionada
            del self.tasks[selected_index]  # Elimina la tarea de la lista
            self.update_task_listbox()  # Actualiza el Listbox
        except IndexError:
            # Muestra una advertencia si no hay ninguna tarea seleccionada
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

    def clear_tasks(self):
        # Método para limpiar todas las tareas
        if messagebox.askyesno("Confirmación", "¿Estás seguro de que quieres limpiar todas las tareas?"):
            self.tasks.clear()  # Limpia la lista de tareas
            self.update_task_listbox()  # Actualiza el Listbox

    def update_task_listbox(self):
        # Método para actualizar el contenido del Listbox con las tareas
        self.task_listbox.delete(0, tk.END)  # Borra el contenido actual del Listbox
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)  # Inserta cada tarea en el Listbox

        
    #añado funcion search_task
    def search_task(self):
        search_term = simpledialog.askstring("Buscar Tarea", "Ingresa el término de búsqueda:")
        if search_term:
            found_tasks = [task for task in self.tasks if search_term.lower() in task.lower()]
            messagebox.showinfo("Resultados de Búsqueda", "\n".join(found_tasks) if found_tasks
        else "No se encontraron tareas.")

# Bloque principal para ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()  # Crea la ventana principal
    app = TaskManager(root)  # Crea una instancia de TaskManager
    root.mainloop()  # Inicia el bucle principal de la interfaz gráfica


