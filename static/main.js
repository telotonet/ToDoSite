$(document).ready(function() {
  $(".add-task").on("click", function() {
    var newIndex = $(".task-input").length;
    var newTaskInput = '<div class="task-input mb-3">' +
      '<label for="task_' + newIndex + '" class="form-label">Задача</label>' +
      '<input type="text" class="form-control" id="task_' + newIndex + '" name="tasks[]" placeholder="Задача" required>' +
      '<button type="button" class="btn btn-primary add-subtask" data-parent="' + newIndex + '">Добавить подзадачу</button>' +
      '<button type="button" class="btn btn-success add-task">Добавить задачу</button>' +
      '<div class="subtasks-container">' +
      '<ul class="subtask-input">' +
      '<label for="subtask_' + newIndex + '_0" class="form-label">Подзадача</label>' +
      '<input type="text" class="form-control" id="subtask_' + newIndex + '_0" name="subtasks[' + newIndex + '][]" placeholder="Подзадача">' +
      '<button type="button" class="btn btn-primary add-subtask" data-parent="' + newIndex + '">+</button>' +
      '</div>' +
      '</ul>' +
      '</div>';

    $(this).parent().before(newTaskInput);
  });

  // Добавление новых полей для подзадач
  $("#tasks-container").on("click", ".add-subtask", function() {
    var parentTaskIndex = $(this).data("parent");
    var subtaskCount = $(".subtask-input").length;
    var newSubtaskInput = '<div class="subtask-input">' +
      '<label for="subtask_' + parentTaskIndex + '_' + subtaskCount + '" class="form-label">Подзадача</label>' +
      '<input type="text" class="form-control" id="subtask_' + parentTaskIndex + '_' + subtaskCount + '" name="subtasks[' + parentTaskIndex + '][]" placeholder="Подзадача">' +
      '<button type="button" class="btn btn-primary add-subtask" data-parent="' + parentTaskIndex + '">+</button>' +
      '</div>';

    $(this).parent().before(newSubtaskInput);
  });
});
