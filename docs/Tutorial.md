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

Based on this example configuration file, `profile_name` can be either `account` or `role`. In the examples below, however, I will use `default` as the `profile_name`.

# Save VPCs to a configuration file
```python
from offprem import AWSPremise

premise = AWSPremise()
premise.assign(profile_name='default')
premise.get_all_vpcs(search_tags=None, empty_tags=True)
```
The code above will collect every VPC ID in every region, and store the results in `~/.aws/environments.ini` for later use. `profile_name` should reflect a named profile in `~/.aws/credentials`.

Imagine we have `vpc-xxxxx` located in `eu-region-5`. This will be saved to the configuration file as:
```ini
[vpc-xxxxx|eu-region-5]
vpc_id = vpc-xxxxx
region_name = eu-region-5
```

To limit the results returned, pass a list of tags to the `search_tags` parameter. This list should only contain 'keys', since the 'value' of the tag will then be saved in the configuration file. The resource will only be named after the first tag found.
```python
search_tags = ['Owner', 'Environment', 'Stack']
premise.get_all_vpcs(search_tags=search_tags, empty_tags=False)
```

Following the example above; if the VPC was tagged with the key `Owner` and the value `saul`, the result saved to the configuration file would be:
```ini
[saul|vpc-xxxxx|eu-region-5]
vpc_id = vpc-xxxxx
region_name = eu-region-5
```

# Leverage the configuration file
Once the configuration file is populated, you can interact with the VPCs saved in the file using the `assign` method seen earlier. This time, we must include the `vpc_name` parameter:
```python
premise.assign(profile_name='default', vpc_name='saul|vpc-xxxxx|eu-region-5')
```

When `profile_name` is provided to `AWSPremise().assign`, STS credentials are automatically generated and passed to `AWSPremise().session`, which is a `boto3.session.Session` object.
```python
resource_ec2 = premise.session.resource('ec2')
```

Use the `session` method as you normally would -- only difference is that it is authenticated on your behalf, and all you had to do was provide a `vpc_name`.