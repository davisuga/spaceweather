import os
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
eventDates = "20140609 20140314 20140201 20131217 20130725 20130524 20130517 20121111 20120923 20120411 20120326 20111120 20111106 20110924 20110331 20110117 20100820 20100603 20070522 20070711".split(' ')
for date in eventDates:
	createFolder(date)
	createFolder(date+"/EUVI_A")
	createFolder(date+"/EUVI_B")
	createFolder(date+"/COR2_A")
	createFolder(date+"/COR2_B")
