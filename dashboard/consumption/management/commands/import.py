from django.core.management.base import BaseCommand
from numpy import average
import csv, os, sys
import requests
from requests.exceptions import RequestException
import glob
import pandas as pd
from consumption.models import User,Consumption
from datetime import datetime as dt
from django.utils.timezone import make_aware





class Command(BaseCommand):
    help = 'import data'
    # import CSV file and store sqlite
    # Declare a path of data.. 
    path=os.chdir('..')
    current_path = os.getcwd()
    # Path of User CSV files...
    user_path = current_path + "/data/"
    
    # Path of Consumption CSV files...
    consumption_path =current_path +"/data/consumption/"
    consumption_files = glob.glob(consumption_path+"*")
    count_consumption_files = len(consumption_files)
    
    
    def add_arguments(self, parser):
        # Postional Argument...
        # Argument of "--user" ...
        parser.add_argument(
            '--user',
            action="store_true",
            help='Read user data',     
        )
        # Argument of "--consumption"...
        parser.add_argument(
            '--consumption',
            
            action="store_true",
            help='Read consumption data',     
        )


    
    def handle(self, *args, **options):
        # Method of option --user...
        if options["user"]:
            sys.stderr.write("*** start ***\n")
            # Read user_data.csv...
            user_data_csv = open(self.user_path+'user_data.csv',"r")
            user_data = csv.reader(user_data_csv)
            next(user_data)
            # Store Data from CSV ...
            for u in user_data:
                print(u)
                hh = User()
                hh.user_id = u[0]
                hh.area = u[1]
                hh.tariff = u[2]
                hh.save()
            sys.stderr.write("*** end ***\n")
            user_data_csv.close()  
            
        elif options["consumption"]:
            # Read consumption csv files...
            sys.stderr.write("*** start ***\n")
            # Store Data from CSV ...
            for c in self.consumption_files:
                print(c)
                csv_file = open(c,"r")
                consumption_data = csv.reader(csv_file) 
                
                next(consumption_data)
                # Get id from File name
                user_id=os.path.splitext(os.path.basename(c))[0]
                for data in consumption_data:
                    print(data)
                    hh = Consumption()
                    hh.user_id = int(user_id)
                    datetime_str =data[0]
                    datetime =dt.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
                    hh.datetime = make_aware(datetime)
                    hh.consumption = data[1]
                    hh.save()
                print("next")
                csv_file.close()  
            sys.stderr.write("*** end ***\n")
            
            
        
        else:
            # Not Include Options...
            self.stdout.write("Unterminated line", ending='')
        