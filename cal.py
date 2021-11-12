import pandas as pd
import sys
import argparse

class cal:
    
    def __init__(self,filename="null"):
        ''' Initializes a cal object with a daily timetable dictionary self.schedule,
        which we use to initialize a cal dataframe self.cal'''
        
        self.filename = filename
        if filename != "null":
            try:
                #try to read csv from filename
                self.cal = pd.read_csv(self.filename)
            except:
                print("can't read cal from filename {}".format(filename))
        
        #make empty cal.
        self.schedule = {
            "08:00": ["","","","","","",""],
            "09:00": ["","","","","","",""],
            "10:00": ["","","","","","",""],
            "11:00": ["","","","","","",""],
            "12:00": ["","","","","","",""],
            "13:00": ["","","","","","",""],
            "14:00": ["","","","","","",""],
            "15:00": ["","","","","","",""],
            "16:00": ["","","","","","",""],
            "17:00": ["","","","","","",""],
        }
        self.cal = pd.DataFrame(self.schedule, 
            index = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
        
    def get_cal(self):
        ''' Getter method to return the self.cal attribute containing our
        schedule for this week.'''
        return self.cal

    def set_event(self,event,day,time):
        '''Takes as input the event we want to enter to our calendar, 
        the day we want this event to happen on, and the time.
        We then insert this into the calendar.'''
        pass

    def read_cal(self,file_name):
        '''reads calendar stored in csv file
        and updates our entries to reflect these values'''
        pass

    def store_cal(self,file_name):
        '''stores our calendar in a csv file called
        file_name'''
        pass

if __name__=="__main__":
    """read calendar file name in from command line argument
       arguments: 
       update / delete at specific time
           -t 09:00
       update / delete at specific day
           -d Monday
       update event at specific time and day.
           -u "event_str" -t "09:00" -d "Monday"
       delete event at specific time
           -del -t "08:00" -d "Tuesday"
       print out calendar
           -p 
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--print_cal',
                    action='store_true',
                    help='Print calender state'
                    )
    parser.add_argument('-f', '--filename',
                    help='Usage: -f mycal.csv',
                    type=str,
                    )
    parser.add_argument('-u', '--update', 
                    help='Usage: -u event_str -t time -d day',
                    type=str,
                    )
    parser.add_argument('-del', '--delete', 
                    help='Usage: -delete -t time -d day',
                    type=str,
                    )
    parser.add_argument('-t', '--time',
                    help='Usage: -t 09:00 (24 hour time in 1 hr increments from 08:00-17:00',
                    choices=['08:00','09:00','10:00',
                    '11:00','12:00','13:00','14:00',
                    '15:00','16:00','17:00'],
                    type=str,
                    )
    parser.add_argument('-d', '--day',
                    help='Usage: -d Monday',
                    choices=['Monday', 'Tuesday',
                    'Wednesday', 'Thursday', 'Friday', 
                    'Saturday', 'Sunday'],
                    type=str,
                    )
    args = parser.parse_args()
    
    #initialize cal object and call it...
    mycal = cal(args.filename)
    if args.print_cal:
        print(mycal.get_cal())
