import requests
import zipfile
import os
from analytics.config import Config

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
        _import_survey(survey_id)


def _import_survey(survey_id):
    file_format = "csv"
    download_request_url = get_export_url()
    download_request_payload = '{"format":"' + file_format + '","surveyId":"' + survey_id + '"}'
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

