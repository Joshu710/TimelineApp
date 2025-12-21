# How to Git

## Branch off existing Branch

`git checkout -b <new branch> <existing>`

## Keep feature branch up-to-date

1. `git fetch`

2. `git checkout <main branch>`

3. `git pull`

4. `git checkout <feature branch>`

5. `git merge main`

6. Address conflicts

7. `git push origin <feature branch>`

## Merge Feature branch into main

1. Make sure feature branch is up-to-date (Steps Above)

2. `git checkout <main branch>`

3. `git merge <feature branch>`

4. Resolve git conclicts.

5. `git push origin main`

6. (IF PUSH DOESN'T WORK).

   `git pull --no-rebase origin main` \
   Do steps 4-7 from [Keep feature branch up-to-date](#keep-feature-branch-up-to-date)
