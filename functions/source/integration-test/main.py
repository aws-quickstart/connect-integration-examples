import cfnresponse
import traceback
from botocore.vendored import requests


def handler(event, context):
    try:
        if event['RequestType'] == 'Create':
            # Test Integration
            print 'Getting all pets'
            response = requests.get(event['ResourceProperties']['IntegrationEndpoint'])
            print "Status code: " + str(response.status_code)
            if response.status_code != 200:
                raise Exception('Error: Status code received is not 200')
        elif event['RequestType'] == 'Update':
            pass
        elif event['RequestType'] == 'Delete':
            pass
        cfnresponse.send(event, context, cfnresponse.SUCCESS, {}, '')
    except:
        print traceback.print_exc()
        cfnresponse.send(event, context, cfnresponse.FAILED, {}, '')
