from NENV import *


# API METHODS

# self.main_widget()        <- access to main widget


# Ports
# self.input(index)                   <- access to input data
# set_output_val(self, index, val)    <- set output data port value
# self.exec_output(index)             <- executes an execution output

# self.create_new_input(type_, label, widget_name=None, widget_pos='under', pos=-1)
# self.delete_input(index or input)
# self.create_new_output(type_, label, pos=-1)
# self.delete_output(index or output)


# Logging
# mylog = self.new_log('Example Log')
# mylog.log('I\'m alive!!')
# self.log_message('hello global!', 'global')
# self.log_message('that\'s not good', 'error')

# ------------------------------------------------------------------------------

import cv2

class %CLASS%(Node):

    new_img = Signal(object)

    def place_event(self):
        self.new_img.connect(self.main_widget().show_image)

    def update_event(self, input_called=-1):
        self.image = self.input(0)
        grayImage = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        result = cv2.adaptiveThreshold(grayImage, self.input(1), cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
        # self.main_widget().show_image(result)
        self.new_img.emit(result)
        self.set_output_val(0, result)

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass # ...


    def remove_event(self):
        pass