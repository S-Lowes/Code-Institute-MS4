var firstSeatLabel = 1;

function setCookie(cname, cvalue, exdays) {
  const d = new Date();
  d.setTime(d.getTime() + (exdays*24*60*60*1000));
  let expires = "expires="+ d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/;SameSite=Lax;";
}

let seat_map = JSON.parse(document.getElementById('seat_map').textContent);

  $(document).ready(function() {
    var $cart = $('#selected-seats'),
      $counter = $('#counter'),
      $total = $('#total'),
      sc = $('#seat-map').seatCharts({
      map: [
        "gggggggggggg","gggggggggggg","gggggggggggg","pppppppppppp","pppppppppppp","gggggggggggg","gggggggggggg","ggggg__ggggg","gggg____gggg","gg________gg"],
      seats: {
        g: {
          price   : 40,
          classes : 'general', //your custom CSS class
          category: 'General'
        },
        p: {
          price   : 60,
          classes : 'premium', //your custom CSS class
          category: 'Premium'
        }         
      
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
          [ 'p', 'available',   'Premium'],
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
          
          return 'selected';
        } else if (this.status() == 'selected') {
          //update the counter
          $counter.text(sc.find('selected').length-1);
          //and total
          $total.text(recalculateTotal(sc)-this.data().price);
        
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
    sc.get(['9_2','1_2', '4_1', '7_1', '7_2']).status('unavailable');

});

function recalculateTotal(sc) {
  var total = 0;

  //basically find every selected seat and sum its price
  sc.find('selected').each(function () {
    total += this.data().price;
  });
  
  return total;
}

/*
* Checkout Function: Create Cookie
* 
*/

document.getElementById("checkout-button").addEventListener("click", checkout);

function checkout() {
  let selectedSeats = document.getElementById("selected-seats");
  let children = selectedSeats.children;
  cookie_seating = [];
  for(var i=0; i<children.length; i++){
    var child = children[i];
    seating = child.getAttribute('id');
    seating_id=seating.substring(10);
    cookie_seating.push(seating_id);
    console.log(cookie_seating);
}

  setCookie("cookie_seating",cookie_seating,1)
};