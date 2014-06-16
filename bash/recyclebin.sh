#!/bin/bash
if test ! -d ~/.recyclebin; then
  echo "OK"
  mkdir ~/.recyclebin
fi

for arg in $@; do
  if [[ $arg != -* && $arg == ?* ]]; then
    echo -n "Move $arg to recycle bin<y/n>?"; read choice
    case $choice in
      [Yy])
        if [[ -f $arg ]]; then
          mv $arg ~/.recyclebin
          echo "Action done: the file/s  is/are moved to “.recyclebin”"
          exit 0
        else
          echo "file:$arg does not exist!"
        fi
        ;;
    esac
  fi
done

while getopts "lp" optname; do
  case "$optname" in
    "l")
        ls -l ~/.recyclebin
        ;;
    "p")
        echo -n "Remove all files in recycle bin<y/n>?"; read choice
        case $choice in
          [Yy])
            if test -f ~/.recyclebin/*; then
              rm ~/.recyclebin/*
              echo "Action done: all files are deleted from “.recyclebin”"
            else
              echo "No files in recycle bin!"
            fi        
            ;;
        esac
        ;;
    "?")
        echo $1
        ;;
  esac
done
