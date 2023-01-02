API
===

This is a fairly standard HTTP api. All you need is one request, pretty simple.

elements of each request:

``user``
just your username, pretty simple

``password``
just your password. as of v1, this is plaintext in the link and not encrypted. 

``UID``
this is your Unique ID, which we assign when you register.

``activity``
this is what activity your request will be sending. this will usually be your button name or link destination.

gateways:

``/dump/?UID=UID``
this is the gateway we use to populate the desktop app. you can get all the data populated by your users from here.

``/login/?user=USERNAME&password=PASSWORD``
this is the gateway we use to login. it will return a UID if the login is successful.

``/heatmap/?UID=UID&activity=ACTIVITY``
this is the gateway we use to send activity data. it will return "Done" if the data is recorded successfully. this return data may be changed in the future to be more useful.

``/users/get?UID=UID``
this will return all individually collected user data to date. this can very quickly expand, so we don't recommend its usage outside of our client.

``/users/?UID=UID&fname=john&lname=smith&email=johnsmith123@gmail.com``
this is the route you'll need to use in order to log user data. we'll be turning much of this request into JSON headers instead of URL args soon. this will only return either a 400 (bad request) or 200 status code, so don't be looking for any data.