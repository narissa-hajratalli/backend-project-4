# Project Proposal - Backend Development

## Live Website
https://leaft.netlify.app/

## Project Schedule

|  Day | Deliverable | Status
|---|---| ---|
|Day 1| Project Description | Complete
|Day 1| Wireframes / Priority Matrix / Timeline `backend` and `frontend`| Complete
|Day 2| Working RestAPI | Complete
|Day 3| Core Application Structure (HTML, CSS, etc.) | Complete
|Day 4| MVP & Bug Fixes | Complete
|Day 5| Final Touches and Present | Complete

## Project Description
The purpose of this project is to create a full CRUD application to track how much meat a user consumes in a week, for people who want to transition to a healther, more sustainable lifestyle.

For the backend application, I plan to have three models total: user (for authentication), daily_consumption that tracks if the user consumed meat that week, and weekly consumption to track total amount of meat consumed in a week. 


## Time/Priority Matrix 
- [Graphic](https://res.cloudinary.com/ds7vqqwb8/image/upload/v1600052787/Project%203%20-%20leaft/IMG_1542_gzw2vb.heic)


## MVP/Post MVP

#### MVP
- Model for daily_consumption
- Model for weekly_consumption
- User model for authentication
- Create: create a user
- Read (show 1): show just daily consumption
- Read (show all): show everyday's consumption and weekly consumption
- Update: update if eaten meat that day and how many servings
- Delete: delete a user's account once logged in 

#### Post MVP
- Add "type_of_meat" for daily consumption
- Make an additional model for carbon-footprint calculation based on the total amount of meat consumed 

## Functional Components

#### MVP
| Component | Priority | Estimated Time | Time Invetsted | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
| Research and Development| H | 5 hrs | 8 hr | 8 hrs |
| Model for daily_consumption| H | 2 hrs | 2 hrs | 2 hrs |
| Model for weekly_consumption | H | 1.5 hrs | 5 hrs | 5 hrs |
| User model for authentication | H | 3 hrs | 1 hrs | 1 hrs |
| Read (show 1): show just daily consumption | H | 3 hrs | 4 hrs | 4 hrs |
| Read (show all): show everyday's consumption | H | 3 hrs | 2 hrs | 2 hrs |
| Read (show all): show weekly consumption | H | 3 hrs | 2 hrs | 2 hrs |
| Read (show all): show weekly consumption | H | 3 hrs | 2 hrs | 2 hrs |
| Update: update how many servings of meat eaten | H | 3 hrs | 2 hrs | 2 hrs |
| Debugging| H | 7 hrs | 8 hrs |  8 hrs |
| Deployment| H | 2 hrs | 6 hrs | 6 hrs |
| Total | - | 44.5 hrs | 42 hrs | 42 hrs |


#### Post MVP
| Component | Priority | Estimated Time | Time Invetsted | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
| Add "type_of_meat" for daily consumption | M | 1.5 hr | -hr | -hr |
| Make an additional model for carbon-footprint calculation based on the total amount of meat consumed  | L | 2.5 hr | -hr | -hr |
| Create: create a user | H | 3 hrs | - hrs | - hrs |
| Total | - | 4 hrs | 0 hr | 0 hr |

## Additional Libraries
- CORS
- Django JWT
- djangorestframework-jwt==1.11.0
- django-heroku==0.3.1
- psycopg2==2.8.6


## Code Snippets
#### Creating the function that populates the dropdown menu with all the providers
I created a loop within my weekly_consumption model to calculate the total servings each user has per a given week.

```
    def consumption_sum(self):
        days = self.dailyconsumption_set.all()
        counter = 0
        for day in days:
            counter += day.daily_servings
        return counter

    weekly_total = property(fget=consumption_sum)
 ```


## Issues and Resolutions
 
####
Issue
I ran into a roadblock when I wanted to show 1 daily log at a time. This was the first error I got when I tested the route in Postman.
``` TypeError: __init__() takes 1 positional argument but 2 were given ```
