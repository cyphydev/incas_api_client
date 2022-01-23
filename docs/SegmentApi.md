# uiuc_incas_client.SegmentApi

All URIs are relative to *https://incas.cs.illinois.edu:8443/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**segment_collection_id_delete**](SegmentApi.md#segment_collection_id_delete) | **DELETE** /segmentCollection/{id} | 
[**segment_collection_id_get**](SegmentApi.md#segment_collection_id_get) | **GET** /segmentCollection/{id} | 
[**segment_collection_id_put**](SegmentApi.md#segment_collection_id_put) | **PUT** /segmentCollection/{id} | 
[**segment_collection_list_get**](SegmentApi.md#segment_collection_list_get) | **GET** /segmentCollection/list | 
[**segment_collection_post**](SegmentApi.md#segment_collection_post) | **POST** /segmentCollection | 

# **segment_collection_id_delete**
> segment_collection_id_delete(id)



Deletes the segment collection by id.

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = uiuc_incas_client.SegmentApi()
id = 'id_example' # str | Segment collection ID

try:
    api_instance.segment_collection_id_delete(id)
except ApiException as e:
    print("Exception when calling SegmentApi->segment_collection_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Segment collection ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **segment_collection_id_get**
> UiucSegmentCollection segment_collection_id_get(id)



Gets a segment collection by id.

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = uiuc_incas_client.SegmentApi()
id = 'id_example' # str | Segment collection ID

try:
    api_response = api_instance.segment_collection_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentApi->segment_collection_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Segment collection ID | 

### Return type

[**UiucSegmentCollection**](UiucSegmentCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **segment_collection_id_put**
> str segment_collection_id_put(body, id)



Update basic segment collection information by id.

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = uiuc_incas_client.SegmentApi()
body = uiuc_incas_client.UiucSegmentCollectionMeta() # UiucSegmentCollectionMeta | The segment collection meta
id = 'id_example' # str | Segment collection ID

try:
    api_response = api_instance.segment_collection_id_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentApi->segment_collection_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UiucSegmentCollectionMeta**](UiucSegmentCollectionMeta.md)| The segment collection meta | 
 **id** | **str**| Segment collection ID | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **segment_collection_list_get**
> list[str] segment_collection_list_get(collection_name=collection_name, provider_name=provider_name, version=version)



Return list of available segment collection keys by collectionName, providerName, and version.

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = uiuc_incas_client.SegmentApi()
collection_name = 'collection_name_example' # str |  (optional)
provider_name = 'provider_name_example' # str |  (optional)
version = 'version_example' # str |  (optional)

try:
    api_response = api_instance.segment_collection_list_get(collection_name=collection_name, provider_name=provider_name, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentApi->segment_collection_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**|  | [optional] 
 **provider_name** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **segment_collection_post**
> str segment_collection_post(body)



Add a new segment collection.

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = uiuc_incas_client.SegmentApi()
body = uiuc_incas_client.UiucSegmentCollectionMeta() # UiucSegmentCollectionMeta | The new segment collection to add

try:
    api_response = api_instance.segment_collection_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentApi->segment_collection_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UiucSegmentCollectionMeta**](UiucSegmentCollectionMeta.md)| The new segment collection to add | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

