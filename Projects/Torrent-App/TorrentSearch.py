from urllib.request import urlopen as uOpen
import bs4 , requests , time , socket , os , sys
from requests import Session
from bs4 import BeautifulSoup as bSoup 
import xml , webbrowser
from xml import etree
from xml.etree import ElementTree
from colorama import Fore , init
import subprocess


init()

# Colors
LightGreen = Fore.LIGHTGREEN_EX     
LightYellow = Fore.LIGHTYELLOW_EX
LightRed = Fore.LIGHTERED_EX
Cyan = Fore.CYAN
LightCyan = Fore.LIGHTCYAN_EX
LightBlue = Fore.LIGHTBLUE_EX

def slowPrint(str):            # Slow print function
   for c in str :
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(0.4)

def rem_tags (st) :         # Removing html tag function

    return ''.join(xml.etree.ElementTree.fromstring(str(st)).itertext())

banner = r"""
▀█▀ █▀█ █▀█ █▀█ █▀▀ █▄ █ ▀█▀  █▀ █▀▀ ▄▀█ █▀█ █▀▀ █ █
 █  █▄█ █▀▄ █▀▄ ██▄ █ ▀█  █   ▄█ ██▄ █▀█ █▀▄ █▄▄ █▀█"""
tagline = """
  [+] Tool by Dhruv Patel       [+] Site 1337x.to
-----------------------------------------------------"""

