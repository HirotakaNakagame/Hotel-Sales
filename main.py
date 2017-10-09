
import CreateEvent
import ModifyWorkersList
import webbrowser
import ViewCompanyLists
import ModifyCompanyList

"""
This was written because of what Mary said.
At her hotel, event managers talk with customers to decide details but they are having hard time splitting work equally.
They want to split work/customers equally so that event managers have 
1. equal amount of work in the current week.
2. equal amount of work in the week of event
"""


print "Dunder Mifflin Paper Company Event Manager Scheduling App"

while True:
	print "\n\nChoose an option. Hit Enter after you choose."
	print "\t1: Create An Event"
	print "\t2: Modify Workers List"
	print "\t3: View Calendar"
	print "\t4: Modify Company Lists"
	option = raw_input("\t:>")
	option = option.upper()
	
	ChoosingDirector = True
	
	if option == "1":
		CreateEvent.func()	
	elif option == "2":
		ModifyWorkersList.Modify()
	elif option == "3":
		webbrowser.open('https://calendar.google.com/calendar/render#main_7%7Cmonth')
	elif option == "4":
		ModifyCompanyList.func()
		#ViewCompanyLists.View_Company()
	else:
		print "Invalid Entry"
		

