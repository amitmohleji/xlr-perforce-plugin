#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import sys
import re
from com.perforce.p4java.server import ServerFactory
from com.perforce.p4java.core.file import FileSpecBuilder


if perforceServer is None:
    print "No perforce server provided"
    sys.exit(1)

credentials = CredentialsFallback(perforceServer, username, password).getCredentials()

server = ServerFactory.getServer(perforceServer['url'], None)
print "Perforce trust file path is : %s" % server.getTrustFilePath()
server.connect()
server.setUserName(credentials['username'])
server.login(credentials['password'])
totalRevisionNumber = 0
repos = re.sub("[ ]+"," ",depotPaths).split(" ")
for repo in repos:
	filespecs = server.getDepotFiles(FileSpecBuilder.makeFileSpecList(repo), False)
	tempEndRevision = 0
	for file in filespecs:
		if tempEndRevision < file.getEndRevision():
			tempEndRevision = file.getEndRevision()
	totalRevisionNumber = totalRevisionNumber + tempEndRevision		
#summary = server.getChangelists(1,FileSpecBuilder.makeFileSpecList(repos),clientName,credentials['username'],True,False,False,True)
#triggerState = "%s" % summary[0].getId()
#print "new changelist id is " + str(triggerState)
triggerState = "%s" % totalRevisionNumber
print "new totalRevisionNumber is " + str(totalRevisionNumber)
commitId = totalRevisionNumber