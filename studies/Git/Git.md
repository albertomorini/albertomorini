# Git
> List of commands

## Config
git config --global user.name myusername
git config --global user.email myemail

### Github token
git config --global github.user myusername
git config --global github.token mytoken


## Create 

`git init` 

------------------------

## Pull
- `git pull` to download the new version from git

Single file
- `git fetch {remote}`
- `git checkout FETCH_HEAD -- {file}`

from different branch
- `git fetch origin master:master`

------------------------

## Push 

- `git add $filename` or `*` to add to remote repo
- `git commit -m $message` to insert the message commit
- `git push` 

------------------------

## Merge and Rebasing

- **merge**: 
1. Suppose originally there were 3 commits, A,B,C:
2. Then developer Dan created commit D, and developer Ed created commit E:

`A<-B<-C and now C<-D and C<-E`

*MERGE*: D+E
*Rebase*: D<-E2 (so "cancel" commit E and create a new commit based on the last commit D)


------------------------


## Checkout & stash

**Checkout**: to change current branch

- `git branch -f` list them
- `git checkout $brnc`

**Stash**: git-stash - Stash the changes in a dirty working directory away

- `git stash list` 
- `git stash show [-u | --include-untracked | --only-untracked] [<diff-options>] [<stash>]` show the differences
- `git stash drop [-q | --quiet] [<stash>]`
- `git stash apply [--index] [-q | --quiet] [<stash>]`
- `git stash branch <branchname> [<stash>]` create new branch
- `git stash [push [-p | --patch] [-S | --staged] [-k | --[no-]keep-index] [-q | --quiet]` Save your local modifications to a new stash entry and roll them back to HEAD
- `git stash create [<message>]` create

