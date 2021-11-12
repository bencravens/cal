# cal
Command line weekly planner.

Usage: 
- Must always specify the filename of the calendar csv file with the -f flag. 
- If the cal file doesn't exist, it will be made with that name
- You can add tasks to a specific time with the -u flag. (update)
- You can delete tasks with the -del flag
- When adding or deleting tasks, you must use the -t flag (time) and the -d flag (day)
- Time flag arguments must be in a 24 hour format from 8 am to 5pm in one hour increments. 08:00 to 17:00
- Day flag arguments must be the full day, caplitalized, i.e Monday to Sunday
- You can print the cal with the -p flag.

Examples:
Update an entry for file test.csv, print the calendar.
```Bash 
python3 cal.py -u "Program computer" -t "09:00" -d "Monday" -f test.csv -p
```
Delete that entry
```Bash
python3 cal.py -del -t "09:00" -d "Monday" -f test.csv -p
```
