try {
  var element = document.getElementById("threads_scroll");
  element.scrollTop = element.scrollHeight ;
} catch (error) {
  console.error(error);
}

document.getElementById("first_name").innerHTML = "First Name"
document.getElementById("last_name").innerHTML = "Last Name"
document.getElementById("username").innerHTML = "Username"
document.getElementById("email").innerHTML = "Email"
document.getElementById("password1").innerHTML = "Password"
document.getElementById("password2").innerHTML = "Confirm Password"


function openForm() {
  document.getElementById("popup-confimation").style.display = "block";
}

function closeForm() {
  document.getElementById("popup-confimation").style.display = "none";
}

function openForm3() {
  document.getElementById("popup-form").style.display = "block";
}

function closeForm3() {
  document.getElementById("popup-form").style.display = "none";
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