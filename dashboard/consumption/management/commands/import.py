from django.core.management.base import BaseCommand
from numpy import average
import csv, os
import requests
from requests.exceptions import RequestException
import glob
import pandas as pd



class Command(BaseCommand):
    def hello(self):
        return "hello"
    help = 'import data'
    
    # Declare a path of data.. 
    path=os.chdir('..')
    current_path = os.getcwd()
    user_path = current_path + "/data/"
    consumption_path =current_path +"/data/consumption/"
    consumption_files = glob.glob(consumption_path+"*")
    count_consumption_files = len(consumption_files)
    
    # Read user_data.csv...
    user_data_csv = open(user_path+'user_data.csv',"r")
    user_data = csv.reader(user_data_csv)
    
    # Function To Get Consumption Data...
    # You Can Return Consumption Data(list) by User_ID
    def get_consumption_data(self,user_id):
        consumption_csv = open(self.consumption_path+user_id+".csv")
        consumption_data = csv.reader(consumption_csv)
        return consumption_data
    
    # Get Total Consumption...
    def get_total_consumption(self):
        total_consumption = 0
        for file in self.consumption_files:
            df=pd.read_csv(file,usecols=[1],header=0)
            sum=df['consumption'].sum()
            total_consumption += int(sum)
        return total_consumption
 
    # Get Average Consumption...
    def get_average_consumption(self):
        total_consumption = 0
        count_files = self.count_consumption_files
        for file in self.consumption_files:
            df=pd.read_csv(file,usecols=[1],header=0)
            sum=df['consumption'].sum()
            total_consumption += int(sum)
        
        return total_consumption/count_files
            

    
    def add_arguments(self, parser):
        # Postional Argument...
        parser.add_argument(
            '--user',
            action="store_true",
            help='Read user data',     
        )
        # Return Count of All Users...
        parser.add_argument(
            '--totalusers',
            action="store_true",
            help='Read Count of All Users',   
        )
        
        # Return All CSV Data of Consumption...
        parser.add_argument(
            '--consumption',
            nargs='?',
            default='', 
            type=str     
        )
        # Return Total Consumption...
        parser.add_argument(
            '--totalconsumption',
            action="store_true",
            help='Read Total Consumption',   
        )
        # Return Average Consumption...
        parser.add_argument(
            '--averageconsumption',
            action="store_true",
            help='Read Average Consumption',   
        )

    
    def handle(self, *args, **options):
        # Option "--readuser"...
        if options["user"]:
            try:
                csv = self.user_data
                next(csv)
                # Write To Console...
                #'user_data'and'count of data'
                for r,i in enumerate(csv):
                    self.stdout.write(str(i)+"count:"+str(r), ending='')  
            except requests.exceptions.RequestException as e:
                print("Error: ",e)
        elif options['totalusers']:
            
            csv = self.user_data
            next(csv)
            # Write To Console...
            # return count of total users
            count = len(list(csv))
            self.stdout.write(str(count))
                
        elif options['consumption']:
            try:
                csv=self.get_consumption_data(options['consumption'])
                next(csv)
                # Write To Console...
                #'consumption data picked by user id'and'count of data'
                for r,i in enumerate(csv):
                    self.stdout.write(str(i)+"count:"+str(r), ending='')  
            except RequestException as e:
                print("Error: ",e)
        elif options['totalconsumption']:
            total_consumption=self.get_total_consumption()
            print(total_consumption)  
        
        elif options['averageconsumption']:
            average_consumption =self.get_average_consumption()
            print(average_consumption)
        
        
        
        else:
            # Not Include Options...
            self.stdout.write("Unterminated line", ending='')

