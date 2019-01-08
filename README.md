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
```bash
# set Git hooks as symbolic link
cd .git && mv hooks hooks_old && ln -s ../../.git-hooks hooks && cd ..

# needed by pre-commit hook
# get .clang-format (need clang-format utility for it to be effective)
cp ../.git-hooks/clang-format.yml ./.clang-format
```

In the parent directory of all repos:
```bash
# get script that checks if files are synced with the ones in .git-hooks
ln -s .git-hooks/check-format-config.sh check-fmt-cfg
# grant execution permission to all user
chmod +x .git-hooks/check-format-config.sh
```

To check if format config files in repo `./ProjName` is synced with the ones in `.git-hooks`:
```bash
./check-fmt-cfg ProjName
```

###### EOF
