- [Mozilla Science Working Open Workshop](https://mozillascience.github.io/working-open-workshop/)
- Best example: [The Ruby on Rails contribution guidelines](https://github.com/rails/rails/blob/master/CONTRIBUTING.md)
    - Also see: [Reporting an Issue](https://edgeguides.rubyonrails.org/contributing_to_ruby_on_rails.html#reporting-an-issue)
- [KHAN Academy Styleguide](https://github.com/Khan/style-guides/blob/master/style/python.md)

# Where to ask for help
- [Issue Tracker]()
- [Documentation]()

# How Can I Contribute?
## Report Bugs
- If you're unable to find an open issue addressing the problem, open a new one. Be sure to include a title and clear description, as much relevant information as possible, and a code sample or an executable test case demonstrating the expected behavior that is not occurring.
- Use the [bug report template](contrib/bug_report_template.md)
- Use a clear and descriptive title for the issue to identify the problem.
- Describe the exact steps which reproduce the problem in as many details as possible. Can you reliably reproduce the issue?
- Provide specific examples to demonstrate the steps. If you're providing snippets in the issue, use Markdown code blocks.
- Describe the behavior you observed after following the steps and point out what exactly is the problem with that behavior.
- Explain which behavior you expected to see instead and why.
- What's the name and version of the OS you're using?
- Are you using a virtual environment?

## Suggest Enhancements / Feature Requests
- Explain why this enhancement would be useful

## Submit Code Changes
### Test Driven Development
### Did you write a patch that fixes a bug?
- Open a new GitHub pull request with the patch.
- Ensure the PR description clearly describes the problem and solution. Include the relevant issue number if applicable.
- Before submitting, please read the Contributing to Ruby on Rails guide to know more about coding conventions and benchmarks.
> Link to documented testing procedures, will probably be in README.md
- Testing: How to test the project, where the tests are located in your directories.
- Run tests before submitting code changes
    - Create new tests to test new enhancements.

### Setup a Local Development Environment
> - Link to documented development procedures, will probably be in README.md
- pip install ..
- `git clone git@github.com:your-username/tree-view.git`
    - Cut a branch
    - Modify code
    - Create a PR
### Python Styleguide
- Use single quotes when possible.
- Use f-strings where possible.
    - Encapsulate f-string in double quotes if single quotes cannot be used.
- `pathlib` instead of `os`
- Take advantage of dataclasses
- Document every function and class.
- Use comments to clarify complex code.

### Git Commit Messages
- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Always write a clear log message for your commits. One-line messages are fine for small changes, but bigger changes should look like this:
    ```
    $ git commit -m "A brief summary of the commit
    > 
    > A paragraph describing what changed and its impact."
    ```