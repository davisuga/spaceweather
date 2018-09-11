from urllib.request import urlopen
from urllib.request import urlretrieve
import os
downloadData='S'

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
MAGENTA = "\033[35m"
REVERSE = "\033[;7m"

bpreto = '\033[40m'
bvermelho = '\033[41m'
bverde = '\033[42m'
bamarelo = '\033[43m'
bazul = '\033[44m'
bmagenta = '\033[45m'
bciano = '\033[46m'
bbranco = '\033[47m'

eventDates ="20140609 20140314 20140201 20131217 20130725 20130524 20130517 20121111 20120723 20120411 20120326 20111120 20111106 20110924 20110331 20110117 20100820 20100603 20070522 20070711".split(' ')

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print (RED+'Error: Creating directory. ' +  directory)

def asciiDataDownload(year, initialMonth, initialDay, finalMonth, finalDay, eventDate, verbose=True):
		webpage = urlopen("https://cdaweb.gsfc.nasa.gov/cgi-bin/eval3.cgi?dataset=STA_L2_MAGPLASMA1M%20STB_L2_MAGPLASMA_1M&select=custom&start={}%2F{}%2F{}+08%3A39%3A49.000&stop={}%2F{}%2F{}+09%3A39%3A49.000&index=istp_public&action=list&var=STA_L2_MAGPLASMA_1M+BTOTAL&var=STB_L2_MAGPLASMA_1M+BTOTAL&var=STA_L2_MAGPLASMA_1M+Np&var=STB_L2_MAGPLASMA_1M+Np&var=STA_L2_MAGPLASMA_1M+BFIELDRTN&var=STB_L2_MAGPLASMA_1M+BFIELDRTN&var=STA_L2_MAGPLASMA_1M+Vp_RTN&var=STB_L2_MAGPLASMA_1M+Vp_RTN&var=STA_L2_MAGPLASMA_1M+Beta&var=STB_L2_MAGPLASMA_1M+Beta&var=STA_L2_MAGPLASMA_1M+Total_Pressure&var=STB_L2_MAGPLASMA_1M+Total_Pressure&var=STA_L2_MAGPLASMA_1M+Vp&var=STB_L2_MAGPLASMA_1M+Vp&var=STA_L2_MAGPLASMA_1M+Tp&var=STB_L2_MAGPLASMA_1M+Tp".format(year, initialMonth, initialDay, year, finalMonth, finalDay))
		print('input url: '+'https://cdaweb.gsfc.nasa.gov/cgi-bin/eval3.cgi?dataset=STA_L2_MAGPLASMA1M%20STB_L2_MAGPLASMA_1M&select=custom&start={}%2F{}%2F{}+08%3A39%3A49.000&stop={}%2F{}%2F{}+09%3A39%3A49.000&index=istp_public&action=list&var=STA_L2_MAGPLASMA_1M+BTOTAL&var=STB_L2_MAGPLASMA_1M+BTOTAL&var=STA_L2_MAGPLASMA_1M+Np&var=STB_L2_MAGPLASMA_1M+Np&var=STA_L2_MAGPLASMA_1M+BFIELDRTN&var=STB_L2_MAGPLASMA_1M+BFIELDRTN&var=STA_L2_MAGPLASMA_1M+Vp_RTN&var=STB_L2_MAGPLASMA_1M+Vp_RTN&var=STA_L2_MAGPLASMA_1M+Beta&var=STB_L2_MAGPLASMA_1M+Beta&var=STA_L2_MAGPLASMA_1M+Total_Pressure&var=STB_L2_MAGPLASMA_1M+Total_Pressure&var=STA_L2_MAGPLASMA_1M+Vp&var=STB_L2_MAGPLASMA_1M+Vp&var=STA_L2_MAGPLASMA_1M+Tp&var=STB_L2_MAGPLASMA_1M+Tp\n'.format(year, initialMonth, initialDay, year, finalMonth, finalDay))
		webpageHtml = webpage.readlines()
		print(BOLD+GREEN+"Reading webpage's html...\n"+RESET)
		linkEnd = str(webpageHtml).find("\">Combined Listing</a> (tar/gzip")
		linkStart = linkEnd-25
		if verbose:
			print("Downloading from link: ",str(webpageHtml)[linkStart:linkEnd])
		dataLink = 'https://cdaweb.gsfc.nasa.gov/'+ str(webpageHtml)[linkStart:linkEnd]
		createFolder(eventDate)
		try:
			urlretrieve(dataLink, eventDate+'/data'+eventDate+'tar.gz')  #
		except FileNotFoundError:
			createAFolder = input("Do you want to create a folder? [Y/N]")
			if createAFolder == 'Y':
				createFolder(eventDate)
				urlretrieve(dataLink, eventDate+'/data'+eventDate+'tar.gz')
			if createAFolder == 'N':
				try:
					os.system('cd '+eventDate)
					urlretrieve(dataLink, eventDate+'/data'+eventDate+'tar.gz')
				except:
					pass
		print(MAGENTA+"Saved on: "+eventDate+'/data'+eventDate+'tar.gz')

