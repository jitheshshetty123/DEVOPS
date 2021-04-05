#!C:/Python3.9/python.exe
import os
import requests
import subprocess
from jproperties import Properties

print ("===================API Build starts==================")

build=os.environ['bamboo_buildNumber']
planName=os.environ['bamboo_planRepository_1_name']

test=os.environ['bamboo_planRepository_repositoryUrl']

print ("API BUILD NUMBER IS ===========> " + build)
print ("API REPO NAME IS ===========> " + test)

# maven clean package to create war file
subprocess.call(["mvn", "clean", "package"], shell=True)

#upload war file into artifactory location
url = os.environ['bamboo_artifactory_url'] + "com/services/{0}/{1}-0.0.1-SNAPSHOT.war".format(build, planName)
file_name = "target/{0}-0.0.1-SNAPSHOT.war".format(planName)
auth=(os.environ['bamboo_artifactory_username'], os.environ['bamboo_artifactory_password'])
with open(file_name, 'rb') as fobj:
    res = requests.put(url, auth=auth, data=fobj)
    print(res.text)
    print(res.status_code)

#Update build number and repo name in the properties file.
p = Properties()
p["BUILD_NUMMBER"] = build
p["REPO_NAME"] = planName
with open("bambo-test.properties", "wb") as f:
    p.store(f, encoding="utf-8")

print ("==================API Build Ends ====================")

#curl -u admin:Welcome@123 -X PUT -F "data=@target/employeservice-0.0.1-SNAPSHOT.war" http://localhost:8082/artifactory/DEMO/com/services/build/employeservice-0.0.1-SNAPSHOT.war