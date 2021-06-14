from google.cloud import storage
import os
import re
import hotpepper

import settings

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = settings.GCS_API


def get_scraping_task(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()
    if request_json and 'bucket_name' in request_json and 'file_name' in request_json:
        bucket_name = request_json['bucket_name']
        file_name = request_json['file_name']
        try:
            # 該当のファイルを取得
            storage_client = storage.Client()

            bucket = storage_client.bucket(bucket_name)
            blob = bucket.get_blob(file_name)
            file_text = blob.download_as_text()

            # スクレイピング処理
            site_info = re.match(r'(.+)/(.+)', file_name).groups()
            if site_info[0] == 'hotpepper':
                restaurant = hotpepper.HotPepper()
                restaurant.scrape_restaurant(file_text)

            print(blob)
            print("OK")

        except BaseException as e:
            print(e)

        return "post success!!"
    else:
        return "post failed!!"
