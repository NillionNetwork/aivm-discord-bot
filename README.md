# AIVM Discord Bot

## Build and run

### With Docker
Run with Docker:

```shell
cd docker
docker build -t aivm-bot -f Dockerfile ..
```

Run with:

```shell
docker run --restart always aivm-bot
```


### From source

```shell
poetry install
```
```shell
poetry run aivm-devnet &
poetry run aivm-bot 
```