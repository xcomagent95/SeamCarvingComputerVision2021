import computer_vision_lib as cvl
print("--> functions imported")

#-----------------------------------------------------------------------------
print("--> running...")
cvl.removeVerticalSeams("images/castle.jpg", 20)
print("--> vertical seam-removal done")
cvl.removeHorizontalSeams("images/castle.jpg", 20)
print("--> horizontal seam-removal done")
