## Setup
Your aws config and credentials files must be properly configured.

## Docker
Using docker-compose:
```
docker-compose up
```
Using docker container run:
```
docker image build -t offprem . && docker container run -v ~/.aws:/root/.aws --name offprem --rm offprem
```

- Without this, an account protected via 2FA would prompt for the code for every region when executing `get_all_vpc`.