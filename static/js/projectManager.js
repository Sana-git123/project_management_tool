
const button = document.getElementById("create");
const modal = document.getElementById("createProjectModal");
const createButton = document.getElementById("save");
const newTask = document.getElementById("newTask")
const taskModal = document.getElementById("taskProjectModal")

newTask.onclick = function () {
    taskModal.style.display = "block"
}
createButton.onclick = function () {
    modal.style.display = "none";
};
button.onclick = function () {
    modal.style.display = "block";
};
