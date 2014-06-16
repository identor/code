#!/bin/bash
# clear variables
plateNumber=""
timeIn=""
timeOut=""
vehicleType=""
#################
# sample inputs
# timeIn="0845"
# timeOut="1915"
# plateNumber="XXX-123"
###############
# read the plate number
pattern="[A-Z][A-Z][A-Z]-[0-9][0-9][0-9]"
while [[ $plateNumber != $pattern ]];
do
    echo -n "Plate number (i.e.: XXX-123): "
    read plateNumber
done
# for vehicleType
pattern="[LHU]"
while [[ $vehicleType != $pattern ]];
do
    echo -n "Type of vehicle (L/U/H): "
    read vehicleType
done
# validate the time in
validTimeInPattern0="0[7-9][0-5][0-9]"
validTimeInPattern1="1[0-9][0-5][0-9]"
validTimeInPattern2="2[0-2][0-5][0-9]"
validTimeInPattern3="23[0-2][0-9]"
validTimeInPattern4="2330"
while [[ $timeIn != $validTimeInPattern0 
        && $timeIn != $validTimeInPattern1
        && $timeIn != $validTimeInPattern2
        && $timeIn != $validTimeInPattern3 
        && $timeIn != $validTimeInPattern4 ]];
do
    echo -n "Time in: "
    read timeIn
done
# validate the time out
validTimeOutPattern0="0[7-9][0-5][0-9]"
validTimeOutPattern1="1[0-9][0-5][0-9]"
validTimeOutPattern2="2[0-2][0-5][0-9]"
validTimeOutPattern3="23[0-2][0-9]"
validTimeOutPattern4="2330"
cmpTI=$timeIn
if [[ "${timeIn:0:1}" == "0" ]]; then
    cmpTI="${timeIn:1:3}"
fi
cmpTO="0000"
while [[ $timeOut != $validTimeOutPattern0 
        && $timeOut != $validTimeOutPattern1
        && $timeOut != $validTimeOutPattern2
        && $timeOut != $validTimeOutPattern3 
        && $timeOut != $validTimeOutPattern4
        &&  $cmpTI -gt $cmpTO ]];
do
    echo -n "Time out: "
    read timeOut
    if [[ $timeOut == $validTimeOutPattern0 
        || $timeOut == $validTimeOutPattern1
        || $timeOut == $validTimeOutPattern2
        || $timeOut == $validTimeOutPattern3 
        || $timeOut == $validTimeOutPattern4 ]]; then
        if [[ "${timeOut:0:1}" == "0" ]]; then
            cmpTO="${timeOut:1:3}"
        else
            cmpTO="0000"
        fi
    fi
done
echo ""
# from here all inputs are valid
hourIn="${timeIn:0:2}"
hourOut="${timeOut:0:2}"
minuteIn="${timeIn:2:2}"
minuteOut="${timeOut:2:2}"
if [[ "${timeIn:0:1}" -eq "0" ]]; then
    hourIn="${timeIn:1:1}"
fi
if [[ "${timeOut:0:1}" -eq "0" ]]; then
    hourOut="${timeOut:1:1}"
fi
if [[ "${timeIn:2:1}" -eq "0" ]]; then
    minuteIn="${timeIn:2:1}"
fi
if [[ "${timeOut:2:1}" -eq "0" ]]; then
    minuteOut="${timeOut:2:1}"
fi
let "minute = minuteOut - minuteIn"
if [[ $minute -lt 0 ]]; then
    carry=1
    let "minute *= -1"
fi
let "hour = hourOut - hourIn - carry"
echo -n "The vehicle with plate number $plateNumber was parked for"
echo -n " $hour hours and $minute minutes. "
parkingCharge=50
if [[ $vehicleType == "L" ]]; then
    let "parkingCharge += hour*5"
    if [[ parkingCharge -gt 100 ]]; then
        parkingCharge=100
    fi
elif [[ $vehicleType == "U" ]]; then
    let "parkingCharge += hour*15"
    if [[ parkingCharge -gt 150 ]]; then
        parkingCharge=150
    fi
else # vehicleType is H
    echo "flag"
    let "parkingCharge += hour*25"
    if [[ parkingCharge -gt 250 ]]; then
        parkingCharge=250
    fi
fi
if [[ hour -le 2 ]]; then
    parkingCharge=50
fi
echo -n "The parking charge for the vehicle is $parkingCharge pesos"
echo ""
echo ""
echo -n "Try again Y/N? "
read again
if [[ $again != "N" ]]; then
     # This command is dependent on the file name
     # and as to where the script is executed.
    ./parking
fi
