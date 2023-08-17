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
        c = self.discovery.list_collections(
            self.wdProjectid
        )
        # [{'name': 'EU regulations PL - Watsonx technical enablement', 'collection_id': '6fb6580e-3362-3337-0000-0189f316bfba'}]
        retVal = []
        for item in c.result['collections']:
            retVal.append(item['collection_id'])
        return retVal

    def queryWD(self, query):
        resp = self.discovery.query(
            project_id = self.wdProjectid,
            collection_ids = self.wdCollectionIds,
            natural_language_query = query
        )
        passages = []
        for res in resp.result['results']:
            # extract file name
            filename = res['extracted_metadata']['filename']

            # extract page numbers
            pageNums = []
            textMappings = json.loads(res['extracted_metadata']['text_mappings'])['text_mappings']
            for page in textMappings:
                pageNum = page['page']['page_number']
                pageNums.append(pageNum)
            pageNums = sorted(set(pageNums))

            for text in res['text']:
                passages.append({ 'filename' : filename, 'pages' : pageNums, 'text' : text })

        passages = passages[:4]
        return passages

if __name__ == '__main__':
    wd = wdService('./service.WD.cred')
    print(wd.queryWD('W jaki sposób projektuje się systemy sztucznej inteligencji wysokiego ryzyka?'))