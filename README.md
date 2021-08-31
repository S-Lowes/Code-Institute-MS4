Code Institute Project 4

For MS4 I have created a website for 'amphii' the theatre company. The website is built with Python, Django, JavaScript, CSS, Bootstrap and HTML. It uses a relational database, Stripe payment and is designed to be responsive across multiple devices although the primary focus was on desktop. amphii allows users to purchase and view tickets for shows.

# MS4: View Live Project [Here](https://amphii.herokuapp.com/)

## User Experience

#### External User

- To Buy tickets to shows available on the website.
- View tickets that they have purchased.

#### External User

- Sell Tickets for shows.
- Promote new shows via their website.

### User Journey

1. User's Journey starts at the homepage. 
1. They are presented with a carousel of the 3 most recently created shows.
1. Underneath this carousel are 3 clickable images with a more intimate picture of the same shows inviting the user in.
1. Click on many of these buttons leads to the Showtimes page or if using the navbar, they are lead to the events page.

![Homepage](documentation/user_journey/index.png)

1. The Event Page features all the events currently on show at amphii which can be filtered using the search bar.
1. The user can click on the buttons to lead themselves to respective showtime page for that event.

![Event Page](documentation/user_journey/events.png)

1. The showtime page will prompt the user to create and account.
1. This is required to use the website as tickets are stored in the users account page.
1. However, if they are already signed in, the user can click on a showtime they can attend and start booking seats.

![Showtimes](documentation/user_journey/showtimes.png)

1. They are presented with the seat chart. This is much like a cinema booking system where the user can choose seats.
1. A running total is displayed on the side so they can see how much the tickets will cost.
1. When ready, they can confirm their seats and proceed to the payment form.

![Seat Chart](documentation/user_journey/seat-chart.png)

1. As the user is registered some of these form elements should already be filled out.
1. After using stripes somewhat dynamic payment elements the user will confirm their booking and lead to the booking view.

![Payment](documentation/user_journey/payment.png)

1. Here the user can see their booking and is notified that the booking is confirmed.

![Booking](documentation/user_journey/booking.png)

1. If the user goes to their profile, they can inspect their ticket.

![Profile](documentation/user_journey/profile-view.png)


### User Stories

- First Time Visitor
    - When I visit this site I want to understand how I can interact with the website.
    - I want to browse the site looking at potential shows I would like to see.
    - I would also consider making an account.
- Returning Visitor
    - As a returning visitor I may be returning to book seats to a certain event.
    - This would involve registering and interacting with the seat chart to choose seats.
    - I would then like to view the booking from my profile.
- Frequent User
    - As a frequent user I would be looking to make multiple bookings.
    - I would also like to sign in a view my tickets at the venue.
    - I would likely be booking another event.

### Design

- Colour Scheme
    - I used a friendly purple color scheme with a gradient on some elements. I decided to only use purple as my chosen color so as to not cause a sensory overload. This was partly because I was using a large images across multiple pages in this project.
- Typography
    - I used a soft font called 'Quicksand' for its curves. I decided to keep the branding in lowercase and it seemed to be more eye catching.
- Imagery
    - Lots of images! 'Hero images' with wider perspectives and 'Normal Images' with closer more intemate moments. Hopefully this would draw people towards certain elements and maybe into booking a ticket.
- Wireframes
    - I created wireframes for the basic ideas. The overall structure of the website persists from the wireframes to the complete project. However certain functionality I was unable to complete due to time contraints and focus on other problems. Things that didn't make the cut include: The Ticket View, The Special Event & The Modal Login. The Ticket view was essentially replaced by the profile booking form view.
        - [Homepage](documentation/wireframes/navigation-footer.png)
        - [Modal Login](documentation/wireframes/modal-login.png)
        - [Events View](documentation/wireframes/events-view.png)
        - [Showtimes](documentation/wireframes/event-showtimes.png)
        - [Ticket View](documentation/wireframes/profile-viewtickets.png)
        - [Special Event](documentation/wireframes/special-event.png)
        - [Ticket View](documentation/wireframes/ticket-view.png)



## Features

- Seat Booking System, Select from seats available during booking process.
- View tickets from account.
- View shows/events that are on.
- Create events and showtimes as a admin/superuser
- Event carousel for homepage
- Allauth social media signup

