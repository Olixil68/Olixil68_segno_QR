#############################################################
# Current code operated on IDLE's "Run Module"              #
# Only URL & FILE NAME variables should be modified         #
#                                                           #
# name.save(..., scale) defines pixels per cell             #
# name.save(..., light) defines background                  #
#                                                           #
# Code does not support IDLE's "RUN...Customized"           #
# "RUN...Customized" enables IDLE Shell to accept sys.argv[]#
#############################################################

# QR Code Library
import segno
    
# Edit Variables
url = 'temp_url'
file_name = 'temp_file_name.png'

# Create QR
qr_code = segno.make(url)

# Save QR
qr_code.save(file_name, scale=5, light=None)

# Console Print Statement
print("QR Code has been saved to Python Files")
