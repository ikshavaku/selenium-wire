import csv

def toList(chunk) :
    '''
    This is a method to convert list of requests into list of lists. Each list containing the complete request.
    '''
    returnList=[]
    for eachrequest in chunk :
        returnList.append([str(eachrequest.method),str(eachrequest.url),str(eachrequest.path),str(eachrequest.querystring),str(eachrequest.params),str(eachrequest.headers),str(eachrequest.body),str(eachrequest.response)])
    return returnList

def reportSheet(chunk):
    chunk=toList(chunk)
    with open('report.csv',mode='w',newline='') as file:
        writer = csv.writer(file,delimiter=',')
        writer.writerows(chunk)
        file.close()
def reportHtml(chunk):
    chunk=toList(chunk)
    f=open('report.html','w')
    begin='''
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Report</title>
<link rel="stylesheet" href="style.css" type="text/css"
</head>
<body>
<h2 align="center">User session Report</h2>
        '''
    requestData='<button class="collapsible">Twitter</button>\n<div class="content">\n'
    for i in chunk:
        requestData+=f'<div class="result"><span class="result">{i[1]}</span> <span class="result">{i[7]}</span></div>\n'
    end='''
</div>\n
<script type="text/javascript" src="classic.js"></script>
</body>
</html>
    '''
    content=begin+requestData+end
    f.write(content)
    f.close()