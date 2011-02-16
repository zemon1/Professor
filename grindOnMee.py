#Jeff Haak
import re
import urllib

def ratings(url):
    data = urllib.urlopen(url)
    html = data.readlines()
    data.close()
    result = []
    topRatings = []
    date = []
    name = []
    ratings = []
    commentsText = []  
    
    matcher = re.compile('<strong>')
    tTipMatcher = re.compile('<li class="tTip"')
    dateMatcher = re.compile('<div class="date">')
    classMatcher = re.compile('<div class="class">')
    ratingsMatcher = re.compile('<p class="r')
    commentMatcher = re.compile('<p class="commentText')
    
    i = 0
    for lines in html:
        
        if matcher.search(lines):
            if tTipMatcher.search(lines):
                lines = lines.split('<strong>')
                type = lines[0].split('id="')
                type = type[1].split('" title="')                                             
                rate = lines[1].split('</strong>')
                topRatings.append([type[0], rate[0]])
                i += 1
                if i == 3:
                    result.append(topRatings)
        if dateMatcher.search(str(lines)):
            lines = lines.strip()
            lines = lines.split('class="date">')
            lines = lines[1].split('</div')
            date = ["Date Posted", lines[0]]
            ratings.append(date)
        if classMatcher.search(str(lines)):
            lines = lines.strip()
            lines = lines.split('class="class">')
            lines = lines[1].split('</div')
            classes = ["Class", lines[0]]
            ratings.append(classes)
        if ratingsMatcher.search(str(lines)):
            lines = lines.split('</strong><span>')
            type = lines[0].split('<strong>')
            type = type[1]
            grade = lines[1].split('</strong>')
            grade = grade[0].split('</span')
            grade = grade[0]
            ratings.append([type, grade])
        if commentMatcher.search(str(lines)):
            lines = lines.strip()
            lines = lines.split('<p class="commentText">')
            lines = lines[1].split('</p>') 
            lines = lines[0]
            ratings.append(["Comments:", lines])
            result.append(ratings)
            ratings = []

    return result
    
def makeList():
    urls = []
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in alph:
        newURL = "http://www.ratemyprofessors.com/SelectTeacher.jsp?the_dept=All&sid=807&orderby=TLName&letter=" + str(i)
        urls.append(newURL)
    return urls

def teachers(url):
    teachers = []
    data = urllib.urlopen(url)
    html = data.readlines()
    data.close()
    
    matcher = re.compile('href="ShowRatings.jsp')
   # matcher = re.compile('href="ShowRatings.jsp')
    
    for lines in html:
        if matcher.search(lines):
            lines = lines.strip()
            lines = lines.split('href="')
            lines = lines[1].split('">')
            url = lines[0]
            lines = lines[1].split('</a>')
            #print url
            teach = lines[0].lower()
            teach = teach.split(', ')
            teach = teach[1] + " " + teach[0]
            teachers.append([teach, url])
    return teachers

def getNames():
    theList = []
    prompt1 = "What is this teacher's name?\n"
    sentinel = 'done'
    sentinel1 = 'Done'
    
    print "Enter the name of the teacher you are looking for in the format: Jeff Haak\nType 'Done' when you are finished.\n"  
    while True:
        name = raw_input(prompt1)
        if name == '':
            print("Please enter a name")
            name = raw_input(prompt1)
            if name.strip() == sentinel or name.strip() == sentinel1:
                return theList
        elif name.strip() == sentinel or name.strip() == sentinel1:
            return theList
        else:
            if len(name.split()) < 2:
                print("Please enter a First and Last name")
                name = raw_input(prompt1)
            name = name.lower()
            name = name.strip()
            theList.append(name)                     
    return theList

def printResult(content):
        for i in range(len(content)):
            if content[i][1] != []:
                name = content[i][0]
                name = name.split()
                realName = name[1][0].upper() + name[1][1:] + ", " + name[0][0].upper() + name[0][1:]
                line = "-----------------------------------------------------------------------------------"
                tops = ""
                for j in content[i][1][0]:
                    score = j[0][0].upper() + j[0][1:] + ": " + j[1] + " | "
                    tops = tops + score
                
                
                
                
                print line
                print realName + "\n"
                print tops + "\n"
                
                count = 0
                for j in content[i][1][1:]:
                    if count == 0:
                        if j[0] == "Date" or j[0] == "Class":
                            j.pop(0)
                    count += 1
                             
                    print j[0][0] + ": " + j[0][1] + " | " + j[1][0] + ": " + j[1][1][0].upper()+ j[1][1][1:].lower()            
                    print j[2][0] + ": " + j[2][1]
                    print j[3][0] + ": " + j[3][1]
                    print j[4][0] + ": " + j[4][1]
                    print j[5][0] + ": " + j[5][1]
                    print j[6][0] + " " + j[6][1] + "\n"
                    
                print content[i][2]
                print line + "\n"
            else:
                name = content[i][0]
                name = name.split()
                realName = name[1][0].upper() + name[1][1:] + ", " + name[0][0].upper() + name[0][1:]
                line = "-----------------------------------------------------------------------------------"
                print line
                print realName + "\n" 
                print "Yo Playa, sorry but I don't know who this G is... My B bro."
                url = content[i][2]
                print url
                print line + "\n"

def main():
    names = getNames()
    urls = makeList()
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mainUrl = "http://www.ratemyprofessors.com/"
    all = []
    temp = []
    found = False
    
    for i in names:
        letter = i.split()
        letter = letter[1][0]
        url = "http://www.ratemyprofessors.com/SelectTeacher.jsp?the_dept=All&sid=807&orderby=TLName&letter=" + letter.upper()
        results = teachers(url)
        for j in results:
            if i == j[0]:
                teachUrl = mainUrl + j[1]
                found = True
                temp = [i, ratings(teachUrl), teachUrl, found]
                all.append(temp)
                
        if found == False:
            all.append([i, [], "", found])
        found = False
            
            
    printResult(all)
    print "This Program was created by Jeff Haak on 1/30/2011.  I hope you enjoy it."
        
    

main()


















