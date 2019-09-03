#!/usr/bin/env bash
# https://stackoverflow.com/a/16365257 

climb () {    
    # Avslutter programmet om argument 1 ikke er ett heltall 
    # Bruker regex for å sjekke om første argument bare består av tegnene 0-9 
    # om ikke avslutter funksjonen  
    if ! [[ $1 =~ ^[0-9]+$ ]] ; then   
        # send bruksinfo til 'stderr'
        echo "usage: climb [numeric number]" >&2; 
        return 1 
    fi

    for i in $(seq 1 $1); do 
        eval cd .. 
    done 
} 