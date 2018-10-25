getAllOrders();

function getAllOrders(){

  let error = document.getElementById('error');
  let successful = document.getElementById('message');
  let code = '';
  token = window.localStorage.getItem('token');
  fetch('http://127.0.0.1:5000/api/v2/orders', {
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
  .then(data=>{
    console.log(data);
    var orders = data['All Orders']
    var orders2 = ` <tr>
    <th>ORDER</th>
    <th>ORDER STATUS</th>
    <th>ORDER LOCATION</th>
    <th>ORDER DATE</th>
    <th>QUANTITY</th>
    <th>CUSTOMER</th>
    </tr>`;
    orders.forEach((element,key) => {
    orders2 += `
    <tr>
    <td>${element.meal_id}</td>
    <td><b>${element.status}</b><h4><a href="#">ACCEPT</a></h4><b><a href="#">CANCEL</a></b></td>
    <td>${element.location}</td>
    <td>${element.order_date}</td>
    <td>${element.quantity}</td>
    <td>${element.user_id}</td>
    </tr>
    `;  

    });
    document.getElementById("customers").innerHTML=orders2;

  });
}

updateOrder();

function updateOrder(id, status){

      let error = document.getElementById('error');
      let successful = document.getElementById('message');
      let code = '';
      token = window.localStorage.getItem('token');
      fetch('http://127.0.0.1:5000/api/v2/orders/1', {
            method:'PUT',
            headers: {
              'content-type':'application/json',
              'Authorization': 'Bearer ' + token
            },
            mode: 'cors',
            body:JSON.stringify({
              "status": status
            })  
      }
      ).then((res)=>{
        console.log(res);
        code = res.code;
        return res.json();
      })
      .then(data=>{
        console.log(data);
        if (data.msg=='order updated'){
          // window.location = 'history.html'
        }
      })
}

document.getElementById('customers').addEventListener('click', function(e){
  e.preventDefault();
  var location = document.getElementById('status').value;
  updateOrder(status);

});


getSpecificOrder();

function getSpecificOrder(id){

  let error = document.getElementById('error');
  let successful = document.getElementById('message');
  let code = '';
  token = window.localStorage.getItem('token');
  fetch('http://127.0.0.1:5000/api/v2/orders/1', {
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
  .then(data=>{
    console.log(data);
    var orders = data['All Orders']
    var orders2 = ` <tr>
    <th>ORDER</th>
    <th>ORDER STATUS</th>
    <th>ORDER LOCATION</th>
    <th>ORDER DATE</th>
    <th>QUANTITY</th>
    <th>CUSTOMER</th>
  </tr>`;
    orders.forEach((element,key) => {
    orders2 += `
    <tr>
    <td>${element.meal_id}</td>
    <td><b>${element.status}</b><h4><a href="#">ACCEPT</a></h4><b><a href="#">CANCEL</a></b></td>
    <td>${element.location}</td>
    <td>${element.order_date}</td>
    <td>${element.quantity}</td>
    <td>${element.user_id}</td>
    </tr>
    `;  

    });
    document.getElementById("one").innerHTML=orders2;

  });
}

document.getElementById('submitmeal').addEventListener('click', function(click){
  newMeal(click);
  
});

function newMeal(event){
      event.preventDefault();
      let name = document.getElementById('meal_name').value;
      let description = document.getElementById('meal_description').value;
      let price = document.getElementById('meal_price').value;

      let error = document.getElementById('error');
      let successful = document.getElementById('message');
      let code = '';
      token = window.localStorage.getItem('token');
      fetch('http://127.0.0.1:5000/api/v2/menu', {
            method:'POST',
            headers: {
              'content-type':'application/json',
              'Authorization': 'Bearer ' + token
            },
            mode: 'cors',
            body:JSON.stringify({
              "meal_name": name,
              "meal_description": description,
              "meal_price": price
            })
      }
      ).then((res)=>{
        code = res.code;
        return res.json();
      })
      .then((data)=> {
        console.log(data);
        if (data.msg == 'menu item added')
        {
          window.location = 'dash.html';
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

