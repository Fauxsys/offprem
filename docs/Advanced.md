Define custom paths for configuration files:
```python
from pathlib import Path

from offprem import AWSPremise, ConfigureVPC, ConfigureCredentials

vpc_configuration_file = Path.home().joinpath('.aws/environments.ini')
vpc_configuration = ConfigureVPC(configuration_file=vpc_configuration_file)

session_configuration_file = Path.home().joinpath('.aws/credentials')
session_configuration = ConfigureCredentials(configuration_file=session_configuration_file)

premise = AWSPremise(vpc_configuration=vpc_configuration, session_configuration=session_configuration)
premise.assign(profile_name='default')
```