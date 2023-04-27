'''Code By: Lalit jagotra'''
from databasev2 import database
import string
import re
import fileinput
import json

class processwebpage():
    def __init__(self, HTMLContent):
        self.HTMLContent=HTMLContent

    def SearchHTML(self):
        db2=database(filename= "C:\Python_Files\Application/HTMLindexing", table="Indexpage")
        db2.create_database()
        query = 'drop table if exists Indexpage'
        db2.sql_noparam(query)
        #query = 'create table Indexpage (ROW_ID int, tagname string, Tagnum int, index int, attributes dict, innerhtmloffset int)'
        #db2.sql_noparam(query)
        Tagsname= "(?P<tagname>(?<=\<)\w+)"
        Tagsboundary="(<\tagname.*?[(\>)|(</\tagname>)])"
        testhtml= "<html><head><link rel='shortcut icon' href='#' /></head><body><div id=1234><p style='bold'>This is default response from server</p></div><div></div></body></html>"
        tagparams={}
        indexedhtml={}
        try:
            Tagsnamere =re.finditer(Tagsname,self.HTMLContent["Default"],re.DOTALL)
            for Tags in Tagsnamere:
                Tagsattributes="(\<" + Tags.groups()[0] +"(\s(?P<attributename>[a-zA-Z0-9]+?)=(?P<attrbutevalue>.*?))+?\s?\/?\>$)"
                Tagsboundary= "(?P<tagboundary><"+Tags.groups()[0]+".*\<\/"+Tags.groups()[0]+"\>)"
                Javascriptids="^(?P<javascript>\<(script).*?\>.*?\<\/\2\>)"
                TagsboundarySearch=re.search(Tagsboundary,self.HTMLContent["Default"][Tags.start()-1:],re.DOTALL)
                if TagsboundarySearch!=None:
                    check="Long"
                else:
                    Tagsboundary2= "(?P<tagboundary>\s*?\<"+Tags.groups()[0]+".*?(\/\>))"
                    Tagsboundary2Search=re.search(Tagsboundary2,self.HTMLContent["Default"][Tags.start()-1:],re.DOTALL)
                    check="Short"
                Tagattributes= "(?P<tagattributes>\<"+Tags.groups()[0]+".*?(\>))"
                if(check=="Long"):
                    TagsattributesSearch=re.search(Tagattributes,TagsboundarySearch.groups()[0][TagsboundarySearch.start():])
                    Tagattributes2='(?P<attributename>(\w\d_-)*)\=(?<attributevalue>(\w\d_-\\\/\.\?)*)'
                    Tagattributes2='\s'
                    TagsattributesSplit1=re.split(Tagattributes2,TagsattributesSearch.groups()[0])
                    TagsattributesSplit2=[]
                    TagsattributesSplit3=[[],[]]
                    i=1
                    while(i<=(len(TagsattributesSplit1)-1)):
                        if(TagsattributesSplit2!=None):
                            TagsattributesSplit2=re.split("\=",TagsattributesSplit1[i].strip('["\'/>]'))
                            print (TagsattributesSplit2)
                            TagsattributesSplit3[0].append(TagsattributesSplit2)
                        else:
                            continue
                        i+=1
                    TagsattributesSplit3[1].append(TagsboundarySearch.groups(1)[0])
                else:
                    TagsattributesSearch=re.search(Tagsattributes,Tagsboundary2Search.groups()[0][Tagsboundary2Search.start():],re.DOTALL)
                    Tagattributes2='(?P<attributename>(\w\d_-)*)\=(?<attributevalue>(\w\d_-\\\/\.\?)*)'
                    Tagattributes2='\s'
                    TagsattributesSplit1=re.split(Tagattributes2,TagsattributesSearch.groups()[0])
                    TagsattributesSplit2=[]
                    TagsattributesSplit3=[[],[]]
                    i=1
                    while(i<=(len(TagsattributesSplit1)-1)):
                        TagsattributesSplit2=re.split("\=",str(TagsattributesSplit1[i]))
                        #print (TagsattributesSplit2)
                        if(TagsattributesSplit2!=None):
                            TagsattributesSplit3[0].append(TagsattributesSplit2)
                        else:
                            continue
                        i+=1
                    TagsattributesSplit3[1].append(Tagsboundary2Search.groups()[0])
                indexedhtml[(Tags.groups()[0]+str(Tags.start())+ "-" + str(Tags.end()))]=TagsattributesSplit3
        finally:
            return indexedhtml

    def UpdateHTMLContent(self, params):
            num=1
            span=[0,0]
            tag=""
            for c in params["Tags"]:
                    print(ord(c))
                    if ((ord(c)>=97 and ord(c)<=122) or (ord(c) >= 65 and ord(c) <= 90)):
                        tag+=c
                    elif((ord(c)>= 48 and ord(c)<= 57) and num==1):
                        print("%s:%d","span0:",int(c))
                        span[0]=(span[0]*10)+int(c)
                    elif(c=='-'):
                        num=2
                    elif((ord(c)>= 48 and ord(c)<= 57) and num==2):
                        print("%s:%d","span0:",int(c))
                        span[1]=(span[1]*10) + int(c)
                    else:
                        break
            indexedhtml= self.SearchHTML()
            print(indexedhtml)
            tagboundaryinitial= len(indexedhtml[params["Tags"]][1])
            updatedattributes=""
            attributestring=""
            for keys in params:
                match keys:
                    case "attributename":
                        if(params["attributename"]==None):
                            continue
                        i=0
                        check=0
                        for attributes in indexedhtml[params["Tags"]][0]:
                            if(attributes[0]==params["attributename"]):
                                indexedhtml["Tags"][0][i][1]=params["attributevalue"]
                                check=1
                                break
                            else: check==0
                            i+=1
                        if check==0:
                            indexedhtml[params["Tags"]][0].append([params["attributename"],params["attributevalue"]])
                        for attribute in indexedhtml[params["Tags"]][0]:
                            if(len(attribute)==2):
                                attributestring+= attribute[0] + "=" + '"' + attribute[1] + '" '
                        updatedattributes= "<" + tag + " " + attributestring + "/>"
                        break
                    case "attributevalue":
                        if(params["attributename"]==None):
                            continue
                        break
                    case "tagcontent":
                        if params["tagcontent"]!= None:
                            indexedhtml[params["Tags"]][1][0]=indexedhtml[params["Tags"]][1][0][:params["tagcontentoffset"]] + params["tagcontent"] + indexedhtml[params["Tags"]][1][0][params["tagcontentoffset"]:] 
                        break
                    case "javascript":
                        if params["javascirpt"]!= None:
                            indexedhtml[params["Tags"]][1][0]=indexedhtml[params["Tags"]][1][0][:params["scriptoffset"]] + params["javascript"] + indexedhtml[params["Tags"]][1][0][params["scriptoffset"]:]
                        break
                    case default:
                        continue
            print(span)
            self.HTMLContent["Updated"]= self.HTMLContent["Default"][:span[0]-1]
            if(params["attributename"]!=None):
                self.HTMLContent["Updated"]+=updatedattributes 
            if(params["tagcontent"]!=None or params["javascript"]!=None):
                self.HTMLContent["Updated"]+= indexedhtml[params["Tags"]][1][0] + self.HTMLContent["Default"][(span[0]-1) +len(indexedhtml[params["Tags"]][1][0])- len("tagcontent"):]
            if(params["attributename"]!=None and (params["tagcontent"]!=None or params["javascript"]!=None)):
                self.HTMLContent["Updated"]= self.HTMLContent["Updated"] + self.HTMLContent["Default"][span[0] + len(updatedattributes) - len(params["attributename"] + params["attributevalue"]):]
            return self.HTMLContent["Updated"]
            
def main():
    wfile={"Default":"", "Updated":""}
    with fileinput.input(files='C:/Python_Files//Application/HTML/index.html',mode='r') as input:
                for line in input:
                    wfile["Default"]+=line
    print("Original Web content:" + wfile["Default"])
    indexhtml1= processwebpage(wfile)
    print("Updated Web content:")
    print(indexhtml1.UpdateHTMLContent({"Tags": "body210-214" ,"attributename" : None, "attributevalue": None,"tagcontent": "<br></br>", "tagcontentoffset":71 , "javascript": None, "javascriptoffset":None}))
     
if __name__=="__main__":main()
