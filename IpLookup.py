import json
from urllib import request
import socket
from termcolor import colored
from colorama import Fore
import colorama
from tqdm import tqdm


colorama.init()

#What This Program ?
def fr():
   print(colored('''
**           **                         **                    
/** ******   /**                        /**             ****** 
/**/**///**  /**        ******   ****** /**  ** **   **/**///**
/**/**  /**  /**       **////** **////**/** ** /**  /**/**  /**
/**/******   /**      /**   /**/**   /**/****  /**  /**/****** 
/**/**///    /**      /**   /**/**   /**/**/** /**  /**/**///  
/**/**       /********//****** //****** /**//**//******/**     
// //        ////////  //////   //////  //  //  ////// //      
 **      **  ****      **** 
/**     /** */// *    *///**
/**     /**/    /*   /*  */*
//**    **    ***    /* * /*
 //**  **    /// *   /**  /*
  //****    *   /* **/*   /*
   //**    / **** /**/ **** 
    //      ////  //  ////  
 **     **                                                 
//**   **                                                  
 //** **   *******  **   ** **    **  *****  ******  ******
  //***   //**///**/**  /**/**   /** **///**//**//* **//// 
   **/**   /**  /**/**  /**//** /** /******* /** / //***** 
  ** //**  /**  /**/**  /** //****  /**////  /**    /////**
 **   //** ***  /**//******  //**   //******/***    ****** 
//     // ///   //  //////    //     ////// ///    //////  
''','blue'))
   print(Fore.GREEN + '''This Program For Track/Whois IP (IP Lookup)
BY Xnuversxploit''') #Print Color Green with Fore and Print text
   print("\n") #For Enter / Give a Newline
   import time #pip / package for time
   import datetime
   from datetime import datetime
   from datetime import date

   #Date Month Year
   a = "Date = "
   b = "Month = "
   t = "Year = "
   hari_ini = datetime.now()
   day = hari_ini.strftime(a+'%d ' + b+'%m ' + t+'%y')
   saat_ini = datetime.now()
   hours = saat_ini.strftime('%H:%M:%S')
   print("====="*5)
   print(day) #print for call day
   print("Hours : ", hours)#Print for call hours
   print("====="*5)
   print("\n") #print a newline

#Menu In this program
def lo():
   fr()
   print(Fore.RED + " [1] By Domain/Web ")
   print(Fore.RED + " [2] By IP Address ")

   pilih = int(input("Number ? : "))
   if (pilih==1):
      DomainToIp()
   elif(pilih==2):
      IpAddress()
   else:
      a = "Your Input is Invalid...".upper()
      print(Fore.YELLOW + a)

def end():
   print ("Thank you For use My Tools...\n")
   print ("Dont Forget to Support me On\n")
   print ("Saweria = https://saweria.co/xnuvers\n")
   print ("Github = https://github.com/Xnuvers007\n")
   print ("Instagram = https://instagram.com/indradwi.25")
   print ("This Program Will be close in 3")
   time.sleep(1)
   print ("2...")
   time.sleep(1)
   print ("1...")
   time.sleep(1)
   input("Press Enter For Exit...")
   exit(code=None)

def Start():
   while(True):
      print("\n")
      cont = input ("Want To Try Again ? [Y/N] : ")
      if (cont=='Y' or cont=='y'):
         lo()
      elif (cont=='N' or cont=='n'):
         end()
      else:
         print("Your Input is Invalid...")
#Get IP from domain name

def DomainToIp():
   choose = input("Please Input Domain To IP (Website) : ")
   host_name = socket.gethostbyname(choose)

   a = "The Domain Is = "+choose
   b = "The Ip From Domain Is = "+ host_name

   print(Fore.BLUE+"\n"+a+"\n"+b)

   url = "http://ipwhois.app/json/"+host_name # URL Endpoint
   response = request.urlopen(url) #HTTP Request to server
   data = json.loads(response.read()) #load data from Request
   for _ in tqdm(range(100),
                 desc="Loading...",
                  ascii=False, ncols=75):
      time.sleep(0.01) #loading...
