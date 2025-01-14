import json

def load_tasks():
    """Load tasks from a file."""
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Save tasks to a file."""
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def list_tasks(tasks):
    """List all tasks."""
    if not tasks:
        print("\nAucune tâche disponible.")
    else:
        print("\nListe des tâches :")
        for i, task in enumerate(tasks):
            status = "[✔]" if task["completed"] else "[ ]"
            print(f"{i + 1}. {status} {task['description']}")

def add_task(tasks):
    """Add a new task."""
    description = input("Entrez la description de la tâche : ")
    tasks.append({"description": description, "completed": False})
    print("Tâche ajoutée avec succès !")

def delete_task(tasks):
    """Delete a task."""
    list_tasks(tasks)
    try:
        index = int(input("Entrez le numéro de la tâche à supprimer : ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"Tâche supprimée : {removed_task['description']}")
        else:
            print("Numéro de tâche invalide.")
    except ValueError:
        print("Veuillez entrer un numéro valide.")

def complete_task(tasks):
    """Mark a task as complete."""
    list_tasks(tasks)
    try:
        index = int(input("Entrez le numéro de la tâche à marquer comme terminée : ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            print(f"Tâche marquée comme terminée : {tasks[index]['description']}")
        else:
            print("Numéro de tâche invalide.")
    except ValueError:
        print("Veuillez entrer un numéro valide.")

def main():
    tasks = load_tasks()
    
    while True:
        print("\n=== Application de Liste de Tâches ===")
        print("1. Afficher les tâches")
        print("2. Ajouter une tâche")
        print("3. Supprimer une tâche")
        print("4. Marquer une tâche comme terminée")
        print("5. Quitter")
        
        choix = input("Choisissez une option : ")
        
        if choix == "1":
            list_tasks(tasks)
        elif choix == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choix == "3":
            delete_task(tasks)
            save_tasks(tasks)
        elif choix == "4":
            complete_task(tasks)
            save_tasks(tasks)
        elif choix == "5":
            save_tasks(tasks)
            print("Au revoir !")
            break
        else:
            print("Option invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()