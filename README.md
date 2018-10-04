# Git Hooks

Enforce a uniform Git hook policy.

This directory should be under the same directory as all other repositories:
```
- DIR
 |- .git-hooks
 |- Project1-repo
 |- ...
```

In each repository:
```
# set Git hooks as symbolic link
cd .git && mv hooks hooks_old && ln -s ../../.git-hooks hooks && cd ..

# needed by pre-commit hook
# get .clang-format (need clang-format utility for it to be effective)
cp ../.git-hooks/clang-format.yml ./.clang-format

# needed by pre-commit hook
# get .whitespace-linter (need Python for it to be effective)
cp ../.git-hooks/whitespace-linter.py ./.whitespace-linter
chmod +x ./.whitespace-linter # grant execution permission to all user
```

In the parent directory of all repos:
```
# get script that checks if format config files are synced with the ones in .git-hooks
ln -s .git-hooks/check-format-config.sh check-format-config
chmod +x .git-hooks/check-format-config.sh # grant execution permission to all user
```

To check if format config files in repo `$REPO` is synced with the ones in `.git-hooks`:
```
./check-format-config $REPO
```

###### EOF
