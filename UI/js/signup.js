document.getElementById('submitbutton').addEventListener('click', function(click){
  newSignup(click);
});

function newSignup(event){
      event.preventDefault();
      let username = document.getElementById('username').value;
      let email = document.getElementById('email').value;
      let password = document.getElementById('password').value;
      let confirmPassword = document.getElementById('confirmPassword').value;

      let error = document.getElementById('error');
      let successful = document.getElementById('message');
      let code = '';
      fetch('http://127.0.0.1:5000/api/v2/auth/sign_up', {
            method:'POST',
            headers: {
              'content-type':'application/json'
            },
            mode: 'cors',
            body:JSON.stringify({
              "user_name": username,
              "user_email": email,
              "user_password": password
            })
      }
      ).then((res)=>{
        code = res.code;
        return res.json();
      })
      .then((data)=> {
        if (data.msg == 'account created')
        {
          window.location = 'index.html';
          error.style.display= 'none';
          successful.style.display= 'block';
          document.getElementById('message').innerHTML = data['message'];
        }else{
          error.style.display='none';
          error.style.display='block';
          document.getElementById('error').innerHTML = data['error'];
        }  
      });
}
