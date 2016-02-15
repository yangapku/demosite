index=0
flag=True
if(flag):
	with open("coredata\\cont.json",'r',encoding="utf-8") as fin:
		line=fin.readline()
		while(line!=""):
			index=index+1
			with open("srcfile\\%04d.json" % index,'w',encoding="utf-8") as fout:
				fout.write(line[:-1])
			line=fin.readline()
index=0
flag=True
if(flag):
	with open("coredata\\exp.seg.json.txt",'r',encoding="utf-8") as fin:
		line=fin.readline()
		while(line!=""):
			index=index+1
			with open("resultfile\\res_%04d.txt" % index,'w',encoding="utf-8") as fout:
				line=line[line.find('{'):]
				fout.write(line[:-1])
			line=fin.readline()	