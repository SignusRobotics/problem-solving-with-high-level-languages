#!/usr/bin/env bash
# https://stackoverflow.com/a/16365257 

climb () {    
    # Avslutter programmet om argument 1 ikke er ett heltall og ikke tomt
    # Bruker regex for aa sjekke om foerste argument bare bestaar av tegnene 0-9 
    # om ikke avslutter funksjonen  
    
    if ! [[ $1 =~ ^[0-9]+$ ]] && [[ "$1" != "" ]] ; then   
        # send bruksinfo til 'stderr'
        echo "usage: climb [numeric number]" >&2; 
        return 1 
    fi

    for i in $(seq 1 $1); do 
        eval cd .. 
    done 
} 