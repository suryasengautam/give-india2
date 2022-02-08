import json,os,requests
from bs4 import BeautifulSoup
from pprintpp import  pprint as pp
# url  = "https://www.giveindia.org/cancer-care"
# url = "https://www.giveindia.org/health"
# page = requests.get(url)
f = open("./health_page.html","r")
# f.write(page.text)
page = f.read()
f.close()
soup = BeautifulSoup(page,"lxml")
group_result1=soup.find("main",class_="jsx-585916480 sc-desktop-padding-style")
group_result =group_result1.find("div",class_="jsx-585916480")
group_result_section1 = (group_result.find("div",class_="px-0 pt-2 container-fluid"))
# pp(group_result_section1)
group_result_section = group_result_section1.find("div",attrs={"id":"search-results-section","class":"search-panel-wrapper row"})
xx=group_result_section.find("div",class_="w-100")
x=xx.find("div",attrs={"style":"padding-top:1rem","class":"row"})
x1=soup.find_all("div",class_="d-flex program-card-11 col-lg-4 col-xl-4 col-md-4 col-sm-6 col-12 col-xs-12 col-12 col-sm-6 col-md-6 col-lg-4")
# first=x[0]
# main =first.find("div",class_="jsx-1989162857 card-body")
# x = group_result_section.find_all("div",class_="d-flex program-card-11 col-lg-4 col-xl-4 col-md-4 col-sm-6 col-12 col-xs-12 col-12 col-sm-6 col-md-6 col-lg-4")
# v=#__next > div:nth-child(2) > main > div > div.px-0.pt-2.container-fluid
# row_element= (soup.find("div",class_="container").find("div",attrs={"class":"row","style":"padding-top:1rem"}))
# for i in x:
#     pp(i)
#     print()
#     print()
    # print()
# y=x.find_all("div",class_="d-flex program-card-11 col-lg-4 col-xl-4 col-md-4 col-sm-6 col-12 col-xs-12 col-12 col-sm-6 col-md-6 col-lg-4")

# pp(x.contents)


# for i in x1:
#     charutar = i
#     pp(charutar)
#     print()
#     print()
#     print()




lis=[]
def health():

    for i in x1:
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
    f = open("./main_ngo/health_out.json","w")
    json.dump(lis,f,indent=4)
    f.close()
    return(lis)
if __name__ == "__main__":
    pp(health())
        