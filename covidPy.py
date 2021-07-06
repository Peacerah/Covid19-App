import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic import *
import sqlite3
from PyQt5.QtSql import *
#import secondpage
#import main_code
#import icons_rc
db = QSqlDatabase("QSQLITE")
db.setDatabaseName("data.sqlite")

db.open()
#query = QSqlQuery(db = db)
''' query.exec_(
    """
    CREATE TABLE "covid" ("PASSPORT_NO"	INTEGER,
    "FULL_NAME"	TEXT,
	"SOURCE_ADDRESS"	TEXT,
	"FROM_COUNTRY"	TEXT,
	"HOME_ADDRESS"	TEXT,
	"AGE"	INTEGER,
	"STATE_OF_ORIGIN"	TEXT,
	"TESTED"	TEXT,
	"TEST_DATE"	TEXT,
	"COVID_RESULT"	TEXT,
	"LOCATION_TWO_WEEKS_AGO"	TEXT,
	"KNOW_ANY_COVID19P"	TEXT,
    "RELATIONSHIP"	TEXT,
	"FEVER"	TEXT,
	"BREATHLESSNESS"	TEXT,
	"COUGH"	TEXT,
	"SORE_THROAT"	TEXT,
	"HEADACHE"	TEXT,
	"MUSLE_PAIN"	TEXT,
	"CHILLS"	TEXT,
	"LOST_TASTE"	TEXT,
	"PHONE_NO"	INTEGER,
	"SEX"	TEXT
    )
    
    
    
    """   
) '''

''' PASSPORT_NO = 1234
FULL_NAME = "Abdulazeez Abdulsalam Adekunle"
SOURCE_ADDRESS = "19, St. Mary Street, New-York City"
FROM_COUNTRY = "USA"
HOME_ADDRESS = "19, Adeola Adeagbo Street"
AGE = 25
STATE_OF_ORIGIN = "Oyo"
TESTED = "Yes"
TEST_DATE = "1/1/2020"
COVID_RESULT = "Negative"
LOCATION_TWO_WEEKS_AGO = "Nigeria"
KNOW_ANY_COVID19P = "Yes"
RELATIONSHIP = "Family"
FEVER = "Yes"
BREATHLESSNESS = "Yes"
COUGH = "Yes"
SORE_THROAT = "Yes"
HEADACHE = "Yes"
MUSLE_PAIN = "Yes"
CHILLS = "Yes"
LOST_TASTE = "No"
PHONE_NO = "No"
SEX = "Female"

query.exec_(
    f"""INSERT INTO covid(
        PASSPORT_NO,FULL_NAME,SOURCE_ADDRESS,FROM_COUNTRY,HOME_ADDRESS, AGE, STATE_OF_ORIGIN,TESTED,
        TEST_DATE,COVID_RESULT,LOCATION_TWO_WEEKS_AGO,KNOW_ANY_COVID19P,RELATIONSHIP,FEVER,
        BREATHLESSNESS ,COUGH ,SORE_THROAT ,HEADACHE,MUSLE_PAIN,CHILLS ,LOST_TASTE,
        PHONE_NO,RELATIONSHIP,SEX)
        VALUES ("{PASSPORT_NO}","{FULL_NAME}","{SOURCE_ADDRESS}","{FROM_COUNTRY}","{HOME_ADDRESS}","{AGE}",
        "{STATE_OF_ORIGIN}","{TESTED}","{TEST_DATE}","{COVID_RESULT}",
        "{LOCATION_TWO_WEEKS_AGO}","{KNOW_ANY_COVID19P}","{RELATIONSHIP}","{FEVER}","{BREATHLESSNESS}",
        "{COUGH}","{SORE_THROAT}","{HEADACHE}","{MUSLE_PAIN}","{CHILLS}","{LOST_TASTE}",
        "{PHONE_NO}","{RELATIONSHIP}","{SEX}")
     """
) '''





