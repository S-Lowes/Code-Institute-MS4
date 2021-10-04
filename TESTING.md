# Testing

[Back to README](README.md)

This is incomplete, I ran out of time... Student Care have suggested to me to submit anyway so as to not incur the wrath of submitting a late project & so I can receive feedback and what I have achieved thus far. Thanks for taking the time to view my project, and hopefully my README will be actually complete next time around.

### Validation

#### HTML
The HTML validation was completed with the [W3C Markup Validator](https://validator.w3.org/). This was done by copying the address of each project page and passing it to the validator. This was necessary to test the code in its final state after being rendered in the Django templates. The HTML code contains no issues.

#### CSS and Javascript
The CSS validation was completed with the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/). Any issues highlighted by the validators were fixed. The code now contains no validity issues.

#### Javascript
The JavaScript validation was completed with the [JS Hint](https://jshint.com/) code analysis tool. Any issues highlighted by the validators were fixed. The code now contains no validity issues.

### Python
All Python code was written to be PEP 8 compliant with the final code being tested with the command ```python3 -m flake8```. Some warnings come from either pre-existing code generated when the Django project was first created, or code generated through the makemigrations command.

### Testing User Stories

As a first time user, I want:
- To quickly be able to understand the purpose of the website and how I can start interacting with it.
    1. Buttons, On hover CSS changes show the user how they can interact with the website.
    1. Simple Navbar encourages interaction.
- To be able to register, sign in and sign out with ease.
    1. Finding registration is easy through the 'Login/Register' Navbar dropdown.
    1. The user will receive a registration email to verify their email address.
    1. Once verified they can sign in and out with ease.
- To navigate through the site intuitively finding potential events to attend.
    1. This can be done from the homepage or from the 'Tickets & Events' link in the navbar.

As a returning visitor, I want:
- To sign in as easily as I did on my first visit and remain signed in.
    1. This is an easy as when they first visited the website.
- To be able to reset my password in the event that I forgot it.
    1. This can be done during login.
- To be able to book seats to a certain event by choosing my seats by way of the seat chart.
    1. Once the user has chosen an event, they can choose a showtime and start interacting with the seat chart.
- To be able to view all my bookings from my profile.
    1. Once seats have been booked, these are found in the profile page which can be found from the navbar 'Account' dropdown.
- To be able to save my details for future purchases.
    1. Users mobile can be saved and change via their profile whenever they would like.

As a frequent user, I want:
- To sign in and view my bookings.
- To continue booking events.
- To change some of my creditials used during the booking process.

The frequent user user stories are very similar to the returning visitor stories.

### Testing User Journey

1. User's Journey starts at the homepage. 
1. They are presented with a carousel of the 3 most recently created shows.
1. Underneath this carousel are 3 clickable images with a more intimate picture of the same shows inviting the user in.
1. Clicking on many of these buttons leads to the Showtimes page or if using the navbar, they are lead to the events page.

All works as intended. Carousel can be interacted with correctly and navigation links lead to correct places.

1. The Event Page features all the events currently on show at amphii which can be filtered using the search bar.
1. The user can click on the buttons to lead themselves to the respective showtime page for that event.

All works as intended. User can search for a specific event by its name and can navigate to the chosen event page.

1. The showtime page will prompt the user to create an account.
1. This is required to use the website as tickets are stored in the users account page.
1. However, if they are already signed in, the user can click on a showtime they can attend and start booking seats.

All works as intended. User is prompted/lead to registration page if they don't already have an account. If they are signed in, they are lead to the seating chart.

1. They are presented with the seat chart. This is much like a cinema booking system where the user can choose seats.
1. A running total is displayed so they can see how much the tickets will cost.
1. When ready, they can confirm their seats and proceed to the payment form.

There is a bug here that will need addressing when I have more time. When the user is selecting their seats they can confirm them, but then choose to cancel them before continuing to payment. Although visually they will look like they have cancelled the chosen seats they will have been sent to the view. This might be addressed by using a modal as a simple fix. Otherwise, The user can choose the seats they want from the seating chart and continue to payment.

1. As the user is registered some of these form elements should already be filled out.
1. After using the somewhat dynamic stripe payment elements the user will confirm their payment and lead to the booking view.

All works as intended. The form works and the payment is received by Stripe.

1. Here the user can see their booking and is notified that the booking is confirmed.

All works as intended. The user can see their booking from the profile with the correct event details showing.

1. If the user goes to their profile, they can inspect their ticket.

## Responsive Website View

### Desktop

1. The UI is clear and concise.
    - I believe the UI is best on this screen size.
    - User can clearly see all the elements of the page.
    - This is true with smaller monitors.
1. Functionality.
    - Users can book seats to events using the seating chart.
    - We have all functionality

### iPad/iPad Pro

1. The UI is clear and concise.
    - HTML elements stack correctly.
    - Seating chart stays central.
1. Functionality.
    - All functionality available.
    - Seat Chart still works.
1. Contrasting with the desktop view:
    - Events/Venues on the homepage stack.
    - Events page cards look great!
    - Showtime page hero image and information elements change their style correctly.

### Mobile 

1. Problems.
    - HTML elements stack correctly.
    - Much like Showcase Cinema's Website the seat chart does not translate well onto mobile.
1. Functionality.
    - We lose the seat chart functionality on mobile. **IMPORTANT!**

    I believe that it might take heavy time investment to correct this. However, with some luck it might be as simple as adding a media query to change the size of seats on smaller screen sizes. If this is not the case, then we would need to look into this further.

1. Contrasting with the desktop view:
    - Stacking HTML elements.

## Different Browser Tests

### [Mozilla Firefox](https://www.mozilla.org/en-GB/firefox/new/)

All the tests and development have been conducted on Firefox. Bugfixes would have been conducted using the browser development tools.

### [Google Chrome](https://www.google.co.uk/chrome/)

### [Safari](https://www.apple.com/uk/safari/)


## Bugs Fixes During Development

**Bug**: Cookie Problem

**Bugfix**: Swapped to using session cookies through Django. Rather than creating them with Javascript.

**Bug**: Web Hooks Errors 401/502

**Bugfix**: This was resolved by making the development port public.

**Bug**: Seating Chart

**Bugfix**: - 


## Further Testing:

Family members have booked tickets and reviewed documentation to point out any bugs and/or user experience issues. These have either been noted or mentioned in additional features.

[Back to README](README.md)