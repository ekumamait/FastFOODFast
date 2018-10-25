var baseUrl = 'https://ekumamaits-fastfoodfast.herokuapp.com/api/v2';

getOrderhistory();

function getOrderhistory(){

  let error = document.getElementById('error');
  let successful = document.getElementById('message');
  let code = '';
  token = window.localStorage.getItem('token');
  fetch(baseUrl+ '/users/orders', {
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
    <th>Meals</th>
    <th>Price</th>
    <th>Status</th>
    <th>Location</th>
    <th>Timestamp</th>
  </tr>`;
    orders.forEach((element,key) => {
    orders2 += `
    <tr>
    <td>${element.meal_name}</td>
    <td>${element.meal_price}</td>
    <td><b>${element.status}</b></td>
    <td>${element.location}</td>
    <td>${element.order_date}</td>
    </tr>
    `;  

    });
    document.getElementById("customers").innerHTML=orders2;

  });
}
