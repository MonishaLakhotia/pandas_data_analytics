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
            str="$@"
            echo "str: $str"
            break
            ;;

  esac
  shift
done

# [[ -p /dev/stdin ]] && { mapfile -t; set -- "${MAPFILE[@]}"; }

echo "#: $#"
echo "@: $@"

# Load the user defined parameters
echo "C: $valC"
echo "N: $valN"

iN="$(printf '%d' $valN 2>/dev/null)"

echo "iN: $iN"
while ((${#str} < $iN)); do 
  # str+='X' # for pad left
  str="X$str"
done

echo $str
echo $(echo "$str" | sed 's/\n//' | wc -c)
