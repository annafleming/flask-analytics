import requests
import zipfile
import os
from analytics.config import Config
from .. import db


try:
    import simplejson as json
except ImportError:
    import json

headers = {
    "content-type": "application/json",
    "x-api-token": Config.QUALTRICS_API_TOKEN,
}


def import_surveys():
    for survey_id in Config.SURVEY_IDS:
        last_exported_id = get_last_imported_survey(Config.SURVEY_IDS[survey_id]['site'], Config.SURVEY_IDS[survey_id]['survey_type'])
        _import_survey(survey_id, last_exported_id)

def _import_survey(survey_id, last_exported_id):
    file_format = "csv"
    download_request_url = get_export_url()
    download_request_payload = '{"format":"' + file_format + '","surveyId":"' + survey_id + '","useLabels":true'
    if last_exported_id:
        download_request_payload = download_request_payload + ',"lastResponseId":"'+last_exported_id+'"'
    download_request_payload = download_request_payload + '}'
    download_request_response = requests.request("POST", download_request_url, data=download_request_payload,
                                                 headers=headers)
    progress_id = download_request_response.json()['result']['id']
    request_check_progress = 0

    while request_check_progress < 100:
        request_check_url = get_export_url() + progress_id
        request_check_response = requests.request("GET", request_check_url, headers=headers)
        request_check_progress = request_check_response.json()['result']['percentComplete']

    request_download_url = get_export_url() + progress_id + '/file'
    request_download = requests.request("GET", request_download_url, headers=headers, stream=True)

    with open("RequestFile.zip", "wb") as f:
        for chunk in request_download.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

    zipfile.ZipFile("RequestFile.zip").extractall("data")
    os.remove("RequestFile.zip")


def get_export_url():
    return "https://"+Config.QUALTRICS_DATA_CENTER_ID+".qualtrics.com/API/v3/responseexports/"


def get_last_imported_survey(site, survey_type):
    response = db.surveys.find_one({"$query": {'site': site, 'survey_type': survey_type},"$orderby": {"$natural": -1}})
    if response and 'ResponseID' in response:
        return response['ResponseID']
    else:
        return None