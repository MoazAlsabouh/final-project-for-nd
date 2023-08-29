# final-project-for-nd
.login here
https://moaz.uk.auth0.com/authorize?audience=restaurant&response_type=token&client_id=DribS2kVibf9SFkcTFNmOoTWQTNA1WwD&redirect_uri=https://capstone-for-nd-udacity.onrender.com/


'''
Barista account
User: barista2@udacity.com
password: udacity123*

this role acsees onle get

Manager account
User: restaurant_manager@udacity.com
password: udacity123*

this role acsees get , post, path and delete
'''

I did not have enough time to build a complete website with Vue.js, so I made a restaurant management system that contains food items and the food itself. There are two ranks, the first is entitled to make all the modifications, and the second can only read the data
Most of the ideas wrote their code for previous projects, so some of the codes did not need to be modified, such as verifying the user, and others I modified them to suit my idea and in the future, God willing, I will create a front-end and develop the project further
All tests are in Postman's file

link in render host
https://capstone-for-nd-udacity.onrender.com/

github repo
https://github.com/MoazAlsabouh/final-project-for-nd

1-
https://capstone-for-nd-udacity.onrender.com/
http://127.0.0.1:5000/
This endpoint is unsecured and public with a link to login and get a token

-2
https://capstone-for-nd-udacity.onrender.com/the-food-detail
http://127.0.0.1:5000/the-food-detail
This endpoint accepts get requests and returns JSON data about our menu
Everyone who owns the Barista and Manager roles has access to it

https://capstone-for-nd-udacity.onrender.com/food-items-detail
http://127.0.0.1:5000/food-items-detail
This endpoint accepts get requests and returns JSON data about our food items
Everyone who owns the Barista and Manager roles has access to it

https://capstone-for-nd-udacity.onrender.com/the-food-detail
http://127.0.0.1:5000/the-food-detail
This endpoint accepts get requests and returns JSON data about our food items
Everyone who owns the Barista and Manager roles has access to it

https://capstone-for-nd-udacity.onrender.com/the-food
http://127.0.0.1:5000/the-food
This endpoint accepts post requests and adds data to our food list, and the data must be sent in a way (Content-Type=application/json) and the object must contain "name" and "rate_it", which is the id number of the food item to which the dish belongs, and if the operation succeeds, it will return Data in JSON format about our menu, and if it fails, it will return an error and its cause
Only those who own the role manager have access to it

https://capstone-for-nd-udacity.onrender.com/food-items
http://127.0.0.1:5000/food-items
This endpoint accepts post requests and adds data to our food items, and the data must be sent in a way (Content-Type=application/json), and the object must contain "type", which is the name of the item. Returns an error and its cause
Only those who own the role manager have access to it

https://capstone-for-nd-udacity.onrender.com//the-food/<int:id>
http://127.0.0.1:5000//the-food/<int:id>
This endpoint accepts PATCH requests and modifies data for a dish from our menu and ends with the id
  For the element that we want to modify, the data must be sent in a way (Content-Type=application/json), and the object must contain "name" and "rate_it", which is the id number of the food item to which the dish belongs. If the process is successful, it returns data in JSON format about the menu What we have, and if it fails, it returns an error and its cause
Only those who own the role manager have access to it

https://capstone-for-nd-udacity.onrender.com/food-items/<int:id>
http://127.0.0.1:5000/food-items/<int:id>
This endpoint accepts PATCH requests and edits data for one of our food items and ends with the id number
  For the element that we want to modify, the data must be sent in a way (Content-Type=application/json), and the object must contain a "type", which is the name of the food item.
Only those who own the role manager have access to it

https://capstone-for-nd-udacity.onrender.com/food-items/<int:id>
http://127.0.0.1:5000/food-items/<int:id>
This endpoint accepts DELETE requests, deleting the element whose id ends with the endpoint
   If the process succeeds, it will return data in JSON format about the number of the deleted element, and if it fails, it will return an error and its cause
Only those who own the role manager have access to it

https://capstone-for-nd-udacity.onrender.com/the-food/<int:id>
http://127.0.0.1:5000/the-food/<int:id>
This endpoint accepts DELETE requests, deleting the element whose id ends with the endpoint
   If the process succeeds, it will return data in JSON format about the number of the deleted element, and if it fails, it will return an error and its cause
Only those who own the role manager have access to it