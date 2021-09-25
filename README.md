# Offprem
A tool to interact with VPCs configured in AWS accounts and roles.

## Installation
Requires Python 3.9+:
```shell
python -m pip install offprem
```

## Features
- Save the VPC ID and region for all VPCs an account/role has access to.
- Supports roles, and accounts with Multi-Factor Authentication enabled.
- Automatically create STS tokens and boto3 sessions to interact with VPCs.

## Usage
Create a configuration file:
```python
from offprem import AWSPremise

search_tags = ['Tags', 'to', 'search', 'for']

premise = AWSPremise()
premise.assign(profile_name='profile_name')
premise.get_all_vpcs(search_tags=search_tags, empty_tags=True)
```

Providing a profile_name and vpc_name to `AWSPremise().assign` will automatically create STS credentials and populates a boto3 session to use. Leverage this by assigning a VPC to query:
```python
from offprem import AWSPremise

premise = AWSPremise()
premise.assign(profile_name='profile_name', vpc_name='vpc_name')
resource_ec2 = premise.session.resource('ec2')
```

## Local Development and Testing
### Development
Development and testing should be done in a virtual environment.
```shell
$ git clone https://github.com/Fauxsys/offprem.git
$ cd offprem
$ python -m venv venv --prompt offprem
$ source venv/bin/activate
(offprem) $ python -m pip install -U pip
```
Install offprem locally.
```shell
(parserconfig) $ python -m pip install -e ".[test]"
```

### Testing
You can test any changes locally with pytest.
```shell
(offprem) $ python -m pytest --cov=offprem 
```

You can also test offprem as an installed package.
```shell
(offprem) $ python -m tox
```

### Building a wheel
```shell
(offprem) $ python -m pip install build
(offprem) $ python -m build --wheel
```

There should now be a wheel in the `dist` directory.
```shell
(offprem) $ ls -1 dist
offprem-0.0.1b0-py3-none-any.whl
```