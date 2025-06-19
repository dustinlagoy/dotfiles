#!/bin/bash
ubuntu="/usr/share/doc/git/contrib/diff-highlight/diff-highlight"
arch="/usr/share/git/diff-highlight/diff-highlight"
if [ -f $ubuntu  ]
then
  script=$ubuntu
else
  script=$arch
fi
perl $script
