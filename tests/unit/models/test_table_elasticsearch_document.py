import json
import unittest

from databuilder.models.table_elasticsearch_document import TableESDocument


class TestTableElasticsearchDocument(unittest.TestCase):

    def test_to_json(self):
        # type: () -> None
        """
        Test string generated from to_json method
        """
        test_obj = TableESDocument(elasticsearch_index='test_index',
                                   elasticsearch_type='test_type',
                                   database='test_database',
                                   cluster='test_cluster',
                                   schema_name='test_schema',
                                   table_name='test_table',
                                   table_key='test_table_key',
                                   table_last_updated_epoch=123456789,
                                   table_description='test_table_description',
                                   column_names=['test_col1', 'test_col2'],
                                   column_descriptions=['test_description1', 'test_description2'],
                                   total_usage=100,
                                   unique_usage=10,
                                   tag_names=['test'])

        expected_index_dict = {"index": {"_type": "test_type", "_index": "test_index"}}
        expected_document_dict = {"database": "test_database",
                                  "cluster": "test_cluster",
                                  "schema_name": "test_schema",
                                  "table_name": "test_table",
                                  "table_key": "test_table_key",
                                  "table_last_updated_epoch": 123456789,
                                  "table_description": "test_table_description",
                                  "column_names": ["test_col1", "test_col2"],
                                  "column_descriptions": ["test_description1", "test_description2"],
                                  "total_usage": 100,
                                  "unique_usage": 10,
                                  "tag_names": ["test"]
                                  }

        result = test_obj.to_json()
        results = result.split("\n")

        # verify two new line characters in result
        self.assertEqual(len(results), 3, "Result from to_json() function doesn't have 2 newlines!")

        self.assertDictEqual(json.loads(results[0]), expected_index_dict)
        self.assertDictEqual(json.loads(results[1]), expected_document_dict)
