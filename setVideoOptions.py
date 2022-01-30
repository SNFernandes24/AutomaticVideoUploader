import os

class VideoOptions:
    description = "test description"
    category = "22"
    keywords = "test"
    privacyStatus = "private"

    def getFileName(self, type):
        for file in os.listdir("H:\TwitchClips"):
            if type == "video" and file.split(".", 1)[1] != "jpg":
                return file