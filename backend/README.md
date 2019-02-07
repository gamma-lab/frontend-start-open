## Table of Contents

* [Quick Start](#quick-start)

## Quick start

Quick start:

- Create virtual environment `virtualenv venv`.
- Load the venv `source venv`.
- Install python packages `pip install -r requirement`.
- Add environment variable
  ```
  export SECRET_KEY=<a long string>
  export FLASK_APP=app
  export FLASK_ENV=development
  ```
- Initialize sqlite database `flask init-db`
- Run `flask run`.