def oneImageDownload(html, outputDir='/'):
	for line in html:       
		if 'browse' in str(line):
			line = str(line)
			linkStart = line.find("urls.unshift( '/browse")
			linkStart+=16

			linkEnd = line.find('.jpg')+4
			imageLink = "https://stereo-ssc.nascom.nasa.gov/"+line[linkStart:linkEnd]
			imageLocation = imageLink.find("512/")+4
			imageName = (imageLink[imageLocation:])
			urlretrieve(imageLink, outputDir+imageName)
			print(MAGENTA+imageLink, outputDir+imageName)

def whereIsStereo(eventDate, initialMonth, year, outputDir=""):
	url ="https://stereo-ssc.nascom.nasa.gov/cgi-bin/make_where_gif?day={}&month={}&year={}&hour=11&minute=21&field=&background=".format(eventDate, initialMonth, year)
	print(url)
	whereIsStereoPage = urlopen(url)
	html = str(whereIsStereoPage.readlines())
	print("Reading webpage's HTML")
	linkStart = html.find("SRC='")
	linkStart+=5
	linkEnd = html.find('\'></P>')
	partialLink=html[linkStart:linkEnd]
	imageLink = "https://stereo-ssc.nascom.nasa.gov/cgi-bin/make_where_gif/"+html[linkStart:linkEnd]
	print('Downloading from: ', imageLink)
	try:
		urlretrieve(imageLink, outputDir+'/'+eventDate+'WIS.gif')
	except PermissionError:
		os.system('sudo chmod -R 775 ../*')
		urlretrieve(imageLink, outputDir+'/'+eventDate+'WIS.gif')
	except FileNotFoundError:
		createAFolder = input("Do you want to create a folder? [Y/N]")
		if createAFolder == 'Y':
			createFolder(eventDate)
			urlretrieve(imageLink, outputDir+'/'+eventDate+'WIS.gif')
		if createAFolder == 'N':
			try:
				os.system('cd '+eventDate)
				urlretrieve(imageLink, outputDir+'/'+eventDate+'WIS.gif')
			except:
				pass
		print(MAGENTA+"Saved on: "+eventDate+'/data'+eventDate+'tar.gz')
	print(MAGENTA+'Saved on: ', outputDir+'/'+eventDate+'WIS.gif')

