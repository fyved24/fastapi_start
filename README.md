# fastapi template

basic example for fastapi project

```shell
├── api # api layer
│   ├── __init__.py # include routers
│   ├── common
│   │   ├── common_response.py 
│   │   └── exceptions_handler.py # global exception handler
│   └── v1 # api version 1
│       ├── records.py
│       └── users.py
├── common # common tools
│   ├── assert_util.py # assert util to raise biz exception
│   ├── biz_exception.py
│   └── errs.py # error code enums
├── core
│   ├── database.py # database connection
│   └── dependencies.py # functions for deps injection
├── dal
│   └── user_dal.py # database access layer
├── models
│   ├── __init__.py # load models for sqlmodel to initialize database
│   └── user.py
├── schemas
│   └── user.py # user schemas，for api layer
├── services # biz logic
│   └── user_service.py
├── main.py 
├── start.sh # startup script

```