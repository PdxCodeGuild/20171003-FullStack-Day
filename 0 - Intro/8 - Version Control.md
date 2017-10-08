
# Version Control & Git

## Version Control

How do multiple people work on a single program without 
'Version Control' . There is a code `repository` or `'repo'` on a remote server. By creating a `branch`, a developer can work and commit changes without changing the `master` copy of the code. After getting the feature in a reasonably-developed state, the developer can then `merge` the branch with master, and others can `pull` their changes from the repository.

Below are some benefits to using a VCS:

- Security: Many hours of work goes into developing software, and it is thus highly valuable to a company or organization. What if a laptop is stolen, or a hurricane floods the data center, or hackers wipe your hard drives?

- Collaboration: Multiple people can edit a program's source code simultaneously.

- History: By keeping track of every change, one can easily reverse a mistaken change they'd made, and always has access to a 'working version' once established.

## Git

[Git](https://git-scm.com/) is one popular form of version control, others include [SVN](https://subversion.apache.org/) and [Mercurial](https://www.mercurial-scm.org/). Git calls the directory it’s tracking all changes in a **repository**. Git stores timestamped snapshots of the state of the repo called **commits**:

    commit 6aeba8f3f2c386e4dc97fd3e0b8fbfee8d751ac5
    Author: David Selassie <david@pdxcodeguild.com>
    Date:   Tue Mar 29 16:29:27 2016 -0700

Each commit has a globally unique **hash,** an author, a timestamp, a description of what changed, and a **parent** commit. Each commit stores the exact changes made to the files from the last commit. Commits build on top of each other to form a **history,** the full record of all snapshots of a project. The most recent commit is called the `HEAD`.

    Time --->
    C1 - C2 - C3 - C4
                    |
                    HEAD

## Git Commands

Git gives you a suite of command line tools. All commands below are run from within the repository directory. You can find more in the [docs](https://git-scm.com/docs).

`git init` creates a repository in your current working directory. This will make an invisible `.git` directory. Don’t touch anything in it or delete it. It contains the repo’s history.

`git clone <url>` creates a local copy of a remote reposity

`git status` displays changes on the current branch since your last commit

`git add <files>` adds the specified files to the pending commit

`git commit -m <message>` commits the changes to the local repository

`git push <remote> <branch>` pushes the changes to the remote repository

`git diff` view the difference between the last commit and your working directory

`git log` view a list of your commits

`git status` view a summary of all the files Git knows about, whether they've changed since the last commit, and whether there are commits that are staged (not yet pushed).
