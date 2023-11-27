# Wonder Cabinet Inventory System

The Wonder Cabinet Inventory System is a Python program that allows users to manage an inventory of items in a wonder cabinet. It provides functionality to add, remove, search, and display items in the inventory.

<img width="430" alt="Screenshot 2023-11-27 at 00 16 53" src="https://github.com/doramagnoni/Wonder_Cabinet/assets/137621206/aa28883b-41dd-4001-87b1-0e1c2bebf2f4">

## Table of Contents

1. Wonder Cabinet Inventory System
- User Experience (UX) Design for Wonder Cabinet Inventory System
- View live website in Heroku
- User Stories
- Interaction Flow
   - Main Menu
   - Add Item
   - Remove Item
   - Search Item
   - Display Inventory
- Design Considerations

2. Technologies Used

3. Testing
- Functionality Testing
- Code Validation
   - PEP 8 Style Checking

4. Deployment
- Prerequisites
- Steps
- Run Locally

5. Credits
6. Screenshots


## User Experience (UX) Design for Wonder Cabinet Inventory System

Overview
The Wonder Cabinet Inventory System is designed to provide a simple and intuitive user experience for managing a collection of items in a wonder cabinet. The user interface is text-based, running in the console, making it accessible and straightforward to use.


## [View life website In Heroku](https://wonder-index-96dba1f69579.herokuapp.com/)
---


## User Stories

- As a collector, I want to easily add new items to my wonder cabinet, providing names, descriptions, and origins for each item.

- As an organizer, I want to remove items from the inventory efficiently when needed, keeping my collection up-to-date.

- As a researcher, I want to search for specific items in the wonder cabinet using keywords, making it easy to find relevant information.

- As a curious individual, I want to display the entire inventory at once, allowing me to explore and appreciate the diversity of my wonder cabinet.


## Interaction Flow

Main Menu:

- Add item (Option 1): Users are guided through a step-by-step process to input details for a new item, with the ability to go back to the main menu at any point.

- Remove item (Option 2): Users are prompted to enter the name of the item they want to remove. If the item is found, it is removed, and the inventory is updated.

- Search item (Option 3): Users can enter a keyword to search for items in the inventory. The results are displayed, or a message indicates no matching items were found.

- Display inventory (Option 4): Users can view the entire wonder cabinet inventory, including names, descriptions, and origins for each item.

- Quit (Option 0): Users can exit the application.


Add Item:

- Users are prompted to enter the name, description, and origin of the new item.
- Input validation is in place to ensure the name is not empty and that duplicate names are not allowed.
- Users can go back to the main menu at any point during the process.


Remove Item:

- Users enter the name of the item they want to remove.
- The system checks if the item exists, removes it if found, and updates the inventory.
- Users receive feedback on whether the removal was successful or if the item was not found.

Search Item:

- Users enter a keyword to search for item names.
- The system displays matching items, providing their names, descriptions, and origins.
- If no matching items are found, users receive a message indicating the absence of items with the specified keyword.

Display Inventory:
- The entire inventory is displayed in a clear and formatted manner, showing names, descriptions, and origins for each item.

## Design Considerations
- Clear Console Output: The console output is formatted to be clear and easy to read, using formatting techniques to distinguish different pieces of information.
- Error Handling: Input validation and error messages provide feedback to users, guiding them in using the application effectively.
- Step-by-Step Interaction: The process of adding an item is broken down into steps, ensuring a guided and user-friendly experience.

The Wonder Cabinet Inventory System aims to provide users with a straightforward and efficient way to manage their wonder cabinet collection. With a text-based interface, the focus is on simplicity and ease of use, making it accessible to a wide range of users.



