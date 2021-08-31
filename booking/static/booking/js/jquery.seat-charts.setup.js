var firstSeatLabel = 1;


// GET VARIBALES FROM JSONSCRIPT IN HTML
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
          classes : 'general', // CUSTOM CSS CLASS
          category: 'Theater'
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
          //Create new <li> to add to the cart items
          $('<li>'+this.data().category+' Seat '+this.settings.label+': <b>£'+this.data().price+'</b> <a href="#" class="cancel-cart-item">[cancel]</a></li>')
            .attr('id', 'cart-item-'+this.settings.id)
            .data('seatId', this.settings.id)
            .appendTo($cart);
          /*
           * Up date the counter and total
           *
           * Add 1 to the length and the current seat price to the total.
           */
          $counter.text(sc.find('selected').length+1);
          $total.text(recalculateTotal(sc)+this.data().price);

          return 'selected';
        } else if (this.status() == 'selected') {
          //update the counter
          $counter.text(sc.find('selected').length-1);
          //and total
          $total.text(recalculateTotal(sc)-this.data().price);

          //Remove the item from our cart
          $('#cart-item-'+this.settings.id).remove();
          //Deat has been vacated
          return 'available';
        } else if (this.status() == 'unavailable') {
          //Seat has been already booked
          return 'unavailable';
        } else {
          return this.style();
        }
      }
    });

    //This will handle "[cancel]" link clicks
    $('#selected-seats').on('click', '.cancel-cart-item', function () {
      //Trigger Click event on the appropriate seat, so we don't have to repeat the logic here
      sc.get($(this).parents('li:first').data('seatId')).click();
    });

    //Used to show which seats are unavailable
    sc.get(seat_taken).status('unavailable');

    /*
    * Onclick find the correct total price and seats chosen by user.
    * Then,
    * AJAX post them to the view for database and webhook handling.
    */
    $('#seatCalcButton').click(function() {
      recalc = recalculateTotal(sc);
      seat_id_label = confirmSeats(sc);
      seat_id = seat_id_label[0]
      seat_label = seat_id_label[1]

      if (recalc != 0){
        document.getElementById('hidden-buttons').style.display = "block";
        document.getElementById('seatCalcButton').style.display = "none";
      }

      $.ajax({
        headers: {
          "X-Requested-With": "XMLHttpRequest",
          "X-CSRFToken": getCookie("csrftoken"),
        },
        url: '',
        method: 'POST',
        dataType: "json",
        data: {
          total_recalc: recalc,
          id_recalc: JSON.stringify(seat_id),
          label_recalc: JSON.stringify(seat_label),
        },
        success: (data) => {
          console.log(data);
        },
        error: (error) => {
          console.log(error);
        }
      });
    });
});

//Find every selected seat and sum its price
function recalculateTotal(sc) {
  var total = 0;
  sc.find('selected').each(function () {
    total += this.data().price;
  });
  return total;
}

//Find every selected seat and create array of its ID & Num
function confirmSeats(sc) {
  let this_id = new Array();
  let this_label = new Array()
  sc.find('selected').each(function () {
    this_id.push(this.settings.id);
    this_label.push(this.settings.label);
  });
  return [this_id,this_label];
}

function closeDiv() {
      document.getElementById('hidden-buttons').style.display = "none";
      document.getElementById('seatCalcButton').style.display = "block";
}