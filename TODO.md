| Feature | Rationale | Example |
|---------|-----------|---------|
| Save tags to the configuration file and allow them to be searched for | `get_vpc_name()` will only reflect the first matched tag in the event multiple are given. Hosts can have multiple tags which will not be reflected in the name. | Generate an iterable of vpc's that match the given tag.
| Store OTP on device | offprem will be able to authenticate itself without requiring an end user to input the OTP token. |
| Moto for mock testing boto3 | Do not make actual boto3 calls. Allow the use of fabricated AWS credentials for testing. | |

| Enhancement | Rationale | Example |
|-------------|-----------|---------|
| Add docstrings and comments to tests | Improved cognition of tests | |
| CONTRIBUTING.md | Guidelines for contributors |  |

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
