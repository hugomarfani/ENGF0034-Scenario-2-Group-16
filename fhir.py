import requests
from fhirResources import *


def add_resource(resource, resource_data_json):

  patient_end_point = f"{fhir_server_url}/{resource.resourceType}"

  try:
    response = requests.post(patient_end_point, json=resource_data_json)

    if response.status_code == 201:
      print(f"{resource.resourceType} added successfully")
    else:
      print(
          f"Failed to add {resource.resourceType} {response.status_code}:{response.text}"
      )

  except requests.exceptions.RequestException as RequestException:
    print(f"Error {RequestException}")


def retrieve_resource_data(patientID):
  try:
    response = requests.get(f"{fhir_server_url}/Patient/{patientID}")

    if response.status_code == 200:
      patient_data = response.json()
      return patient_data
    else:
      print(
          f"Failed to retrieve {patientID} {response.status_code}:{response.text}"
      )
      return None
  except requests.exceptions.RequestException as RequestException:
    print(f"Error retrieving data: {RequestException}")
    return None
