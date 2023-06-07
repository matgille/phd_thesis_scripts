#!/bin/bash
######
#  Lancer gnome-screenshot, enregistrer le fichier sous un nom dans le dossier d'un témoin et copier dans le presse-papier.
######



function assert {
  # First parameter is the message in case the assertion is not verified
  message="$1"

  # The remaining arguments make the command to execute
  shift

  # Run the command, $@ ensures arguments will remain in the same position.
  # "$@" is equivalent to "$1" "$2" "$3" etc.
  "$@"

  # Get the return code
  rc=$?

  # If everything is okay, there's nothing left to do
  [ $rc -eq 0 ] && return 0

  # An error occured, retrieved the line and the name of the script where
  # it happend
  set $(caller)

  # Get the date and time at which the assertion occured
  date=$(date "+%Y-%m-%d %T%z")

  # Output an error message on the standard error
  # Format: date script [pid]: message (linenumber, return code)
  echo "$date $2 [$$]: $message (line=$1, rc=$rc)" >&2

  # Exit with the return code of the assertion test
  exit $rc
}


temoin=$1
nom_du_fichier=$2


assert "There must be two arguments" test $# -eq 2

gnome-screenshot -af /home/mgl/Bureau/These/Edition/hyperregimiento-de-los-principes/Dedans/Facsimiles/$1/$2

chemin_relatif="/home/mgl/Bureau/These/Edition/hyperregimiento-de-los-principes/Dedans/Facsimiles/$1/$2"
 echo $chemin_relatif| tr -d '\n' | xclip -selection clipboard;