[Back to Table of contents](#table-of-contents)
__

# Technologies used


### PYTHON
* As a programming language.

### GitHub
* As a software hosting platform to keep projects in a remote location.

### Git
* As a version-control system tracking.

### HEROKU
* As a development hosting platform.



[Back to Table of contents](#table-of-contents)

___
# Testing

## Functionality testing 

 I used Chrome developer tools throughout the project for testing and solving problems with responsiveness and style issues.
 
 


## Code Validation


Before deploying the Wonder Cabinet Inventory System, I used PEP 8 Style Checking

### PEP 8 Style Checking

To check for PEP 8 compliance I USED `flake8`, by running:
pip install flake8



[Back to Table of contents](#table-of-contents)

___
# Deployment

The project was deployed on HEROKU. 
[View life website In Heroku](https://wonder-index-96dba1f69579.herokuapp.com/)

I used Gitpod as a development environment where I committed all changes to git version control system.
I used the push command in Gitpod to save changes into GitHub.

To deploy a project I had to: 

### Prerequisites

- [Heroku Account](https://signup.heroku.com/)
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

### Steps

 * Create a Heroku Account:
  sign up for a Heroku account [here](https://signup.heroku.com/).

* Install Heroku CLI:
   Download and install the Heroku Command Line Interface (CLI) from [https://devcenter.heroku.com/articles/heroku-cli](https://devcenter.heroku.com/articles/heroku-cli).

* Login to Heroku:
   Open a terminal and run the following command to log in to your Heroku account:
   ```bash
   heroku login


To run locally:
* Log in to GitHub and click on the repository to download ([MP1](https://github.com/doramagnoni/Wonder_Cabinet.git))
* select `Code` and click Download the ZIP file.
* After downloading you can extract the file and use it in your local environment.

___
# Credits


* To complete this project I used the Code Institute student template: [gitpod full template](https://github.com/Code-Institute-Org/gitpod-full-template)
      
* I would like to express my gratitude to my mentor Adegbenga Adeye who helped me extensively to fix numerous problems with my code and supported me very patiently throughout all the stages of the creation of this portfolio. 

___
[Back to Table of contents](#table-of-contents)

# Screenshots

<img width="430" alt="Screenshot 2023-11-27 at 00 16 53" src="https://github.com/doramagnoni/Wonder_Cabinet/assets/137621206/9cb3e072-d81d-4649-b22a-ecafe73bcc59">


<img width="383" alt="Screenshot 2023-11-27 at 00 17 09" src="https://github.com/doramagnoni/Wonder_Cabinet/assets/137621206/701cd847-e4ae-410f-8f2d-574aa815f68c">


<img width="504" alt="Screenshot 2023-11-27 at 00 17 20" src="https://github.com/doramagnoni/Wonder_Cabinet/assets/137621206/ad2d28fe-0a4b-42f1-952a-9810107cd2f6">


<img width="397" alt="Screenshot 2023-11-27 at 00 17 44" src="https://github.com/doramagnoni/Wonder_Cabinet/assets/137621206/10c708bd-269b-4af2-a690-3ed87fab7b8d">


<img width="643" alt="Screenshot 2023-11-27 at 00 20 05" src="https://github.com/doramagnoni/Wonder_Cabinet/assets/137621206/5ac25243-e60b-4069-939f-2805b5e77724">


<img width="556" alt="Screenshot 2023-11-27 at 00 20 59" src="https://github.com/doramagnoni/Wonder_Cabinet/assets/137621206/8c0fe04b-97e9-4082-8a9c-70f059bab9a1">


<img width="494" alt="Screenshot 2023-11-27 at 00 22 32" src="https://github.com/doramagnoni/Wonder_Cabinet/assets/137621206/eab2319a-5e91-4bef-8d6a-939bedf6d474">


<img width="729" alt="Screenshot 2023-11-27 at 00 22 47" src="https://github.com/doramagnoni/Wonder_Cabinet/assets/137621206/76dfb6df-2798-4d7a-992d-48ac3f0a7879">


<img width="725" alt="Screenshot 2023-11-27 at 00 23 36" src="https://github.com/doramagnoni/Wonder_Cabinet/assets/137621206/7acf072a-728e-496d-b835-9063023f364c">


<img width="470" alt="Screenshot 2023-11-27 at 00 23 49" src="https://github.com/doramagnoni/Wonder_Cabinet/assets/137621206/c0d4495f-d7ce-4c78-bc3d-8d0c44915ae2">
