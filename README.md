# Offprem
Offprem will query AWS for all VPC's a profile has access to.
The vpc_id, region, and associated tags of each discovered VPC is stored in a configuration file, which can then be leveraged to automatically create STS tokens and boto3 sessions.

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
Read the [tutorial](/docs/Tutorial.md).

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
offprem-0.0.2b0-py3-none-any.whl
```