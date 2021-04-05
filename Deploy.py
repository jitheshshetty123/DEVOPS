#!C:/Python3.9/python.exe
import os
import subprocess
import shutil
from artifactory import ArtifactoryPath
from jproperties import Properties

print("===================API Deployment starts==================")

p = Properties()
with open("bambo-test.properties", "rb") as f:
    p.load(f)

build = p["BUILD_NUMMBER"].data
planName = p["REPO_NAME"].data
print("BUILD NUMBER IS =====> " + build)
print("REPO NAME IS =====> " + planName)

url = os.environ['bamboo_artifactory_url'] + "com/services/{0}/{1}-0.0.1-SNAPSHOT.war".format(build, planName)
print("Artifactory URL ====> " + url)
auth = (os.environ['bamboo_artifactory_username'], os.environ['bamboo_artifactory_password'])
path = ArtifactoryPath(url, auth=auth)
with path.open() as fd, open("{0}-0.0.1-SNAPSHOT.war".format(planName), "wb") as out:
    out.write(fd.read())

src = "{0}-0.0.1-SNAPSHOT.war".format(planName)
dst = "C:\\apache-tomcat-9.0.44\\webapps\\{0}-0.0.1-SNAPSHOT.war".format(planName)
shutil.copyfile(src, dst, )
print(" Deployment Sucessful")

print("==================API Deployment Ends ====================")

# curl -u admin:Welcome@123 -X GET "http://localhost:8082/artifactory/DEMO/com/services/1/employeservice-0.0.1-SNAPSHOT.war" -o "employeservice-0.0.1-SNAPSHOT.war"