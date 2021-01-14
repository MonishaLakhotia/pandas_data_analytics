#!/bin/bash

echo "#: $#"
echo "@: $@"
while [[ $# > 0 ]]
do
  case "$1" in

    -c|--valueC)
            valC="$2"
            shift
            ;;

    -n|--valueN)
            valN="$2"
            shift
            ;;

    --help)
            echo "Usage:"
            echo "    --valueC \"value\""
            echo "    --valueN \"value\""
            echo "    --help"
            exit 1
            ;;

    *)
            strs="$@"
            break
            ;;

  esac
  shift
done

# [[ -p /dev/stdin ]] && { mapfile -t; set -- "${MAPFILE[@]}"; }

echo "#: $#"
echo "@: $@"

# valC="X"
# valN="10"
# strs=("pad" "me\n" "daddy ya ya")
# Load the user defined parameters
echo "C: $valC"
echo "N: $valN"

iN="$(printf '%d' $valN 2>/dev/null)"

echo "iN: $iN"

declare -a arr
for str in ${strs[@]}
do
  while ((${#str} < $iN)); do 
    # str+="$valC" # for pad right
    str="$valC$str" # for pad left
  done
  arr=( "${arr[@]}" "$str" )
done

printf '%s\n' "${arr[@]}"
