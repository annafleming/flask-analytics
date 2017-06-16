import requests, zipfile, os, json
from analytics.config import Config
from .db_operations import fetch_last_survey

FILE_DIRECTORY = "data"
FILE_FORMAT = "csv"
ZIP_ARCHIVE_NAME = "RequestFile.zip"


def import_surveys():
    for survey_id in Config.SURVEY_IDS:
        last_exported_id = _get_last_imported_survey(Config.SURVEY_IDS[survey_id]['site'],
                                                     Config.SURVEY_IDS[survey_id]['survey_type'])
        _import_survey(survey_id, last_exported_id)


def _get_last_imported_survey(site, survey_type):
    response = fetch_last_survey(site, survey_type)
    if response and 'ResponseID' in response:
        return response['ResponseID']
    else:
        return None


def _import_survey(survey_id, last_exported_id):
    progress_id = _start_download(last_exported_id, survey_id)
    _monitor_progress(progress_id)
    _fetch_file(progress_id)
    _extract_file()


def _start_download(last_exported_id, survey_id):
    download_request_response = requests.request("POST",
                                                 _get_request_url(),
                                                 data=_compose_download_params(last_exported_id, survey_id),
                                                 headers=_get_headers())
    return download_request_response.json()['result']['id']


def _monitor_progress(progress_id):
    progress = 0
    while progress < 100:
        progress_check_url = _get_request_url() + progress_id
        progress_check_response = requests.request("GET", progress_check_url, headers=_get_headers())
        progress = progress_check_response.json()['result']['percentComplete']


def _fetch_file(progress_id):
    request_download_url = _get_request_url() + progress_id + '/file'
    request_download = requests.request("GET", request_download_url, headers=_get_headers(), stream=True)
    with open(ZIP_ARCHIVE_NAME, "wb") as f:
        for chunk in request_download.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)


def _extract_file():
    zipfile.ZipFile(ZIP_ARCHIVE_NAME).extractall(FILE_DIRECTORY)
    os.remove(ZIP_ARCHIVE_NAME)


def _get_headers():
    return {
        "content-type": "application/json",
        "x-api-token": Config.QUALTRICS_API_TOKEN,
    }


def _get_request_url():
    return "https://" + Config.QUALTRICS_DATA_CENTER_ID + ".qualtrics.com/API/v3/responseexports/"


def _compose_download_params(last_exported_id, survey_id):
    params = {
        "format": FILE_FORMAT,
        "surveyId": str(survey_id),
        "useLabels": True,
    }
    if last_exported_id:
        params["lastResponseId"] = str(last_exported_id)
    return json.dumps(params, separators=(',', ':'))


