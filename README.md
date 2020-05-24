# Example Contest

This is an example Git repository maintaining programming contest problems
with [Bazel] and [rules_contest].

You can use this repository as a template of a new repository for your
programming contest. Click the [Use this template] button in GitHub UI to
quickly create a new repository.


## Checking latest test results

If this repository is hosted on GitHub, tests are automatically run by
[GitHub Actions] and reports are uploaded to the `report` branch as a Markdown
document.


## Running tests locally

1. Install [Bazel].
2. Run `bazel test //...`


## Documentation

Documentation is available at https://rules-contest.readthedocs.io/.


[Bazel]: https://bazel.build/
[rules_contest]: https://github.com/nya3jp/rules_contest
[Use this template]: https://help.github.com/articles/creating-a-repository-from-a-template/
[GitHub Actions]: https://github.com/features/actions