## Data Schema

![Data Scheme](documentation/images/db-diagram.png)

This gradually changed as the project went on. initially I would have liked to implement individual tickets to the booking and have a seperate price table for each showtime. However, since I was struggling to use the JQUERY seat charts I had to opt ot do things differently.

## Taking The Project Further (Additional Features)

If I could take the project further, I would like to check in real time when seats are made available or taken away.
I would also like to improvements to iPhone deployment as the seat chart is not interactible on smaller devices.
I would also like to implement QR codes to the booking for scannign when entering a event.

## Technologies

### Languages

- [HTML5](https://en.wikipedia.org/wiki/HTML5)

- [CSS3](https://en.wikipedia.org/wiki/CSS)

- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries & Programs Used

1. [Django](https://en.wikipedia.org/wiki/Django_%28web_framework%29)

1. [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)

1. [Bootstrap](https://getbootstrap.com/)

1. [Heroku](https://en.wikipedia.org/wiki/Heroku)

1. [Git](https://git-scm.com/)

1. [Github](https://github.com/)

1. [Gitpod](https://www.gitpod.io/)

1. [Firefox Dev Tools](https://firefox-dev.tools/)

1. [Google Fonts](https://fonts.google.com/?query=Oswa)

1. [Font Awesome](https://fontawesome.com/)

1. [Balsamiq](https://balsamiq.com/)

1. [Favicon.cc](https://www.favicon.cc/)

1. [TinyPNG](https://tinypng.com/)

1. [Multi Media Mockup](https://techsini.com/multi-mockup/)

1. [Adobe Spark](https://spark.adobe.com/sp)

1. [DBDiagram](https://dbdiagram.io/home)

1. [JQUERY Seat Chart](https://github.com/mateuszmarkowski/jQuery-Seat-Charts/blob/master/jquery.seat-charts.css)


## [TESTING](TESTING.md)

Testing Document can be found here: [TESTING](TESTING.md)


## Deployment, Forking, Cloning

### Deployment to Heroku

##### Create Application

1. Navigate to Heroku.com and login.
1. Click on the "New" button in the top right of the page and select "Create new app."
1. Enter the name of the app, select the region and click "Create app."

##### Connect to GitHub Repository

1. Click the deploy tab and select "GitHub - Connect to GitHub."
1. Under the section "Search for a repository to connect to" enter the repository name in the box provided.
1. Once the repository has been found, click the "Connect" button.

##### Setting Environment Variables

Click on the settings tab and then click "Reveal Config Vars" and add the following:
- key: 

##### Enable Automatic Deployment

1. Click on the Deploy tab
1. Under the "Automatic Deploy" section, select the branch from GitHub that you want to deploy the app from and then click Enable Automatic Deploys

### Forking the GitHub Repository

By forking the GitHub Repository we are making a copy of the original repository on a GitHub account to view and/or make changes without affecting the original repository. This is done with the following steps:

- Log in to [GitHub](https://github.com/) and locate the GitHub Repository.
- At the top of the Repository just above the "Settings" button on the menu, locate the "Fork" button.
- Click the button and now you should have a copy of the original repository in your GitHub account.

### Making a Local Clone

- Log in to [GitHub](https://github.com/) and locate the GitHub Repository.
- Under the repository name, click "Clone or download".
- To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
- Open Git Bash
- Change the current working directory to the location that you want the cloned directory to be made.
- Type `git clone`, and then paste the URL you copied earlier.

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) for a more detailed explanation of the cloning process.


## Credits

1. [JQUERY Seat Chart](https://github.com/mateuszmarkowski/jQuery-Seat-Charts/blob/master/jquery.seat-charts.css)
1. [Carousel](https://www.youtube.com/watch?v=gor5BvT2z88&t=1037s)
1. [AJAX REQUESTS](https://testdriven.io/blog/django-ajax-xhr/)
1. [Safely Including Data for JavaScript in a Django Template](https://adamj.eu/tech/2020/02/18/safely-including-data-for-javascript-in-a-django-template/)




### Code & Media

The space to share any resources I have used to help me build this project.

1. [Zip](https://www.w3schools.com/python/ref_func_zip.asp)

### Acknowledgements