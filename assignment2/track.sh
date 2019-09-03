#!/usr/bin/env bash

track () {

    STATE=$1; 
    LABEL=$2; 
    LABELTXT="LABEL";
    ARGNR=$#; 

    STATE=${STATE^^} 

    if [ "$STATE" == "START" ]; then 
        # Sjekker om LOGFILE siste linje frste ord er LABEL. 
        if [ "$(tail -n 1 $LOGFILE | cut -d' ' -f1)" == "$LABELTXT" ]; then
            echo "Allready running task"
            return;
        else  
            # skriv til logfil: 
            echo "START $(date)" >> $LOGFILE;
            echo "LABEL $LABEL" >> $LOGFILE; 
        fi
    fi 

    if [[ "$STATE" == "STOP" ]]; then 
        # Sjekker aktiv oppgave. Siste linje i logfile.txt starter på LABEL.
        if [ "$(tail -n 1 $LOGFILE | cut -d' ' -f1)" == "$LABELTXT" ]; then
            echo "END" $(date)$'\n' >>  $LOGFILE; 
        else 
            echo "Currently no active task"
        fi
    fi 

    if [[ "$STATE" == "STATUS" ]]; then 
        if [ "$(tail -n 1 $LOGFILE | cut -d' ' -f1)" == "$LABELTXT" ]; then
            echo "Currently tracking $(tail -n 1 $LOGFILE | cut -f 2- -d ' ')"; 
        else 
            echo "Currently no active task"
        fi
    fi 
    
    i=1
    if [ "$STATE" == "LOG" ]; then 
        # read line by line 
        times=$(cut -f 2- -d ' ' $LOGFILE)

        regex="(\w+) (.*)"
        while read line ; do 
            if [[ $line =~ $regex ]]; then 
                linetype="${BASH_REMATCH[1]}"
                linevalue="${BASH_REMATCH[2]}"

                if [[ "$linetype" == *"START"*  ]]; then 
                    startclk=$(date -d "$linevalue" +%s)
                fi 
                                
                if [[ "$linetype" == *"LABEL"*  ]]; then 
                    timelabel=$linevalue
                fi 
                
                if [[ "$linetype" == *"END"*  ]]; then 
                    stopclk=$(date -d "$linevalue" +%s)
                    timeused=$((stopclk-startclk)) 
                    #skriver ut tid brukt til skjerm
                    echo "$timelabel: $(date -d "1970-01-01 + $timeused seconds" "+%H:%M:%S")" 
                    startclk=0;
                    stopclk=0;
                fi 
            fi
            done < $LOGFILE;
    fi

    if [[ "$STATE" != "START" ]] && [[ "$STATE" != "STOP" ]] && [[ "$STATE" != "STATUS" ]] && [[ "$STATE" != "LOG"  ]]; then 
        echo " usage: ./track.sh [start/stop/status/log] ["label"]";  
        return;
    fi
}

track $1 "$2" 