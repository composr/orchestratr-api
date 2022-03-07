# FastApi Skeleton
A FastApi project aimed at being a functional automation service

# Install dependencies
poetry is the package manager of choice. please install using `pip install poetry -g`

Once poetry is installed, install dependencies using `poetry install`

# Running anything
Ensure you are shelled into your virtualenv with `poetry shell` 

# Starting the app
From the root of the repository run:
`uvicorn app.main:app --port 8080 --reload`

# Running tests
From the root of the repository run:
`pytest tests`
