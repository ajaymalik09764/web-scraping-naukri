from selenium import webdriver
import os
from time import sleep
from bs4 import BeautifulSoup
import pandas as pd
import re
from datetime import datetime
class sele:
    def driver(self,search_item):
        self.b=webdriver.Chrome(executable_path='C:/path/chromedriver.exe')
        self.b.get("https://www.naukri.com/")
        sleep(1)
        self.a=self.b.find_element_by_id("qsbClick")
        self.a.click()
        sleep(1)
        self.search=self.b.find_element_by_name("qp")
        self.search.send_keys(search_item)
        self.clk=self.b.find_element_by_id("qsbFormBtn")
        self.clk.click()
        self.htmlpage=self.b.page_source
        print("done")
    def scrap(self):
        
        self.page_content = BeautifulSoup(self.htmlpage, "html.parser")
        self.c=self.page_content.find(class_="srp_container")
        self.d=self.c.find_all(class_="row",attrs={'type':'tuple'})



        self.job_url=[]
        self.title=[]
        self.company_name=[]
        self.exp=[]
        self.location=[]
        self.skill=[]
        self.salary=[]
        self.postedby=[]

        for f in self.d:
            self.job_url.append(f["data-url"])
            self.title.append(f.ul.li["title"])
            self.company_name.append(f.span.span.span.string)
            self.exp.append(f.find(class_="exp").text)
            self.location.append(f.find(class_="loc").text)
            self.skill.append(f.find(class_="skill").text)
            self.salary.append(f.find(class_="salary").text)
            self.postedby.append(f.find(class_="rec_details").text)
        self.file={'job url':self.job_url,'title':self.title,'company name':self.company_name,'exp':self.exp,'location':self.location,'skill':self.skill,'salary':self.salary,'details':self.postedby}
        print("done")
    def savedata(self):
        
    
        self.ds=pd.DataFrame(self.file)
        self.ds.to_csv(datetime.now().strftime("%m-%d-%y,%H-%M-%S")+".csv")
        print("done")
















