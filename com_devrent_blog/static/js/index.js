const deleteSubmitForm = document.getElementById('delete-page-form');

function deleteSubmitEvent(event) {
  event.preventDefault();
  const answer = confirm("삭제하시겠습니까?");
  
  if (answer === true) {
    deleteSubmitForm.submit();
  }
}

deleteSubmitForm.addEventListener('submit', deleteSubmitEvent);
