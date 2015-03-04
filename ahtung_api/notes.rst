Ahtung server api documentation
===============================

Ahtung server accept commands in form of HTTP GET or POST requests.
Address of api server is `http://API_HOST/api/ACTION`, where ACTION is one of function name

Command arguments sends via url parameters.
Request body must be empty. For some commands must be provided request body in application/json format.

Example of parameters:

::

  "arg1" : "value1"
  "arg2" : "value2"

Url for this example:  `http://API_HOST/api/ACTION?arg1=value1&arg2=value2`

Format of request body described in command description.

Result returns in JSON format.

::

  {
      "status" : "STATUS_CODE",
      "data" : 
          {
              RESULT_STRUCTURE
          }
  }


Command list
------------


`GET api/get_users`
~~~~~~~~~~~~~~~~~~~

Get list of persons names in given group.

Request:

::

  "group_id" = "GROUP_ID"

Response:

::

  {
      "status" : "STATUS_CODE",
      "data" : 
          {
              "persons" : ["NAME 1", "NAME 2", ...]
          }
  }


`POST join_group`
~~~~~~~~~~~~~~~~~

Register new user in given group.
If user already exist in other group, it will be removed from old group end registered in new given one.
Returns enabled signals.

Request:

::

  "group_id" = "GROUP_ID",
  "registration_id" = "REGISTRATION_ID",
  "name" = "NAME_1"

Response:

::

  {
      "status" : "STATUS_CODE",
      "data" :
      {

      }
  }

POST leave_group`
~~~~~~~~~~~~~~~~~

Deletes given user from database.

Request:

::

              "registration_id" = "REGISTRATION_ID"

Response:

::

  {
      "status" : "STATUS_CODE"
  }


`POST api/create_group`
~~~~~~~~~~~~~~~~~~~~~~~

Group recurse must be provided in request body.

Create group with enabled signals and return GROUP_ID.

Request:

For this command arguments must be provided in request body.

::
{
  "signals" : ["SIGNAL_1", "SIGNAL_2", ...]
}

Response:

::

  {
      "status" : "STATUS_CODE",
      "data" :
      {
          "group_id" : "GROUP_ID"
      }
  }

`POST api/send_signal`
~~~~~~~~~~~~~~~~~~~~~~

Request:

::

  "registration_id" : "REGISTRATION_ID",
  "signal" : "SIGNAL_2"

Response:

::

  {
      "status" : "STATUS_CODE",
      "data" :
      {
          "persons" : ["NAME 1", "NAME 2", ...]
      }
  }

