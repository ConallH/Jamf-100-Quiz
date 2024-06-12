from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
import random

class QuizApp(App):
    def build(self):
        self.questions = [
            {
        'question': "iOS apps exist in a self-contained environment called an App Sandbox.",
        'answers': ['A. True', 'B. False'],
        'correct': 'A'
        },
        {
            'question': "Swiping down from the top right on an iOS device (iPhone X and later) will access which feature?",
            'answers': ['A. Notification Center', 'B. Control Center', 'C. Tips', 'D. Search'],
            'correct': 'B'
        },
        {
            'question': "An Apple ID is required to complete iOS Setup Assistant.",
            'answers': ['A. True', 'B. False'],
            'correct': 'B'
        },
        {
            'question': "Along with apps, which feature can be added to the iOS Home Screen that gives quick access to additional information such as World Clock and Batteries?",
            'answers': ['A. Complications', 'B. Widgets', 'C. Quick Look', 'D. Notification Center'],
            'correct': 'B'
        },
        {
            'question': "To delete an app from an iOS device:",
            'answers': ['A. Touch and hold the app until a menu pops up > tap Remove App', 'B. Navigate to Settings > General > About', 'C. Use the App Store to uninstall the app', 'D. Apps cannot be deleted from iOS devices'],
            'correct': 'A'
        },
            {
            'question': "Under which section of the Settings > General would a user be able to update the name of their iOS device?",
            'answers': ['A. Legal & Regulatory', 'B. Date & Time', 'C. About', 'D. Erase All Content and Settings'],
            'correct': 'C'
        },
        {
            'question': "Some iOS apps allow users to purchase additional features within the app after download. What is noted next to the Get button to inform users of this?",
            'answers': ['A. Purchase More Content', 'B. Additional Downloads', 'C. More Content Available', 'D. In-App Purchases'],
            'correct': 'D'
        },
        {
            'question': "A user can opt out of sending app analytics and crash data to app developers during iOS Setup Assistant.",
            'answers': ['A. True', 'B. False'],
            'correct': 'A'
        },
        {
            'question': "Property list files use which file extension?",
            'answers': ['A. .prop', 'B. .propli', 'C. .plist', 'D. .prolist'],
            'correct': 'C'
        },
        {
            'question': "Which command can be used to reveal the contents of a macOS directory in the command-line interface?",
            'answers': ['A. ls', 'B. cd', 'C. mkdir', 'D. cp'],
            'correct': 'A'
        },
        {
            'question': "Which character represents the current user's home directory in the command-line interface?",
            'answers': ['A. /', 'B. *', 'C. ~', 'D. #'],
            'correct': 'C'
        },
        {
            'question': "An internet connection is required to set up a Mac.",
            'answers': ['A. True', 'B. False'],
            'correct': 'B'
        },
        {
            'question': "Which of the following is contained in the macOS Apple menu?",
            'answers': ['A. Finder Preferences', 'B. System Preferences', 'C. Connect to Server', 'D. Time Machine'],
            'correct': 'B'
        },
        {
            'question': "Which keyboard shortcut can be used to access Spotlight on macOS?",
            'answers': ['A. Shift-Command-4', 'B. Command-S', 'C. Option-Space bar', 'D. Command-Space bar'],
            'correct': 'D'
        },
        {
            'question': "In order for a macOS app to run and pass Apple's Gatekeeper settings, it must be submitted to Apple for notarization.",
            'answers': ['A. True', 'B. False'],
            'correct': 'A'
        },
        {
            'question': "Which macOS feature can be used to quickly search the web, open applications, and even do quick calculations?",
            'answers': ['A. Spotlight', 'B. Quick Look', 'C. Control Center', 'D. Notification Center'],
            'correct': 'A'
        },
        {
            'question': "Which character is used to instruct a command-line interpreter to ignore a line in a script, and is often used to provide comments?",
            'answers': ['A. /', 'B. #', 'C. &', 'D. ;'],
            'correct': 'B'
        },
        {
            'question': "Which two items cannot be removed from the Dock in macOS?",
            'answers': ['A. The Finder and Trash', 'B. System Preferences and Calendar', 'C. News and Contacts', 'D. Pages and Mail'],
            'correct': 'A'
        },
        {
            'question': "In the command-line interface, which command can be used to display the manual page for other commands?",
            'answers': ['A. help', 'B. ls', 'C. man', 'D. cd'],
            'correct': 'C'
        },
        {
            'question': "Which menu in the macOS menu bar contains commonly used tasks like Cut, Copy, and Paste?",
            'answers': ['A. File menu', 'B. Apple menu', 'C. Edit menu', 'D. Window menu'],
            'correct': 'C'
        },
            {
            'question': "Where can information on macOS version, processor type, and a computer's serial number be found in About This Mac?",
            'answers': ['A. Displays', 'B. Storage', 'C. Support', 'D. Overview'],
            'correct': 'D'
        },
        {
            'question': "System settings for Location Services, Analytics, and Screen Time can be reconfigured in System Preferences after completing Setup Assistant.",
            'answers': ['A. True', 'B. False'],
            'correct': 'A'
        },
        {
            'question': "Which macOS feature allows users to navigate the file system to view the contents of their computer, including files, apps, and storage devices?",
            'answers': ['A. Finder', 'B. Explorer', 'C. Terminal', 'D. Pages'],
            'correct': 'A'
        },
        {
            'question': "Along with Computers and Devices, what is the third tab in the top left of the Jamf Pro interface?",
            'answers': ['A. Security', 'B. Enrollment', 'C. Users', 'D. Settings'],
            'correct': 'C'
        },
        {
            'question': "What can be created within Apple Business Manager and Apple School Manager to allow user-based app and book deployment or utilize Shared iPad?",
            'answers': ['A. Jamf Pro Users', 'B. School and Business IDs', 'C. Administrator Accounts', 'D. Managed Apple IDs'],
            'correct': 'D'
        },
        {
            'question': "By default, user-initiated enrollment is enabled for computers.",
            'answers': ['A. True', 'B. False'],
            'correct': 'B'
        },
        {
            'question': "Which Jamf Pro user account privilege set will grant permissions to create, read, update, and delete content in Jamf Pro?",
            'answers': ['A. Administrator', 'B. Read-Only', 'C. Auditor', 'D. None'],
            'correct': 'A'
        },
        {
            'question': "Mobile device management (MDM) allows organizations to wirelessly configure, update, and deploy content to devices.",
            'answers': ['A. True', 'B. False'],
            'correct': 'A'
        },
        {
            'question': "A push certificate is required to facilitate communication between Apple Push Notification service and a mobile device management platform.",
            'answers': ['A. True', 'B. False'],
            'correct': 'A'
        },
        {
            'question': "What is the name of the payload within a computer PreStage enrollment that determines what type of user account is created during Setup Assistant?",
            'answers': ['A. User and Location', 'B. Configuration Profiles', 'C. Account Settings', 'D. Certificates'],
            'correct': 'C'
        },
        {
            'question': "In Jamf Pro, custom messaging and end-user license agreements can be added to the user-initiated enrollment screens.",
            'answers': ['A. True', 'B. False'],
            'correct': 'A'
        },
        {
            'question': "Computers can receive remote commands, configuration profiles, and app deployments from Jamf Pro if they're unable to communicate with APNs.",
            'answers': ['A. True', 'B. False'],
            'correct': 'B'
        },
        {
            'question': "Which section within Jamf Pro might show important information about the state of the Jamf Pro server, such as a push certificate is expiring soon?",
            'answers': ['A. Status', 'B. Notifications', 'C. Warnings', 'D. Updates'],
            'correct': 'B'
        },
        {
            'question': "Simple device inventory search results can be exported from Jamf Pro in the following file formats:",
            'answers': ['A. .txt,.pdf, or .pages', 'B. .docx, .txt, or .rtf', 'C. .psd, .pdf, or .doc', 'D. .tsv, .csv, or XML'],
            'correct': 'D'
        },
        {
            'question': "Static device group membership is variable and updates automatically based on device eligibility.",
            'answers': ['A. True', 'B. False'],
            'correct': 'B'
        },
            {
            'question': "In an advanced mobile device search, which operator can be used to find all matches that contain the specified value, not just exact matches?",
            'answers': ['A. is', 'B. is not', 'C. like', 'D. not like'],
            'correct': 'C'
        },
        {
            'question': "Creating separate mobile device configuration profiles is preferred over bundling many payloads into a single configuration profile.",
            'answers': ['A. True', 'B. False'],
            'correct': 'A'
        },
        {
            'question': "The following character can be used as a wildcard in a simple mobile device search:",
            'answers': ['A. !', 'B. ~', 'C. #', 'D. *'],
            'correct': 'D'
        },
        {
            'question': "Which intervals are available for email reporting in saved advanced mobile device searches?",
            'answers': ['A. Hourly, Daily, or Weekly', 'B. Specific days, Daily, Weekly, or Monthly', 'C. Daily, Monthly, or Yearly', 'D. Hourly, Weekly, or Yearly'],
            'correct': 'B'
        },
        {
            'question': "Where can a Jamf Pro admin go to change the inventory attributes listed when completing a simple mobile device search?",
            'answers': ['A. Settings > Global Management > Categories', 'B. Settings > Device Management > Inventory Display', 'C. Settings > Self Service > iOS', 'D. Settings > Jamf Pro Information > Jamf Pro Summary'],
            'correct': 'B'
        },
        {
            'question': "Advanced mobile device searches can only report on managed devices.",
            'answers': ['A. True', 'B. False'],
            'correct': 'B'
        },
        {
            'question': "A device configuration profile was created and saved without a target scoped. Which devices will receive this configuration profile?",
            'answers': ['A. All devices', 'B. No devices', 'C. Only devices in the All Device Smart Group', 'D. Only managed devices'],
            'correct': 'B'
        },
        {
            'question': "App Store apps installed by Jamf Pro can be updated automatically.",
            'answers': ['A. True', 'B. False'],
            'correct': 'A'
        },
        {
            'question': "The remote commands available for mobile devices vary depending on ownership type, device model, operating system version, and supervision status.",
            'answers': ['A. True', 'B. False'],
            'correct': 'A'
        },
        {
            'question': "Computer configuration profiles can be used to enforce local user account password compliance.",
            'answers': ['A. True', 'B. False'],
            'correct': 'A'
        },
        {
            'question': "Issuing a Lock Computer remote command will log out the user, restart the computer, and set a firmware-level passcode that will need to be entered before the computer can be used again.",
            'answers': ['A. True', 'B. False'],
            'correct': 'A'
        },
        {
            'question': "The following can be configured to remove a specific computer, building, or department from the scope of a configuration profile:",
            'answers': ['A. Limitation', 'B. Omission', 'C. Target', 'D. Exclusion'],
            'correct': 'D'
        },
        {
            'question': "Configuration profiles may only be created in Jamf Pro.",
            'answers': ['A. True', 'B. False'],
            'correct': 'B'
        },
        {
            'question': "To troubleshoot computer configuration profiles, an admin should verify the payloads are configured appropriately and review which area in Jamf Pro for additional information?",
            'answers': ['A. Logs within the selected profile', 'B. PreStage Enrollment for Devices', 'C. Mac App Store', 'D. Settings > Global Management > Categories'],
            'correct': 'A'
        },
        {
            'question': "It is considered good practice to avoid bundling multiple, non-related payloads, into a single computer configuration profile.",
            'answers': ['A. True', 'B. False'],
            'correct': 'A'
        },
            {
            'question': "In a computer policy, what determines when the policy will run?",
            'answers': ['A. Trigger', 'B. Execution Frequency', 'C. Starter', 'D. Scope'],
            'correct': 'A'
        },
        {
            'question': "Scripts and software can be deployed with a policy.",
            'answers': ['A. True', 'B. False'],
            'correct': 'A'
        },
        {
            'question': "macOS App Store apps cannot be made available for a user to download in Self Service using Jamf Pro.",
            'answers': ['A. True', 'B. False'],
            'correct': 'B'
        },
        {
            'question': "Computer configuration profiles and policies can be scoped to categories.",
            'answers': ['A. True', 'B. False'],
            'correct': 'B'
        },
        {
            'question': "If a macOS App Store app is scoped to the Minneapolis building and the IT department, who will receive the app?",
            'answers': ['A. Everyone in the Minneapolis building and everyone in the IT department', 'B. Everyone will receive the app', 'C. Everyone in the IT department, except those in the Minneapolis building', 'D. Everyone in the Minneapolis building, except those in the IT department'],
            'correct': 'A'
        },
        {
            'question': "macOS App Store app updates can be forced if the app is managed.",
            'answers': ['A. True', 'B. False'],
            'correct': 'A'
        },
        {
            'question': "If a Jamf Pro admin wanted to create a computer group where the membership updated automatically, what type of group should be created?",
            'answers': ['A. Static', 'B. Dynamic', 'C. Automatic', 'D. Smart'],
            'correct': 'D'
        },
        {
            'question': "Smart computer group membership and policy status can be monitored from the Jamf Pro Dashboard.",
            'answers': ['A. True', 'B. False'],
            'correct': 'A'
        },
        {
            'question': "Under a computer policy's execution frequency, which is not an option?",
            'answers': ['A. Ongoing', 'B. Once per year', 'C. Once per computer', 'D. Once every day'],
            'correct': 'B'
        },
        {
            'question': "When deploying a configuration profile, policy, or app, which tab defines who will receive the management task?",
            'answers': ['A. List', 'B. Scope', 'C. General', 'D. Computer'],
            'correct': 'B'
        },
        ]
        
        random.shuffle(self.questions)

        self.current_question = 0
        self.score = 0

        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        # Set the background color using a Rectangle
        with self.layout.canvas:
            Color(0, 0, 0, 0.8)  # RGBA color values (r, g, b, a)
            self.rect = Rectangle(pos=self.layout.pos, size=self.layout.size)
        # Bind the Rectangle's size and position to the layout's size and position
        self.layout.bind(pos=self.update_rect, size=self.update_rect)

        # Create a label for the countdown timer
        self.timer_label = Label(text="Time Left: 60:00", size_hint_y=None, height=30)
        self.layout.add_widget(self.timer_label)

        self.question_label = Label(text=self.questions[0]['question'], size_hint_y=None, height=100)
        self.layout.add_widget(self.question_label)

        self.answer_widgets = []

        self.answer_grid = GridLayout(cols=2, spacing=10, size_hint_y=None, height=200)
        for answer in self.questions[0]['answers']:
            checkbox = CheckBox(group='answers')
            checkbox_label = Label(text=answer)

            self.answer_grid.add_widget(checkbox)
            self.answer_grid.add_widget(checkbox_label)

            self.answer_widgets.append((checkbox, checkbox_label))

        self.layout.add_widget(self.answer_grid)

        self.submit_button = Button(text='Submit Answer', on_press=self.check_answer, size_hint_y=None, height=50)
        self.layout.add_widget(self.submit_button)

        self.progress_bar = ProgressBar(max=len(self.questions), size_hint_y=None, height=30)
        self.layout.add_widget(self.progress_bar)

        self.percentage_label = Label(text='', size_hint_y=None, height=30)
        self.layout.add_widget(self.percentage_label)

        # Start the countdown timer when the app is built
        self.timer = 3600  # 60 minutes in seconds
        Clock.schedule_interval(self.update_timer, 1)

        return self.layout
    
    def update_rect(self, instance, value):
        # Update the Rectangle's size and position when the layout's size or position changes
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def update_timer(self, dt):
        if self.timer > 0:
            self.timer -= 1
            minutes = self.timer // 60
            seconds = self.timer % 60
            self.timer_label.text = f"Time Left: {minutes:02}:{seconds:02}"
        else:
            self.timer_label.text = "Time's up!"
            Clock.unschedule(self.update_timer)

    def next_question(self):
        self.current_question += 1

        if self.current_question < len(self.questions):
            self.question_label.text = self.questions[self.current_question]['question']

            for checkbox, _ in self.answer_widgets:
                checkbox.active = False

            answers = self.questions[self.current_question]['answers']

            self.answer_grid.clear_widgets()
            self.answer_widgets = []

            for answer in answers:
                checkbox = CheckBox(group='answers')
                checkbox_label = Label(text=answer)

                self.answer_grid.add_widget(checkbox)
                self.answer_grid.add_widget(checkbox_label)

                self.answer_widgets.append((checkbox, checkbox_label))

            self.submit_button.disabled = False
            self.progress_bar.value = self.current_question + 1
        else:
            self.question_label.text = f'Quiz completed! Your score: {self.score}/{len(self.questions)}'
            self.submit_button.disabled = True

    def check_answer(self, instance):
        selected_answers = [label.text.split('. ')[0] for checkbox, label in self.answer_widgets if checkbox.active]
        correct_answer = self.questions[self.current_question]['correct']

        self.display_feedback(selected_answers == [correct_answer])

        self.next_question()

    def display_feedback(self, is_correct):
        feedback_labels = ["Correct!", "Incorrect."]

        for label_text in feedback_labels:
            for widget in self.layout.children[:]:
                if isinstance(widget, Label) and widget.text == label_text:
                    self.layout.remove_widget(widget)

        if is_correct:
            feedback_label = Label(text="Correct!", color=(0, 1, 0, 1))
        else:
            feedback_label = Label(text="Incorrect.", color=(1, 0, 0, 1))

        self.layout.add_widget(feedback_label)

        self.score += 1 if is_correct else 0  # Update the score

        # Calculate percentage score
        percentage = (self.score / len(self.questions)) * 100

        # Update the percentage label
        self.percentage_label.text = f'Your percentage score: {percentage:.2f}%'

        if self.current_question < len(self.questions):
            self.submit_button.disabled = False
        else:
            self.question_label.text = f'Quiz completed! Your score: {self.score}/{len(self.questions)}'
            self.submit_button.disabled = True

if __name__ == '__main__':
    QuizApp().run()