import requests
import random
from bs4 import BeautifulSoup as bs

session = requests.session()

def English():
	global session
	endpoint2 = "https://mykids.ggusd.us/LoginParent.aspx"
	payload2 = {
		"checkCookiesEnabled":"true",
		"checkMobileDevice":"false",
		"checkStandaloneMode":"false",
		"checkTabletDevice":"false",
		"portalAccountUsername":"richard24680123@gmail.com",
		"portalAccountPassword":"r1357924680",
		"portalAccountUsernameLabel":"",
		"submit":""
	}
	responce2 = session.post(endpoint2, data=payload2)
	endpoint1 = "https://mykids.ggusd.us/Widgets/ClassSummary/RedirectToGradebook?GradebookNumber=8994987&Term=S&CDS=30665220000000&SC=83"
	responce1 = session.get(endpoint1)
	soup = bs(responce1.text, "html.parser")
	div = soup.find("td",{"id":"ctl00_MainContent_subGBS_DataSummary_ctl07_tdOverallPCT"})
	grade = str(div)
	grade = grade[152:-5]
	if grade == "":
		English()
	else:
		print grade


def Math():
	global session
	endpoint2 = "https://mykids.ggusd.us/LoginParent.aspx"
	payload2 = {
		"checkCookiesEnabled":"true",
		"checkMobileDevice":"false",
		"checkStandaloneMode":"false",
		"checkTabletDevice":"false",
		"portalAccountUsername":"richard24680123@gmail.com",
		"portalAccountPassword":"r1357924680",
		"portalAccountUsernameLabel":"",
		"submit":""
	}
	responce2 = session.post(endpoint2, data=payload2)
	endpoint1 = "https://mykids.ggusd.us/Widgets/ClassSummary/RedirectToGradebook?GradebookNumber=5431808&Term=S&CDS=30665220000000&SC=83"
	responce1 = session.get(endpoint1)
	soup = bs(responce1.text, "html.parser")
	div = soup.find("td",{"id":"ctl00_MainContent_subGBS_DataSummary_ctl04_tdPCT"})
	grade = str(div)
	grade = grade[145:-5]
	if grade == "":
		Math()
	else:
		print grade

def PE():
	global session
	endpoint2 = "https://mykids.ggusd.us/LoginParent.aspx"
	payload2 = {
		"checkCookiesEnabled":"true",
		"checkMobileDevice":"false",
		"checkStandaloneMode":"false",
		"checkTabletDevice":"false",
		"portalAccountUsername":"richard24680123@gmail.com",
		"portalAccountPassword":"r1357924680",
		"portalAccountUsernameLabel":"",
		"submit":""
	}
	responce2 = session.post(endpoint2, data=payload2)
	endpoint1 = "https://mykids.ggusd.us/Widgets/ClassSummary/RedirectToGradebook?GradebookNumber=8606068&Term=S&CDS=30665220000000&SC=83"
	responce1 = session.get(endpoint1)
	soup = bs(responce1.text, "html.parser")
	div = soup.find("td",{"id":"ctl00_MainContent_subGBS_DataSummary_ctl03_tdPCT"})
	grade = str(div)
	grade = grade[145:-5]
	if grade == "":
		PE()
	else:
		print grade

def Chem():
	global session
	endpoint2 = "https://mykids.ggusd.us/LoginParent.aspx"
	payload2 = {
		"checkCookiesEnabled":"true",
		"checkMobileDevice":"false",
		"checkStandaloneMode":"false",
		"checkTabletDevice":"false",
		"portalAccountUsername":"richard24680123@gmail.com",
		"portalAccountPassword":"r1357924680",
		"portalAccountUsernameLabel":"",
		"submit":""
	}
	responce2 = session.post(endpoint2, data=payload2)
	endpoint1 = "https://mykids.ggusd.us/Widgets/ClassSummary/RedirectToGradebook?GradebookNumber=3269881&Term=S&CDS=30665220000000&SC=83"
	responce1 = session.get(endpoint1)
	soup = bs(responce1.text, "html.parser")
	div = soup.find("td",{"id":"ctl00_MainContent_subGBS_DataSummary_ctl04_tdPCT"})
	grade = str(div)
	grade = grade[145:-5]
	if grade == "":
		Chem()
	else:
		print grade

def History():
	global session
	endpoint2 = "https://mykids.ggusd.us/LoginParent.aspx"
	payload2 = {
		"checkCookiesEnabled":"true",
		"checkMobileDevice":"false",
		"checkStandaloneMode":"false",
		"checkTabletDevice":"false",
		"portalAccountUsername":"richard24680123@gmail.com",
		"portalAccountPassword":"r1357924680",
		"portalAccountUsernameLabel":"",
		"submit":""
	}
	responce2 = session.post(endpoint2, data=payload2)
	endpoint1 = "https://mykids.ggusd.us/Widgets/ClassSummary/RedirectToGradebook?GradebookNumber=3298564&Term=S&CDS=30665220000000&SC=83"
	responce1 = session.get(endpoint1)
	soup = bs(responce1.text, "html.parser")
	div = soup.find("td",{"id":"ctl00_MainContent_subGBS_DataSummary_ctl05_tdPCT"})
	grade = str(div)
	grade = grade[145:-5]
	if grade == "":
		History()
	else:
		print grade

def Spanish():
	global session
	endpoint2 = "https://mykids.ggusd.us/LoginParent.aspx"
	payload2 = {
		"checkCookiesEnabled":"true",
		"checkMobileDevice":"false",
		"checkStandaloneMode":"false",
		"checkTabletDevice":"false",
		"portalAccountUsername":"richard24680123@gmail.com",
		"portalAccountPassword":"r1357924680",
		"portalAccountUsernameLabel":"",
		"submit":""
	}
	responce2 = session.post(endpoint2, data=payload2)
	endpoint1 = "https://mykids.ggusd.us/Widgets/ClassSummary/RedirectToGradebook?GradebookNumber=7976007&Term=S&CDS=30665220000000&SC=83"
	responce1 = session.get(endpoint1)
	soup = bs(responce1.text, "html.parser")
	div = soup.find("td",{"id":"ctl00_MainContent_subGBS_DataSummary_ctl04_tdPCT"})
	grade = str(div)
	grade = grade[145:-5]
	if grade == "":
		Spanish()
	else:
		print grade

def All():
	print "English:"
	English()
	print "Math:"
	Math()
	print "PE:"
	PE()
	print "Chem:"
	Chem()
	print "History:"
	History()
	print "Spanish:"
	Spanish()


All()