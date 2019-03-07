from example2.pytas import TAS
from example2.services import FilesService

SECRET_KEY="12456"

def file_listing(username, system, path):
    client = TAS(SECRET_KEY)
    user = client.getUser(username)
    listing = FilesService.list(user, system, path)
    out = []
    for file in listing:
        file["version"] = "3"
        out.append(file)
    return out




