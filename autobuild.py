#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from optparse import OptionParser
import subprocess
import os

CODE_SIGN_IDENTITY 	   = "iPhone Distribution: Cao Yushi (E6RMPYQ5SD)"
PROVISIONING_PROFILE   = "XC_BBM_HOC_Profile"
CONFIGURATION          = "Debug"
SDK                    = "iphoneos9.1"

PGYER_UPLOAD_URL  	   = "http://www.pgyer.com/apiv1/app/upload"
DOWNLOAD_BASE_URL 	   = "http://www.pgyer.com"
USER_KEY          	   = "eac08a60086cef4ac700321e47387117"
API_KEY           	   = "cc124ba28de1f55c2e162501493e5898"

ARCHIVEPATH            = "auto_build/BBK_iOS.xcarchive"
EXPORTPATH             = "auto_build/"
EXPORTOPTIONSPLISTPATH = "auto_build/export_debug.plist"
UPLOADPGY_PYTHON_PATH  = "auto_build"

def buildWorkspace(workspace, scheme):
	process = subprocess.Popen("pwd", stdout=subprocess.PIPE)
	(stdoutdata, stderrdata) = process.communicate()
	buildDir = stdoutdata.strip() + '/build'
	print "buildDir: " + buildDir
	#build
	buildbld = 'xcodebuild -sdk %s -workspace %s -scheme %s -configuration %s -arch arm64 -arch armv7 CODE_SIGN_IDENTITY="%s" clean build' %(SDK,workspace,scheme,CONFIGURATION,CODE_SIGN_IDENTITY)
	process = subprocess.Popen(buildbld,shell = True)
	killProcess(process)
	#archive
	buildarh = 'xcodebuild -workspace %s  -scheme %s -arch armv7 -arch arm64 -archivePath %s archive' %(workspace,scheme,ARCHIVEPATH)
	process = subprocess.Popen(buildarh,shell = True)
	killProcess(process)
	#exportArchive
	buildearh = 'xcodebuild -exportArchive -archivePath %s -exportPath %s -exportOptionsPlist %s CODE_SIGN_IDENTITY="%s" PROVISIONING_PROFILE="%s"' %(ARCHIVEPATH,EXPORTPATH,EXPORTOPTIONSPLISTPATH,CODE_SIGN_IDENTITY,PROVISIONING_PROFILE)
	process = subprocess.Popen(buildearh,shell=True)
	killProcess(process)

	(stdoutdata, stderrdata) = process.communicate()
	print '####################################################'
	print '\n'
	print '\n'
	print 'exportArchive successful，Ready to Upload to 蒲公英'
	print '\n'
	print '\n'
	print '####################################################'
	os.chdir(UPLOADPGY_PYTHON_PATH)
	buildpyn = 'python UploadToPgy.py'
	process = subprocess.Popen(buildpyn,shell = True)
	killProcess(process)
	
def killProcess(process):
	#等待子线程结束
	process.wait()
	#判断子线程是否结束
	if process.poll() is None == False:
		process.terminate()
		process.kill()

def xcbuild(options):
	workspace = options.workspace
	target    = options.target
	scheme    = options.scheme

	if workspace is not None:
		buildWorkspace(workspace, scheme)

def main():
	parser = OptionParser()
	parser.add_option("-w", "--workspace", help="Build the workspace name.xcworkspace.", metavar="name.xcworkspace")
	parser.add_option("-s", "--scheme", help="Build the scheme specified by schemename. Required if building a workspace.", metavar="schemename")
	parser.add_option("-t", "--target", help="Build the target specified by targetname. Required if building a project.", metavar="targetname")
	(options, args) = parser.parse_args()
	print "options: %s, args: %s" % (options, args)
	xcbuild(options)

if __name__ == '__main__':
	main()