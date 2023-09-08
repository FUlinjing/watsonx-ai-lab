import json
from ibm_watson import DiscoveryV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


class wdService:
    def __init__(self, configFile):
        self.configFile = configFile
        self._readWDconfig()
        self._crWD()
        self.wdCollectionIds = self._getWDcollections()

    
    def _readWDconfig(self):
        with open(self.configFile, 'r') as json_file:
            data = json.load(json_file)
            self.wdApiKey = data['apikey']
            self.wdUrl = data['url']
            self.wdProjectid = data['projectid']
            #print(self.wdApiKey, self.wdUrl)
    
    def _crWD(self):
        authenticator = IAMAuthenticator(self.wdApiKey)
        self.discovery = DiscoveryV2(
            version='2020-08-30',
            authenticator=authenticator
        )
        self.discovery.set_service_url(self.wdUrl)

    def _getWDcollections(self):
        # print("DEBUG _getWDcollections self.wdProjectid - ", self.wdProjectid)
        c = self.discovery.list_collections(
            self.wdProjectid
        )
        # [{'name': 'EU regulations PL - Watsonx technical enablement', 'collection_id': '6fb6580e-3362-3337-0000-0189f316bfba'}]
        retVal = []
        for item in c.result['collections']:
            # print("DEBUG _getWDcollections item['collection_id'] - ", item['collection_id'])
            retVal.append(item['collection_id'])
        return retVal

    def queryWD(self, query):
        # print("DEBUG queryWD self.wdProjectid - ", self.wdProjectid)
        # print("DEBUG queryWD self.wdCollectionIds - ", self.wdCollectionIds)
        # print("DEBUG queryWD question - ", query)
        resp = self.discovery.query(
            project_id = self.wdProjectid,
            collection_ids = self.wdCollectionIds,
            natural_language_query = query
        )
        passages = []
        if resp.result['matching_results'] != 0:
            # print("DEBUG: queryWD resp - ", resp)
            
            for res in resp.result['results']:
                # print("DEBUG: res value : ", res)
                # extract file name
                filename = res['extracted_metadata']['filename']
                # print( "DEBUG: file name", filename)
                # extract page numbers
                pageNums = []
                # print( "DEBUG: res['extracted_metadata']:", res['extracted_metadata'])

                try:
                    textMappings = json.loads(res['extracted_metadata']['text_mappings'])['text_mappings']
                    for page in textMappings:
                        pageNum = page['page']['page_number']
                        pageNums.append(pageNum)
                    pageNums = sorted(set(pageNums))

                    for text in res['text']:
                        passages.append({ 'filename' : filename, 'pages' : pageNums, 'text' : text })
                except:
                    pageNums = []
    
            curated_passages = []
            for passage in passages:
                if len(passage['pages']) <= 2:
                    curated_passages.append(passage)
            passages = curated_passages[:4]

            # print("DEBUG: passages : ", json.dumps(passages))

        return passages


if __name__ == '__main__':
    wd = wdService('./service.WD.cred')
    print(wd.queryWD('How are high-risk AI systems designed?'))