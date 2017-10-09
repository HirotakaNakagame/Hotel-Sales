
EventManagers = []
Directors = []

def func():
	d = open("Directors.txt", 'r')
	d2 = d.readline().split()
	for j in range(len(d2)):
		Directors.append(d2[j])
	d.close()
	e = open("EventManagers.txt", "r")
	e2 = e.readline().split()
	for j in range(len(e2)):
		EventManagers.append(e2[j])
	e.close()
	
	print "We are pround of our team!\t\t"
	print "List of directors: %s" % (Directors)
	print "List of eventmanagers: %s" % (EventManagers)


func()
















