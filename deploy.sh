# gunicorn -b 0.0.0.0:12005 manage:manage --log-level=info --access-logfile=access.log --error-logfile=error.log -D
gunicorn -c gunicorn_deploy_conf.py manage:manage -D
