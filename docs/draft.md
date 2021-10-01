## Setup
Your `~/.aws/credentials` file must be properly configured.

```ini
[account]
aws_access_key_id = ABCDEFG
aws_secret_access_key = HIJKLMNOP
mfa_serial = arn:aws:iam:987654321:mfa/UserName

[role]
role_arn = arn:aws:iam::123456789:role/RoleName
source_profile = account
```

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