#print the data
   print("\n")
   print(f"Ip Address : {data['ip']}")
   print(f"Status : {data['success']}")
   print(f"Type : {data['type']}")
   print(f"Continent : {data['continent']}")
   print(f"Continent Code : {data['continent_code']}")
   print(f"Country : {data['country']}")
   print(f"Country Code : {data['country_code']}")
   print(f"Flag : {data['country_flag']}")
   print(f"Country Capital : {data['country_capital']}")
   print(f"Country Phone : {data['country_phone']}")
   print(f"Country Neighbours : {data['country_neighbours']}")
   print(f"Region : {data['region']}")
   print(f"City : {data['city']}")
   print(f"Latitude : {data['latitude']}")
   print(f"Longtitude : {data['longitude']}")
   print(f"Autonomous System Number (ASN) : {data['asn']}")
   print(f"Organization : {data['org']}")
   print(f"Internet Service Provider (ISP) : {data['isp']}")
   print(f"Timezone : {data['timezone']}")
   print(f"Timezone Name : {data['timezone_name']}")
   print(f"Timezone Destination Offset : {data['timezone_dstOffset']}")
   print(f"Greenwich Mean Time Offset : {data['timezone_gmtOffset']}")
   print(f"Timezone GMT : {data['timezone_gmt']}")
   print(f"Currency : {data['currency']}")
   print(f"Currency Code : {data['currency_code']}")
   print(f"Currency Symbol : {data['currency_symbol']}")
   print(f"Currency Rates : {data['currency_rates']}")
   print(f"Currency Plural : {data['currency_plural']}")
   print(f"Completed Requests : {data['completed_requests']}")

#BY IP ADDRESS
def IpAddress():
   choose = input("Please enter the IP Address : ")
   print(Fore.RED+"The Ip Address Is : "+choose)
   url = "http://ipwhois.app/json/"+choose # URL Endpoint
   response = request.urlopen(url) #HTTP Request to server
   data = json.loads(response.read()) #load data from Request
   for _ in tqdm(range(100),
                 desc="Loading...",
                 ascii=False, ncols=75):
      time.sleep(0.01) #loading...
#print Data
   print("\n")
   print(f"Ip Address : {data['ip']}")
   print(f"Status : {data['success']}")
   print(f"Type : {data['type']}")
   print(f"Continent : {data['continent']}")
   print(f"Continent Code : {data['continent_code']}")
   print(f"Country : {data['country']}")
   print(f"Country Code : {data['country_code']}")
   print(f"Flag : {data['country_flag']}")
   print(f"Country Capital : {data['country_capital']}")
   print(f"Country Phone : {data['country_phone']}")
   print(f"Country Neighbours : {data['country_neighbours']}")
   print(f"Region : {data['region']}")
   print(f"City : {data['city']}")
   print(f"Latitude : {data['latitude']}")
   print(f"Longtitude : {data['longitude']}")
   print(f"Autonomous System Number (ASN) : {data['asn']}")
   print(f"Organization : {data['org']}")
   print(f"Internet Service Provider (ISP) : {data['isp']}")
   print(f"Timezone : {data['timezone']}")
   print(f"Timezone Name : {data['timezone_name']}")
   print(f"Timezone Destination Offset : {data['timezone_dstOffset']}")
   print(f"Greenwich Mean Time Offset : {data['timezone_gmtOffset']}")
   print(f"Timezone GMT : {data['timezone_gmt']}")
   print(f"Currency : {data['currency']}")
   print(f"Currency Code : {data['currency_code']}")
   print(f"Currency Symbol : {data['currency_symbol']}")
   print(f"Currency Rates : {data['currency_rates']}")
   print(f"Currency Plural : {data['currency_plural']}")
   print(f"Completed Requests : {data['completed_requests']}")

fr()
import time
import os
time.sleep(3)
#Linux  = os.system('clear')
os.system('cls') #Windows
lo()
Start()


#COPYRIGHT 2020 @ XnuversXploitXentzh
