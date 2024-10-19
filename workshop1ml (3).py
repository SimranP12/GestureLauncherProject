#!/usr/bin/env python
# coding: utf-8

# In[ ]:


5+2


# In[ ]:


print("hello")


# In[ ]:


x=5


# In[ ]:


print("x")


# In[ ]:


x = 6


# In[ ]:


print(x)


# In[ ]:


y=[5,10,20,30]


# In[ ]:


print(y)


# In[ ]:


system("chrome")


# In[ ]:


system(date /t)


# In[ ]:


import os


# In[ ]:


os.system("chrome")


# In[ ]:


names=["shrish", "simran", "khushi"]


# In[ ]:


names


# In[ ]:


names[0:2]


# In[ ]:


names[0:3]


# In[ ]:


names[1:3]


# In[ ]:


db=["shrish", 111, "ok"],["sim", 222, "good"], ["khush",333,"okie"]


# In[ ]:


table=["shrish", 111, "ok"],["sim", 222, "good"], ["khush",333,"okie"]


# In[ ]:


table


# In[ ]:


db=["shrish", 111, 'ok'],["sim", 222, 'good'], ['khush',333,'okie']


# In[ ]:


db


# In[ ]:


db[0]


# In[ ]:


db[2][1]


# In[ ]:


db[:2][1]


# In[ ]:


db[1][:1]


# In[ ]:





# In[ ]:


db[0:1]


# In[ ]:


db[][0:1]


# In[ ]:


import numpy


# In[ ]:


numpy.array(db)


# In[ ]:


b=numpy.array(db)


# In[ ]:


b[:,2]


# In[ ]:


b[2]


# In[ ]:


b[:1,2]


# In[ ]:


b[1:3]


# In[ ]:


b[1:3, 1:3]


# In[ ]:


import cv2


# In[ ]:


import ec2


# In[ ]:


pip install open cv


# In[ ]:


import cv2


# In[ ]:


cap=cv2.VideoCapture(0)


# In[ ]:


status, photo=cap.read()


# In[ ]:


status


# In[ ]:


cv2.imwrite("cat.jpeg",photo)


# In[ ]:


photo


# In[ ]:


photo.shape


# In[ ]:


crop1=photo[200:360, 120:450]


# In[ ]:


cv2.imwrite("crop.jpeg",crop1)


# In[ ]:


cv2.imshow("myphoto",photo)
cv2.waitKey(5000)
cv2.destroyAllWindows()


# In[ ]:


while True :
    status , photo = cap.read()
    cv2.imshow("myphoto", photo)
    print(cv2.waitKey() )
    cv2.destroyAllWindows()
    
    
    status,photo=cap.read()
    
    cv2.imshow("myphoto",photo)
    print( cv2.waitKey() )
    cv2.destroyAllWindows()


# In[37]:


cap.release()


# In[40]:


allOS=[]


# In[43]:





# In[35]:


import cv2
cap=cv2.VideoCapture(0)


# In[36]:


from cvzone.HandTrackingModule import HandDetector
detector = HandDetector(maxHands=1)
status, photo=cap.read()
hand=detector.findHands(photo,draw=False)
if hand:
    lmlist=hand[0]
    totalFinger=detector.fingersUp(lmlist)
    if totalFinger==[0,1,1,0,0] :
        print("2 and 3 finger is up")
        myOSLaunch()
    elif totalFinger==[0,1,0,0,0] :
         print("1 finger up, index finger")
             osTerminate()
    else:
        print("do it with attitude")


# In[ ]:


cap.release()


# In[44]:


import boto3


# In[45]:


ec2=boto3.resource("ec2")


# In[ ]:


t2.micro 
ami-0a2acf24c0d86e927
def myOSLaunch():
instances=ec2.create_instances(
ImageId="ami-0a2acf24c0d86e927",
MinCount=1,
Maxcount=1,
Instancetype="t2.micro",
SecurityGroupsIds="sg-0042ea78f2f411484")
myid=instances[0].id
allOS.append(myid)
print("total OS:",len(allOS))
print(myid)


# In[ ]:


myOSLaunch()


# In[ ]:


def osTerminate();
    osdelete=allOS.pop()


    osdelete = allOS.pop()
    ec2.instances.filter(InstanceId='').terminate()


# In[ ]:





# In[ ]:




