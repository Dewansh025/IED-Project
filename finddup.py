lines_seen = set()
outfile = open('/home/saurav/Desktop/project_master/redresultfinal.txt',"w")
for line in open ('/home/saurav/Desktop/project_master/redresult.txt',"r"):
    if line not in lines_seen:
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
