getAllOrders();

function getAllOrders(){

  let error = document.getElementById('error');
  let successful = document.getElementById('message');
  let code = '';
  token = window.localStorage.getItem('token');
  fetch('/api/v2/orders', {
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
    <th>ORDER ID</th>
    <th>PAYMENT METHOD</th>
    <th>ORDER STATUS</th>
    <th>ORDER TYPE</th>
    <th>ORDER LOCATION</th>
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

// function updateOrder(status){

//       let error = document.getElementById('error');
//       let successful = document.getElementById('message');
//       let code = '';
//       token = window.localStorage.getItem('token');
//       fetch('/api/v2/orders/<int:order_id>', {
//             method:'PUT',
//             headers: {
//               'content-type':'application/json',
//               'Authorization': 'Bearer ' + token
//             },
//             mode: 'cors',
//             body:JSON.stringify({
//               "status": status
//             })  
//       }
//       ).then((res)=>{
//         code = res.code;
//         return res.json();
//       })
//       .then(data=>{
//         console.log(data);
//         if (data.msg=='order updated'){
//           window.location = 'history.html'
//         }
//       })
// }

// document.getElementById('submit').addEventListener('click', function(e){
//   e.preventDefault();
//   var location = document.getElementById('status').value;
//   updateOrder(status);

// });