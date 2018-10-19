document.getElementById('signinButton').addEventListener('click', function(click){
  login(click);
});

function login(event){
      event.preventDefault();
      let username = document.getElementById('username').value;
      let password = document.getElementById('password').value;

      let error = document.getElementById('error');
      let successful = document.getElementById('message');
      let code = '';
      fetch('http://127.0.0.1:5000/api/v2/auth/login', {
            method:'POST',
            headers: {
              'content-type':'application/json'
            },
            mode: 'cors',
            body:JSON.stringify({
              'Username':username,
              'Password':password
            })
      }
      ).then((res)=>{
        code = res.code;
        return res.json();
      })
      .then((data)=> {
        console.log(data);
        if (data.message == "succefully"){
          window.localStorage.setItem('token', data.access_token);
          if(data.role.admin==true){
            window.location = 'admin.html'
          }
          else{
            window.location = 'dash.html'
          }
        }
      })
}

function logout(){
  localStorage.removeItem('token');
  window.location.href = 'index.html'
}