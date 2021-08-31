# Testing

The W3C Markup Validator, W3C CSS Validator, JSHint and PEP8Online services were used to validate the pages of this project. This ensures there were no syntax errors. I also used formatters for my HTML, CSS & JS.

#### Validators

##### HTML

[W3C Markup Validator](https://validator.w3.org/)

1. [Homepage](documentation/html_validation/homepage.png)
1. [Search](documentation/html_validation/search.png)
1. [Login](documentation/html_validation/login.png)
1. [Register](documentation/html_validation/register.png)
1. [View Recipe (cook)](documentation/html_validation/cook.png)
1. [Create Recipe](documentation/html_validation/create.png)
1. [Edit Recipe](documentation/html_validation/edit.png)

After creating extra input elements with the dynamic form the HTML validator will display erros. This is due to these inputs sharing an ID which is necessaery when selecting them for deletion.

##### CSS, Python, Javascript

-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - [Results](documentation/validation/css_valid.png)
-   [JSHint](https://jshint.com/) - [Results](documentation/validation/jshint.png)
-   [PEP8](http://pep8online.com/) - [Results](documentation/validation/pep8.png)

#### Formatters

- [HTML Formatter](https://www.freeformatter.com/html-formatter.html)
- [CSS Formatter](https://www.freeformatter.com/css-beautifier.html)
- [JS Formatter](https://beautifier.io/)

### Testing User Journey
1. The user begins at the Homepage and is prompted to register so they can create a recipe. 
    - User can see the brief description of the website at the homepage. This gently guides the user towards registration.
1. Or they can take a look at 3 of the most recent recipes created by other users.
    - These are visible just below the description of the website.
1. Upon clicking 'Register' the user can then create an account.
    - When the relevant navigation is clicked the user is correctly taken to the registration form.
1. After making an account they are automatically logged in and taken to their recipe page.
    - This happens as intended.
    - User cannot submit invalid form inputs or those that do not meet the format expected.
1.  If they already have recipes then those will displayed, If not, then the user is prompted to create a recipe.
    - All of users recipes are displayed or a button that leads to creation is present. Both these expectations are met.
1. If the user then decides to create a recipe they can click the create recipe tab in the navbar or the button on myrecipes.
    - Both options that leads to recipe creation work.
1. This brings them to the creation page. This Dynamic form allows the user to add ingredients and instructions dynamically.
    - Dynamic form works as intended.
1. Once the recipe is created it will appear in their 'My Recipes' tab.
    - Upon creation of a recipe we can see it on the homepage and in my recipe tab. This works are intended.
1. They can edit and delete any recipe that they make.
    - Editing works as intended.
    - Deleting also works as intended.
1. Searching for a recipe.
    - Upon clicking 'search recipe' in the navbar the user is taken to the search page correctly.
    - Searching for an ingredient such as 'salt' or a name of a recipe such as 'luganica' works as intended.

* Testuser was created to explore the users journey.
* Testuser created the recipe 'Testing User Journey.'
* Testuser edited this same recipe changing the image via a new url.
* Testuser edited further by adding a new ingredient and step to this test recipe.
* Testuser then deleted the edited recipe recipe.
* Testuser created and deleted a different recipe.


### Testing User Stories

- First Time Visitor
    - When I visit this site I want to understand how I can interact with the website.
        1. Ways to interact with the website are briefly explained on the homepage.
        1. The use of enticing buttons and a simple navbar allow for easy interaction.
    - I want to find a recipe to cook.
        1. The most recent recipes are displayed to the user.
        1. The user can also search for recipes or browse all recipes by clicking or 'Search Recipes' in navbar.
    - I would also consider making an account.
        1. Easily achieved by clicking on 'Register' in the navbar.
- Returning Visitor
    - As a returning visitor I may be searching for the same recipe.
        1. This can be achieved by searching for the name of that recipe.
    - I have returned to register an account so that I can make create a recipe.
        1. Easily achieved by clicking on register in the navbar.
    - I may be logging in to create my own recipe.
        1. This can be done through the navbar and filling in the dynamic form.
- Frequent User
    - As a frequent user I would be looking to create multiple recipes.
        1. This can be done through the navbar and filling in the dynamic form.
        1. The users multiple recipes can be found in 'My Recipes' Tab.
    - I may also be searching through other users recipes to find inspiration or a recipe to cook.
        1. This is lacking, but the search functionality will help as well as all other users recipes being displayed.

## Responsive Website View

### Desktop

1. The UI is clear and concise.
    - User can clearly see all the elements of the page.
    - This is true with some smaller monitors.
    - Although, the sticky header and fixed footer encourage scrolling.
1. Functionality.
    - All CRUD functionality is available.
    - Dynamic form is indeed dynamic and input field can be added or taken away.

### iPad/iPad Pro

1. The UI is clear and concise.
    - I believe the UI is best on this screen size.
    - This is especially true when scrolling across many recipes with the sticky header and fixed footer.
1. Functionality.
    - All CRUD functionality is available.
    - Dynamic form is indeed dynamic and input field can be added or taken away.
1. Contrasting with the desktop view:
    - Header and Footer shrink
    - Cook, Delete and Edit buttons also change size.
    - Buttons stack if needed so they can fit onto the screen.

### Mobile 

1. The UI is clear and concise.
    - User can see all the elements of the page.
1. Functionality.
    - All CRUD functionality is available.
    - Dynamic form is indeed dynamic and input field can be added or taken away.
1. Contrasting with the desktop view:
    - The header and footer are now static. This is because they obstructed the mobile view too much.
    - Recipe cards now stack so they can fit onto the screen.

## Different Browser Tests

### [Mozilla Firefox](https://www.mozilla.org/en-GB/firefox/new/)

All the tests and development have been conducted on Firefox. Bugfixes would have been conducted using the browser development tools.

### [Google Chrome](https://www.google.co.uk/chrome/)

The forms works and UI appear as designed.

### [Safari](https://www.apple.com/uk/safari/)

The forms works and UI appears as designed.

## Bugs Fixes During Development

**Bug**: Static Header and Footer caused white space below footer on certain pages.

**Bugfix**: Fixed by adding a min-height to css of those particular pages.

**Bug**: Data was not sending to database in correct format.

**Bugfix**: This was resolved thanks to the Zip function in Python.

**Bug**: Validation of HTML caused an error with shared ID across HTML elements.

**Bugfix**: This was fixed via some small edits to Javascript and HTML. (Although issue still would appear when creating multiple form elements from the dynamic form)

**Bug**: Jinja loop caused a validation error.

**Bugfix**: This was fixed by getting rid of the unnecessary else statement.

**Bug**: 403 error form was not displaying.

**Bugfix**: This was because I had not added a validation check as to whether or not the user trying to delete or edit a recipe (using the url and id) was the user that created it. This was resolved by adding a check for the session user in the relevant Python functions and then rendering the error page.

**Bug**: Could not edit ingredients as they were not appearing.

**Bugfix**: I had missed deleting an 's' on the end of a name of an input.

## Further Testing:

Family members have created and deleted recipes and reviewed documentation to point out any bugs and/or user experience issues. These have either been noted or mentioned in additional features.