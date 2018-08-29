datas ="20140609 20140314 20140201 20131217 20130725 20130524 20130517 20121111 20120923 20120411 20120326 20111120 20111106 20110924 20110331 20110117 20100820 20100603 20070522 20070522 20070711".split(' ')
for data in datas:
   ano = data[0:4]
   mesinicial = data[4:6]
   mesfinal = mesinicial
   diainicial = data[6:8]
   diafinal = str(int(diainicial) + 2)
   if int(diainicial) >= 31:
             diafinal = str(int(int(diainicial)-31 + 2))
             diafinal = '0'+diafinal
             mesfinal = str(int(mesinicial)+1)
             mesfinal = '0'+mesfinal
   print('\n', ano, mesinicial, diainicial, ano, mesfinal, diafinal)

   print("https://cdaweb.gsfc.nasa.gov/cgi-bin/eval3.cgi?dataset=STA_L2_MAGPLASMA_1M%20STB_L2_MAGPLASMA_1M&select=custom&start={}%2F{}%2F{}+08%3A39%3A49.000&stop={}%2F{}%2F{}+09%3A39%3A49.000&index=istp_public&action=list&var=STA_L2_MAGPLASMA_1M+BTOTAL&var=STB_L2_MAGPLASMA_1M+BTOTAL&var=STA_L2_MAGPLASMA_1M+Np&var=STB_L2_MAGPLASMA_1M+Np&var=STA_L2_MAGPLASMA_1M+BFIELDRTN&var=STB_L2_MAGPLASMA_1M+BFIELDRTN&var=STA_L2_MAGPLASMA_1M+Vp_RTN&var=STB_L2_MAGPLASMA_1M+Vp_RTN&var=STA_L2_MAGPLASMA_1M+Beta&var=STB_L2_MAGPLASMA_1M+Beta&var=STA_L2_MAGPLASMA_1M+Total_Pressure&var=STB_L2_MAGPLASMA_1M+Total_Pressure&var=STA_L2_MAGPLASMA_1M+Vp&var=STB_L2_MAGPLASMA_1M+Vp&var=STA_L2_MAGPLASMA_1M+Tp&var=STB_L2_MAGPLASMA_1M+Tp".format(ano, mesinicial, diainicial, ano, mesfinal, diafinal))
   print("https://stereo-ssc.nascom.nasa.gov/cgi-bin/images?Detectors=aheadXeuviX195&Resolution=512&Display=Slideshow&Start={}&Finish={}&Sample=1".format(str(data), str(ano)+str(mesfinal)+str(diafinal)))
   print("https://stereo-ssc.nascom.nasa.gov/cgi-bin/images?Detectors=behindXeuviX195&Resolution=512&Display=Slideshow&Start={}&Finish={}&Sample=1".format(str(data), str(ano)+str(mesfinal)+str(diafinal)))
   print("https://stereo-ssc.nascom.nasa.gov/cgi-bin/images?Detectors=aheadXcor2&Resolution=512&Display=Slideshow&Start={}&Finish={}&Sample=1".format(str(data), str(ano)+str(mesfinal)+str(diafinal)))
   print("https://stereo-ssc.nascom.nasa.gov/cgi-bin/images?Detectors=behindXcor2&Resolution=512&Display=Slideshow&Start={}&Finish={}&Sample=1".format(str(data), str(ano)+str(mesfinal)+str(diafinal)))
