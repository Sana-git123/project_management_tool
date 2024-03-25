
const button = document.getElementById("create");
const modal = document.getElementById("createProjectModal");
// const closeButton = document.getElementById("cancel");
const createButton = document.getElementById("save");
const newTask = document.getElementById("newTask")
const taskModal = document.getElementById("taskProjectModal")
// const taskcancel = document.getElementById("taskcancel")

// const logoutModal = document.getElementById("logoutModal");
// const logout = document.getElementById("logoutButton");
// const logoutSave = document.getElementById("logoutsave");
// const logoutCancel = document.getElementById("logoutcancel");

newTask.onclick = function () {
    taskModal.style.display = "block"
}
// taskcancel.onclick = function () {
//     taskModal.style.display = "none"
// }

createButton.onclick = function () {
    modal.style.display = "none";
};
button.onclick = function () {
    modal.style.display = "block";
};
// closeButton.onclick = function () {
//     modal.style.display = "none";
// };


// logout.onclick = () => {
//     logoutModal.style.display = "block";
//     console.log('jhavhja')
// }

// logoutCancel.onclick = () => {
//     logoutModal.style.display = "none";
// };

// logoutSave.onclick = () => {
//     logoutModal.style.display = "none";
//     window.location.href = "/";
// };
