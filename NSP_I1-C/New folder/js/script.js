window.addEventListener("load",function (){
var username = document.getElementById("Username");
var password = document.getElementById("Password");
var submit=document.getElementById("submitButton");
var messageContainer=document.getElementById("Login");
var auth =new Auth();

submit.addEventListener("click",function()

{

var username = document.getElementById("Username").value;
var password = document.getElementById("Password").value;

});
auth.Login();




auth.Login(username,password)
.then(function(response){
const token=response.accessToken;
auth.login(auth.Token);
auth.token=token;
document.cookie="accessToken="+token;
console.log(response.accessToken);
})
.catch(function(e) {
console.log(e) ;
loginContainer.innerHTML=e.status+ " You have to be registered in order to login";
});

});


class Auth {
    constructor() {
    }
    Login(Username, Password) {
        var root = 'https://ancient-caverns-16784.herokuapp.com';
        return $.post(root + "/auth/login", {
            username: 'test',
            password: 'test'
        },
            function (response) {
                var xmlhttp = new XMLHttpRequest();
                console.log(xmlhttp);
                xmlhttp.open("post", "Login", true);
                xmlhttp.onreadystatechange = function () {
                    if (xmlhttp.readyState == 401 && xmlhttp.status == 200 && Username=="test" && Password=="test") {
                        loginResults();
                    }
                };
                console.log(response);
            });


    }
}

