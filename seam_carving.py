import computer_vision_lib as cvl

#-----------------------------------------------------------------------------
#cvl.arrayToImage(cvl.fullSobelFilter("images/delphin.jpg"))
#cvl.removeVerticalSeam("images/mann_auf_pferd.jpg", cvl.findVerticalSeam("images/mann_auf_pferd.jpg"))

cvl.removeVerticalSeams("images/mann_auf_pferd.jpg", 1)

#cvl.arrayToImage(cvl.sobelHorizontalFilter("images/mann_auf_pferd.jpg"))