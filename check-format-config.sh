#!/usr/bin/env sh
# NOTE this file should be copied to the parent directory of repos

if [ $# -ne 1 ]; then
	echo "[Error] one argument needed: repository path, $# given"
	exit 1
fi

# repo directory path
REPO_DIR=$1

if [ ! -d $REPO_DIR ]; then
	echo "[Error] directory $REPO_DIR not found"
	exit 1
fi

GIT_HOOKS_DIR="$(dirname $0)/.git-hooks"
ERROR=0

# (1)
if [ ! -f $REPO_DIR/utils/tidy/all.py ]; then
	echo "[Error] lacks tidiness script"
	echo "to get around (fake an empty script), run:"
	echo "  mkdir -p $REPO_DIR/utils/tidy"
	echo "  touch $REPO_DIR/utils/tidy/all.py"
	echo "  chmod +x $REPO_DIR/utils/tidy"
	exit 1
fi

# (2)
diff $REPO_DIR/.clang-format $GIT_HOOKS_DIR/clang-format.yml > /dev/null
DIFF_EXIT=$?
if [ $DIFF_EXIT -eq 2 ]; then # 0: no difference; 1: difference found; 2: diff error
	echo "[Error] diff error"
	exit 1
elif [ $DIFF_EXIT -eq 1 ]; then
	ERROR=1
	echo "[OUTDATED] $REPO_DIR/.clang-format"
	echo "\trun: cp $GIT_HOOKS_DIR/clang-format.yml $REPO_DIR/.clang-format"
else
	echo "[Good] $REPO_DIR/.clang-format"
fi

exit $ERROR
