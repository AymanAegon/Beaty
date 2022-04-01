var element = document.getElementById("threads_scroll");
element.scrollTop = element.scrollHeight ;

function openForm() {
  document.getElementById("popup-confimation").style.display = "block";
}

function closeForm() {
  document.getElementById("popup-confimation").style.display = "none";
}

function openForm2() {
  document.getElementById("popup-confimation").style.display = "block";
  id = document.getElementById("msg_id").innerHTML;
  document.getElementById("input-msg-id").value = id;
}

function closeForm2() {
  document.getElementById("popup-confimation").style.display = "none";
  document.getElementById("input-msg-id").value = "";
}