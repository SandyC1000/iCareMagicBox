// alert('= ajax js =  is connected !! <<<<<<<');
"use strict";
const userButton = document.querySelector("#show-user-form");
const userForm = "#create-user"
const user_form = document.getElementById("create-user");
user_form.hidden = true;
// 1. create new user form - init hidden=true; allow user to click to hide 
userButton.addEventListener('click', ()=>{
    user_form.hidden = !user_form.hidden
    })
// 2. create new user form - filling input fields information on browser
const userRegForm = document.querySelector("#user-reg-form");
userRegForm.addEventListener('submit',(evt) => {
    evt.preventDefault();
    alert("*** Entering userRegForm ")

    const formInputs = {
        fname : document.getElementById('reg-fname').value,
        lname : document.getElementById('reg-lname').value,
        email : document.getElementById('reg-email').value,
        password : document.getElementById('reg-password').value,
        phone : document.getElementById('reg-phone').value,
        birthday : document.getElementById('reg-birthday').value,
        address : document.getElementById('reg-address').value
                        };
    fetch('/register/API',{
        method: 'POST',
        body: JSON.stringify(formInputs),
        headers: {
            'Content-Type': 'application/json',
                },
    })
        .then(response => response.json())
        .then(responseJson => {
            alert(responseJson.status);
            });
    // document.querySelector('input[name="word"]');
    // document.querySelector('input[name="fname"]');
    console.log(formInputs)
})
