from django.core.management.base import BaseCommand
from numpy import average
import csv, os, sys
import requests
from requests.exceptions import RequestException
import glob
import pandas as pd
from consumption.models import User



class Command(BaseCommand):
    help = 'check the data in DB'
    # import CSV file and store sqlite
    # Declare a path of data.. 
  
    

   
    
    # def add_arguments(self, parser):
    #     # Postional Argument...
    #     parser.add_argument(
    #         '--user',
    #         action="store_true",
    #         help='Read user data',     
    #     )
    #     # Return Count of All Users...
    #     parser.add_argument(
    #         '--totalusers',
    #         action="store_true",
    #         help='Read Count of All Users',   
    #     )
        
    #     # Return All CSV Data of Consumption...
    #     parser.add_argument(
    #         '--consumption',
    #         nargs='?',
    #         default='', 
    #         type=str     
    #     )
    #     # Return Total Consumption...
    #     parser.add_argument(
    #         '--totalconsumption',
    #         action="store_true",
    #         help='Read Total Consumption',   
    #     )
    #     # Return Average Consumption...
    #     parser.add_argument(
    #         '--averageconsumption',
    #         action="store_true",
    #         help='Read Average Consumption',   
    #     )

    
    def handle(self, *args, **options):
        sys.stderr.write("*** start ***\n")
        # Read user_data.csv...

        for h in User.objects.all():
            print(h.user_id,"\t",end="")
            print(h.area,"\t",end="")
            print(h.tariff,"\t")

        sys.stderr.write("*** end ***\n")
        # # Option "--readuser"...
        # if options["user"]:
        #     try:
        #         csv = self.user_data
        #         next(csv)
        #         # Write To Console...
        #         #'user_data'and'count of data'
        #         for r,i in enumerate(csv):
        #             self.stdout.write(str(i)+"count:"+str(r), ending='')  
        #     except requests.exceptions.RequestException as e:
        #         print("Error: ",e)
        # elif options['totalusers']:
            
        #     csv = self.user_data
        #     next(csv)
        #     # Write To Console...
        #     # return count of total users
        #     count = len(list(csv))
        #     self.stdout.write(str(count))
                
        # elif options['consumption']:
        #     try:
        #         csv=self.get_consumption_data(options['consumption'])
        #         next(csv)
        #         # Write To Console...
        #         #'consumption data picked by user id'and'count of data'
        #         for r,i in enumerate(csv):
        #             self.stdout.write(str(i)+"count:"+str(r), ending='')  
        #     except RequestException as e:
        #         print("Error: ",e)
        # elif options['totalconsumption']:
        #     total_consumption=self.get_total_consumption()
        #     print(total_consumption)  
        #     return total_consumption
        
        # elif options['averageconsumption']:
        #     average_consumption =self.get_average_consumption()
        #     return float(average_consumption)
        
        
        
        # else:
        #     # Not Include Options...
        #     self.stdout.write("Unterminated line", ending='')

