#!/bin/bash

apiBaseURL="https://rest.opensubtitles.org/search"

while getopts s: option
do
    case "${option}"
    in
    s) searchQuery=${OPTARG};;
    esac
done

function search_using_string() {
    local query=${1//" "/"%20"}
    local searchURL="$apiBaseURL/query-$query/sublanguageid-eng"
    curl -A 'TemporaryUserAgent' $searchURL
    #echo $searchURL
}

search_using_string "$searchQuery"