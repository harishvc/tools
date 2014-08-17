# Query Github public timeline using Bigquery and display top new repositories
# Modified from sources
## https://developers.google.com/bigquery/bigquery-api-quickstart#completecode
## https://gist.github.com/igrigorik/f8742314320e0a4b1a89

import httplib2
import pprint
import sys
import time
import json
import logging
from apiclient.discovery import build
from apiclient.errors import HttpError
from apiclient import errors
from pprint import pprint
from oauth2client.client import SignedJwtAssertionCredentials
from oauth2client.client import AccessTokenRefreshError
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run

#Debug
# https://developers.google.com/api-client-library/python/guide/logging
#httplib2.debuglevel = 4
#logger = logging.getLogger()
#logger.setLevel(logging.INFO)



def main():
    PROJECT_NUMBER = 'xxx' #TODO: Add project number
    SERVICE_ACCOUNT_EMAIL = 'xxx@developer.gserviceaccount.com'   #TODO: Add service account
    f = file('xxx-key.p12', 'rb') #TODO: Add key
    key = f.read()
    f.close()
    credentials = SignedJwtAssertionCredentials(
    		SERVICE_ACCOUNT_EMAIL,
    		key,
    		scope='https://www.googleapis.com/auth/bigquery.readonly')
    http = httplib2.Http()
    http = credentials.authorize(http)
    bigquery_service = build('bigquery', 'v2', http=http)

    #https://developers.google.com/bigquery/docs/reference/v2/jobs/query
    #https://code.google.com/p/python-sqlparse/
    #http://sqlformat.org/
    #TODO: Change timestamp
    try:
        query_request = bigquery_service.jobs()
        query_data = {
                   "kind": "bigquery#job",
                   'query': 'SELECT repository_url, repository_language, COUNT(repository_name) AS cnt, \
                            FROM githubarchive:github.timeline \
                            WHERE TYPE="WatchEvent" \
                              AND PARSE_UTC_USEC(created_at) >= PARSE_UTC_USEC("2014-08-15 00:00:00") \
                              AND repository_url IN \
                                (SELECT repository_url \
                                 FROM githubarchive:github.timeline \
                                 WHERE TYPE="CreateEvent" \
                                   AND PARSE_UTC_USEC(repository_created_at) >= PARSE_UTC_USEC("2014-08-15 00:00:00") \
                                   AND repository_fork = "false" \
                                   AND payload_ref_type = "repository" \
                                 GROUP BY repository_url) \
                            GROUP BY repository_name, \
                                     repository_language, \
                                     repository_description, \
                                     repository_url HAVING cnt >= 5 \
                            ORDER BY cnt DESC LIMIT 5;',
                     "useQueryCache": "False"  # True or False                         
                     }
        
         #Trigger on-demand query
         #Quota & Policy info https://developers.google.com/bigquery/quota-policy                            
        query_response = query_request.query(projectId=PROJECT_NUMBER,body=query_data).execute()
        
        #Did the bigquery get processed?
        if ((query_response['jobComplete']) and (query_response['totalRows'] >1) and (query_response['totalBytesProcessed'] > 0 )):
            #Store result for further analysis
            with open( 'toprepositories.json', 'w' ) as outfile:
                json.dump( query_response,outfile)
            #Print results
            print "Top Repositories in Github"
            for row in query_response['rows']:
                result_row = []
                for field in row['f']:
                    result_row.append(field['v'])
                    print('\t'.join(map(str,result_row)))
        else:
            print "Ignore: jobComplete=%s \t totalRows=%s \t totalBytesProcessed=%s" % (query_response['jobComplete'],query_response['totalRows'], query_response['totalBytesProcessed'])

            
    except HttpError as err:
    		print "Error:", pprint(err.content)
    
    except AccessTokenRefreshError:
    		print "Token Error: Credentials have been revoked or expired"
    
if __name__ == '__main__':
	main()
