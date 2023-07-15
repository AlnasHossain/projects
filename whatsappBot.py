from selenium import webdriver
import math
import time as Tt
import datetime
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
print("""
 █████╗ ██╗   ██╗████████╗ ██████╗ ███╗   ███╗ █████╗ ████████╗██╗ ██████╗         
██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗████╗ ████║██╔══██╗╚══██╔══╝██║██╔════╝         
███████║██║   ██║   ██║   ██║   ██║██╔████╔██║███████║   ██║   ██║██║              
██╔══██║██║   ██║   ██║   ██║   ██║██║╚██╔╝██║██╔══██║   ██║   ██║██║              
██║  ██║╚██████╔╝   ██║   ╚██████╔╝██║ ╚═╝ ██║██║  ██║   ██║   ██║╚██████╗         
╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝         
                                                                                   
██╗    ██╗██╗  ██╗ █████╗ ████████╗███████╗ █████╗ ██████╗ ██████╗                 
██║    ██║██║  ██║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██╔══██╗                
██║ █╗ ██║███████║███████║   ██║   ███████╗███████║██████╔╝██████╔╝                
██║███╗██║██╔══██║██╔══██║   ██║   ╚════██║██╔══██║██╔═══╝ ██╔═══╝                 
╚███╔███╔╝██║  ██║██║  ██║   ██║   ███████║██║  ██║██║     ██║                     
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝                     
                                                                                   
██╗     ██╗███╗   ██╗██╗  ██╗    ███████╗███████╗███╗   ██╗██████╗ ███████╗██████╗ 
██║     ██║████╗  ██║██║ ██╔╝    ██╔════╝██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗
██║     ██║██╔██╗ ██║█████╔╝     ███████╗█████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝
██║     ██║██║╚██╗██║██╔═██╗     ╚════██║██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
███████╗██║██║ ╚████║██║  ██╗    ███████║███████╗██║ ╚████║██████╔╝███████╗██║  ██║
╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝    ╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                                         
""")
def check():
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://web.whatsapp.com")
    print("Scan QR and hit Enter") 
    input() 
    print("Logged in")
    Tt.sleep(5)
    def mondayClass():
        comm="*FREE CLASS !  ~bot*"
        em="""
        *ENGINEERING MATHEMATICS CLASS:*

        https://teams.microsoft.com/l/meetup-join/19%3ade7067483e184d57be56544cb61902b6%40thread.tacv2/1617382585949?context=%7b%22Tid%22%3a%22b1703185-2d99-40e5-86e1-3a22312faf76%22%2c%22Oid%22%3a%22f90c11cc-c176-4393-a09d-d2d9802decac%22%7d

        *ALL MUST JOIN IN TIME*

        *~bot*
        """
        mech="""
        *ENGINEERING MECHANICS CLASS:*

        https://teams.microsoft.com/l/meetup-join/19%3ab4cb7133fda740c2a1de1b5274738a41%40thread.tacv2/1618300844223?context=%7b%22Tid%22%3a%22b1703185-2d99-40e5-86e1-3a22312faf76%22%2c%22Oid%22%3a%226b54fd47-ba08-4966-aa11-e931045d20fa%22%7d

        *ALL MUST JOIN IN TIME*

        *~bot*
        """
        lunch = "*ITS LUNCH TIME from 12:30 to 1:30  ~bot*"
        freePeriod="*ITS FREE PERIOD NOW, NEXT CLASS IN 2:30 ~bot*"
        emS="""
        *ENGINEERING MATHEMATICS CLASS (SUMIT SIR):*

        https://teams.microsoft.com/l/meetup-join/19%3ade7067483e184d57be56544cb61902b6%40thread.tacv2/1617382585949?context=%7b%22Tid%22%3a%22b1703185-2d99-40e5-86e1-3a22312faf76%22%2c%22Oid%22%3a%22f90c11cc-c176-4393-a09d-d2d9802decac%22%7d

        *ALL MUST JOIN IN TIME*

        *~bot*
        """
        evs="""
        *ENVIRONMENTAL SCIENCE CLASS:*
    
        https://teams.microsoft.com/l/meetup-join/19%3a5b2c98f129334a7786405c496d964aa1%40thread.tacv2/1617726344396?context=%7b%22Tid%22%3a%22b1703185-2d99-40e5-86e1-3a22312faf76%22%2c%22Oid%22%3a%22a70f3740-08d6-434b-b4bf-52be1dad31f0%22%7d

        *ALL MUST JOIN IN TIME*

        *~bot*
        """
        minor="*ITS MINOR THEORY CLASS. THOSE WHO HAVE OPTED FOR IT MUST JOIN THEIR RESPECTIVE CLASSES  ~bot*"
        search_box=driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]") 
        search_box.send_keys(contact) 
        search_box.send_keys(Keys.ENTER) 
        Tt.sleep(3)
        msg_box=driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]") 
        msg_box.send_keys(comm) 
        Tt.sleep(2) 
        msg_box.send_keys(Keys.ENTER)
        Tt.sleep(3600) 
        msg_box.send_keys(em) 
        Tt.sleep(2) 
        msg_box.send_keys(Keys.ENTER)
        Tt.sleep(3600)
        msg_box.send_keys(mech)
        Tt.sleep(2)
        msg_box.send_keys(Keys.ENTER) 
        Tt.sleep(3600)
        msg_box.send_keys(lunch)
        Tt.sleep(2)
        msg_box.send_keys(Keys.ENTER) 
        Tt.sleep(3600)
        msg_box.send_keys(freePeriod)
        Tt.sleep(2)
        msg_box.send_keys(Keys.ENTER) 
        Tt.sleep(3600) 
        msg_box.send_keys(emS) 
        Tt.sleep(2) 
        msg_box.send_keys(Keys.ENTER) 
        Tt.sleep(3600) 
        msg_box.send_keys(evs) 
        Tt.sleep(2) 
        msg_box.send_keys(Keys.ENTER) 
        Tt.sleep(3600) 
        msg_box.send_keys(minor) 
        Tt.sleep(2) 
        msg_box.send_keys(Keys.ENTER) 
        Tt.sleep(5) 
        driver.quit()
    def tuesdayClass():
        em="""
        *ENGINEERING MATHEMATICS CLASS:*

        https://teams.microsoft.com/l/meetup-join/19%3ade7067483e184d57be56544cb61902b6%40thread.tacv2/1617382663441?context=%7b%22Tid%22%3a%22b1703185-2d99-40e5-86e1-3a22312faf76%22%2c%22Oid%22%3a%22f90c11cc-c176-4393-a09d-d2d9802decac%22%7d

        *ALL MUST JOIN IN TIME*

        *~bot*
        """
        ip="""
        *INTRODUCTION TO PROGRAMMING CLASS:*

        https://teams.microsoft.com/l/meetup-join/19:meeting_MzU0OGEwMGQtMjM1Zi00NGEyLTlkNDMtMGY2ODIwZmJkYjkz@thread.v2/0?context=%7b%22Tid%22%3a%22b1703185-2d99-40e5-86e1-3a22312faf76%22%2c%22Oid%22%3a%2280fffabb-cfd2-4b92-8d2b-7f11fbaa093d%22%7d

        *ALL MUST JOIN IN TIME*

        *~bot*   
        """
        mech="""
        *ENGINEERING MECHANICS CLASS:*

        https://teams.microsoft.com/l/meetup-join/19%3ab4cb7133fda740c2a1de1b5274738a41%40thread.tacv2/1618300844223?context=%7b%22Tid%22%3a%22b1703185-2d99-40e5-86e1-3a22312faf76%22%2c%22Oid%22%3a%226b54fd47-ba08-4966-aa11-e931045d20fa%22%7d

        *ALL MUST JOIN IN TIME*

        *~bot*
        """
        minor="*ITS MINOR THEORY CLASS. THOSE WHO HAVE OPTED FOR IT MUST JOIN THEIR RESPECTIVE CLASSES  ~bot*"
        search_box=driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]") 
        search_box.send_keys(contact) 
        search_box.send_keys(Keys.ENTER) 
        Tt.sleep(3)
        msg_box=driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]") 
        msg_box.send_keys(em) 
        Tt.sleep(2) 
        msg_box.send_keys(Keys.ENTER) 
        Tt.sleep(3600) 
        msg_box.send_keys(ip) 
        Tt.sleep(2) 
        msg_box.send_keys(Keys.ENTER) 
        Tt.sleep(14400) 
        msg_box.send_keys(mech) 
        Tt.sleep(2) 
        msg_box.send_keys(Keys.ENTER) 
        Tt.sleep(7200) 
        msg_box.send_keys(minor) 
        Tt.sleep(2) 
        msg_box.send_keys(Keys.ENTER) 
        Tt.sleep(5) 
        driver.quit()
    def wednesdayClass():
        progLab="""
        *INTRODUCTION TO PROGRAMMING LAB: - GROUP 1*

        https://teams.microsoft.com/l/meetup-join/19%3ameeting_MjE5NjY0YTMtNmY3Ny00NzY1LWI4ZGEtODVlNjhiYWFhYTE5%40thread.v2/0?context=%7b%22Tid%22%3a%22b1703185-2d99-40e5-86e1-3a22312faf76%22%2c%22Oid%22%3a%2280fffabb-cfd2-4b92-8d2b-7f11fbaa093d%22%7d

        *ALL MUST JOIN IN TIME*

        *~bot*
        """
        enggDraw="""
        *ENGINEERING DRAWING / CAD: - GROUP 2*

        https://teams.microsoft.com/l/meetup-join/19%3Ameeting_ZjhmYmI0ZjItMmNhNS00OTg0LWI3OTAtYWMyOTFkNzNiZjhi%40thread.v2/0?context=%7B%22Tid%22%3A%22b1703185-2d99-40e5-86e1-3a22312faf76%22%2C%22Oid%22%3A%2282ee3c8f-f39d-4261-866c-fa5e5bd8bed6%22%7D

        *ALL MUST JOIN IN TIME*

        *~bot*
        """
        capstone="*JOIN YOUR RESPECTIVE CAPSTONE CLASSES USING THE LINK SENT IN YOUR OUTLOOK/PERSONAL EMAIL-ID  ~bot*"
        search_box=driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]") 
        search_box.send_keys(contact) 
        search_box.send_keys(Keys.ENTER) 
        Tt.sleep(3)
        msg_box=driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]") 
        msg_box.send_keys(progLab) 
        Tt.sleep(2) 
        msg_box.send_keys(Keys.ENTER) 
        Tt.sleep(5) 
        msg_box.send_keys(enggDraw) 
        Tt.sleep(2) 
        msg_box.send_keys(Keys.ENTER) 
        Tt.sleep(14400) 
        msg_box.send_keys(capstone) 
        Tt.sleep(2) 
        msg_box.send_keys(Keys.ENTER) 
        Tt.sleep(5) 
        driver.quit()
    def thursdayClass():
        evs="""
        *ENVIRONMENTAL SCIENCE CLASS:*
    
        https://teams.microsoft.com/l/meetup-join/19%3a5b2c98f129334a7786405c496d964aa1%40thread.tacv2/1617726288078?context=%7b%22Tid%22%3a%22b1703185-2d99-40e5-86e1-3a22312faf76%22%2c%22Oid%22%3a%22a70f3740-08d6-434b-b4bf-52be1dad31f0%22%7d

        *ALL MUST JOIN IN TIME*
        *~bot*
        """
        emS="""
        *ENGINEERING MATHEMATICS -II CLASS:*

        https://teams.microsoft.com/l/meetup-join/19%3ade7067483e184d57be56544cb61902b6%40thread.tacv2/1617459810672?context=%7b%22Tid%22%3a%22b1703185-2d99-40e5-86e1-3a22312faf76%22%2c%22Oid%22%3a%22096070cb-f173-4d93-b3dd-e60a446a2fcd%22%7d

        *ALL MUST JOIN IN TIME*

        *~bot*
        
        """
        progLab="""
        *INTRODUCTION TO PROGRAMMING LAB - GROUP2:*

        https://teams.microsoft.com/l/meetup-join/19%3ameeting_NWY1MTI0OTctMTMwNC00Y2MzLTlkMTctYjg4YWE2NmZhNWYz%40thread.v2/0?context=%7b%22Tid%22%3a%22b1703185-2d99-40e5-86e1-3a22312faf76%22%2c%22Oid%22%3a%2280fffabb-cfd2-4b92-8d2b-7f11fbaa093d%22%7d

        *ALL MUST JOIN IN TIME*

        *~bot*
        """
        enggDraw="""
        *ENGINEERING DRAWING / CAD - GROUP 1:*

        https://teams.microsoft.com/l/channel/19%3ab74722bd3778487f9661ee9c89ec9f78%40thread.tacv2/General?groupId=5a05a0f1-9437-4244-95d6-3e6a83ef8cfd&tenantId=b1703185-2d99-40e5-86e1-3a22312faf76

        *ALL MUST JOIN IN TIME*

        *~bot*
        """
        minor="*ITS MINOR THEORY CLASS. THOSE WHO HAVE OPTED FOR IT MUST JOIN THEIR RESPECTIVE CLASSES  ~bot*"
        search_box=driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]") 
        search_box.send_keys(contact) 
        search_box.send_keys(Keys.ENTER) 
        Tt.sleep(3)
        msg_box=driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]") 
        msg_box.send_keys(evs) 
        Tt.sleep(2) 
        msg_box.send_keys(Keys.ENTER) 
        Tt.sleep(3600) 
        msg_box.send_keys(emS) 
        Tt.sleep(2) 
        msg_box.send_keys(Keys.ENTER)
        Tt.sleep(10800) 
        msg_box.send_keys(progLab) 
        Tt.sleep(2) 
        msg_box.send_keys(Keys.ENTER) 
        Tt.sleep(5) 
        msg_box.send_keys(enggDraw) 
        Tt.sleep(2) 
        msg_box.send_keys(Keys.ENTER) 
        Tt.sleep(10800) 
        msg_box.send_keys(minor) 
        Tt.sleep(2) 
        msg_box.send_keys(Keys.ENTER) 
        Tt.sleep(5) 
        driver.quit()
    def fridayClass():
        mech1="""
        *ENGINEERING MECHANICS CLASS:*

        https://teams.microsoft.com/l/meetup-join/19%3Ab4cb7133fda740c2a1de1b5274738a41%40thread.tacv2/1618300844223?context=%7B%22Tid%22%3A%22b1703185-2d99-40e5-86e1-3a22312faf76%22%2C%22Oid%22%3A%226b54fd47-ba08-4966-aa11-e931045d20fa%22%7D

        *ALL MUST JOIN IN TIME*

        *~bot*
        """
        comm="""
        *COMMUNICATION AND COLLABORATION CLASS:*
    
        https://teams.microsoft.com/l/meetup-join/19%3ameeting_MWE3ZWVlNzgtNjhmZS00Nzk4LWJkZTktYWZhZTBhZDUzZTM2%40thread.v2/0?context=%7b%22Tid%22%3a%22b1703185-2d99-40e5-86e1-3a22312faf76%22%2c%22Oid%22%3a%2294cbf7de-6299-47f0-8689-eb674413207b%22%7d

        *ALL MUST JOIN IN TIME*

        *~bot*
        """
        ip="""
        *INTRODUCTION TO PROGRAMMING:*

        https://teams.microsoft.com/l/meetup-join/19:meeting_OWQ5OTU0ZDItNDI5YS00NjU5LThjOWQtMjVkZjkwMGZmYmNl@thread.v2/0?context=%7b%22Tid%22%3a%22b1703185-2d99-40e5-86e1-3a22312faf76%22%2c%22Oid%22%3a%2280fffabb-cfd2-4b92-8d2b-7f11fbaa093d%22%7d

        *ALL MUST JOIN IN TIME*

        *~bot*
        """
        mech2="""
        *ENGINEERING MECHANICS CLASS:*
    
        https://teams.microsoft.com/l/meetup-join/19%3Ab4cb7133fda740c2a1de1b5274738a41%40thread.tacv2/1618300844223?context=%7B%22Tid%22%3A%22b1703185-2d99-40e5-86e1-3a22312faf76%22%2C%22Oid%22%3A%226b54fd47-ba08-4966-aa11-e931045d20fa%22%7D

        *ALL MUST JOIN IN TIME*

        *~bot*
        """
        evs="""
        *ENVIRONMENTAL SCIENCE CLASS:*

        https://teams.microsoft.com/dl/launcher/launcher.html?url=%2F_%23%2Fl%2Fmeetup-join%2F19%3A5b2c98f129334a7786405c496d964aa1%40thread.tacv2%2F1617726288078%3Fcontext%3D%257b%2522Tid%2522%253a%2522b1703185-2d99-40e5-86e1-3a22312faf76%2522%252c%2522Oid%2522%253a%2522a70f3740-08d6-434b-b4bf-52be1dad31f0%2522%257d%26anon%3Dtrue&type=meetup-join&deeplinkId=3b9e8748-13be-4ac7-8b89-37e1c3f552f7&directDl=true&msLaunch=true&enableMobilePage=true&suppressPrompt=true

        *ALL MUST JOIN IN TIME*

        *~bot*
        
        """
        minor="ITS MINOR THEORY CLASS. THOSE WHO HAVE OPTED FOR IT MUST JOIN THEIR RESPECTIVE CLASSES  ~bot"
        search_box=driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]") 
        search_box.send_keys(contact) 
        search_box.send_keys(Keys.ENTER) 
        Tt.sleep(3)
        msg_box=driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]") 
        msg_box.send_keys(mech1) 
        Tt.sleep(2) 
        msg_box.send_keys(Keys.ENTER) 
        Tt.sleep(3600) 
        msg_box.send_keys(comm) 
        Tt.sleep(2) 
        msg_box.send_keys(Keys.ENTER) 
        Tt.sleep(3600) 
        msg_box.send_keys(ip) 
        Tt.sleep(2) 
        msg_box.send_keys(Keys.ENTER) 
        Tt.sleep(7200) 
        msg_box.send_keys(mech2) 
        Tt.sleep(2) 
        msg_box.send_keys(Keys.ENTER) 
        Tt.sleep(3600) 
        msg_box.send_keys(evs) 
        Tt.sleep(2) 
        msg_box.send_keys(Keys.ENTER)
        Tt.sleep(7200) 
        msg_box.send_keys(minor) 
        Tt.sleep(2) 
        msg_box.send_keys(Keys.ENTER)
        Tt.sleep(5) 
        driver.quit()
    def extraClass():
        print("""Will there be class today?
        1. Yes
        2. No""")
        ch = int(input("Enter your choice: "))
        if ch==2:
            exit()
        elif ch==1:
            print("""Which day's routine will be followed ??
            1. Monday
            2. Tuesday
            3. Wednesday
            4. Thursday
            5. Friday
            """)
            ch= int(input("Enter choice: "))
            if ch==1:
                mondayClass()
            elif ch==2:
                tuesdayClass()
            elif ch==3:
                wednesdayClass()
            elif ch==4:
                thursdayClass()
            elif ch==5:
                fridayClass()
            else:
                print("Wrong input")   
    if __name__ == '__main__':
        x = datetime.datetime.now() 
        day= x.strftime("%A").lower()
        contact="Python code test" 
        if day=='monday':
            mondayClass()
        elif day=='tuesday':
            tuesdayClass()
        elif day=='wednesday':
            wednesdayClass()
        elif day=='thursday':
            thursdayClass()
        elif day=='friday':
            fridayClass()
        else:
            extraClass()

d=datetime.datetime.now()
x= d.strftime("%H:%M")
if x=='09:20':
    try:
        check()
    except:
        print("Error Arrived")
else:
    from datetime import time,timedelta
    import time as T
    currentTime= datetime.datetime.now()
    hour=currentTime.hour
    minute=currentTime.minute
    t1=timedelta(hours=hour,minutes=minute)
    t2=timedelta(hours=9, minutes=20)
    t3=t2-t1
    sec=int(t3.total_seconds())
    T.sleep(sec)
    check()