try:
    print(Cyan + banner)
    print(LightCyan + tagline)

    phrase = input("\nSearch Torrents : ")

    url = "https://1337x.to/srch?"           # Searching for film with get request
    param = {"search": phrase}

    res = requests.get(url , params=param)

    if res.status_code == 200 :          
        
        reDir_url = res.url                 # Getting the redirected url
        #print(reDir_url)    
        print("\nSearching",end="")
        time.sleep(0.5)
        slowPrint("....")                #print dots slowly

        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (like Gecko) Chrome/84.0.4147.105 Safari/537.36 OPR/70.0.3728.95"
        }
        time.sleep(0.5)
        os.system('cls')
        print(Cyan + banner)
        print(LightCyan + tagline)
        print(LightCyan + f"\nSearch Results For \"{phrase}\" : \n")
        Resp = requests.get(reDir_url , headers=headers)      # Get request to get html code
        
        if Resp.status_code == 200 :
            
            link_list = []
            t_no = 0
            #print(Resp.text)
            #uClient = uOpen(reDir_url)
            page_html = Resp.text #uClient.read()                     # Setting response text as page_html
            #uClient.close()
            page_soup = bSoup(page_html,"html.parser")

            names = page_soup.find_all("td",{"class":"coll-1 name"})         # Finding elements 
            seeds = page_soup.find_all("td",{"class":"coll-2 seeds"})
            leaches = page_soup.find_all("td",{"class":"coll-3 leeches"})
            times = page_soup.find_all("td",{"class":"coll-date"})
            sizes = page_soup.find_all("td",{"class":"coll-4"})
            uploader = page_soup.find_all("td",{"class":"coll-5"})
            
            if len(names) == 0 :                                        # checking if theres no torrents found  
                os.system('cls')
                print(LightRed + f"No results for \"{phrase}\" ")
                time.sleep(4)
                exit()

            for i in range(len(names)) :    

                nameN = rem_tags(names[i])                 # Removing Html tags and assign to new variable
                seedN = rem_tags(seeds[i])
                leachN = rem_tags(leaches[i])
                timeN = rem_tags(times[i])
                sizeN = rem_tags(sizes[i])
                uploaderN = rem_tags(uploader[i])
                links = names[i].find_all("a")    
                link = str(links[1])
                
                while True :                  # Getting site link of torrent
                    if link[0] == "\""  :
                        break
                    link = link[+1:]
                
                while True :
                    if link[-1] == "\""  :
                        break
                    link = link[:-1]
                
                while True :                  # removing useless tag inside torrent size
                    if sizeN[-1] == "B" : 
                        break
                    sizeN = sizeN[:-1]   
                t_no += 1
                link = link[:-1]        # Removing double quotes before and after the link
                link = link[+1:]
                linkN = "https://1337x.to" + link   # joining to make full url
                link_list.append(linkN)
                
                print(LightCyan +"\n[",t_no,"] ",end="")       # Printing torrent list (for search phrase)
                print(LightYellow + "",nameN)    
                print(LightGreen +"Seeds :",seedN,end="  ")
                print("Leeches :",leachN,end="  ")
                print("Time :",timeN)
                print("Size :",sizeN,end="  ")
                print("Uploader :",uploaderN)
                #print("Link :",linkN)
                time.sleep(0.3)
            
            print(LightCyan + "")
            
            try:
                #print(lC +"\nTorrent Link :\n",lY + link_list[int(choice)-1])
                choice = input("Enter torrent no : ")                          # Input torrent number 
                Torr_link = link_list[int(choice)-1]
            except Exception as e2:
                print(LightRed + "Error",e2)    
                print("Enter only displayed numbers !")                       # Error Handling

            resp3 = requests.get(Torr_link)    # Get request to get html data of selected torrent
            Down_links = []
            Down_sites = []

            page_html2 = resp3.text 
            page_soup2 = bSoup(page_html2,"html.parser")
            dropdown = page_soup2.find("li",{"class":"dropdown"})  #Getting download dropdown elements
            headerNM = page_soup2.find("h1")
            saveNM = rem_tags(headerNM)
            
            downside_names = dropdown.find_all("a")
            for b in range(len(downside_names)) :
                if b != 0 :
                    #print(rem_tags(downside_names[b]))
                    Down_sites.append(rem_tags(downside_names[b])) #append downloading site names to a list ex- torrents 

            for a in dropdown.find_all('a', href=True):
                
                if a['href'] != "#" and a['href'] != "" :
                    #print("\n",a['href'])
                    Down_links.append(a['href'])    #append download links to a list 

            print(LightCyan + "\n[1] Download Torrent File (Direct) \n[2] Open Torrent Client (Magnet Link) \n[3] Manual Download (links)")
            choice2 = input("\nChoose Download Method : ")     
            if choice2 == "1" :                               # Download direct method (.torrent)  
                print(LightRed + "\nDownloading...")
                time.sleep(1)
                direct_link = str(Down_links[0])

                #if "https" not  in direct_link :                       
                    #direct_link = direct_link.replace("http","https")                    

                saveNM = saveNM.replace("(","") # Removing illegal chars
                saveNM = saveNM.replace(")","")
                saveNM = saveNM.replace("[","")
                saveNM = saveNM.replace("]","")
                saveNM = saveNM.replace("-","")
                saveNM = saveNM.replace("/","")
                saveNM = saveNM.replace(".","")
                
                session = Session()
                session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ( like Gecko) Chrome/85.0.4183.121 Safari/537.36'
                
                r = session.get(direct_link)
                
                saveNM = saveNM + ".torrent"
                if r.status_code == 200 :
                    open(saveNM, 'wb').write(r.content)   # Saving file 
                    print("\nSaved Successfully > check current folder ")
                    print("Ex - ",os.path.abspath(saveNM))
    
                else:
                    print(LightRed + "Something went wrong, Error code ",r.status_code,"\nFailed to download :",direct_link)

                print(LightCyan +"")
                downcome = input("Didn't work ? \nTry another method ! (Y/n) : ")  # asking if downloaded or not 

                if downcome == "Y" or downcome == "y" :
                    webbrowser.open_new_tab(Down_links[0])    # open another link in web browser
                else:
                    print("")
                
            elif choice2 == "2":
                try:
                    webbrowser.open_new_tab(Down_links[-1])          # Torrent magnet download
                    print(LightGreen + "Opening Torrent Client...")         # opening torrent client 
                except Exception as eee:
                    print(LightRed + "Error while opening torrent client")
                    print(eee)
                else:
                    print("")       
                     
            elif choice2 == "3" :                                 #Manual method
                
                print(LightGreen + f"Site link : {Torr_link} \n")        # Display all download links
                print("All Download links \n")
                for z in range(len(Down_sites)) :
                    print("\n",LightCyan + Down_sites[z],":",LightGreen + Down_links[z])
                    time.sleep(0.5)  

            else:
                print(LightRed + "Invalid option !")          

        else:                                                      
            print(LightRed + "Redirection Failed",Resp.status_code)   # If Request error occurs these are printed

    else:
        print(LightRed + "Error occurred while searching",res.status_code)    

except Exception as e :
    print(LightRed + "Something went wrong\n",e)

input("\nExit >")