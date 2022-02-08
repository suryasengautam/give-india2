import requests,os,json
from pprintpp import pprint as pp
from bs4 import BeautifulSoup
url=requests.get("https://www.giveindia.org/differentlyabled")
# pp(os.getcwd())
# f = open("give_india/live_page.html","r")
# url = f.read()
# # f.write(url.text)
# f.close()
# pp("done")
soup=BeautifulSoup(url.text,"lxml")
main_tag =(soup.main)
main_div = main_tag.find("div",class_="px-0 pt-2 container-fluid")
x = main_div.find_all("div",class_="d-flex program-card-11 col-lg-4 col-xl-4 col-md-4 col-sm-6 col-12 col-xs-12 col-12 col-sm-6 col-md-6 col-lg-4")
lis=[]
def differently():
    global x
    for i in x:
        dic = {}
        x= (i.find("div",class_="jsx-4112ddb4c4eeda09 card-body"))
        ngo_work= ((x.contents[1]).get_text()).split("by")[0].replace("\xa0","")
        ngo_name= ((x.contents[1]).get_text()).split("by")[1].replace("\xa0","")
        ngo_place=(((x.contents[0]).contents[1]).get_text())
        Purpose_ngo = (x.find("div",class_="jsx-4112ddb4c4eeda09 col-6 col-lg-6 col-md-12 col-sm-6 p-0")).get_text()
        dic["ngo_name"]=ngo_name
        dic["ngo_work"]=ngo_work
        dic["Place"]=ngo_place
        dic["Purpose_ngo"]=Purpose_ngo
        lis.append(dic)
    f = open("./main_ngo/differently_out.json","w")
    json.dump(lis,f,indent=4)
    f.close()
    return(lis)
if __name__ == "__main__":
       print (differently())
