#!/usr/local/bin/bash
# echo 'hello world'
# while read name; do
#     if[[ name ]]
# done < example.ini
# declare -A animals
# animals=(["dodo"]="wow" ["doodoo"]="huh")
# echo animals["dodo"]

echo '{'
echo '"_": {'
while read name; do
    if [[ ${name:0:1} = "#" ]]; then
        continue
    elif [[ ${name:0:1} = "[" ]]; then
        echo '},'
        echo "\"${name:1:-1}\": {"
    elif [[ $name != "" ]];then
        echo $name | awk -F " *= *" '{print "  \""$1"\"\: ""\""$2"\""}'
    else
        continue
    fi
done < example.ini
echo '}'
echo '}'