#!/usr/bin/env bash
# exit on error
set -o errexit

# rm all files
git rm -r --cached .
# add all files as per new .gitignore
git add .
# now, commit for new .gitignore to apply
git commit -m ".gitignore is now working"