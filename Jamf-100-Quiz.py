# Define the quiz questions and answers
questions = [
    "iOS apps exist in a self-contained environment called an App Sandbox.\n(a) True\n(b) False\n",
    "Swiping down from the top right on an iOS device (iPhone X and later) will access which feature?\n(a) Notification Center\n(b) Control Center\n(c) Tips\n(d) Search\n",
    "An Apple ID is required to complete iOS Setup Assistant.\n(a) True\n(b) False\n",
    "Along with apps, which feature can be added to the iOS Home Screen that gives quick access to additional information such as World Clock and Batteries?\n(a) Complications\n(b) Widgets\n(c) Quick Look\n(d) Notification Center\n",
    "To delete an app from an iOS device:\n(a) Touch and hold the app until a menu pops up > tap Remove App\n(b) Navigate to Settings > General > About\n(c) Use the App Store to uninstall the app\n(d) Apps cannot be deleted from iOS devices\n",
    "Under which section of the Settings > General would a user be able to update the name of their iOS device?\n(a) Legal & Regulatory\n(b) Date & Time\n(c) About\n(d) Erase All Content and Settings\n",
    "Some iOS apps allow users to purchase additional features within the app after download. What is noted next to the Get button to inform users of this?\n(a) Purchase More Content\n(b) Additional Downloads\n(c) More Content Available\n(d) In-App Purchases\n",
    "A user can opt out of sending app analytics and crash data to app developers during iOS Setup Assistant.\n(a) True\n(b) False\n",
    "Property list files use which file extension?\n(a) .prop\n(b) .propli\n(c) .plist\n(d) .prolist\n",
    "Which command can be used to reveal the contents of a macOS directory in the command-line interface?\n(a) ls\n(b) cd\n(c) mkdir\n(d) cp\n",
    "Which character represents the current user's home directory in the command-line interface?\n(a) /\n(b) *\n(c) ~\n(d) #\n",
    "An internet connection is required to set up a Mac.\n(a) True\n(b) False\n",
    "Which of the following is contained in the macOS Apple menu?\n(a) Finder Preferences\n(b) System Preferences\n(c) Connect to Server\n(d) Time Machine\n",
    "Which keyboard shortcut can be used to access Spotlight on macOS?\n(a) Shift-Command-4\n(b) Command-S\n(c) Option-Space bar\n(d) Command-Space bar\n",
    "In order for a macOS app to run and pass Apple's Gatekeeper settings, it must be submitted to Apple for notarization.\n(a) True\n(b) False\n",
    "Which macOS feature can be used to quickly search the web, open applications, and even do quick calculations?\n(a) Spotlight\n(b) Quick Look\n(c) Control Center\n(d) Notification Center\n",
    "Which character is used to instruct a command-line interpreter to ignore a line in a script, and is often used to provide comments?\n(a) /\n(b) #\n(c) &\n(d) ;\n",
    "Which two items cannot be removed from the Dock in macOS?\n(a) The Finder and Trash\n(b) System Preferences and Calendar\n(c) News and Contacts\n(d) Pages and Mail\n",
    "In the command-line interface, which command can be used to display the manual page for other commands?\n(a) help\n(b) ls\n(c) man\n(d) cd\n",
    "Which menu in the macOS menu bar contains commonly used tasks like Cut, Copy, and Paste?\n(a) File menu\n(b) Apple menu\n(c) Edit menu\n(d) Window menu\n",
    "Where can information on macOS version, processor type, and a computer's serial number be found in About This Mac?\n(a) Displays\n(b) Storage\n(c) Support\n(d) Overview\n",
    "System settings for Location Services, Analytics, and Screen Time can be reconfigured in System Preferences after completing Setup Assistant.\n(a) True\n(b) False\n",
    "Which macOS feature allows users to navigate the file system to view the contents of their computer, including files, apps, and storage devices?\n(a) Finder\n(b) Explorer\n(c) Terminal\n(d) Pages\n",
    "Along with Computers and Devices, what is the third tab in the top left of the Jamf Pro interface?\n(a) Security\n(b) Enrollment\n(c) Users\n(d) Settings\n",
    "What can be created within Apple Business Manager and Apple School Manager to allow user-based app and book deployment or utilize Shared iPad?\n(a) Jamf Pro Users\n(b) School and Business IDs\n(c) Administrator Accounts\n(d) Managed Apple IDs\n",
    "By default, user-initiated enrollment is enabled for computers.\n(a) True\n(b) False\n",
    "Which Jamf Pro user account privilege set will grant permissions to create, read, update, and delete content in Jamf Pro?\n(a) Administrator\n(b) Read-Only\n(c) Auditor\n(d) None\n"
    "Mobile device management (MDM) allows organizations to wirelessly configure, update, and deploy content to devices.\n(a) True\n(b) False\n",
    "A push certificate is required to facilitate communication between Apple Push Notification service and a mobile device management platform.\n(a) True\n(b) False\n",
    "What is the name of the payload within a computer PreStage enrollment that determines what type of user account is created during Setup Assistant?\n(a) User and Location\n(b) Configuration Profiles\n(c) Account Settings\n(d) Certificates\n",
    "In Jamf Pro, custom messaging and end-user license agreements can be added to the user-initiated enrollment screens.\n(a) True\n(b) False\n",
    "Computers can receive remote commands, configuration profiles, and app deployments from Jamf Pro if they're unable to communicate with APNs.\n(a) True\n(b) False\n",
    "Which section within Jamf Pro might show important information about the state of the Jamf Pro server, such as a push certificate is expiring soon?\n(a) Status\n(b) Notifications\n(c) Warnings\n(d) Updates\n",
    "Simple device inventory search results can be exported from Jamf Pro in the following file formats:\n(a) .txt,.pdf, or .pages\n(b) .docx, .txt, or .rtf\n(c) .psd, .pdf, or .doc\n(d) .tsv, .csv, or XML\n",
    "Static device group membership is variable and updates automatically based on device eligibility.\n(a) True\n(b) False\n",
    "In an advanced mobile device search, which operator can be used to find all matches that contain the specified value, not just exact matches?\n(a) is\n(b) is not\n(c) like\n(d) not like\n",
    "Creating separate mobile device configuration profiles is preferred over bundling many payloads into a single configuration profile.\n(a) True\n(b) False\n",
    "The following character can be used as a wildcard in a simple mobile device search:\n(a) !\n(b) ~\n(c) #\n(d) *\n",
    "Which intervals are available for email reporting in saved advanced mobile device searches?\n(a) Hourly, Daily, or Weekly\n(b) Specific days, Daily, Weekly, or Monthly\n(c) Daily, Monthly, or Yearly\n(d) Hourly, Weekly, or Yearly\n",
    "Where can a Jamf Pro admin go to change the inventory attributes listed when completing a simple mobile device search?\n(a) Settings > Global Management > Categories\n(b) Settings > Device Management > Inventory Display\n(c) Settings > Self Service > iOS\n(d) Settings > Jamf Pro Information > Jamf Pro Summary\n",
    "Advanced mobile device searches can only report on managed devices.\n(a) True\n(b) False\n",
    "A device configuration profile was created and saved without a target scoped. Which devices will receive this configuration profile?\n(a) All devices\n(b) No devices\n(c) Only devices in the 'All Device' Smart Group\n(d) Only managed devices\n",
    "App Store apps installed by Jamf Pro can be updated automatically.\n(a) True\n(b) False\n",
    "The remote commands available for mobile devices vary depending on ownership type, device model, operating system version, and supervision status.\n(a) True\n(b) False\n",
    "Computer configuration profiles can be used to enforce local user account password compliance.\n(a) True\n(b) False\n",
    "Issuing a Lock Computer remote command will log out the user, restart the computer, and set a firmware-level passcode that will need to be entered before the computer can be used again.\n(a) True\n(b) False\n",
    "The following can be configured to remove a specific computer, building, or department from the scope of a configuration profile:\n(a) Limitation\n(b) Omission\n(c) Target\n(d) Exclusion\n",
    "Configuration profiles may only be created in Jamf Pro.\n(a) True\n(b) False\n",
    "To troubleshoot computer configuration profiles, an admin should verify the payloads are configured appropriately and review which area in Jamf Pro for additional information?\n(a) Logs within the selected profile\n(b) PreStage Enrollment for Devices\n(c) Mac App Store\n(d) Settings > Global Management > Categories\n",
    "It is considered good practice to avoid bundling multiple, non-related payloads, into a single computer configuration profile.\n(a) True\n(b) False\n",
    "In a computer policy, what determines when the policy will run?\n(a) Trigger\n(b) Execution Frequency\n(c) Starter\n(d) Scope\n",
    "Scripts and software can be deployed with a policy.\n(a) True\n(b) False\n",
    "macOS App Store apps cannot be made available for a user to download in Self Service using Jamf Pro.\n(a) True\n(b) False\n",
    "Computer configuration profiles and policies can be scoped to categories.\n(a) True\n(b) False\n",
    "If a macOS App Store app is scoped to the Minneapolis building and the IT department, who will receive the app?\n(a) Everyone in the Minneapolis building and everyone in the IT department\n(b) Everyone will receive the app\n(c) Everyone in the IT department, except those in the Minneapolis building\n(d) Everyone in the Minneapolis building, except those in the IT department\n",
    "macOS App Store app updates can be forced if the app is managed.\n(a) True\n(b) False\n",
    "If a Jamf Pro admin wanted to create a computer group where the membership updated automatically, what type of group should be created?\n(a) Static\n(b) Dynamic\n(c) Automatic\n(d) Smart\n",
    "Smart computer group membership and policy status can be monitored from the Jamf Pro Dashboard.\n(a) True\n(b) False\n",
    "Under a computer policy's execution frequency, which is not an option?\n(a) Ongoing\n(b) Once per year\n(c) Once per computer\n(d) Once every day\n",
    "When deploying a configuration profile, policy, or app, which tab defines who will receive the management task?\n(a) List\n(b) Scope\n(c) General\n(d) Computer\n"
]

# Define correct answers
answers = [
    "a",
    "b",
    "b",
    "b",
    "a",
    "c",
    "d",
    "a",
    "c",
    "a",
    "c",
    "b",
    "b",
    "d",
    "a",
    "a",
    "b",
    "a",
    "c",
    "c",
    "d",
    "a",
    "a",
    "c",
    "d",
    "b",
    "a",
    "a",
    "a",
    "c",
    "a",
    "b",
    "b",
    "d",
    "b",
    "c",
    "a",
    "d",
    "b",
    "b",
    "b",
    "b",
    "a",
    "a",
    "a",
    "a",
    "d",
    "b",
    "a",
    "a",
    "a",
    "a",
    "b",
    "b",
    "a",
    "a",
    "d",
    "a",
    "b",
    "b"
]

# Initialize score
score = 0

# Function to run the quiz
def run_quiz(questions, answers):
    global score
    for i in range(len(questions)):
        user_answer = input(questions[i]).strip().lower()
        if user_answer == answers[i]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. The correct answer is ({answers[i]}).\n")

    print(f"You got {score} out of {len(questions)} questions correct!")

# Run the quiz
print("Welcome to the Jamf 100 quiz!\n")
run_quiz(questions, answers)
