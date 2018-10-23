
dashBoard();

function dashBoard(){

      let error = document.getElementById('error');
      let successful = document.getElementById('message');
      let code = '';
      token = window.localStorage.getItem('token');
      fetch('http://127.0.0.1:5000/api/v2/menu', {
            method:'GET',
            headers: {
              'content-type':'application/json',
              'Authorization': 'Bearer ' + token
            },
            mode: 'cors',
           
      }
      ).then((res)=>{
        code = res.code;
        return res.json();
      })
      .then((data)=> {
        console.log(data);
          let images = ["burger.jpg","double.PNG","kungpao.JPG","ricebiryani.JPG","silver.JPG","snack.JPG"];
          let list = data.message;
          var meals = '';
          var meals2 = '';
          list.forEach((element,key) => {
            meals += `
            <div class="menu_item">
                <div class="snack-data">
                    <small>${element.meal_price}</small>
                </div>
                <h2 class="snack-title">${element.meal_name}</h2>
                <img src="img/${images[key]}" >
                <p class="snack-content">${element.meal_description}</p>
            </div>
            `;
            meals2 += `
            <option value="${element.meal_name}">${element.meal_name}</option>
            `;  
          });
          document.getElementById("meals2").innerHTML=meals2;
          document.getElementById("meals").innerHTML=meals;

          
      });
}

function placeOrder(meal_name, quantity, location){

      let error = document.getElementById('error');
      let successful = document.getElementById('message');
      let code = '';
      token = window.localStorage.getItem('token');
      fetch('http://127.0.0.1:5000/api/v2/users/orders', {
            method:'POST',
            headers: {
              'content-type':'application/json',
              'Authorization': 'Bearer ' + token
            },
            mode: 'cors',
            body:JSON.stringify({
              'meal_name':meal_name,
              'quantity':quantity,
              'location': location
            })  
      }
      ).then((res)=>{
        code = res.code;
        return res.json();
      })
      .then(data=>{
        console.log(data);
        if (data.msg=='order placed'){
          window.location = 'history.html'
        }
      })
}

document.getElementById('submit').addEventListener('click', function(e){
  e.preventDefault();
  var location = document.getElementById('location').value;
  var quantity = document.getElementById('number-of-piece').value;
  var meal_name = document.getElementById('meals2').value;
  placeOrder(meal_name, quantity, location);

});