
# Version Control & Git

How do multiple people work on a single program without 
'Version Control' . There is a code `repository` or `'repo'` on a remote server. By creating a `branch`, a developer can work and commit changes without changing the `master` copy of the code. After getting the feature in a reasonably-developed state, the developer can then `merge` the branch with master, and others can `pull` their changes from the repository.

Below are some benefits to using a VCS:

- Security: Many hours of work goes into developing software, and it is thus highly valuable to a company or organization. What if a laptop is stolen, or a hurricane floods the data center, or hackers wipe your hard drives?

- Collaboration: Multiple people can edit a program's source code simultaneously.

- History: By keeping track of every change, one can easily reverse a mistaken change they'd made, and always has access to a 'working version' once established.

[Git](https://git-scm.com/) is one popular form of version control, others include [SVN](https://subversion.apache.org/) and [Mercurial](https://www.mercurial-scm.org/). Below are some common CLI commands for working with Git, you can find more in the [docs](https://git-scm.com/docs).

`git init` creates a local repository in your current working directory

`git clone <url>` creates a local copy of a remote reposity

`git status` displays changes on the current branch since your last commit

`git add <files>` adds the specified files to the pending commit

`git commit -m <message>` commits the changes to the local repository

`git push <remote> <branch>` pushes the changes to the remote repository