def eventImagesZipDownload(initialDate, finalDate, eventDate):
	baseurl = 'https://stereo-ssc.nascom.nasa.gov/cgi-bin/images?frame=Displaying+1+of+573&fstart=1&fstop=573&Download=Download+all+Behind+COR2&Session=Display&Start=20120720&Finish=20120724&Resolution=512&NumImg=0&Sample=1'
	eventUrl = "https://stereo-ssc.nascom.nasa.gov/cgi-bin/images?frame=Displaying+1+of+573&fstart=1&fstop=573&Download=Download+all+Behind+EUVI+195&Session=Display&Start={}&Finish={}&Resolution=512&NumImg=0&Sample=1".format(initialDate,finalDate)
	print('Downloading .zip files from: '+eventUrl)
	urlretrieve(eventUrl, eventDate+'/EUVI_B/images'+eventDate+'.zip')
	print('.zip Saved on: '+eventDate+'/EUVI_B/images'+eventDate+'.zip')

	eventUrl = "https://stereo-ssc.nascom.nasa.gov/cgi-bin/images?frame=Displaying+1+of+573&fstart=1&fstop=573&Download=Download+all+Ahead+COR2&Session=Display&Start=20120723&Finish=20120724&Resolution=512&NumImg=0&Sample=1".format(initialDate,finalDate)
	print('Downloading .zip files from: '+eventUrl)
	urlretrieve(eventUrl, eventDate+'/COR2_A/images'+eventDate+'.zip')
	
	print(MAGENTA+'.zip Saved on: '+eventDate+'/COR2_A/images'+eventDate+'.zip')

	eventUrl = "https://stereo-ssc.nascom.nasa.gov/cgi-bin/images?Detectors=aheadXcor2&frame=Displaying+1+of+573&fstart=1&fstop=573&Download=Download+all+Behind+COR2&Session=Display&Start={}&Finish={}&Resolution=512&NumImg=0&Sample=1".format(initialDate,finalDate)
	print('Downloading .zip files from: '+eventUrl)
	urlretrieve(eventUrl, eventDate+'/COR2_B/images'+eventDate+'.zip')
	print('.zip Saved on: '+eventDate+'/COR2_B/images'+eventDate+'.zip')

	eventUrl = "https://stereo-ssc.nascom.nasa.gov/cgi-bin/images?Detectors=aheadXeuviX195&frame=Displaying+1+of+573&fstart=1&fstop=573&Download=Download+all+Ahead+EUVI+195&Session=Display&Start={}&Finish={}&Resolution=512&NumImg=0&Sample=1".format(initialDate,finalDate)
	print('Downloading .zip files from: '+eventUrl)
	urlretrieve(eventUrl, eventDate+'/EUVI_A/images'+eventDate+'.zip')
	print(MAGENTA+'.zip Saved on: '+eventDate+'/EUVI_A/images'+eventDate+'.zip')



