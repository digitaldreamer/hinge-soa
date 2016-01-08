#########
HINGE SOA
#########

This is an idea on how the services can be isolated and how they would interact.


Get Matches Request "stack trace"
#################################

* get matches requst is generated from the client `https://api.hinge.co/v1/users/{uid}/matches`
* request gets picked up by the router
* router sees the endpoint is mapped to the matchmaker service and asks for the user's matches calling `https://api.hinge.co:8002/v1/matches`
* matchmaker service accepts the request
* matchmaker gets the match records for a user
* matchmaker detects that it needs to translate the match records to matched user resources
* matchmaker extracts the user uid list
* matchmaker asks the router to get the user's list `https://api.hinge.co/v1/users`
* router handles the request and sees that the users resource is mapped to the identity service
* router asks the identity service for the list of users `https://api.hinge.co:8001/v1/users`
* identity service accepts the request
* identity fetches the list of users and gives it back to the router
* router returns the hydrated users to matchmaker
* matchmaker gets the hydrated users
* matchmaker compiles the payload and returns the match list to the router
* router returns the hydrated match list to the client


NOTES:

* the focus of this design is isolation: it gives each component descreet single-minded problem sets and tasks to deal with leading to smaller classes and functions containing less logic
* all API request go through the router
* there is no business logic inside the router, it simply takes a request and sends it to the appropriate service
* services are ideally (but not required to be) in the same data center so all router-to-service communication goes through the inet
* service-to-service communication is not allowed. If a service needs a resource that it doesn't controll then the service interacts with it through the router
* a service can manage many resources and collections, however a single resource and collection can only be interacted directly on by one service
* all services could connect to the same datastore (mongo database) as long as they abide by the contract of not accessing collections that another service controlls
* each resource can be written in the language/tools of choice that best fit its problem domain
* because the data for the resource is isolated to a single service the storage engine (mongo, postgres, cassandra) can be different without affecting other services
* a developer only has to deal with the context within a single service at any given time
* testing is simplified as resources between services are (hopefully) decoupled and requests to the router for resources can be mocked
* there are alternative ways on how to support service-to-service communication but passing everything through the router is a simple design


Services
########

These run as seperate processes.

::

    router  # dispatches HTTP requests to the required service
    identity  # controls users and principle (identity) verification
    matchmaker  # manages potentials, ratings, and matches


Service Ports
#############

::

    443 - router
    8001 - identity
    8002 - matchmaker


router API endpoints
####################

::

    https://api.hinge.co/v1/matches
    https://api.hinge.co/v1/users
    https://api.hinge.co/v1/users/{uid}
    https://api.hinge.co/v1/users/{uid}/matches


identity API endpoints
######################

::

    https://api.hinge.co:8001/v1/users
    https://api.hinge.co:8001/v1/users/{uid}


matches API endpoints
#####################

::

    https://api.hinge.co:8002/v1/matches
