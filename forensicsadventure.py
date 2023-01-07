from ast import If, Lambda
from inspect import trace
from re import search
from tkinter import *
from tkinter import ttk
from types import LambdaType

root = Tk()
root.title("Murder in Python: A Forensics Adventure")

# Designate height and width
appWidth = 750
appHeight = 500
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)
root.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')

# Create a main frame
mainFrame = Frame(root)
mainFrame.pack(fill=BOTH, expand=1)

# Create a canvas
myCanvas = Canvas(mainFrame)
myCanvas.pack(side=LEFT, fill=BOTH, expand=1)

#Add a scrollbar to the canvas
scrollbar = ttk.Scrollbar(mainFrame, orient=VERTICAL, command=myCanvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

#Configure the canvas
myCanvas.configure(yscrollcommand=scrollbar.set)
myCanvas.bind("<Configure>",lambda e : myCanvas.config(scrollregion= myCanvas.bbox(ALL)))

#Create another frame inside the canvas
secondFrame = Frame(myCanvas)
secondFrame.pack(fill=BOTH, expand=1)
secondFrame.bind('<Configure>', lambda e : myCanvas.configure(scrollregion = myCanvas.bbox(ALL)))


#Add new frame to a window in the canvas
myCanvas.create_window((0,0), window=secondFrame, anchor="nw")

def invalidFunction():
    invalidLabel = Label(secondFrame, text="CSI Kim: Sorry, I don't think that was one of the answer choices.\nCheck your spelling or try something else.\n")
    invalidLabel.pack()
    myCanvas.update_idletasks()
    myCanvas.yview_moveto('1')

# Begin game if user agreed
def beginFunction():
    if introEntry.get().lower().strip() == "yes":
        nameFunction()
    elif introEntry.get().lower().strip() == "no":
        noLabel = Label(secondFrame, text="CSI Kim: That's too bad. We'll have to solve it on our own.") 
        noLabel.pack()
    else:
        invalidFunction()


# Greet user
def nameFunction():
    nameLabel = Label(secondFrame, text="CSI Kim: Great. What is your name?")
    nameLabel.pack()
    global nameEntry
    nameEntry = Entry(secondFrame)
    nameEntry.pack()
    nameButton = Button(secondFrame, text="Submit", command=coffeeOrCrimeFunction)
    nameButton.pack()
    myCanvas.update_idletasks()
    myCanvas.yview_moveto('1')



#  Greet user.Ask user if they want coffee or to go to the scene.
def coffeeOrCrimeFunction():
    global name
    name = nameEntry.get().strip()
    greeting = text="Kim: Hello, Detective " + name + "."
    greetingLabel = Label(secondFrame, text=greeting)
    greetingLabel.pack()
    infoLabel = Label(secondFrame, text="\nCSI Kim: The victims are a young couple. \nThey were found inside their house this morning. \n CSI is processing the scene.")
    infoLabel.pack()
    headingLabel = Label(secondFrame, text="CSI Kim: It's pretty early in the morning.\nWould you like to head to the crime scene now?\nOr grab a cup of coffee first? (crime scene/coffee shop)")
    headingLabel.pack()
    global coffeeOrCrimeEntry
    coffeeOrCrimeEntry = Entry(secondFrame)
    coffeeOrCrimeEntry.pack()
    coffeeOrCrimeButton = Button(secondFrame, text="Submit", command=coffeeFunction)
    coffeeOrCrimeButton.pack()
    myCanvas.update_idletasks()
    myCanvas.yview_moveto('1')



# Direct which function the code should continue to
def coffeeFunction():
    if coffeeOrCrimeEntry.get().lower().strip() == "coffee shop":
        yesCoffeeFunction()
    elif coffeeOrCrimeEntry.get().lower().strip() == "crime scene":
        noCoffeeFunction()
    else:
        invalidFunction()

# Head to coffee shop and order
def yesCoffeeFunction():
    yesCoffeeLabel = Label(secondFrame, text="CSI Kim: If you insist. The nearest coffee shop is a half hour away.\nWe will probably be a little late to the crime scene...\nLooking at evidence right away is essential, but it's up to you, boss.")
    yesCoffeeLabel.pack()
    global elipsesLabel
    elipsesLabel = Label(secondFrame, text="\n......................\n")
    elipsesLabel.pack()
    coffeeShopLabel = Label(secondFrame, text="\n CSI Kim: Here we are. What flavor are you thinking?\nThey have black coffee, caramel latte, and their original flavor:\nbanana marshmallow americano with hints of pineapple.\nWhich flavor sounds good? (black/latte/americano)")
    coffeeShopLabel.pack()
    global coffeeShopEntry
    coffeeShopEntry = Entry(secondFrame)
    coffeeShopEntry.pack()
    yesCoffeeButton = Button(secondFrame, text="Submit", command=coffeeOrderFunction)
    yesCoffeeButton.pack()
    myCanvas.update_idletasks()
    myCanvas.yview_moveto('1')
    global yesCoffee
    yesCoffee = 1

# Check for coffee order and valid input
def checkCoffeeFunction():
    if coffeeShopEntry.get().lower().strip() == "black" or coffeeShopEntry.get().lower().strip() == "latte" or coffeeShopEntry.get().lower().strip() == "americano":
        coffeeOrderFunction()
    else:
        invalidFunction()

# Give user coffee order
def coffeeOrderFunction():
    coffeeOrderLabel = Label(secondFrame, text="\nCSI Kim: Here's your " + coffeeShopEntry.get().lower().strip() + ".\nHopefully it was worth it...")
    coffeeOrderLabel.pack()
    headingFunction()
    myCanvas.update_idletasks()
    myCanvas.yview_moveto('1')

# Head to crime scene without coffee
def noCoffeeFunction():
    noCoffeeLabel = Label(secondFrame, text="\nCSI Kim: That's a good idea. We need to get to the crime scene ASAP, before any evidence degrades.")
    noCoffeeLabel.pack()
    elipsesLabel = Label(secondFrame, text="\n......................\n")
    elipsesLabel.pack()
    headingFunction()
    myCanvas.update_idletasks()
    myCanvas.yview_moveto('1')
    global noCoffee
    noCoffee = 1

# Head to crime scene
def headingFunction():
    headingLabel = Label(secondFrame, text="CSI Kim: Let's get going...\nWhile we're heading there, I can catch you up a bit on what we know.\n The Victims are newlyweds Connor and Delilah Garnett, both 27 years old.\nMr. Garnett is a local psychiatrist. Mrs. Garnett is a dentist.\nThe contractor they hired to fix things around their house found this morning at about 5:00am.\nSo far it's looking like they have gunshot wounds, maybe even stabbing wounds.")
    headingLabel.pack()
    myCanvas.update_idletasks()
    myCanvas.yview_moveto('1')
    arrivingFunction()

# Arrive at crime scene, introduce Johnson
def arrivingFunction():
    elipsesLabel = Label(secondFrame, text="\n......................\n")
    elipsesLabel.pack()
    arrivingLabel = Label(secondFrame, text="CSI Kim: Here we are. Oh, there's CSI Johnson.")
    arrivingLabel.pack()
    arrivingLabel2 = Label(secondFrame, text= "\nCSI Akugri: Hi, " + name + ". I'm CSI Akugri.\nI've been working the scene a couple hours now.\nBoth victims show signs of blunt force trauma and the back door was forced in.\n We're collecting samples from all around the hosuse.\n\n Wini: What would you like to do first? (examine bodies/search home/collect more samples)")
    arrivingLabel2.pack()
    global arrivingEntry
    arrivingEntry = Entry(secondFrame)
    arrivingEntry.pack()
    arrivingButton = Button(secondFrame, text= "Submit", command=evidenceFunction1)
    arrivingButton.pack()
    myCanvas.update_idletasks()
    myCanvas.yview_moveto('1')



# Check what evidence the user wants to analyze and direct to function
def evidenceFunction1():
    elipsesLabel = Label(secondFrame, text="\n......................\n")
    elipsesLabel.pack()
    if arrivingEntry.get().lower().strip() == "examine bodies":
        examineFunction()
    elif arrivingEntry.get().lower().strip() == "search home":
        searchFunction()
    elif arrivingEntry.get().lower().strip() == "collect more samples":
        sampleFunction()
    else:
        invalidFunction()

# Let user choose another type of evidence
def redirectEvidenceFunction():
    elipsesLabel = Label(secondFrame, text="\n......................\n")
    elipsesLabel.pack()
    global x
    if x <= 2:
        redirectLabel = Label(secondFrame, text= "CSI Kim: Let's look at " + str(3-x) + " more piece(s) of evidence. What would you like to analyze? (examine bodies/search home/collect more samples)")
        redirectLabel.pack()
        global redirectEntry
        redirectEntry = Entry(secondFrame)
        redirectEntry.pack()
        redirectButton = Button(secondFrame, text= "Submit", command=evidenceFunction2)
        redirectButton.pack()
        myCanvas.update_idletasks()
        myCanvas.yview_moveto('1')
    else:
        labFunction()


# Check what evidence the user wants to analyze and direct to function
def evidenceFunction2():
    elipsesLabel = Label(secondFrame, text="\n......................\n")
    elipsesLabel.pack()
    if redirectEntry.get().lower().strip() == "examine bodies":
        examineFunction()
    elif redirectEntry.get().lower().strip() == "search home":
        searchFunction()
    elif redirectEntry.get().lower().strip() == "collect more samples":
        sampleFunction()
    else:
        invalidFunction()

# Ask user which body they would like to examine
def examineFunction():
    examineLabel = Label(secondFrame, text= "\nCSI Kim: Good choice. Would you like to look at Mr. or Mrs. Garnett? (Mr./Mrs.)")
    examineLabel.pack()
    global examineEntry
    examineEntry = Entry(secondFrame)
    examineEntry.pack()
    examineButton = Button(secondFrame, text= "Submit", command=checkExamineFunction)
    examineButton.pack()
    myCanvas.update_idletasks()
    myCanvas.yview_moveto('1') 

# Check which body user would like to examine
def checkExamineFunction():
    if  examineEntry.get().lower().strip() == "mr." or examineEntry.get().lower().strip() == "mr":
        examineMrFunction()
    elif  examineEntry.get().lower().strip() == "mrs." or examineEntry.get().lower().strip() == "mrs":
        examineMrsFunction()
    else:
        invalidFunction()

# Ask user if they would like to examine traumt or clothing
def examineMrFunction():
    examineMrLabel = Label(secondFrame, text="\nCSI Kim: Good plan. Would you like to examine the blunt force trauma or the trace evidence on his clothes? (trauma/clothes)")
    examineMrLabel.pack()
    global examineMrEntry
    examineMrEntry = Entry(secondFrame)
    examineMrEntry.pack()
    examineMrButton = Button(secondFrame, text= "Submit", command=checkMrExamineFunction)
    examineMrButton.pack()
    myCanvas.update_idletasks()
    myCanvas.yview_moveto('1')

# Check what the user chose to examine
def checkMrExamineFunction():
    if  examineMrEntry.get().lower().strip() == "trauma":
        examineMrTraumaFunction()
    elif  examineMrEntry.get().lower().strip() == "clothes":
        examineMrClothesFunction() 
    else:
        invalidFunction()
    
# Describe blunt force traumt    
def examineMrTraumaFunction():
    mrTraumaLabel = Label(secondFrame, text="\nCSI Kim: Gunshot wounds are complex and often difficult to analyze. They occur when a bullet enters the body after being fired.\n In this case, the entry wound is near the belly button and the exit wound is on the upper back.\n This suggests that Mr. Garnett was shot at an upward angle.\n Further, the wound appears to be close range.)")
    mrTraumaLabel.pack()
    myCanvas.update_idletasks()
    myCanvas.yview_moveto('1')
    global x
    x += 1
    global examineMrTrauma
    examineMrTrauma = 1
    redirectEvidenceFunction()


# Describe trace evidence
def examineMrClothesFunction():
    traceLabel = Label(secondFrame, text="\nCSI Kim: \"Every contanct leaves a trace\" -- Dr. Edmond Locard \n Trace evidence includes fibers, hairs, rope, soil, glass, and other materials.\n We have identified a brown hairs on the victim; Mrs. Garnett has black hair.")
    traceLabel.pack()
    myCanvas.update_idletasks()
    myCanvas.yview_moveto('1')
    global x
    x += 1
    global examineMrClothes
    examineMrClothes = 1
    redirectEvidenceFunction()


# Ask user if they would like to examine trauma or clothing
def examineMrsFunction():
    examineMrsLabel = Label(secondFrame, text="\nCSI Kim: Good idea. Would you like to examine the blunt force trauma or the blood stains on her clothes? (trauma/clothes)")
    examineMrsLabel.pack()
    global examineMrsEntry
    examineMrsEntry = Entry(secondFrame)
    examineMrsEntry.pack()
    examineMrsButton = Button(secondFrame, text= "Submit", command=checkMrsExamineFunction)
    examineMrsButton.pack()
    myCanvas.update_idletasks()
    myCanvas.yview_moveto('1')

# Check what the user chose to examine
def checkMrsExamineFunction():
    if  examineMrsEntry.get().lower().strip() == "trauma":
        examineMrsTraumaFunction()
    elif  examineMrsEntry.get().lower().strip() == "clothes":
        examineMrsClothesFunction() 
    else:
        invalidFunction()

# Describe blunt force trauma
def examineMrsTraumaFunction():
    mrsTraumaLabel = Label(secondFrame, text="\nCSI Kim: Stabs wounds are often identified by an injury whenere the legnth is less than thte depth.\n These result when the assailant thrusts a pointed object into a victim.\nThe clean cut edges and sharp wounds suggest that Mrs. Garneet was indeed stabbed.\nThis seems more personal than a gunshot.")
    mrsTraumaLabel.pack()
    myCanvas.update_idletasks()
    myCanvas.yview_moveto('1')
    global x
    x += 1
    global examineMrsTrauma
    examineMrsTrauma = 1
    redirectEvidenceFunction()

# Describe blood staining
def examineMrsClothesFunction():
    stainLabel = Label(secondFrame, text="\nCSI Kim: Often actions can be recreated by analyzing bloodstains.\nObviously Mrs. Garnett has some blood stains on her shirt from her stab wood, but there also appear to be passive stains on her pants.\nSomeone else's blood appears to have dripped over the victim while she was already laying down.")
    stainLabel.pack()
    myCanvas.update_idletasks()
    myCanvas.yview_moveto('1')
    global x
    x += 1
    global examineMrsClothes
    examineMrsClothes = 1
    redirectEvidenceFunction()

# Ask user which part of the house they would like to search
def searchFunction():
    searchLabel = Label(secondFrame, text="\nCSI Kim: Let's do some searching. Where should we start? (trash/closet/under the bed/kitchen)")
    searchLabel.pack()
    global searchEntry
    searchEntry = Entry(secondFrame)
    searchEntry.pack()
    searchButton = Button(secondFrame, text="Submit", command=checkSearchFunction)
    searchButton.pack()
    myCanvas.update_idletasks()
    myCanvas.yview_moveto('1')

# Check what the user would like to search
def checkSearchFunction():
    if  searchEntry.get().lower().strip() == "trash":
        searchTrashFunction()
    elif searchEntry.get().lower().strip() == "closet":
        searchClosetFunction()() 
    elif searchEntry.get().lower().strip() == "under the bed" or searchEntry.get().lower().strip() == "under bed":
        searchBedFunction()
    elif searchEntry.get().lower().strip() == "kitchen":
        searchKitchenFunction()
    else:
        invalidFunction()

# Describe receipts in the trash
def searchTrashFunction():
    trashLabel = Label(secondFrame, text="\nCSI Kim: Oh, I think this might be helpful.\nA receipt for two banana marshmallow americano with hints of pineapples.\nIt apperas to be signed by Mrs. Garnett.\n Documents are often very helpful, but have to be verified by a forensic expert.\nAnyway, maybe this has something to do with the murderer.")
    trashLabel.pack()
    myCanvas.update_idletasks()
    myCanvas.yview_moveto('1')
    global x
    x += 1
    global searchTrash
    searchTrash = 1
    redirectEvidenceFunction()

# Describe fingerprints in the closet
def searchClosetFunction():
    closetLabel = Label(secondFrame, text="\nCSI Kim: Look over here: fingerprints!\nWe leave our fingerprints everywhere, and no two people have the same fingerprints.\nThis means fingerprints can be used to identify suspects (as they have been for 100+ years).\nThese prints on this box do not seem to match either of our victims.\n Hmmm, this box seems to be pictures of old photos. Maybe the murderer is from their past?")
    closetLabel.pack()
    myCanvas.update_idletasks()
    myCanvas.yview_moveto('1')
    global x
    x += 1
    global searchCloset
    searchCloset = 1
    redirectEvidenceFunction()

# Describe digital evidence found under the bed
def searchBedFunction():
    bedLabel = Label(secondFrame, text="\nCSI Kim: Ah! Looks like there's a cellphone under the bed.\n Digital evience can help investigators because we can analyze people's digital evidence trails.\nIt seems like this is Mr. Garnett's phone.\nThe location shows he was at his office late at night, a few hours before his murder.")
    bedLabel.pack()
    myCanvas.update_idletasks()
    myCanvas.yview_moveto('1')
    global x
    x += 1
    global searchBed
    searchBed = 1
    redirectEvidenceFunction()

# Describe footprints in the kitchen
def searchKitchenFunction():
    kitchenLabel = Label(secondFrame, text="\nCSI Kim: Look, this is what we call \"pattern evidence:\" a shoe print!\nFootwear leaves specific patterns based on the size, brand, style, etc.\n This appears to be a boot for about a men's size 11.")
    kitchenLabel.pack()
    myCanvas.update_idletasks()
    myCanvas.yview_moveto('1')
    global x
    x += 1
    global searchKitchen
    searchKitchen = 1
    redirectEvidenceFunction()

# Ask user what kind of samples they would like to collect
def sampleFunction():
    sampleLabel = Label(secondFrame, text="\nCSI: Ahh, you're a good decision maker.\nThere seems to be DNA under Mrs. Garnett's nails, a gun in their safe--we aren't sure if it was used in this crime--\nand white powder on the kitchen counter.\nWhere samples would you like to collect? (dna/gun/powder)")
    sampleLabel.pack()
    global sampleEntry
    sampleEntry = Entry(secondFrame)
    sampleEntry.pack()
    sampleButton = Button(secondFrame, text="Submit", command=checkSampleFunction)
    sampleButton.pack()
    myCanvas.update_idletasks()
    myCanvas.yview_moveto('1')

# CHeck which sample the user would like to take
def checkSampleFunction():
    if  sampleEntry.get().lower().strip() == "dna":
        sampleDNAFunction()
    elif sampleEntry.get().lower().strip() == "gun":
        sampleGunFunction() 
    elif sampleEntry.get().lower().strip() == "powder":
        samplePowderFunction()
    else:
        invalidFunction()

# Give user DNA results
def sampleDNAFunction():
    DNALabel = Label(secondFrame, text="\nCSI Kim: DNA evidence is not only incredibly accurate, but can be recovered from very small samples.\nThe DNA found under Mrs. Garnett's nails belongs to a male--not Mr. Garnett--but we have no one to match it to.\nThis suggests she scratched this person in a struggle.")
    DNALabel.pack()
    myCanvas.update_idletasks()
    myCanvas.yview_moveto('1')
    global x
    x += 1
    global sampleDNA
    sampleDNA = 1
    redirectEvidenceFunction()

# Give user stain results
def sampleGunFunction():
    gunLabel = Label(secondFrame, text="\nCSI Kim: Ballistics analysis help us identify murder weapons.\nLet's take a look at the gun in the Garnett's safe.\nHmm...looks a .45 caliber revolver.")
    gunLabel.pack()
    myCanvas.update_idletasks()
    myCanvas.yview_moveto('1')
    global x
    x += 1
    global sampleGun
    sampleGun = 1
    redirectEvidenceFunction()

# Give user powder results
def samplePowderFunction():
    powderLabel = Label(secondFrame, text="\nCSI Kim: Poisoning is no longer the perfect murder weapon, because we can know test for chemicals with toxicology.\nSo let's take a look at this suspicious powder...\nWow, looks it was just some spilled powder sugar!")
    powderLabel.pack()
    myCanvas.update_idletasks()
    myCanvas.yview_moveto('1')
    global x
    x += 1
    global samplePowder
    samplePowder = 1
    redirectEvidenceFunction()

# Give user options at the lab
def labFunction():
    labLabel = Label(secondFrame, text="\nCSI Kim: Let's head to the lab.")
    labLabel.pack()
    elipsesLabel = Label(secondFrame, text="\n......................\n")
    elipsesLabel.pack()
    labLabel2 = Label(secondFrame, text="Here we are. You have a few options, but first let's talk to the medical examiner.")
    labLabel2.pack()
    medicalLabel = Label(secondFrame, text="\nMedical Examiner: Hi. I'm Dr. Aboyure. It's a pleasure to have you working with us.\nI have been doing the autopsies and our lab has been running tests.\nWould you like to know more about the cause of death, blood results, or foreign DNA? (death/blood/dna)")
    medicalLabel.pack()
    global labEntry
    labEntry = Entry(secondFrame)
    labEntry.pack()
    labButton = Button(secondFrame, text="Submit", command=checkLabFunction)
    labButton.pack()
    myCanvas.update_idletasks()
    myCanvas.yview_moveto('1')


# Check which lab results the user wants
def checkLabFunction():
    if  labEntry.get().lower().strip() == "death":
        labDeathFunction()
    elif labEntry.get().lower().strip() == "blood":
        labBloodFunction() 
    elif labEntry.get().lower().strip() == "dna":
        labDNAFunction()
    else:
        invalidFunction()

# Give user more infromation on cause of death
def labDeathFunction():
    labDeathLabel = Label(secondFrame, text="\nMedical Examiner: Cause of death appears to be as expected. Mr. Garnett was killed with a 9mm.\nThere is only one bullet wound.\nThe most likely scenario is that the murderer fell to the floor and shot Mr. Garnett while he was leaning over.\nMrs. Garnett was killed with a knife, likely a common kitchen knife. That suggests the stabbing was more spur of the moment.")
    labDeathLabel.pack()
    myCanvas.update_idletasks()
    myCanvas.yview_moveto('1')
    global labDeath
    labDeath = 1
    reviewFunction()

# Give user more information on blood analysis.
def labBloodFunction():
    labBloodLabel = Label(secondFrame, text="\nMedical Examiner: The passive blood stain on Mrs. Garnett was analyzed for DNA.\nIt was from a male, but that's about all we know.\nHe does have O positive blood though, which is farely common.")
    labBloodLabel.pack()
    myCanvas.update_idletasks()
    myCanvas.yview_moveto('1')
    global labBlood
    labBlood = 1
    reviewFunction()

# Give user more information on foreign DNA.
def labDNAFunction():
    labDNALabel = Label(secondFrame, text="\nMedical Examiner: Further analysis of the DNA shows that it comes from the same male that left a passive blood stain on Mrs. Garnett.")
    labDNALabel.pack()
    myCanvas.update_idletasks()
    myCanvas.yview_moveto('1')
    global labDNA
    labDNA = 1
    reviewFunction()

# Give user a recount of all evidence.
def reviewFunction():
    elipsesLabel = Label(secondFrame, text="\n......................\n")
    elipsesLabel.pack()
    if yesCoffee == 1:
        reviewLabel1 = Label(secondFrame, text="\nCSI Kim: We started off the day with a cup of coffee, then headed to the scene.\n That was a while ago. Let's do a recap of the evidence:")
        reviewLabel1.pack()
    if noCoffee == 1:
        reviewLabel2 = Label(secondFrame, text="\nCSI Kim: We started by skipping coffee and headed to the crime scrime scene.\n That was a while ago. Let's do a recap of the evidence:")
        reviewLabel2.pack()
    if examineMrTrauma == 1:
        reviewLabel3 = Label(secondFrame, text="-Mr. Garnett was shot close range just above his belly button")
        reviewLabel3.pack()
    if examineMrClothes == 1:
        reviewLabel4 = Label(secondFrame, text="-Mr. Garnett had some black hairs on his shirt.")
        reviewLabel4.pack()
    if examineMrsTrauma == 1:
        reviewLabel5 = Label(secondFrame, text="-Mrs. Garnett was stabbed.")
        reviewLabel5.pack()
    if examineMrClothes == 1:
        reviewLabel6 = Label(secondFrame, text="-Mrs. Garnett had passive blood stains dripped on her.")
        reviewLabel6.pack()
    if searchTrash == 1:
        reviewLabel7 = Label(secondFrame, text="-A receipt for two banana marshmallow americano with hints of pineapples--signed by Mrs. Garnett.")
        reviewLabel7.pack()
    if searchCloset == 1:
        reviewLabel8 = Label(secondFrame, text="-Fingerprints were found on a photo box in the Garnetts' closet.")
        reviewLabel8.pack()
    if searchBed == 1:
        reviewLabel9 = Label(secondFrame, text="-Mr. Garnett's phone location shows he was at his office shortly before the murder.")
        reviewLabel9.pack()
    if searchKitchen == 1:
        reviewLabel10 = Label(secondFrame, text="-A men's size 8 bootprint was found in the kitchen.")
        reviewLabel10.pack()
    if sampleDNA == 1:
        reviewLabel11 = Label(secondFrame, text="-DNA under Mrs. Garnett's nails belongs to a male.")
        reviewLabel11.pack()
    if sampleGun == 1:
        reviewLabel12 = Label(secondFrame, text="-The Gun in the Garnett's safe is a .45 caliber.")
        reviewLabel12.pack()
    if samplePowder == 1:
        reviewLabel13 = Label(secondFrame, text="-The mysterious powder on the kitchen counter is just powder sugar.")
        reviewLabel13.pack()
    if labDeath == 1:
        reviewLabel14 = Label(secondFrame, text="-Mr. Garnett was killed with a 9mm and was likely shot leaning over the murderer.\nMrs. Garnett was stabbed with a kitchen knife.")
        reviewLabel14.pack()
    if labDNA == 1:
        reviewLabel15 = Label(secondFrame, text="-The blood stain on Mrs. Garnett comes from a male with O positive blood.")
        reviewLabel15.pack()
    if labBlood == 1:
        reviewLabel16 = Label(secondFrame, text="-The male DNA under Mrs. Garnett's nails matched the DNA from the blood stain on her shirt.")
        reviewLabel16.pack()
    myCanvas.update_idletasks()
    myCanvas.yview_moveto('1')
    guessKillerFunction()

# Let user pick a killer.
def guessKillerFunction():
    elipsesLabel = Label(secondFrame, text="\n......................\n")
    elipsesLabel.pack()
    guessKillerLabel1 = Label(secondFrame, text="We have a few suspects. Here they are:\n Brady Johnson:\n-26 year old male.\n-Works at a local coffee shop.\n-An ex boyfriend of Mrs. Garnett.\n-About 6'1\".\n-Wears size 10.5 shoes.\n-O positive blood.")
    guessKillerLabel1.pack()
    gueessKillerLabel2 = Label(secondFrame, text="Katherine Bailey:\n-57 year old women.\n-Works in construction.\nA client of Mr. Garnett.\n About 5'10\". Wears size 11 men's boots for work.\nAB blood type.")
    gueessKillerLabel2.pack()
    guessKillerLabel3 = Label(secondFrame, text="Kurt Taylor:\n-33 year old male.\nHas a trust fund; does not work.\nNeighbor to the Garnett's.\nWears men's size 9 shoes.\n-O positive blood.")
    guessKillerLabel3.pack()
    guessKillerLabel = Label(secondFrame, text="Who do you think the killer is? (Johnson/Bailey/Taylor)")
    guessKillerLabel.pack()
    global guessKillerEntry
    guessKillerEntry = Entry(secondFrame)
    guessKillerEntry.pack()
    guessKillerButton = Button(secondFrame, text="Submit", command=checkKillerFunction)
    guessKillerButton.pack()
    myCanvas.update_idletasks()
    myCanvas.yview_moveto('1')

# Check the user's guess
def checkKillerFunction():
    if guessKillerEntry.get().lower().strip() == "johnson":
        correctLabel = Label(secondFrame, text="\n\nYOU'RE RIGHT, CONGRATS!")
        correctLabel.pack()
    elif guessKillerEntry.get().lower().strip() == "bailey":
        incorrectLabel = Label(secondFrame, text="\n\nSorry, that's not correct. It was...\nBRADY JOHNSON")
        incorrectLabel.pack()
    elif guessKillerEntry.get().lower().strip() == "taylor":
        incorrectLabel = Label(secondFrame, text="\n\nSorry, that's not correct. It was...\nBRADY JOHNSON")
        incorrectLabel.pack()
    else:
        invalidFunction()
    thanksLabel = Label(secondFrame, text="\n\nThanks for playing.")
    thanksLabel.pack()
    myCanvas.update_idletasks()
    myCanvas.yview_moveto('1')
    sourcesFunction()

    


# List sources.
def sourcesFunction():
    sourcesLabel = Label(secondFrame, text="\nSources:\nhttps://www.ncbi.nlm.nih.gov/books/NBK556119/ \n https://www.ncbi.nlm.nih.gov/books/NBK556119/ \n https://www.fbi.gov/services/laboratory/scientific-analysis/trace-evidence and https://www.theguardian.com/science/2008/apr/27/genetics.cancer\n\n")
    sourcesLabel.pack()
    myCanvas.update_idletasks()
    myCanvas.yview_moveto('1')

# Introductory code, call greetingFunction
introLabel = Label(secondFrame, text="CSI Kim: Hi. I'm Kim, a local CSI. There's been a murder. Would you like to help investigate? (yes/no) ")
introLabel.pack()
introEntry = Entry(secondFrame)
introEntry.pack()
introButton = Button(secondFrame, text="Submit", command=beginFunction)
introButton.pack()
# Set evidence variable to zero
x = 0
# Initialize review variables
yesCoffee = 0
noCoffee = 0
examineMrTrauma = 0
examineMrsClothes = 0
examineMrsTrauma = 0
examineMrClothes = 0
searchTrash = 0
searchCloset = 0
searchBed = 0
searchKitchen = 0
sampleDNA = 0
sampleGun = 0
samplePowder = 0
labDeath = 0
labDNA = 0
labBlood = 0

root.mainloop()

