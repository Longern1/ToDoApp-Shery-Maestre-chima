from task_model import TaskModel

def main():
    task = TaskModel ("Estudiar para el examen")
    print(f"Tarea creada: {task.get_task_name()}")
    task.mark_as_complete()
    print(f"Tarea completada: {task.is_completed}")
    task.remove_task()
    print(f"Tarea eliminada:{task.get_task_name()}")
    
if __name__ == "__main__":
    main()