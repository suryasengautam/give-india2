import requests,os,json
from pprintpp import pprint as pp
from bs4 import BeautifulSoup
# url=requests.get("https://www.giveindia.org/children")
# pp(os.getcwd())
f = open("./children_page.html","r")
url = f.read()
# f.write(url.text)
f.close()
# pp("done")
soup=BeautifulSoup(url,"lxml")
main_tag =(soup.main)
main_div = main_tag.find("div",class_="px-0 pt-2 container-fluid")
# x= main_tag.find_all("div",class_="container")

x = main_div.find_all("div",class_="d-flex program-card-11 col-lg-4 col-xl-4 col-md-4 col-sm-6 col-12 col-xs-12 col-12 col-sm-6 col-md-6 col-lg-4")
# for i in x:
#     pp(i)
#     print()
#     print()
#     print()
#     print()
#     print()
#     print()

lis=[]
def children():
    global x

    for i in x:
        dic = {}
        # dic = {"ngo_name":"","ngo_work":"","Purpose_ngo":"","Place":""}
        x= (i.find_all("div",class_="jsx-1989162857 card-body"))[0]
        Purpose_ngo=((x.find("span",class_="jsx-1989162857 small-text float-left")).get_text())
        y = x.find("span",class_="jsx-1989162857 small-text float-left")
        Place = ((x.find("span",class_="jsx-1989162857 small-text mid-grey float-right")).get_text())
        ngo_work_nme_tag=((i.find("div",class_="jsx-1989162857 card-body")).find("h5",class_="jsx-1989162857 card-title text-clamp-3"))
        ngo_work =(ngo_work_nme_tag.get_text())
        ngo_name1= ((ngo_work_nme_tag.find("span",class_="jsx-1989162857 sh w-100")).get_text())
        ngo_name=(ngo_name1.replace('\xa0', ' '))[4:]
        dic["ngo_name"]=ngo_name
        dic["ngo_work"]=ngo_work.split("Charutar")[0].split("\xa0by")[0]
        dic["Place"]=Place
        dic["Purpose_ngo"]=Purpose_ngo
        lis.append(dic)

    f = open("./main_ngo/children_out.json","w")
    json.dump(lis,f,indent=4)
        
    return(lis)
if __name__ == "__main__":
   print (children())