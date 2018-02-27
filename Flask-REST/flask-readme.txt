# Tutorial Link
# https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

# REST end points
# URL ROOT  http://[hostname]/todo/api/v1.0/
# GET	    http://[hostname]/todo/api/v1.0/tasks	Retrieve list of tasks
# GET	    http://[hostname]/todo/api/v1.0/tasks/[task_id]	Retrieve a task
# POST	    http://[hostname]/todo/api/v1.0/tasks	Create a new task
# PUT	    http://[hostname]/todo/api/v1.0/tasks/[task_id]	Update an existing task
# DELETE	http://[hostname]/todo/api/v1.0/tasks/[task_id]	Delete a task

# How to run Flask App
# First make sure flask is installed in the anaconda environment
# conda list | grep flask
# conda install flask

# Run the program
# python app.py to start the application
# end point to access web app once it is started

# http://localhost:5000
should show "Hello World" message

# Run GET command
# To run commandline - curl -i http://localhost:5000/todo/api/v1.0/tasks
# To run commandline - curl -i http://localhost:5000/todo/api/v1.0/tasks/2
# To run commandline - curl -i http://localhost:5000/todo/api/v1.0/tasks/3
# Open chrome browser and access GET URL
# http://localhost:5000/todo/api/v1.0/tasks

# Run POST command to create a new task
# curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' http://localhost:5000/todo/api/v1.0/tasks


# Run PUT command to update an existing task
# curl -i -H "Content-Type: application/json" -X PUT -d '{"done":true}' http://localhost:5000/todo/api/v1.0/tasks/2


# Run DELETE command to delete an existing task
#
