## Docker
Using docker-compose:
```
docker-compose up
```
Using docker container run:
```
docker image build -t offprem . && docker container run -v ~/.aws:/root/.aws --name offprem --rm offprem
```

- Without using STS credentials, an account protected via 2FA would require a token code for every region when executing `get_all_vpc`.
- `get_all_vpcs` is safe to re-run since every section is uniquely named.
- After time, it is possible that VPCs are decommissioned. Your configuration can be cleaned manually by deleting specific sections, but it could potentially save more time simply deleting the file and re-running `get_all_vpcs`.
```python
from pathlib import Path

configuration_file = Path.home().joinpath('.aws/environments.ini')
configuration_file.unlink()
```