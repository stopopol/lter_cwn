import datetime
import webdav.client as wc
import os

options = {
 'webdav_hostname': "https://ucloud.univie.ac.at",
 'webdav_root': 	"/remote.php/webdav", #important to define webdav root otherwise download_sync won't find the files
 'webdav_login':    "******",
 'webdav_password': "******"
}
client = wc.Client(options)

current_folder =  os.path.dirname(os.path.realpath(__file__))

count_var = 0


for x in (client.list('Shared/LterCWN/')):
	if (x == "LterCWN/") or (x=="log.txt"):
		continue
	temp_path = "Shared/LterCWN/" + x
	local_download_path = current_folder + "/data/" + x
	client.download_sync(remote_path=temp_path, local_path=local_download_path)
	client.clean(temp_path)
	count_var += 1

if count_var > 0:
	with open('log.txt', 'a+') as file:
		file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' Script successfully downloaded ' + str(count_var) + ' file(s) from univie' + '\n')
else: 
	with open('log.txt', 'a+') as file:
		file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' No files to download on the server\n')

#Upload log.file to server
current_local_path = current_folder + '/log.txt'
client.upload_sync(remote_path="Shared/LterCWN/log.txt", local_path=current_local_path)
