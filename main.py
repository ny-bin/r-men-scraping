
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
    if request_json and 'bucket_name' in request_json:
        print(request_json['bucket_name'])
        print(request_json['file_name'])
        return "post success!!"
    else:
        return "post failed!!"
