while :
do
timeout -k 2 3600 python3 finder.py -w 25 -t 100 -p proxies.txt
sleep 5
done