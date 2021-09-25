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


Define custom paths for configuration files:
```python
from pathlib import Path

from offprem import AWSPremise, ConfigureVPC, ConfigureCredentials

vpc_configuration_file = Path.home().joinpath('.aws/environments.ini')
vpc_configuration = ConfigureVPC(configuration_file=vpc_configuration_file)

session_configuration_file = Path.home().joinpath('.aws/credentials')
session_configuration = ConfigureCredentials(configuration_file=session_configuration_file)

premise = AWSPremise(vpc_configuration=vpc_configuration, session_configuration=session_configuration)
premise.assign(profile_name='profile_name')
```

- Query AWS for all VPC's a profile has access to.
- Found VPC's can be stored in a configuration file along with the name, id, and region.
- The configuration file can then be leveraged to automatically create STS tokens and boto3 sessions.
