layout = [[sg.Text('         IoT-ভিত্তিক ফসলের সুপারিশ সিস্টেম', font=("Helvetica", 30), text_color = 'blue')],                                                    # Defining the layout of the Graphical User Interface. It consist of some text, Buttons, and blanks to take Input.
         [sg.Text('অনুগ্রহ করে নিম্নলিখিত বিবরণ লিখুন :-', font=("Helvetica", 20))],                                                                                          # We have defined the text size, font type, font size, blank size, colour of the text in the GUI.
         [sg.Text('মাটিতে নাইট্রোজেনের অনুপাত                :', font=("Helvetica", 20)), sg.InputText(font=("Helvetica",20), size = (20,1),default_text=dist )],
         [sg.Text('মাটিতে ফসফরাসের অনুপাত                  :', font=("Helvetica", 20)), sg.Input(font=("Helvetica", 20),size = (20,1))],
         [sg.Text('মাটিতে পটাসিয়ামের অনুপাত                  :', font=("Helvetica", 20)), sg.Input(font=("Helvetica", 20),size = (20,1))],
         [sg.Text('মাঠের চারপাশে গড় তাপমাত্রার মান            :', font=("Helvetica", 20)), sg.Input(font=("Helvetica", 20),size = (20,1)), sg.Text('*C', font=("Helvetica", 20))],
         [sg.Text('মাঠের চারপাশে আর্দ্রতার গড় শতাংশ           :', font=("Helvetica", 20)), sg.Input(font=("Helvetica", 20),size = (20,1)), sg.Text('%', font=("Helvetica", 20))],
         [sg.Text('মাটির PH মান লিখুন                     :', font=("Helvetica", 20)), sg.Input(font=("Helvetica", 20),size = (20,1))],
         [sg.Text('মাঠের চারপাশে বৃষ্টিপাতের গড় পরিমাণ লিখুন    :', font=("Helvetica", 20) ), sg.Input(font=("Helvetica", 20),size = (20,1)),sg.Text('mm', font=("Helvetica", 20))],
         [sg.Text(size=(50,1),font=("Helvetica",20) , text_color = 'yellow', key='-OUTPUT1-' )],
         [sg.Button('Submit', font=("Helvetica", 20)),sg.Button('Quit', font=("Helvetica", 20))] ]
window = sg.Window('IoT-based Crop Recommendation System using Machine Learning for Precision Agriculture', layout)
