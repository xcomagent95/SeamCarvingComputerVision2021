import computer_vision_lib as cvl
import time
print("--> functions imported")

#-----------------------------------------------------------------------------
startTime = time.clock()
cvl.removeVerticalSeams("images/castle.jpg", 20)
print("--> vertical seam-removal done")
cvl.removeHorizontalSeams("images/castle.jpg", 20)
print("--> horizontal seam-removal done")
endTime = time.clock()
print("--> image processing took:: ", (endTime-startTime)/60, "min")