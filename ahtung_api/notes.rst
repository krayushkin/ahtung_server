Ahtung server api documentation
===============================

Ahtung server accept commands in form of HTTP POST requests.
Address of api server is `http://API_HOST/api`

Command arguments sends via JSON format.

::
  
  {
      "action" : "API_FUNCTION_NAME",
      "args" : 
          {
              RESULT_STRUCTURE
          }
  }

Result returns in JSON format too.

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

1. `action` = `get_users`

Get list of persons names in given group.

Request:

::

  {
      "action" : "get_users",
      "args" : 
          {
              "group_id" = "GROUP_ID"
          }
  }

Response:

::

  {
      "status" : "STATUS_CODE",
      "data" : 
          {
              "persons" : ["NAME 1", "NAME 2", ...]
          }
  }


2. `action` = `join_group`

Register new user in given group.
If user already exist in other group, it will be removed from old group end registered in new given one.
Returns enabled signals.
Request:

::

  {
      "action" : "join_group",
      "args" : 
          {
              "group_id" = "GROUP_ID",
              "registration_id" = "REGISTRATION_ID",
              "name" = "NAME_1"
          }
  }

Response:

::

  {
      "status" : "STATUS_CODE",
      "data" : 
      {
        "signals" : ["SIGNAL_1", "SIGNAL_2"]
      }
  }

3. `action` = `leave_group`

Deletes given user from database.

Request:

::

  {
      "action" : "leave_group",
      "args" : 
          {
              "registration_id" = "REGISTRATION_ID"
          }
  }

Response:

::

  {
      "status" : "STATUS_CODE"
  }


4. `action` = `create_group`

Create group with enabled signals and return GROUP_ID.

Request:

::

  {
      "action" : "create_group"
      "args" : 
      {
          "signals" : ["SIGNAL_1", "SIGNAL_2", ...]
      }
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

5. `action` = `send_signal`


Request:

::

  {
      "action" : "send_signal",
      "args" : 
          {
              "registration_id" : "REGISTRATION_ID",
              "signal" : "SIGNAL_2"
          }
  }

Response:

::

  {
      "status" : "STATUS_CODE"
  }