class Covid(QMainWindow):
    #FIRST, PREV, NEXT, LAST = range(4)
    def __init__(self, parent = None):
        super(Covid, self).__init__(parent)
        loadUi("covidUi.ui", self)
        
        self.country = ['USA', 'India', 'Brazil', 'France', 'Turkey', 'Russia', 'UK', 'Argentina', 'Italy', 'Colombia', 'Spain', 'Germany', 'Iran', 'Poland', 'Mexico', 'Ukraine', 'Indonesia', 'Peru', 'South', 'Netherlands', 'Czechia', 'Chile', 'Canada', 'Philippines', 'Iraq', 'Sweden', 'Belgium', 'Romania', 'Pakistan', 'Bangladesh', 'Portugal', 'Israel', 'Hungary', 'Japan', 'Jordan', 'Malaysia', 'Serbia', 'Switzerland', 'Austria', 'Nepal', 'UAE', 'Lebanon', 'Morocco', 'Saudi', 'Ecuador', 'Bolivia', 'Bulgaria', 'Greece', 'Kazakhstan', 'Belarus', 'Paraguay', 'Panama', 'Slovakia', 'Tunisia', 'Georgia', 'Uruguay', 'Croatia', 'Costa', 'Kuwait', 'Azerbaijan', 'Dominican Republic', 'Palestine', 'Denmark', 'Guatemala', 'Egypt', 'Lithuania', 'Ethiopia', 'Ireland', 'Venezuela', 'Bahrain', 'Slovenia', 'Oman', 'Moldova', 'Honduras', 'Sri Lanka', 'Thailand', 'Armenia', 'Qatar', 'Bosnia and Herzegovina', 'Libya', 'Kenya', 'Cuba', 'Nigeria', 'North Macedonia', 'S. Korea', 'Myanmar', 'Zambia', 'Latvia', 'Algeria', 'Albania', 'Estonia', 'Norway', 'Kyrgyzstan', 'Afghanistan', 'Uzbekistan', 'Mongolia', 'Montenegro', 'Ghana', 'Finland', 'China', 'Cameroon', 'El Salvador', 'Namibia', 'Uganda', 'Cyprus', 'Mozambique', 'Maldives', 'Luxembourg', 'Botswana', 'Singapore', 'Jamaica', 'Ivory Coast', 'Cambodia', 'Zimbabwe', 'Senegal', 'Madagascar', 'DRC', 'Angola', 'Sudan', 'Malawi', 'Rwanda', 'Cabo Verde', 'Trinidad and Tobago', 'Malta', 'Australia', 'RÃ©union', 'French Guiana', 'Syria', 'Gabon', 'Guinea', 'Suriname', 'Mauritania', 'Mayotte', 'Guyana', 'French Polynesia', 'Eswatini', 'Haiti', 'Papua New Guinea', 'Guadeloupe', 'Somalia', 'Seychelles', 'Mali', 'Taiwan', 'Vietnam', 'Andorra', 'Togo', 'Burkina Faso', 'Tajikistan', 'Belize', 'Bahamas', 'Congo', 'CuraÃ§ao', 'Martinique', 'Hong', 'Djibouti', 'Lesotho', 'Aruba', 'South Sudan', 'Timor-Leste', 'Equatorial Guinea', 'Benin', 'Nicaragua', 'CAR', 'Yemen', 'Iceland', 'Gambia', 'Eritrea', 'Niger', 'Burundi', 'Saint Lucia', 'San Marino', 'Sierra Leone', 'Chad', 'Gibraltar', 'Channel Islands', 'Barbados', 'Comoros', 'Guinea-Bissau', 'Liberia', 'Liechtenstein', 'Fiji', 'New', 'Sint', 'Monaco', 'Bermuda', 'Turks', 'Sao', 'St. Vincent Grenadines', 'Saint Martin', 'Laos', 'Bhutan', 'Mauritius', 'Caribbean Netherlands', 'Isle of Man', 'Antigua and Barbuda', 'St. Barth', 'Faeroe Islands', 'Diamond Princess', 'Cayman Islands', 'Tanzania', 'Wallis and Futuna', 'Saint Kitts and Nevis', 'British Virgin Islands', 'Brunei', 'Dominica', 'Grenada', 'New Caledonia', 'Anguilla', 'Falkland Islands', 'Macao', 'Greenland', 'Vatican City', 'Saint Pierre Miquelon', 'Montserrat', 'Solomon Islands', 'Western Sahara', 'MS Zaandam', 'Vanuatu', 'Marshall Islands', 'Samoa', 'Saint Helena', 'Micronesia']
        self.country_highRisk =  ['USA', 'India', 'Brazil', 'France', 'Turkey', 'Russia', 'UK', 'Argentina', 'Italy', 'Colombia', 'Spain', 'Germany', 'Iran', 'Poland', 'Mexico', 'Ukraine', 'Indonesia', 'Peru', 'South', 'Netherlands', 'Czechia', 'Chile', 'Canada', 'Philippines', 'Iraq', 'Sweden', 'Belgium', 'Romania', 'Pakistan', 'Bangladesh', 'Portugal', 'Israel', 'Hungary', 'Japan', 'Jordan', 'Malaysia', 'Serbia', 'Switzerland', 'Austria', 'Nepal', 'UAE', 'Lebanon', 'Morocco', 'Saudi', 'Ecuador', 'Bolivia', 'Bulgaria', 'Greece', 'Kazakhstan', 'Belarus', 'Paraguay', 'Panama', 'Slovakia', 'Tunisia', 'Georgia', 'Uruguay', 'Croatia', 'Costa', 'Kuwait', 'Azerbaijan', 'Dominican Republic', 'Palestine', 'Denmark', 'Guatemala', 'Egypt', 'Lithuania', 'Ethiopia', 'Ireland', 'Venezuela', 'Bahrain', 'Slovenia', 'Oman', 'Moldova', 'Honduras', 'Sri Lanka', 'Thailand', 'Armenia', 'Qatar', 'Bosnia and Herzegovina', 'Libya', 'Kenya', 'Cuba', 'Nigeria', 'North Macedonia', 'S. Korea', 'Myanmar', 'Zambia', 'Latvia', 'Algeria', 'Albania', 'Estonia', 'Norway', 'Kyrgyzstan', 'Afghanistan', 'Uzbekistan', 'Mongolia', 'Montenegro', 'Ghana', 'Finland', 'China', 'Cameroon', 'El Salvador', 'Namibia', 'Uganda', 'Cyprus', 'Mozambique', 'Maldives', 'Luxembourg', 'Botswana', 'Singapore', 'Jamaica', 'Ivory Coast', 'Cambodia', 'Zimbabwe', 'Senegal', 'Madagascar', 'DRC', 'Angola', 'Sudan', 'Malawi', 'Rwanda', 'Cabo Verde', 'Trinidad and Tobago', 'Malta', 'Australia', 'RÃ©union', 'French Guiana', 'Syria', 'Gabon', 'Guinea', 'Suriname', 'Mauritania', 'Mayotte', 'Guyana', 'French Polynesia', 'Eswatini', 'Haiti', 'Papua New Guinea', 'Guadeloupe', 'Somalia', 'Seychelles', 'Mali', 'Taiwan', 'Vietnam', 'Andorra', 'Togo', 'Burkina Faso', 'Tajikistan', 'Belize', 'Bahamas', 'Congo', 'CuraÃ§ao', 'Martinique', 'Hong', 'Djibouti', 'Lesotho', 'Aruba', 'South Sudan', 'Timor-Leste', 'Equatorial Guinea', 'Benin', 'Nicaragua', 'CAR', 'Yemen', 'Iceland', 'Gambia', 'Eritrea', 'Niger', 'Burundi', 'Saint Lucia', 'San Marino', 'Sierra Leone', 'Chad', 'Gibraltar', 'Channel Islands', 'Barbados', 'Comoros', 'Guinea-Bissau', 'Liberia', 'Liechtenstein', 'Fiji', 'New', 'Sint', 'Monaco', 'Bermuda', 'Turks', 'Sao', 'St. Vincent Grenadines', 'Saint Martin', 'Laos', 'Bhutan', 'Mauritius', 'Caribbean Netherlands', 'Isle of Man', 'Antigua and Barbuda', 'St. Barth', 'Faeroe Islands', 'Diamond Princess', 'Cayman Islands', 'Tanzania', 'Wallis and Futuna', 'Saint Kitts and Nevis', 'British Virgin Islands', 'Brunei', 'Dominica', 'Grenada', 'New Caledonia', 'Anguilla', 'Falkland Islands', 'Macao', 'Greenland', 'Vatican City', 'Saint Pierre Miquelon', 'Montserrat', 'Solomon Islands', 'Western Sahara', 'MS Zaandam', 'Vanuatu', 'Marshall Islands', 'Samoa', 'Saint Helena', 'Micronesia']
        self.Nstate = ['Abia', 'Adamawa', 'Akwa Ibom', 'Anambra', 'Bauchi', 'Bayelsa', 'Benue', 'Borno', 'Cross River', 'Delta', 'Ebonyi', 'Edo', 'Ekiti', 'Enugu', 'FCT', 'Gombe', 'Imo', 'Jigawa', 'Kaduna', 'Kano', 'Katsina', 'Kebbi', 'Kogi', 'Kwara', 'Lagos', 'Nasarawa', 'Niger', 'Ogun', 'Ondo', 'Osun', 'Oyo', 'Plateau', 'Rivers', 'Sokoto', 'Taraba', 'Yobe', 'Zamfara']
        self.ageComboBox.addItems([str(x) for x in range(1,300)])
        self.immediateSourceCountryComboBox.addItems(self.country)
        self.whereTwoWeeksAgoComboBox.addItems(self.country)
        self.stateOriginComboBox.addItems(self.Nstate)
        
        
        
        
        self.model = QSqlTableModel(db=db)
        self.mapper = QDataWidgetMapper(self)
        self.mapper.setModel(self.model)

        
        #self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)        
        self.mapper.addMapping(self.passportEdit, 0) #PASSPORT_NO
        self.mapper.addMapping(self.nameEdit,1 ) #NAME
        self.mapper.addMapping(self.sourceCountryHomeAddressEdit, 2) #SOURCE_ADDRESS
        self.mapper.addMapping(self.immediateSourceCountryComboBox,3 ) #FROM_COUNTRY
        self.mapper.addMapping(self.nigeriaHomeAddressEdit, 4) #HOME_ADDRESS
        self.mapper.addMapping(self.ageComboBox, 5) #AGE
        self.mapper.addMapping(self.stateOriginComboBox, 6) #STATE_OF_ORIGIN
        self.mapper.addMapping(self.haveDoneCovidTestComboBox, 7) #TESTED
        self.mapper.addMapping(self.lastTestDateEdit, 8) #TEST_DATE
        self.mapper.addMapping(self.lastTestResultComboBox, 9) #COVID_RESULT
        self.mapper.addMapping(self.whereTwoWeeksAgoComboBox, 10) #LOCATION_TWO_WEEKS_AGO
        self.mapper.addMapping(self.knowCovidPatientComboBox,11 )#kNOW_ANY_COVID19P
        self.mapper.addMapping(self.relatedWithCovPatientComboBox,12 )#RELATIONSHIP
        self.mapper.addMapping(self.feverishComboBox,13 )#FEVER        
        self.mapper.addMapping(self.breathlessnessComboBox,14 )#BREATHLESSNESS
        self.mapper.addMapping(self.coughComboBox,15 ) #COUGH
        self.mapper.addMapping(self.soreThroatComboBox,16 ) #SORE_THROAT
        self.mapper.addMapping(self.headacheComboBox,17 )  #HEADACHE
        self.mapper.addMapping(self.muslePainComboBox,18 ) #MUSLE_PAIN
        self.mapper.addMapping(self.chillsComboBox,19 ) #CHILLS
        self.mapper.addMapping(self.lostTasteComboBox,20 ) #LOST_TASTE
        self.mapper.addMapping(self.nigeriaPhoneNoEdit, 21 ) #PHONE_NO
        self.mapper.addMapping(self.sexComboBox, 22 )#RELATIONSHIP 
        self.mapper.addMapping(self.photoLabel, 23,b"self.ba" )
        #self.mapper.addMapping(self.feverishComboBox, FEVER)
        self.model.setTable("covid")
        self.model.select()
        self.mapper.toFirst()

        #connection of buttons to slots
        self.firstButton.clicked.connect(self.mapper.toFirst)
        self.prevButton.clicked.connect(self.mapper.toPrevious)
        self.nextButton.clicked.connect(self.mapper.toNext)
        self.lastButton.clicked.connect(self.mapper.toLast)
        self.addButton.clicked.connect(self.mapper.submit)
        self.deleteButton.clicked.connect(self.deleteRecord)
        self.refreshButton.clicked.connect(self.refreshAll)
        self.uploadPhotoButton.clicked.connect(self.uploadPhoto)
        self.predictButton.clicked.connect(self.predict)
        
        

        
        
        
        
        
        
    def showMessage(self, title, text):
        mesgbox = QMessageBox()
        mesgbox.setIcon(QMessageBox.Information)
        mesgbox.setWindowTitle(title)
        mesgbox.setText(text)
        mesgbox.setStandardButtons(QMessageBox.Ok)
        mesgbox.exec_()  
        
    def uploadPhoto(self):
        self.photFilename = QFileDialog.getOpenFileName(self, "Upload photo","c\\","Image Files(*.png *.jpg *bmp)")
        #self.photFilename = QFileDialog.getOpenFileName(self, "Upload photo",QDir.currentPath(),"Image Files(*.png *.jpg *bmp)")
        pixmap = QPixmap(str(self.photFilename[0]))
        self.photoLabel.setPixmap(pixmap)
        if  self.photFilename:
            self.saveImage(self.photFilename[0])
        #pixmap = QPixmap(str(self.photFilename))    
        #pixmap = QPixmap(str(self.photFilename[0]))
        
        
    def saveImage(self, filename):
        file = QFile(filename)
        if not file.open(QIODevice.ReadOnly):
            return
        self.ba = file.readAll()
        
        
    


    def saveRecord(self, where):
        row = self.mapper.currentIndex()
        self.mapper.submit()
        if where == Covid.FIRST:
            row = 0
        elif where == Covid.PREV:
            row = 0 if row <= 1 else row - 1
        elif where == Covid.NEXT:
            row += 1
        if row >= self.model.rowCount():
            row = self.model.rowCount() - 1
        elif where == Covid.LAST:
            row = self.model.rowCount() - 1
            self.mapper.setCurrentIndex(row)
        
        
    def addRecord(self):
        row = self.model.rowCount()
        self.mapper.submit()
        self.model.insertRow(row)
        self.mapper.setCurrentIndex(row)
        self.showMessage("Add Record","Record added sucessfully")
        #now = QDateTime.currentDateTime()
        
    def refreshAll(self):
        self.passportEdit.setText(" ")
        self.nameEdit.setText(" ") #NAME
        self.sourceCountryHomeAddressEdit.setText(" ") #SOURCE_ADDRESS
        self.nigeriaHomeAddressEdit.setText(" ") #HOME_ADDRESS
        self.nigeriaPhoneNoEdit.setText(" ") #PHONE_NO

        
    def closeEvent(self, event):
        self.mapper.submit()
        reply = QMessageBox.question(self, "Message", "Are you sure you want to close the Window?", QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        
    def deleteRecord(self):
        p = self.passportEdit.text()
        n = self.nameEdit.text()
        if QMessageBox.question(self,"Delete",f"Delete record of {n} with Passport no. {p}?",QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
            return
    
        row = self.mapper.currentIndex()
        self.model.removeRow(row)
        self.model.submitAll()
        if row + 1 >= self.model.rowCount():
            row = self.model.rowCount() - 1
        self.mapper.setCurrentIndex(row)
    
    ''' def predict(self):
        if ((haveDoneCovidTestComboBox.currentText()=='Yes'or haveDoneCovidTestComboBox.currentText()=='No') and (lastTestResultComboBox.currentText()=='Negative') and(knowCovidPatientComboBox.currentText()=='Yes'or knowCovidPatientComboBox.currentText()=='No')and(relatedWithCovPatientComboBox.currentText()=='Family'or relatedWithCovPatientComboBox.currentText()=='Intimate friend')and(feverishComboBox.currentText()=='Yes'or feverishComboBox.currentText==()=='No')and(breathlessnessComboBox.currentText()=='Yes'or breathlessnessComboBox.currentText()=='No')and(coughComboBox.currentText()=='Yes'or coughComboBox.currentText()=='No')and(soreThroatComboBox.currentText()=='Yes'or soreThroatComboBox.currentText()=='No')and(headacheComboBox.currentText()=='Yes'or headacheComboBox.currentText()=='No')and(muslePainComboBox.currentText()=='Yes'or muslePainComboBox.currentText()=='No')and(chillsComboBox.currentText()=='Yes'or chillsComboBox.currentText()=='No')and(lostTasteComboBox.currentText()=='Yes'or lostTasteComboBox.currentText()=='No')and(immediateSourceCountryComboBox.currentText() in self.country[:28])):
            predictOutput = "High Covid19 Risk"
            print(predictOutput)
        elif ((haveDoneCovidTestComboBox.currentText()=='Yes'or haveDoneCovidTestComboBox.currentText()=='No') and (lastTestResultComboBox.currentText()=='Negative') and(knowCovidPatientComboBox.currentText()=='Yes'or knowCovidPatientComboBox.currentText()=='No')and(relatedWithCovPatientComboBox.currentText()=='Ordnary friend'or relatedWithCovPatientComboBox.currentText()=='Business Partner')and(feverishComboBox.currentText()=='Yes'or feverishComboBox.currentText()=='No')and(breathlessnessComboBox.currentText()=='Yes'or breathlessnessComboBox.currentText()=='No')and(coughComboBox.currentText()=='Yes'or coughComboBox.currentText()=='No')and(soreThroatComboBox.currentText()=='Yes'or soreThroatComboBox.currentText()=='No')and(headacheComboBox.currentText()=='Yes'or headacheComboBox.currentText()=='No')and(muslePainComboBox.currentText()=='Yes'or muslePainComboBox.currentText()=='No')and(chillsComboBox.currentText()=='Yes'or chillsComboBox.currentText()=='No')and(lostTasteComboBox.currentText()=='Yes'or lostTasteComboBox.currentText()=='No')and(immediateSourceCountryComboBox.currentText in self.country[28:196])):
            predictOutput = "Medium Covid19 Risk"
            print(predictOutput)
           
        elif ((haveDoneCovidTestComboBox.currentText()=='Yes'or haveDoneCovidTestComboBox.currentText()=='No') and (lastTestResultComboBox.currentText()=='Negative') and(knowCovidPatientComboBox.currentText()=='Yes'or knowCovidPatientComboBox.currentText()=='No')and(relatedWithCovPatientComboBox.currentText()=='No relationship')and(feverishComboBox.currentText()=='Yes'or feverishComboBox.currentText()=='No')and(breathlessnessComboBox.currentText()=='Yes'or breathlessnessComboBox.currentText()=='No')and(coughComboBox.currentText()=='Yes'or coughComboBox.currentText()=='No')and(soreThroatComboBox.currentText()=='Yes'or soreThroatComboBox.currentText()=='No')and(headacheComboBox.currentText()=='Yes'or headacheComboBox.currentText()=='No')and(muslePainComboBox.currentText()=='Yes'or muslePainComboBox.currentText()=='No')and(chillsComboBox.currentText()=='Yes'or chillsComboBox.currentText()=='No')and(lostTasteComboBox.currentText()=='Yes'or lostTasteComboBox.currentText()=='No')and(immediateSourceCountryComboBox.currentText() in self.country[196:])):
            predictOutput = "Low Covid19 Risk"
            print(predictOutput)
            
        self.showMessage("Covid19 Risk Predict",f"{nameEdit.text()} might have been exposed to {predictOutput}") '''
            
        ##
    def predict(self):
        if self.lastTestResultComboBox.currentText() == "Positive":
            predictOutput = "has been tested covid19 positive\n, kindly put in a special quarantine"
        elif ((self.haveDoneCovidTestComboBox.currentText()=='Yes'or self.haveDoneCovidTestComboBox.currentText()=='No') and (self.lastTestResultComboBox.currentText()=='Negative') and(self.knowCovidPatientComboBox.currentText()=='Yes'or self.knowCovidPatientComboBox.currentText()=='No')and(self.relatedWithCovPatientComboBox.currentText()=='Family'or self.relatedWithCovPatientComboBox.currentText()=='Intimate friend')and(self.feverishComboBox.currentText()=='Yes'or self.feverishComboBox.currentText==()=='No')and(self.breathlessnessComboBox.currentText()=='Yes'or self.breathlessnessComboBox.currentText()=='No')and(self.coughComboBox.currentText()=='Yes'or self.coughComboBox.currentText()=='No')and(self.soreThroatComboBox.currentText()=='Yes'or self.soreThroatComboBox.currentText()=='No')and(self.headacheComboBox.currentText()=='Yes'or self.headacheComboBox.currentText()=='No')and(self.muslePainComboBox.currentText()=='Yes'or self.muslePainComboBox.currentText()=='No')and(self.chillsComboBox.currentText()=='Yes'or self.chillsComboBox.currentText()=='No')and(self.lostTasteComboBox.currentText()=='Yes'or self.lostTasteComboBox.currentText()=='No')and(self.immediateSourceCountryComboBox.currentText() in self.country[:28])):
            predictOutput = "might have been exposed to high Covid19 Risk"
            print(predictOutput)
        elif ((self.haveDoneCovidTestComboBox.currentText()=='Yes'or self.haveDoneCovidTestComboBox.currentText()=='No') and (self.lastTestResultComboBox.currentText()=='Negative') and(self.knowCovidPatientComboBox.currentText()=='Yes'or self.knowCovidPatientComboBox.currentText()=='No')and(self.relatedWithCovPatientComboBox.currentText()=='Ordnary friend'or self.relatedWithCovPatientComboBox.currentText()=='Business Partner')and(self.feverishComboBox.currentText()=='Yes'or self.feverishComboBox.currentText()=='No')and(self.breathlessnessComboBox.currentText()=='Yes'or self.breathlessnessComboBox.currentText()=='No')and(self.coughComboBox.currentText()=='Yes'or self.coughComboBox.currentText()=='No')and(self.soreThroatComboBox.currentText()=='Yes'or self.soreThroatComboBox.currentText()=='No')and(self.headacheComboBox.currentText()=='Yes'or self.headacheComboBox.currentText()=='No')and(self.muslePainComboBox.currentText()=='Yes'or self.muslePainComboBox.currentText()=='No')and(self.chillsComboBox.currentText()=='Yes'or self.chillsComboBox.currentText()=='No')and(self.lostTasteComboBox.currentText()=='Yes'or self.lostTasteComboBox.currentText()=='No')and(self.immediateSourceCountryComboBox.currentText in self.country[28:196])):
            predictOutput = "might have been exposed to medium Covid19 Risk"
            print(predictOutput)
           
        elif ((self.haveDoneCovidTestComboBox.currentText()=='Yes'or self.haveDoneCovidTestComboBox.currentText()=='No') and (self.lastTestResultComboBox.currentText()=='Negative') and(self.knowCovidPatientComboBox.currentText()=='Yes'or self.knowCovidPatientComboBox.currentText()=='No')and(self.relatedWithCovPatientComboBox.currentText()=='No relationship')and(self.feverishComboBox.currentText()=='Yes'or self.feverishComboBox.currentText()=='No')and(self.breathlessnessComboBox.currentText()=='Yes'or self.breathlessnessComboBox.currentText()=='No')and(self.coughComboBox.currentText()=='Yes'or self.coughComboBox.currentText()=='No')and(self.soreThroatComboBox.currentText()=='Yes'or self.soreThroatComboBox.currentText()=='No')and(self.headacheComboBox.currentText()=='Yes'or self.headacheComboBox.currentText()=='No')and(self.muslePainComboBox.currentText()=='Yes'or self.muslePainComboBox.currentText()=='No')and(self.chillsComboBox.currentText()=='Yes'or self.chillsComboBox.currentText()=='No')and(self.lostTasteComboBox.currentText()=='Yes'or self.lostTasteComboBox.currentText()=='No')and(self.immediateSourceCountryComboBox.currentText() in self.country[196:])):
            predictOutput = "might have been exposed to low Covid19 Risk"
            print(predictOutput)
        else:
            predictOutput = "has an usual feelings to covid19 sympthoms"
            
        self.showMessage("Covid19 Risk Predict",(self.nameEdit.text() +" "+ predictOutput))
        
        ##
        
        
        
        
        
        
        


if __name__ =="__main__":
    app = QApplication(sys.argv)
    screen = Covid()
    screen.show()
    sys.exit(app.exec_())