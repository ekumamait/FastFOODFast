var baseUrl = 'https://ekumamaits-fastfoodfast.herokuapp.com/api/v2';
getAllOrders();

function getAllOrders(){

  let error = document.getElementById('error');
  let successful = document.getElementById('message');
  let code = '';
  token = window.localStorage.getItem('token');
  fetch(baseUrl+ '/orders', {
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
    <th>UPDATE STATUS</th>
    <th>ORDER LOCATION</th>
    <th>ORDER DATE</th>
    <th>QUANTITY</th>
    <th>CURRENT STATUS</th>
    <th>CUSTOMER</th>
    </tr>`;
    orders.forEach((element,key) => {
    orders2 += `
    <tr>
    <td>${element.meal_name}</td>
    <td><h4>
    <div class="pointer" onClick="updateOrder('${element.order_id}','processing')">ACCEPT</div>
    <b>
    <div class="pointer" onClick="updateOrder('${element.order_id}','completed')">COMPLETED</div>
    </h4><b><div class="pointer" onClick="updateOrder('${element.order_id}','cancelled')">CANCEL</div>
    </b></td>
    <td>${element.location}</td>
    <td>${element.order_date}</td>
    <td>${element.quantity}</td>
    <td>${element.status}</td>
    <td>${element.user_name}</td>
    </tr>
    `;  

    });
    document.getElementById("customers").innerHTML=orders2;

  });
}


function updateOrder(id, status){
      console.log(id+status);
      let error = document.getElementById('error');
      let successful = document.getElementById('message');
      let code = '';
      token = window.localStorage.getItem('token');
      fetch(baseUrl+'/orders/'+parseInt(id), {
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
        code = res.code;
        return res.json();
      })
      .then(data=>{
        console.log(data);
        if (data.msg=='Order updated'){
          getAllOrders();
        }
      })
}

try {
  document.getElementById('submitmeal').addEventListener('click', function(click){
    newMeal(click);
    
  });
} catch (error) {
  
}

function newMeal(event){
      event.preventDefault();
      let name = document.getElementById('meal_name').value;
      let description = document.getElementById('meal_description').value;
      let price = document.getElementById('meal_price').value;

      let error = document.getElementById('error');
      let successful = document.getElementById('message');
      let code = '';
      token = window.localStorage.getItem('token');
      fetch(baseUrl+'/menu', {
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
        if (data.message == 'menu item added')
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

