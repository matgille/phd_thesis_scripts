#!/bin/bash
# bash generate random 32 character alphanumeric string (lowercase only)
# | tr -d '\n'| permet de supprimer le saut de ligne (https://ubuntuforums.org/showthread.php?t=2125844)
aleatoire=$(cat /dev/urandom | tr -dc 'a-zA-Z' | fold -w 10 | head -n 1) ;
 echo " xml:id=\"$aleatoire\""| tr -d '\n' | xclip -selection clipboard;
 xdotool sleep 0.4 key "ctrl+v";
