################################################################################################################
# CROWDSTRIKE FALCON                                                                                           #
# OAuth2 API - Customer SDK                                                                                    #
#                                                                                                              #
# prevention_policy - Falcon X Prevention Policy API Interface Class                                           #
################################################################################################################
# This is free and unencumbered software released into the public domain.

# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.

# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

# For more information, please refer to <https://unlicense.org>

import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

class Prevention_Policy:
    """ The only requirement to instantiate an instance of this class
        is a valid token provided by the Falcon API SDK OAuth2 class.
    """

    def __init__(self, access_token, base_url='https://api.crowdstrike.com'):
        """ Instantiates the base class, ingests the authorization token, 
            and initializes the headers and base_url global variables. 
        """
        self.headers = { 'Authorization': 'Bearer {}'.format(access_token) }
        self.base_url = base_url

    class Result:
        """ Subclass to handle parsing of result client output. """
        def __init__(self):
            """ Instantiates the subclass and initializes the result object. """
            self.result_obj = {}
            
        def __call__(self, status_code, headers, body):
            """ Formats values into a properly formatted result object. """
            self.result_obj['status_code'] = status_code
            self.result_obj['headers'] = dict(headers)
            self.result_obj['body'] = body
            
            return self.result_obj

    def queryCombinedPreventionPolicyMembers(self, parameters={}):
        """ Search for members of a Prevention Policy in your environment by providing an FQL filter 
            and paging details. Returns a set of host details which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/prevention-policies/queryCombinedPreventionPolicyMembers
        FULL_URL = self.base_url+'/policy/combined/prevention-members/v1'
        HEADERS = self.headers
        PARAMS = parameters
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = self.Result()(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = self.Result()(500, {}, str(e))
        
        return returned

    def queryCombinedPreventionPolicies(self, parameters={}):
        """ Search for Prevention Policies in your environment by providing an FQL filter and 
            paging details. Returns a set of Prevention Policies which match the filter criteria. 
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/prevention-policies/queryCombinedPreventionPolicies
        FULL_URL = self.base_url+'/policy/combined/prevention/v1'
        HEADERS = self.headers
        PARAMS = parameters
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = self.Result()(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = self.Result()(500, {}, str(e))
        
        return returned

    def performPreventionPoliciesAction(self, parameters, body):
        """ Perform the specified action on the Prevention Policies specified in the request. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/prevention-policies/performPreventionPoliciesAction
        FULL_URL = self.base_url+'/policy/entities/prevention-actions/v1'
        HEADERS = self.headers
        PARAMS = parameters
        BODY = body
        try:
            response = requests.request("POST", FULL_URL, params=PARAMS, json=BODY, headers=HEADERS, verify=False)
            returned = self.Result()(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = self.Result()(500, {}, str(e))
        
        return returned

    def setPreventionPoliciesPrecedence(self, body):
        """ Sets the precedence of Prevention Policies based on the order of IDs specified in the request.
            The first ID specified will have the highest precedence and the last ID specified will have the lowest.
            You must specify all non-Default Policies for a platform when updating precedence.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/prevention-policies/setPreventionPoliciesPrecedence
        FULL_URL = self.base_url+'/policy/entities/prevention-precedence/v1'
        HEADERS = self.headers
        BODY = body
        try:
            response = requests.request("POST", FULL_URL, json=BODY, headers=HEADERS, verify=False)
            returned = self.Result()(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = self.Result()(500, {}, str(e))
        
        return returned

    def getPreventionPolicies(self, ids):
        """ Retrieve a set of Prevention Policies by specifying their IDs. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/prevention-policies/getPreventionPolicies
        ID_LIST = str(ids).replace(",","&ids=")
        FULL_URL = self.base_url+'/policy/entities/prevention/v1?ids={}'.format(ID_LIST)
        HEADERS = self.headers
        try:
            response = requests.request("GET", FULL_URL, headers=HEADERS, verify=False)
            returned = self.Result()(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = self.Result()(500, {}, str(e))
        
        return returned

    def createPreventionPolicies(self, body):
        """ Create Prevention Policies by specifying details about the policy to create. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/prevention-policies/createPreventionPolicies
        FULL_URL = self.base_url+'/policy/entities/prevention/v1'
        HEADERS = self.headers
        BODY = body
        try:
            response = requests.request("POST", FULL_URL, json=BODY, headers=HEADERS, verify=False)
            returned = self.Result()(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = self.Result()(500, {}, str(e))
        
        return returned

    def deletePreventionPolicies(self, ids):
        """ Delete a set of Prevention Policies by specifying their IDs. """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/prevention-policies/deletePreventionPolicies
        ID_LIST = str(ids).replace(",","&ids=")
        FULL_URL = self.base_url+'/policy/entities/prevention/v1?ids={}'.format(ID_LIST)
        HEADERS = self.headers
        try:
            response = requests.request("DELETE", FULL_URL, headers=HEADERS, verify=False)
            returned = self.Result()(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = self.Result()(500, {}, str(e))
        
        return returned

    def updatePreventionPolicies(self, body):
        """ Update Prevention Policies by specifying the ID of the policy and details to update. """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/prevention-policies/updatePreventionPolicies
        FULL_URL = self.base_url+'/policy/entities/prevention/v1'
        HEADERS = self.headers
        BODY = body
        try:
            response = requests.request("PATCH", FULL_URL, json=BODY, headers=HEADERS, verify=False)
            returned = self.Result()(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = self.Result()(500, {}, str(e))
        
        return returned

    def queryPreventionPolicyMembers(self, parameters={}):
        """ Search for members of a Prevention Policy in your environment by providing an FQL filter 
            and paging details. Returns a set of Agent IDs which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/prevention-policies/queryPreventionPolicyMembers
        FULL_URL = self.base_url+'/policy/queries/prevention-members/v1'
        HEADERS = self.headers
        PARAMS = parameters
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = self.Result()(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = self.Result()(500, {}, str(e))
        
        return returned

    def queryPreventionPolicies(self, parameters={}):
        """ Search for Prevention Policies in your environment by providing an FQL filter 
            and paging details. Returns a set of Prevention Policy IDs which match the filter criteria. 
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/prevention-policies/queryPreventionPolicies
        FULL_URL = self.base_url+'/policy/queries/prevention/v1'
        HEADERS = self.headers
        PARAMS = parameters
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = self.Result()(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = self.Result()(500, {}, str(e))
        
        return returned