for eventDate in eventDates:
	year = eventDate[0:4]
	initialMonth = eventDate[4:6]
	finalMonth = initialMonth
	eventDay = int(eventDate[6:8])
	initialDay =  eventDay - 1
	finalDay = str(int(eventDay) + 1)
	initialDate = str(year)+str(initialMonth)+str(initialDay)
	initialDay, initialDate, finalDay, initialMonth, finalMonth, eventDate, year = str(initialDay), str(initialDate), str(finalDay), str(initialMonth), str(finalMonth), str(eventDate), str(year)
	if int(initialDay) <1:
		initialMonth = int(initialMonth)-1
		initialDay = 30 + int(initialDay)

	if int(initialDay) >= 31:
		finalDay = str(int(int(initialDay)-31 + 2))
		finalDay = '0'+finalDay
		finalMonth = str(int(initialMonth)+1)
		finalMonth = '0'+finalMonth

	if int(finalDay) >= 31:
		finalDay = str(int(int(finalDay)-31 + 2))
		finalDay = '0'+finalDay
		finalMonth = str(int(initialMonth)+1)
		finalMonth = '0'+finalMonth

	if len(str(initialDay))==1: initialDay="0"+initialDay

	if len(finalDay)==1: finalDay="0"+finalDay

	if len(str(initialMonth))==1: initialMonth="0"+str(initialMonth)

	initialDay, initialDate, finalDay, initialMonth, finalMonth, eventDate, year = str(initialDay), str(initialDate), str(finalDay), str(initialMonth), str(finalMonth), str(eventDate), str(year)
	print(BLUE, '\n Event occurred on the day:', GREEN,eventDay, '\n', year, initialMonth, initialDay, year, finalMonth, finalDay)
	#print("sdo.gsfc.nasa.gov/data/aiahmi/browse")
	#print("lasco-www.nrl.navy.mil/daily_mpeg/{}_{}".format(year, initialMonth))
	#print("https://cdaweb.gsfc.nasa.gov/cgi-bin/eval3.cgi?dataset=STA_L2_MAGPLASMA1M%20STB_L2_MAGPLASMA_1M&select=custom&start={}%2F{}%2F{}+08%3A39%3A49.000&stop={}%2F{}%2F{}+09%3A39%3A49.000&index=istp_public&action=list&var=STA_L2_MAGPLASMA_1M+BTOTAL&var=STB_L2_MAGPLASMA_1M+BTOTAL&var=STA_L2_MAGPLASMA_1M+Np&var=STB_L2_MAGPLASMA_1M+Np&var=STA_L2_MAGPLASMA_1M+BFIELDRTN&var=STB_L2_MAGPLASMA_1M+BFIELDRTN&var=STA_L2_MAGPLASMA_1M+Vp_RTN&var=STB_L2_MAGPLASMA_1M+Vp_RTN&var=STA_L2_MAGPLASMA_1M+Beta&var=STB_L2_MAGPLASMA_1M+Beta&var=STA_L2_MAGPLASMA_1M+Total_Pressure&var=STB_L2_MAGPLASMA_1M+Total_Pressure&var=STA_L2_MAGPLASMA_1M+Vp&var=STB_L2_MAGPLASMA_1M+Vp&var=STA_L2_MAGPLASMA_1M+Tp&var=STB_L2_MAGPLASMA_1M+Tp".format(year, initialMonth, initialDate, year, finalMonth, finalDay))
	#print("https://stereo-ssc.nascom.nasa.gov/cgi-bin/images?Detectors=aheadXeuviX195&Resolution=512&Display=Slideshow&Start={}&Finish={}&Sample=1&Session=Display".format(year+initialMonth+initialDate, year+finalMonth+finalDay))
	#print("https://stereo-ssc.nascom.nasa.gov/cgi-bin/images?Detectors=behindXeuviX195&Resolution=512&Display=Slideshow&Start={}&Finish={}&Sample=1&Session=Display".format(year+initialMonth+initialDate, year+finalMonth+finalDay))
	#print("https://stereo-ssc.nascom.nasa.gov/cgi-bin/images?Detectors=aheadXcor2&Resolution=512&Display=Slideshow&Start={}&Finish={}&Sample=1&Session=Display".format(year+initialMonth+initialDate, year+finalMonth+finalDay))
	#print("https://stereo-ssc.nascom.nasa.gov/cgi-bin/images?Detectors=behindXcor2&Resolution=512&Display=Slideshow&Start={}&Finish={}&Sample=1&Session=Display".format(year+initialMonth+initialDate, year+finalMonth+finalDay))
	#print("https://stereo-ssc.nascom.nasa.gov/cgi-bin/make_where_gif?Day={}&month={}&year={}&hour=11&minute=21&field=&background=".format(eventDate, initialMonth, year))
	while downloadData != 'n' and downloadData != 'N':
		downloadData = input(CYAN+'What do you need to download? [(D)ata in Ascii/ (I)mages from EUVI/COR / (W)here is Stereo? / (N)othing]'+MAGENTA+'\n'+'')
		print(downloadData)
		if downloadData == "D" or downloadData == "d":
			asciiDataDownload(year, initialMonth, initialDay, finalMonth, finalDay, eventDate)
		else:
			pass

		if downloadData == 'W' or downloadData == 'w':
			whereIsStereo(eventDate, initialMonth, year, eventDate)

		if downloadData == 'i' or downloadData == 'I':
			eventImagesZipDownload(year+initialMonth+initialDay, year+finalMonth+finalDay, eventDate)
	downloadData='s'