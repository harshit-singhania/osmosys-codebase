document.addEventListener("DOMContentLoaded", function () {
  let taskInput = document.getElementById("task-input");
  let addTaskButton = document.getElementById("add-task-button");
  let taskList = document.getElementById("task-list");

  let tasks = JSON.parse(localStorage.getItem("tasks")) || [];

  function saveTasks() {
    localStorage.setItem("tasks", JSON.stringify(tasks));
  }

  function renderTasks() {
    taskList.innerHTML = "";
    for (let i = 0; i < tasks.length; i++) {
      let task = tasks[i];
      let taskItem = document.createElement("li");
      taskItem.className = "task-item";
      if (task.completed) {
        taskItem.className += " completed";
      }
      taskItem.innerHTML = `
                <span>${task.text}</span>
                <button class="edit-button" data-index="${i}">Edit</button>
                <button class="delete-button" data-index="${i}">Delete</button>
            `;
      taskItem
        .querySelector(".edit-button")
        .addEventListener("click", function () {
          let newTaskText = prompt("Edit task:", task.text);
          if (newTaskText !== null) {
            task.text = newTaskText.trim();
            saveTasks();
            renderTasks();
          }
        });
      taskItem
        .querySelector(".delete-button")
        .addEventListener("click", function () {
          tasks.splice(i, 1);
          saveTasks();
          renderTasks();
        });
      taskItem.addEventListener("click", function (e) {
        if (
          !e.target.classList.contains("edit-button") &&
          !e.target.classList.contains("delete-button")
        ) {
          task.completed = !task.completed;
          saveTasks();
          renderTasks();
        }
      });
      taskList.appendChild(taskItem);
    }
  }

  addTaskButton.addEventListener("click", function () {
    let taskText = taskInput.value.trim();
    if (taskText) {
      tasks.push({ text: taskText, completed: false });
      saveTasks();
      renderTasks();
      taskInput.value = "";
    }
  });

  clearAllButton.addEventListener("click", function () {
    tasks = [];
    saveTasks();
    renderTasks();
  });

  renderTasks();
});
