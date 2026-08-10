#!/usr/bin/env bash
set -o errexit
set -o nounset

source ${HOME}/.ssh-agent-thing
source "$(dirname ${BASH_SOURCE[0]})/config.$HOST"
export RESTIC_PASSWORD="$(eval $BACKUP_PASSWORD_COMMAND)"
export RESTIC_REPOSITORY="$BACKUP_REPOSITORY"
/home/lagoyd/.local/bin/restic -v backup --dry-run "$BACKUP_ITEMS"
if [[ $? == 0 || $? == 3 ]]
then
  /home/lagoyd/.local/bin/restic -v forget \
    --keep-within-daily 7d \
    --keep-within-weekly 1m \
    --keep-within-monthly 2y \
    --keep-within-yearly 75y
else
  echo "backup failed"
  exit 1
fi
