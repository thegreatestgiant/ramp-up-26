# Book-Library Api
>
> By: Shlomo Alter

## Install

Just clone it, and install the requirements

```sh
uv add -r requirements.txt
```

## Run

There are a few ways to run it.

```sh
uv run uvicorn main:app --port 8080
```

```sh
uv run fastapi dev --port 8080
```

Once the server is up and running. You can visit the [swagger docs](http://localhost:8080/docs#/) to test without cUrl
