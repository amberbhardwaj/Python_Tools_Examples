"""
Created on Mon Mar 01 2021

@author: Amber 
@description: 
This source code took from multiple online sources.
and used to parse the video frames and display
"""
import CV2
import QRTool

# This function is used to extarct the frames from the live video
def ExtractFramesFromVideo (path):
    # Open the camera and capture live video
    vObject = cv2.VideoCapture(path)
    # Check if camera opened successfully
    if (vObject.isOpened() == False): 
        print("Error opening video stream or file")
    count = 0
    success = True
    
    numberOfFrameToBeCaptured = 11
    while success:
        success, image = vObject.read()

     #  print("Success = ", success)
     #  if success == True:
     #      gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
     #      cv2.imshow('image', gray)
     #      if cv2.waitKey(25) & 0xFF == ord('q'):
     #          break
        cv2.imwrite("FrameStorageDir/frame%d.png" % count, image)
        if count == numberOfFrameToBeCaptured:
            break
        p = " "
        scanQrData = qrtools.QR()
        data = 'frame'+ str(count) + '.png'
        scanQrData.decode ("FrameStorageDir//"+data)
		print scanQrData.data
        count +=1
         
    vObject.release()
    # Closes all the frames
    cv2.destroyAllWindows()
    
'''
# Utility function to know Frame captured per second
'''   
def KnowFpsCapturedFromVideo():
    #Start Block: 
    #Function to get the current frame/second (only for video not for cam)
    video = cv2.VideoCapture(0)
    #video.set(cv2.cv.CV_CAP_PROP_FPS , 100)
    # Find OpenCV version
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
     
    # With webcam get(CV_CAP_PROP_FPS) does not work.
    # Let's see for ourselves.
     
    if int(major_ver)  < 3 :
        fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
        print "Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps)
    else :
        fps = video.get(cv2.CAP_PROP_FPS)
        print "Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps)
    video.release()
    #End Block
    
