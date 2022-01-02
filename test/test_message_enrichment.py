"""
    INCAS TA2-UIUC Datatypes

    This API document is defined based on INCAS Common Datatypes version 0.0.3.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import uiuc_incas_client
from uiuc_incas_client.model.array_message_enrichment import ArrayMessageEnrichment
from uiuc_incas_client.model.category_message_enrichment import CategoryMessageEnrichment
from uiuc_incas_client.model.numeric_message_enrichment import NumericMessageEnrichment
from uiuc_incas_client.model.text_message_enrichment import TextMessageEnrichment
globals()['ArrayMessageEnrichment'] = ArrayMessageEnrichment
globals()['CategoryMessageEnrichment'] = CategoryMessageEnrichment
globals()['NumericMessageEnrichment'] = NumericMessageEnrichment
globals()['TextMessageEnrichment'] = TextMessageEnrichment
from uiuc_incas_client.model.message_enrichment import MessageEnrichment


class TestMessageEnrichment(unittest.TestCase):
    """MessageEnrichment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMessageEnrichment(self):
        """Test MessageEnrichment"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MessageEnrichment()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
