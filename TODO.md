| Feature | Rationale | Example |
|---------|-----------|---------|
| Allow tags to be searched for | Allow an alternative, more intuitive way to assign a VPC to `AWSPremise`. | Generate an iterable of vpc's that match the given tag. |
| Store OTP on device | offprem will be able to authenticate itself without requiring an end user to input the OTP token. |
| Moto for mock testing boto3 | Do not make actual boto3 calls. Allow the use of fabricated AWS credentials for testing. | [test_ec2](https://github.com/spulec/moto/tree/e00af2f73cb7d27c3755f18b2161b9acbd8ca8aa/tests/test_ec2) |
| Command Line Tool | VPCs can be easily listed from the terminal. | `__main__.py` can run `get_all_vpcs` with a `--profiles` option; or a `--search` flag to show VPCs that match a tag.

| Enhancement | Rationale | Example |
|-------------|-----------|---------|
| Add docstrings and comments to tests | Improved cognition of tests | |
| CONTRIBUTING.md | Guidelines for contributors |  |
| Consider saving the profile name to the configuration file | When `AWSPremise().assign` is called, only `vpc_name` is required. `profile_name` can be optional. |
| Automated deletion of stale VPCs | Remove the need to manually prune the configuration file. | Load a new parser before saving the contents when `get_all_vpcs` is called. The implementation must be profile-specific since multiple profiles can exist in the file. |

| Bug | Context | Impact |
|-----|---------|--------|
| Custom config/credentials files need to be added to as environment variables | ConfigureCredentials may need to override `__post_init__` to update environment variables |  |
| Improve handling of MFA errors | Put it in a while loop and tell the user to try again | boto3 will balk at a valid MFA if used twice |

# Resources
## Packaging
- [Python Application Dependency Management](https://hynek.me/articles/python-app-deps-2018/)
- [Maintaining a Python Project](https://hynek.me/talks/python-foss/)
## Future-proof Packaging
- [Docker packaging guide for Python](https://pythonspeed.com/docker/)
- [A perfect way to Dockerize your Python application](https://sourcery.ai/blog/python-docker/)
- [Python in GitHub Actions](https://hynek.me/articles/python-github-actions/)
- [GitHub Actions for perfect Python Continuous Integration](https://sourcery.ai/blog/github-actions/)
## Lazy Importing/Loading
- [An approach to lazy importing in Python 3.7](https://snarky.ca/lazy-importing-in-python-3-7/)
- [Python Trick: Lazy Module Loading](https://levelup.gitconnected.com/python-trick-lazy-module-loading-df9b9dc111af)
