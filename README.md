# tsg-redis

You will need to use environment variable for MacOS
`OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES`

You will need to use environemtn variable for SendGrid API Key (this can be setup in .env file)
`SENDGRID_API_KEY=`

You will need to build redis from source
`sh setup_redis.sh`

You will need to start redis
`sh start_redis.sh`

You will need to install requirements with poetry
`poetry install`

You will need to start a shell with the proper virtualenv
`poetry shell`

You will need to start listener in this shell
`rqworker`
