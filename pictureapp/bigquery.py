from google.cloud import bigquery
from django.conf import settings
from django.core.files.storage import default_storage


def get_pictures(search_request):
    """Function sends request to BigQueryAPI

    Args:
        search_request String: your search request string.

    Returns:
        pictures Dict: dictionary of 0-10 strings contains:
        {
            'id': piture id from table,
            'filename': picture filename,
            'url': url to insert in your Django Template
        }.

    """    

    # Construct a BigQuery client object.
    client = bigquery.Client(credentials=settings.GS_CREDENTIALS)
    bucket_name = settings.GS_BUCKET_NAME
    query = """
        SELECT *
        FROM `solid-feat-305921.pictures.pictures_table`
        WHERE filename LIKE '%{}%'
        LIMIT 10;
    """.format(search_request)
    query_job = client.query(query)  # Make an API request.
    
    # Modify GS string 'image_location' to 'url' for using in templates
    pictures = [{
        "id": pic.id,
        "filename": pic.filename,
        "url": default_storage.url(pic.image_location.split(bucket_name)[1])
    } for pic in query_job]
    return pictures
