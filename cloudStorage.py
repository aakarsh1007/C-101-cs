#sl.BBuMdRFI5CnfddxzPD612uJ_3M7HpAwv8NSwnLM344CgnxeQov-9wcC1p8hEFDRqXFb2K__-jIpd9J843M1B97RmFRrE9SXgVxyHbkan7hIJEPwn4oyhlqbmvl4hgj8MBJpVwQ4
import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)
        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)


def main():
    access_token = 'sl.BBuMdRFI5CnfddxzPD612uJ_3M7HpAwv8NSwnLM344CgnxeQov-9wcC1p8hEFDRqXFb2K__-jIpd9J843M1B97RmFRrE9SXgVxyHbkan7hIJEPwn4oyhlqbmvl4hgj8MBJpVwQ4'
    transferData = TransferData(access_token)

    #file_from = 'D:/PYTHON WHJ/p-98-fuctions/text.py'
    #file_to = '/test.py'

    file_from = input("Enter the file path to transfer:")
    file_to = input("Enter the full path to upload to dropbox:")

    transferData.upload_file(file_from, file_to)
    print("File has been uploaded to dropbox")


main()

