#!/opt/python/bin/python3
import argparse
import sys
import subprocess

STATE_OK=0
STATE_CRITICAL=2

def fortinet(IP, OID, THRESHOLD):
    try:
        SNMP_SECRET='75Pubm4t1cSNMP'
        command="snmpwalk -v2c -c "+str(SNMP_SECRET)+" "+str(IP)+" "+str(OID)+" | awk '{print $4}'"
        USAGE=int(subprocess.getoutput(command))
        if   USAGE > THRESHOLD:
                    MSG=("Usage:{0} | 'usage'={0}".format(USAGE))
                    print("CRITICAL {0}".format(MSG))
                    sys.exit(2)
        elif USAGE <= THRESHOLD:
                    MSG=("Usage:{0} | 'usage'={0}".format(USAGE))
                    print("OK {0}".format(MSG))
                    sys.exit(0)
        else:
                    MSG="Unable to fetch data"
                    print("CRITICAL {0}".format(MSG))
                    sys.exit(2)
    except Exception as e:
            print("ERROR:{0}".format(e))
            sys.exit(2)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip')
    parser.add_argument('--oid')
    parser.add_argument('--threshold')
    args = parser.parse_args()
    ip=args.ip
    oid=args.oid
    threshold=int(args.threshold)
    fortinet(ip, oid, threshold)

if __name__ == '__main__':
    main()
