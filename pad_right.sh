#!/bin/bash

# Load the user defined parameters
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

    --help|*)
            echo "Usage:"
            echo "    --valueC \"value\""
            echo "    --valueN \"value\""
            echo "    --help"
            exit 1
            ;;

  esac
  shift
done

echo "C: $valC"
echo "N: $valN"

iN="$(printf '%d' $valN 2>/dev/null)"

str="12345678"
echo "iN: $iN"
while ((${#str} < $iN)); do 
  # str+='X' # for pad left
  str="X$str"
done

echo $str
echo $(echo "$str" | sed 's/\n//' | wc -c)
