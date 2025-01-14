# Decentralization_Technologies_TodoList_Vabret
# Task Management Application

## Description
This is a simple task management application written in Python. It allows users to manage a list of tasks with functionalities to add, delete, complete, and list tasks. The tasks are saved in a `tasks.json` file for persistence.

## Features
- **View Tasks**: Displays a list of all tasks with their completion status.
- **Add Tasks**: Allows users to add new tasks while ensuring no duplicates.
- **Delete Tasks**: Remove tasks by selecting their number from the list.
- **Mark Tasks as Complete**: Update the status of a task to "completed".
- **Persistent Storage**: Tasks are saved to a JSON file for future use.

## Installation
1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd <project-directory>
   ```
3. Ensure you have Python 3 installed on your machine.

## Usage
1. Run the script:
   ```bash
   python <script-name>.py
   ```
2. Follow the menu prompts to manage your tasks:
   - **1**: Display all tasks
   - **2**: Add a new task
   - **3**: Delete an existing task
   - **4**: Mark a task as completed
   - **5**: Exit the application

## Example
### Adding a Task
```
Entrez la description de la tâche : Acheter du lait
Tâche ajoutée avec succès !
```
### Listing Tasks
```
Liste des tâches :
1. [ ] Acheter du lait
```
### Marking a Task as Complete
```
Entrez le numéro de la tâche à marquer comme terminée : 1
Tâche marquée comme terminée : Acheter du lait
```

## How to Contribute
1. Fork this repository.
2. Clone your forked repository:
   ```bash
   git clone <your-forked-repo-url>
   ```
3. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
4. Make your changes and commit them:
   ```bash
   git commit -m "Description of changes"
   ```
5. Push your branch to your fork:
   ```bash
   git push origin feature-name
   ```
6. Open a Pull Request to the original repository.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
