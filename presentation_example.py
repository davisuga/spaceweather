from urllib.request import urlretrieve
import matplotlib.pyplot as plt
from requests import post
from glob import glob
import numpy as np
import tarfile
import csv

initialDate="2013/07/19"
finalDate="2013/07/26"

data = [
('dataset', ' STA_L2_MAGPLASMA_1M STB_L2_MAGPLASMA_1M'),
('start', '2011/09/20 18:00:00.000'),
('stop', '2011/09/30 18:00:00.000'),
('bin_value', '15'),
('time_unit', 'min'),
('missval', 'fillval'),
('spike_opt', 'none'),
('index', 'sp_phys'),
('nobin_spike_opt', 'light'),
('spinner', '1'),
('autoChecking', 'on'),
('action', 'list'),
('var', 'STA_L2_MAGPLASMA_1M BTOTAL'),
('var', 'STB_L2_MAGPLASMA_1M BTOTAL'),
('var', 'STA_L2_MAGPLASMA_1M Np'),
('var', 'STB_L2_MAGPLASMA_1M Np'),
('var', 'STA_L2_MAGPLASMA_1M BFIELDRTN'),
('var', 'STB_L2_MAGPLASMA_1M BFIELDRTN'),
('var', 'STA_L2_MAGPLASMA_1M Vp_RTN'),
('var', 'STB_L2_MAGPLASMA_1M Vp_RTN'),
('var', 'STA_L2_MAGPLASMA_1M Beta'),
('var', 'STB_L2_MAGPLASMA_1M Beta'),
('var', 'STA_L2_MAGPLASMA_1M Total_Pressure'),
('var', 'STB_L2_MAGPLASMA_1M Total_Pressure'),
('var', 'STA_L2_MAGPLASMA_1M Vp'),
('var', 'STB_L2_MAGPLASMA_1M Vp'),
('var', 'STA_L2_MAGPLASMA_1M Tp'),
('var', 'STB_L2_MAGPLASMA_1M Tp'),
('csv', '1')
]

webpageRaw = post('https://cdaweb.gsfc.nasa.gov/cgi-bin/eval3.cgi', data=data)
webpageHtml = webpageRaw.text
linkEnd = webpageHtml.find("\">Combined Listing</a> (tar/gzip")
linkStart = linkEnd-42
dataLink = 'https://cdaweb.gsfc.nasa.gov/'+ webpageHtml[linkStart:linkEnd]
urlretrieve(dataLink+'.tar.gz')

fileName = glob("*.tar.gz")[0]
tar = tarfile.open(fileName, "r:gz")
tar.extractall()
tar.close()

STAFileName = glob("STA*.csv")
STBFileName = glob("STB*.csv")

STAFile = open(STAFileName, 'r')
STBFile = open(STBFileName, 'r')

STAdata = csv.reader(STAFile)
STBdata = csv.reader(STBFile)

for line in STAdata:
    print(line)

timeAxis = []
BTOTAL = []
NP = []
SPEED = []
TEMPERATURE = []
VP_RTN = []
BETA = []
TOTAL_PRESSURE = []
BX = []
BY = []
BZ = []
THERMAL_SPEED = []
fileContent = []