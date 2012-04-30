import httplib
import argparse
import json

parser = argparse.ArgumentParser(
        description="Does a get request on the hosts defined in the payload")
parser.add_argument("-payload", type=str, required=True,
        help="The location of a file containing a JSON payload.")
parser.add_argument("-e", type=str, required=False,
        help="The environment")
parser.add_argument("-d", type=str, required=False,
        help="Iron passes this. Don't know what it means")				
parser.add_argument("-id", type=str, required=False,
		        help="The id of the task or something. Also passed by Iron.")				
		
args = parser.parse_args()

hosts = False
if args.payload is not None:
    payload = json.loads(open(args.payload).read())
    if 'herokuping' in payload:
        hosts = (payload['herokuping']['hosts'])

print hosts

for host in hosts:
  print "Pinging "+host
  httpServ = httplib.HTTPConnection(host, 80)
  httpServ.connect()
  httpServ.request('GET', "/")