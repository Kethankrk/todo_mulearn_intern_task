const addTodoBtn = document.getElementById('add-todo')
const addTodoModal = document.getElementById('add-todo-modal')
const cancelFormBtn = document.getElementById('form-cancle')
const idExpireInput = document.getElementById('id_expire')


const getCurrentTime = () => {
    const currentDate = new Date();

    const year = currentDate.getFullYear();
    const month = ('0' + (currentDate.getMonth() + 1)).slice(-2);
    const day = ('0' + currentDate.getDate()).slice(-2);
    const hours = ('0' + currentDate.getHours()).slice(-2);
    const minutes = ('0' + currentDate.getMinutes()).slice(-2); 

    const formattedDate = year + '-' + month + '-' + day + ' ' + hours + ':' + minutes;
    return formattedDate
}

idExpireInput.value = getCurrentTime()

addTodoBtn.addEventListener('click', () => {
    addTodoModal.classList.remove('hidden')
    addTodoModal.classList.add('flex')
})


cancelFormBtn.addEventListener('click', () => {
    addTodoModal.classList.remove('flex')
    addTodoModal.classList.add('hidden')
})
