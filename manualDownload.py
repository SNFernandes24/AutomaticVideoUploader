
# def downloadClip(clipName):
#     time.sleep(3)
#     app = Application(backend="uia").connect(path=r"C:\Users\Nikil Fernandes\Desktop\Twitch_Downloader\TwitchDownloader.exe")
#     app = app.window_(title_re='Twitch Downloader')
#     app.btnClipDownload.click()
#     app.ClipLinkEdit.set_text(clipName)
#     app.btnGetInfo.click()
#     app.btnDownload.click()
#     popupDialog = Desktop(backend="win32").window(title='Save As')
#     if popupDialog.exists:
#         try:
#             popupDialog.Save.click()
#             popupDialog.wait_not('visible')
#         except:
#             saveDialog = Desktop(backend="win32").window(title='Save As', found_index = 0)
#             if saveDialog.exists:
#                 saveDialog.Yes.click()
#                 saveDialog.wait_not('visible')