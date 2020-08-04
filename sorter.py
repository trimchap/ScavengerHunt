
# -------------------------------------------------------------------------------------
# sorter.py - for the Scavenger Hunt
# PROBLEM: We created a 3-day Scavenger Hunt Game with prizes for the R2 Virtual
# Convention. Participants email in their completed entry form. The entry form was 
# available on a public site. This script sorts out the entries by email to keep
# the prizes for the registered participants, also removes duplicate entries and 
# pairs the registrant's name with their email address so we can add their name to 
# the spinning prize wheel.
# SOLUTION: Open the csv file of the game entry email addresses, filters out dupes,
# filter out entries not associated with a registration email, and writes a file 
# of valid entry email addresses and names.
# ------------------------------------------------------------------------------------- 

# registered.csv = all registered conference attendees
opened_file = open('./registered.csv') 
from csv import reader
read_file = reader(opened_file)
registered_data = list(read_file)
# entries.csv = all scavenger hunt entries that were received
opened_file = open('./entries.csv') 
read_file = reader(opened_file)
entries_data = list(read_file)
# create empty lists
registered_email_list = []
registered_name_list = []
entries_email_list = []
# extract the emails and the attendee names from the registration info
for row in registered_data[1:]: # skip over the header row
    email = row[4]              # email is in row 4
    name = row[7]               # name is in row 7
    registered_email_list.append(email)
    registered_name_list.append(name)

# extract the emails and the names from the entries received
entries_email_list = []
for row in entries_data: # no header row in entries.csv
    email = row[0]
    entries_email_list.append(email)

# use sets to filter out duplicates and find the intersection of 
# attendees that both registered for the event and sent in an entry 
registered_email_set = set(registered_email_list)
entries_email_set = set(entries_email_list)
valid_entries = registered_email_set.intersection(entries_email_set)
valid_email_list = []
valid_name_list = []

# build ordered lists of valid entry email addresses and attendee names 
for email in valid_entries:
    if email in registered_email_list:
        valid_email_list.append(email)
        index = registered_email_list.index(email)
        valid_name_list.append(registered_name_list[index])
#       print(index)

# valid.csv will contain valid entries email and name
opened_file = open('/Users/trishtunney/Projects/ScavengerHunt/valid.csv') 

import csv
# write the result to valid.csv
with open('./valid.csv', mode='w') as valid_file:
    valid_writer = csv.writer(valid_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    index = 0
    for email in valid_email_list:
        valid_writer.writerow([valid_name_list[index], email])
        index+=1


