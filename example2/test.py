from unittest import TestCase
from unittest.mock import patch

#import the function that we are testing
from example2.files import file_listing

class TestFilesListing(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @patch('example2.example2.TAS')
    @patch('example2.example2.FilesService')
    def test_files_listing(self, mock_files_service, tas_client):
        """
        IMPORTANT: Look at how those service classes were mocked here. They HAVE to be mocked
        at the location of where they are imported in the function that we are testing. Change it to
        @patch('TAS') and it will fail for you
        """

        # give a return value to the mock files service
        mock_files_service.list.return_value = [
            {"name": "file1.txt", "path": "/home/jmeiring/"},
            {"name": "file2.txt", "path": "/home/jmeiring/"},
        ]
        listing = file_listing("jmeiring", "test.system", "/")

        #make sure that our mocked TAS client was called with the correct username
        self.assertTrue(tas_client().getUser.called_with("jmeiring"))

        #make sure that we got back the 2 listings defined above
        self.assertTrue(len(listing) == 2)
        f1 = listing[0]

        #in the file_listing function we add a version to the listing, so lets make sure
        #thats there too
        self.assertTrue(f1["version"] == "3")


