# -*- coding:utf-8 -*-


def deleteEroorString (old_file):
    
    new_file="./20130814/deleted/"+old_file
    
    ptn1 = ''
    ptn1 += '{\n'
    ptn1 += '  "error": {\n'
    ptn1 += '    "id": "EXCEEDED_REQS", \n'
    ptn1 += '    "text": "Exceeded max daily requests"\n'
    ptn1 += '  }\n'
    ptn1 += '}\n'
    
    #print "ptn1 : " + ptn1
    
    ptn2 = ''
    ptn2 += '{\n'
    ptn2 += '  "error": {\n'
    ptn2 += '    "description": "The maximum number of accessible results is 1000",\n' 
    ptn2 += '    "field": "offset", \n'
    ptn2 += '    "id": "INVALID_PARAMETER", \n'
    ptn2 += '    "text": "One or more parameters are invalid in request"\n'
    ptn2 += '  }\n'
    ptn2 += '}\n'
    
    #print "ptn2 : " + ptn2
    
    f = open("./20130814/"+old_file)
    old_data = f.read()
    new_data = old_data.replace(ptn1, '')
    new_data = new_data.replace(ptn2, '')
    f.close()
    
    f = open(new_file, 'w')
    f.write(new_data) 
    
i = 0
while i<=9311: 
    file = "restaurant_ca_"+str(i)+".json"
    #file = "food_ca_"+str(i)+".json"
    print file   
    deleteEroorString (file)
    i+=1
