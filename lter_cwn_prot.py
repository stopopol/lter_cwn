import datetime
import webdav.client as wc
import os

# webdav parameters
options = {
 'webdav_hostname': "https://ucloud.univie.ac.at",
 'webdav_root': 	"/remote.php/webdav", #important to define webdav root otherwise download_sync won't find the files
 'webdav_login':    "*****",
 'webdav_password': "*****"
}
client = wc.Client(options)

# iterate through folder content
count_var = 0
for x in (client.list('Shared/LterCWN/')):
	if x == "LterCWN/":
		continue
	temp_path = "Shared/LterCWN/" + x
	local_download_path = "/home/USER/curl_test/data/" + x
	client.download_sync(remote_path=temp_path, local_path=local_download_path)
	client.clean(temp_path)
	count_var += 1

# Print message to logfile
if count_var > 0:
	with open('log.txt', 'a+') as file:
		file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' Script successfully downloaded ' + str(count_var) + ' file(s) from univie' + '\n')
else: 
	with open('log.txt', 'a+') as file:
		file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' No files to download on the server\n')

# Upload log.file to server
client.upload_sync(remote_path="Shared/LterCWN/log.txt", local_path="/home/USER/curl_test/log.txt")
