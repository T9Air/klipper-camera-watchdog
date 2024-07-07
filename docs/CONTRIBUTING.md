# Contributing
All help in developing this repo is greatly appreciated. However, I have a few requests to make to simplify the debugging/tracking process:

1. Please do not fork and PR against the main branch. Anything in the main branch should be considered live, released code.
2. If you are making changes to the Python script please fork and PR only to the Python-Script-Additions branch
3. Likewise with any changes to the G-Code macro
4. If you are making changes that require both the Python script and the G-Code macro to be changed fork and PR to the development branch and include in your pull request that you are changing both
5. Do not PR to the development branch if you are changing both the Python script and the G-Code macro, but the changes to each are not needed for the other, (make 2 individual PRs, one to the Python-Script-Additions branch and one to the G-Code-Macro-Additions branch)
6. If you are making standalone changes to the docs (contributing.md, installation.md, or the readme.md) that are not because you have changed any code, please fork and make PRs to the Docs branch
7. If you are changing any of the docs that are necessary because of changes to any code, include those changes with the PR of your code (see 1 - 5)
8. Any changes that do not have a specified branch should be forked and PRed to the Development branch
9. Please name your commits accordingly, and add some context as to what you have added.
