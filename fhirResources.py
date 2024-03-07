#FHIR server base URL
fhir_server_url = "https://hapi.fhir.org/baseR4"

class FHIRResource:
  def __init__(self,resourceType,patientID):
    self.resourceType = resourceType
    self.patientID = patientID

#classes for some of the FHIR resources
# FHIR resources include many things, but these three were chose for our project
class Patient(FHIRResource):
  def __init__(self, patientID, name, familyName, gender, birthdate, idWithServer = ""):
    super().__init__("Patient",patientID)
    self.idWithServer = idWithServer
    self.name = name
    self.familyName = familyName
    self.gender = gender
    self.birthdate = birthdate

  def get_patient_json(self):
    patient_json = {
      "resourceType": "Patient",
      "identifier":[{
          "system": f"{fhir_server_url}/patient-id",
          "value":self.patientID
        }],
      "name":[{
        "family":self.familyName,
        "given":[self.name]
      }],
      "gender":self.gender,
      "birthDate":self.birthdate
    }
    return patient_json

class Observation(FHIRResource): #the class might be superfluous
  def __init__(self, status, code, valueQuantity, date, patientID, idWithServer = ""):
    super().__init__("Observation", patientID)
    self.status = status

    #code should be a list containing a list coding and corresponding text
     #-> [[system, code, display], text],
      #e.g. [["https://loinc.org","789-8","Erythrocytes count"],"Erythrocytes in Blood by Automated count"]
    self.code = code

    #valueQuantity should be a list -> [value, unit, system, code]
     #e.g. [120,"mmHg","hhtp://unitsofmeasure.org","mm[Hg]"]
    self.valueQuantity = valueQuantity

    self.date = date

  def get_observation_json(self):
    observation_json = {
      "resourceType":"Observation",
      "code":{
        "coding":[{
          "system":self.code[0][0],
          "code":self.code[0][1],
          "display":self.code[0][2]
        }],
      "text":self.code[1]
      },
      "valueQuantity":{
        "value":self.valueQuantity[0],
        "unit":self.valueQuantity[1],
        "system":self.valueQuantity[2],
        "code":self.valueQuantity[3]
      },
      "subject":{
        "reference":f"Patient/{self.patientID}"
      },
      "effectiveDateTime":self.date
    }

    return observation_json

#attributes to consider: 
#class Condition(FHIRResource):
#  def __init__(self,patientID, '''attributes according to FHIR standard for Condition resource'''):
#    pass

class Condition(FHIRResource):
  def __init__(self, ):
    pass
  