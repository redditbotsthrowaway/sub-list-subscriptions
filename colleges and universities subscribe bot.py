import praw
import time
from time import sleep
import random

a = input("What's your client_id? ")
b = input("What's your client secret? ")
c = input("What's your username? ")
d = input("What's your password? ")

reddit = praw.Reddit(client_id = str(a), 
                     client_secret = str(b),
                     username = str(c), 
                     password = str(d), 
                     user_agent = "test")


college_sub_list = ['Aberystwyth','AcadiaU','Algonquin_College','amarillocollege','AmericanU','amherstcollege','AndersonUniversity','appstate','aquinas',
                    'ASU','ArkansasState','auburn','australiancatholicuni','Anu','apu','Babson','BallState','Baruch','baylor','berea','Berklee',
                    'BinghamtonUniversity','Biola','bsu','theBAC','bostoncollege','BostonU','BournemouthUni','Bowdoin','bradleyuniversity','brandeis',
                    'byu','BCIT','brocku','Broward','BrownU','brunel','bucknell','butleruniversity','CCA','Caltech','calarts','CalPoly','CalPolyPomona',
                    'csuci','CSUC','CSUDH','CSUEB','csuf','CSULB','CSULA','csumb','csun','CSUS','CSUSB','csusm','fresnostate','calupa','CCCU','CapU',
                    'CarletonCollege','CarletonU','cmu','cwru','centralmich','chalmers','chapmanuniversity','CNU','CCNY','cityuniversitylondon','CUNY',
                    'claremontcolleges','ClarkU','Clemson','CCU','Colby','Colgate','CofC','Wooster','HolyCross','ColoradoSchoolOfMines','CSUFoCo','colum',
                    'columbia','Concordia','Conestoga','conncoll','Cornell','CovUni','curtin','Dalhousie','dartmouth','davidson','DePauw','devry','deakin',
                    'Denison','depaul','DVC','digipen','Drexel','duke','durhamcollege','Durhamu','EarlhamCollege','ECU','ETSU','ECSU','emu','ewu',
                    'eastmanschool','erau','EmersonCollege','Emory','fairfieldU','fanshawe','flaglercollege','FAU','fgcu','floridatech','FIU','fsu','FLC',
                    'Fontbonne','Fordham','fandm','fullsail','Furman','gmu','gwu','georgetown','gcsu','gatech','GSU','GaState','goldsmiths','Gonzaga',
                    'GVSU','GMACEWAN','greenvillecollege','GriffithUni','Grinnell','grossmont','gcsc','gustavus','hamiltoncollege','HampshireCollege',
                    'HarfordCC','Harvard','harveymudd','HendersonState','heriotwatt','hillsdale','houstoncc','Humber','humboldtstate','HunterCollege','IIT',
                    'ilstu','IllinoisWesleyan','Imperial','indstate','IndianaUniversity','IUP','IST','iastate','IthacaCollege','JSU','jamescook','jmu',
                    'jcu','jhu','JuniataCollege','kth','KState','KSU','KentStateUniversity','Kettering','KCL','kingstonu','kutztown','lakeheadu','langara',
                    'lawrenceu','leedsbeckett','Lehigh','LibertyUniversity','linkopinguniversity','TheLse','Longwood','lufbra','LSU','LouisianaTech','LMU',
                    'Decorah','LyonCollege','grantmacewan','Macon_State','MacUni','MMU','ManhattanCollege','marist','marlborocollege','Marquette',
                    'MarshallUniversity','mit','MayfieldCollege','mcgill','McKendree_University','McMaster','memorialuniversity','MSCD','miamioh','msu',
                    'MTU','MTSU','matc','MSOE','Msstate','missouristate','Rolla','mohawkcollege','MSUcats','mpc','MRU','MountainState','MtSanJacintoCollege',
                    'murdoch','Murray','nus','Neumont','NJTech','nmt','nmsu','nyu','niagaracollege','NSU','NCSU','NDSU','NEU','NAIT','NAU','NIU','NKU',
                    'Northwestern','ntnu','oaklanduniversity','oberlin','Oxy','OSU','ohiouniversity','OCU','OKState','ODU','olin','OpenUniversity','OCC',
                    'OregonStateUniv','Otterbein','OxfordBrookes','pace','PLU','ParklandCollege','PennStateUniversity','gopct','Pepperdine',
                    'PolkStateCollege','PolyMTL','pomonacollege','PUC','portlandstate','princeton','ProvidenceCollege','Purdue','QMULandBarts',
                    'queensuniversity','QueensBelfast','QUTreddit','Quinnipiac','rmit','radforduniversity','reedcollege','RPI','riceuniversity',
                    'RichardStockton','RCC','rit','Roosevelt','rosehulman','RowanUniversity','RHUL','rutgers','ryerson','SVSU','stedwards','stfx','THWND',
                    'billikens','SMUHalifax','stolaf','SLCC','SHSU','SDSU','SFSU','SJSU','SCU','scad','SOAS','sva','scrippscollege','seattleu','Seneca',
                    'SHU','sheffieldhallam','sheridan','ship','siena','SierraCollege','simonfraser','SSU','SDSMT','semo','SAIT','SIU','SIUE','SMU','SPSU',
                    'stjohnscollege','Spc','stanford','Oswego','Potsdam','SFA','stevens','SBU','swanseauni','swinburne','ethz','SyracuseU','tarleton',
                    'TaylorUniversity','tuberlin','tud','teccr','TeessideUniversity','Temple','tsu','aggies','TCU','txstate','TexasTech','TCNJ',
                    'williamandmary','evergreen','tesu','Touro','Towson','TrentUniversity','TCD','trinityu','TroyU','Tufts','Tulane','usna','ucrcr','USAC',
                    'UCL','ualbany','UBreddit','UniAdelaide','uakron','capstone','UAB','UAH','uAlberta','UofArizona','UniversityofArkansas',
                    'universityofauckland','UBALTIMORE','BathUni','UofB','UOB','UBC','ubco','UCalgary','berkeley','UCDavis','UCI','ucla','ucmerced','ucr',
                    'UCSD','UCSantaBarbara','UCSC','cambridge_uni','UCT','UCA','ucf','UCO','uchicago','uCinci','cudenver','cuboulder','UCCS','UCONN',
                    'uofdayton','udel','denveru','UEA','Edinburgh_University','essexuni','Exe','ufl','UGA','GlasgowUni','uoguelph','guelphhumber','uhart',
                    'UniversityofHawaii','-UniOfHertfordshire','UniversityOfHouston','uhd','uofi','uichicago','UIUC','uiowa','UniversityofKansas','KentUni',
                    'UniversityofKentucky','lancasteruni','LeedsUni','UoL','universityoflimerick','LincolnUni','ragincajuns','AllHail','umaine',
                    'manchester_uni','umanitoba','UMW','UMD','UMBC','umass','umassd','uml','unimelb','UofMemphis','UMiami','uofm','uofmn','UofMnDuluth',
                    'olemiss','mizzou','UMKC','UMT','Montevallo','UNLincoln','UNLV','unr','unh','unm','unsw','UoNau','tarheels','UNCCharlotte','UNCG',
                    'UNCW','und','UNF','unt','UNBC','UNI','notredame','UoN','sooners','uoit','geegees','oxforduni','UPenn','unipi','Pitt','UQreddit',
                    'universityofredlands','University_Of_Regina','URochester','roehamptonuni','standrews','USD','usfca','usask','universityofscranton',
                    'uos','Gamecocks','USF','USC','USI','stthomas','strathclyde','universityofsussex','usyd','UTS','UTK','UTAustin','utdallas','UTEP',
                    'UTPA','UTSA','UTT','UniversityOfToledo','UofT','utulsa','uofu','UniversityofVermont','uvic','UVA','UniversityOfWarwick','udub','uwb',
                    'uwaterloo','UWG','uwa','uwo','WestminsterUni','UWindsor','UWEauClaire','uwgb','UWMadison','UWMilwaukee','UWOshkosh','UWWhitewater',
                    'UOW','uwyo','universityofyork','UFV','UoP','peyups','uwe','UdeM','usherbrooke','UQAM','UVU','VIU','Vanderbilt','vassar','vcccd',
                    'villanova','vcu','VirginiaTech','vub','wfu','WakeTech','wsu','washu','waynestate','WellesleyCollege','WIT','Wesleyan','wcupa',
                    'westliberty','wtamu','WVU','WCU','Wcsu','WGU','WKU','WMU','WWU','WestminsterCollege','Westmont','Wheaton','Widener','wlu','WoodsWay',
                    'WilliamsCollege','WPI','wrightstate','yale','yorku','etsmtl']

for sub in sub_list:
    subreddit = reddit.subreddit(sub)
    a = random.randint(1,3)
    subreddit.subscribe()
    sleep(a)
