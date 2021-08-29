var firstSeatLabel = 1;

let seat_map = JSON.parse(document.getElementById('seat_map').textContent);
let seat_taken = JSON.parse(document.getElementById('seat_taken').textContent);
let ticket_price = parseInt(JSON.parse(document.getElementById('ticket_price').textContent));

// Set Cookie (W3S)
function setCookie(cname, cvalue, exdays) {
  const d = new Date();
  d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
  let expires = "expires=" + d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/;SameSite=Lax;";
}

// Get Cookie (Django)
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + "=")) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

// Blank Cookies on page load
window.onload = function(){
  setCookie("cookie_seating","",-1)
  setCookie("cookie_number","",-1)
};

  $(document).ready(function() {
    var $cart = $('#selected-seats'),
      $counter = $('#counter'),
      $total = $('#total'),
      sc = $('#seat-map').seatCharts({
      map: seat_map,
      seats: {
        g: {
          price   : ticket_price
          ,
          classes : 'general', //your custom CSS class
          category: ''
        },       
      
      },
      naming : {
        top : false,
        getLabel : function (character, row, column) {
          return firstSeatLabel++;
        },
      },
      legend : {
        node : $('#legend'),
          items : [
          [ 'g', 'available',   'General' ],
          [ 'f', 'unavailable', 'Already Booked']
          ]
      },

      click: function () {
        if (this.status() == 'available') {
          //let's create a new <li> which we'll add to the cart items
          $('<li>'+this.data().category+' Seat '+this.settings.label+': <b>£'+this.data().price+'</b> <a href="#" class="cancel-cart-item">[cancel]</a></li>')
            .attr('id', 'cart-item-'+this.settings.id)
            .data('seatId', this.settings.id)
            .appendTo($cart);
          /*
           * Lets up<a href="https://www.jqueryscript.net/time-clock/">date</a> the counter and total
           *
           * .find function will not find the current seat, because it will change its stauts only after return
           * 'selected'. This is why we have to add 1 to the length and the current seat price to the total.
           */
          $counter.text(sc.find('selected').length+1);
          $total.text(recalculateTotal(sc)+this.data().price);

          // ===== Set cookie_seating cookie ADD =====
          function add_select_to_cookie(cookie_name, selected) {
            current_cookie = getCookie(cookie_name);
            if (current_cookie == null || current_cookie == "") {
              setCookie(cookie_name, selected, 1);
            } else {
              let arr = current_cookie.split(",");
              arr.push(selected);
              setCookie(cookie_name, arr.toString());
            };
          };

          add_select_to_cookie("cookie_seating",this.settings.id);
          add_select_to_cookie("cookie_number",this.settings.label.toString());

          return 'selected';
        } else if (this.status() == 'selected') {
          //update the counter
          $counter.text(sc.find('selected').length-1);
          //and total
          $total.text(recalculateTotal(sc)-this.data().price);
          
          // ===== Set cookie_seating cookie SUBTRACT =====
          function remove_select_from_cookie(cookie_name, selected) {
            let arr = getCookie(cookie_name).split(",");
            j = selected
            arr = arr.filter(function (item) {
              return item !== j
            });
            let text = arr.toString();
            setCookie(cookie_name, text, 1)
          };

          remove_select_from_cookie("cookie_seating",this.settings.id);
          remove_select_from_cookie("cookie_number",this.settings.label.toString());


          //remove the item from our cart
          $('#cart-item-'+this.settings.id).remove();
          //seat has been vacated
          return 'available';
        } else if (this.status() == 'unavailable') {
          //seat has been already booked
          return 'unavailable';
        } else {
          return this.style();
        }
      }
    });

    //this will handle "[cancel]" link clicks
    $('#selected-seats').on('click', '.cancel-cart-item', function () {
      //let's just trigger Click event on the appropriate seat, so we don't have to repeat the logic here
      sc.get($(this).parents('li:first').data('seatId')).click();
    });

    //let's pretend some seats have already been booked
    sc.get(seat_taken).status('unavailable');

});

function recalculateTotal(sc) {
  var total = 0;

  //basically find every selected seat and sum its price
  sc.find('selected').each(function () {
    total += this.data().price;
  });
  return total;
}

// $('#checkout-button').click(function() {    
//   $.ajax({
//       headers: {
//         "X-Requested-With": "XMLHttpRequest",
//         "X-CSRFToken": getCookie("csrftoken"),
//       },
//       url: '',
//       method: 'POST',
//       dataType: "json",
//       data: {seat_taken_cookie: getCookie("cookie_seating"),
//       seat_number_cookie: getCookie("cookie_number")},
//       success: (data) => {
//         console.log("Yay Hurray!", data);
//       },
//       error: (error) => {
//         console.log("oh no!", error);
//       }
//   });
// });
