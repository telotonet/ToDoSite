// let taskCounter = 0;

// function addTask() {
//     taskCounter++;
//     const taskList = document.querySelector('#tasks-container');
//     const newTaskItem = document.createElement('div');
//     newTaskItem.className = 'mt-2 d-flex justify-content-md-center';

//     // Создаем элементы для задачи и кнопку удаления
//     const taskInput = document.createElement('input');
//     taskInput.type = 'text';
//     taskInput.name = `tasks`;
//     taskInput.className = 'form-control form-control-sm w-50 d-block';
//     taskInput.placeholder = 'Задача';
//     taskInput.required = true;

//     const deleteButton = document.createElement('button');
//     deleteButton.type = 'button';
//     deleteButton.className = 'btn btn-sm btn-danger delete-task';
//     deleteButton.textContent = 'Удалить';

//     // Добавляем элементы в список задач
//     newTaskItem.appendChild(taskInput);
//     newTaskItem.appendChild(deleteButton);
//     taskList.appendChild(newTaskItem);

//     // Добавляем обработчик для кнопки удаления
//     deleteButton.addEventListener('click', () => {
//         taskList.removeChild(newTaskItem);
//         taskCounter--
//     });

//     addSubtaskButtonListeners();
// }

// document.querySelector('.add-task').addEventListener('click', addTask);
