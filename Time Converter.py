#Time Converter

#user input
time_raw = int(input("Enter time to be converted (in secs) : "))

#Convert to hours
hour = time_raw//(60*60)

#Convert to minutes
minutes = ((time_raw - (hour*60)*60)//60)

#Seconds left
seconds = time_raw-((hour*60*60)+(minutes*60))

#output
print ("Time : ",hour,"hr, ",minutes,"min, ",seconds,"sec ")

