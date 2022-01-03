import computer_vision_lib as cvl

#-----------------------------------------------------------------------------
#cvl.removeVerticalSeams("images/mann_auf_pferd.jpg", 5)
#cvl.arrayToImage(cvl.fullSobelFilter("images/lena.png"))
#cvl.removeVerticalSeams("images/mann_auf_pferd.jpg", 10)
cvl.removeHorizontalSeams("images/mann_auf_pferd.jpg", 10)