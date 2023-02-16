# To Do List App
The To Do List App has a title that speaks for itself. It is a application that helps you create, edit and sort through a to do list.

![Mockup](https://github.com/luayidriss/to-do-list-app/blob/72406f10aae9f84ea0372029352f017e7c913f19/media/app.png)
## Features 

The app lets you add new tasks, remove previous tasks, edit task's parameters (name, due date and completion status). It also allows you to save your to do list, and load other to do lists.

### How to Use

- __Main Menu__

  - You have a choice between different options to manipulate your to do list.

![Main Menu](https://github.com/luayidriss/to-do-list-app/blob/72406f10aae9f84ea0372029352f017e7c913f19/media/main_menu.png)

- __Adding a Task__

  - Provide a Task Name and a Due Date. 

![Add Task](https://github.com/luayidriss/to-do-list-app/blob/72406f10aae9f84ea0372029352f017e7c913f19/media/add_task.png)

- __Editing a Task__

  - All tasks are automatically added as incomplete, here you can change their status of completion. You can also edit their name and due date.

![Edit Tasks](https://github.com/luayidriss/to-do-list-app/blob/72406f10aae9f84ea0372029352f017e7c913f19/media/edit_task.png)

- __Sort To Do List__ 

  - You can sort your to do list by due date (from closest to the latest due date), as well as by status of completion (in progress, then incomplete, and completed tasks at the end).

![Sort Tasks](https://github.com/luayidriss/to-do-list-app/blob/72406f10aae9f84ea0372029352f017e7c913f19/media/sort.png)

- __Save and Load__

  - Saves and Loads your to do lists unto the application.

### Features Left to Implement

- Another feature idea is to be able to save and load files to a google cloud storage space.

## Testing 

I have manually tested the application by doing the following

  - Passed the code through PEP8 linter
  - Given Invalid Inputs: strings when numbers are expected, invalid dates, empty task names
  - Tested in Local Terminal and Heroku

- __Unfixed Bugs__

When deployed to Heroku, the save and load features do not work since Heroku does not recognize the local directories in the workspace of this project. A future feature as outlined above is to use Google Cloud Storage API to store our data elsewhere so it can be accessed even on Heroku.

- __Validator Testing__
PEP8:
  - Only errors returned were too long lines of code, which could not be avoided as they are print statments.
  -
## Deployment

- The site was deployed to Heroku. The steps to deploy are as follows: 
  - Create a new Heroku App
  - Set the building blocks to python and node.js in that order
  - Link the Heroku App to the repositery
  - Click on Deploy

## Credits 

Code Institute for the deployment terminal and all templates and knowledge and my Mentor for his ongoing support.
