"""
"""
import json

from lm_client.common.api_service import RestService


# .............................................................................
class OpenTreeApiService(RestService):
    """
    """
    end_point = 'api/v2/opentree'

    # ...........................
    def post(self, taxon_ids):
        """
        """
        return RestService.post(
            self, self.end_point, body=json.dumps(taxon_ids),
            headers={'Content-Type': 'application/json'})
