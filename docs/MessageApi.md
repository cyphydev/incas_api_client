# uiuc_incas_client.MessageApi

All URIs are relative to *https://incas.cs.illinois.edu/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**actor_enrichments_delete**](MessageApi.md#actor_enrichments_delete) | **DELETE** /actor/enrichments | 
[**message_enrichments_delete**](MessageApi.md#message_enrichments_delete) | **DELETE** /message/enrichments | 
[**message_enrichments_get**](MessageApi.md#message_enrichments_get) | **GET** /message/enrichments | 
[**message_enrichments_post**](MessageApi.md#message_enrichments_post) | **POST** /message/enrichments | 
[**message_enrichments_put**](MessageApi.md#message_enrichments_put) | **PUT** /message/enrichments | 
[**message_id_enrichments_delete**](MessageApi.md#message_id_enrichments_delete) | **DELETE** /message/{id}/enrichments | 
[**message_id_enrichments_get**](MessageApi.md#message_id_enrichments_get) | **GET** /message/{id}/enrichments | 
[**message_id_enrichments_post**](MessageApi.md#message_id_enrichments_post) | **POST** /message/{id}/enrichments | 
[**message_id_enrichments_put**](MessageApi.md#message_id_enrichments_put) | **PUT** /message/{id}/enrichments | 
[**message_id_get**](MessageApi.md#message_id_get) | **GET** /message/{id} | 


# **actor_enrichments_delete**
> actor_enrichments_delete()



Delete specific message enrichment meta by providerName, enrichmentName and version

### Example


```python
import time
import uiuc_incas_client
from uiuc_incas_client.api import message_api
from pprint import pprint
# Defining the host is optional and defaults to https://incas.cs.illinois.edu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = uiuc_incas_client.Configuration(
    host = "https://incas.cs.illinois.edu/api/v1"
)


# Enter a context with an instance of the API client
with uiuc_incas_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = message_api.MessageApi(api_client)
    enrichment_name = "category" # str |  (optional)
    provider_name = "providerName_example" # str |  (optional)
    version = "version_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.actor_enrichments_delete(enrichment_name=enrichment_name, provider_name=provider_name, version=version)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling MessageApi->actor_enrichments_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrichment_name** | **str**|  | [optional]
 **provider_name** | **str**|  | [optional]
 **version** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Deleted |  -  |
**404** | id not found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_enrichments_delete**
> message_enrichments_delete()



Delete specific message enrichment meta by providerName, enrichmentName and version

### Example


```python
import time
import uiuc_incas_client
from uiuc_incas_client.api import message_api
from pprint import pprint
# Defining the host is optional and defaults to https://incas.cs.illinois.edu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = uiuc_incas_client.Configuration(
    host = "https://incas.cs.illinois.edu/api/v1"
)


# Enter a context with an instance of the API client
with uiuc_incas_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = message_api.MessageApi(api_client)
    enrichment_name = "category" # str |  (optional)
    provider_name = "providerName_example" # str |  (optional)
    version = "version_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.message_enrichments_delete(enrichment_name=enrichment_name, provider_name=provider_name, version=version)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling MessageApi->message_enrichments_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrichment_name** | **str**|  | [optional]
 **provider_name** | **str**|  | [optional]
 **version** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Deleted |  -  |
**404** | id not found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_enrichments_get**
> MessageEnrichmentMeta message_enrichments_get()



Returns current message enrichment meta by providerName, enrichmentName and version

### Example


```python
import time
import uiuc_incas_client
from uiuc_incas_client.api import message_api
from uiuc_incas_client.model.message_enrichment_meta import MessageEnrichmentMeta
from pprint import pprint
# Defining the host is optional and defaults to https://incas.cs.illinois.edu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = uiuc_incas_client.Configuration(
    host = "https://incas.cs.illinois.edu/api/v1"
)


# Enter a context with an instance of the API client
with uiuc_incas_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = message_api.MessageApi(api_client)
    enrichment_name = "category" # str |  (optional)
    provider_name = "providerName_example" # str |  (optional)
    version = "version_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.message_enrichments_get(enrichment_name=enrichment_name, provider_name=provider_name, version=version)
        pprint(api_response)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling MessageApi->message_enrichments_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrichment_name** | **str**|  | [optional]
 **provider_name** | **str**|  | [optional]
 **version** | **str**|  | [optional]

### Return type

[**MessageEnrichmentMeta**](MessageEnrichmentMeta.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of message enrichment meta |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_enrichments_post**
> MessageEnrichmentMeta message_enrichments_post(message_enrichment_meta)



Creates message enrichment meta (post after all messages have been added)

### Example


```python
import time
import uiuc_incas_client
from uiuc_incas_client.api import message_api
from uiuc_incas_client.model.message_enrichment_meta import MessageEnrichmentMeta
from pprint import pprint
# Defining the host is optional and defaults to https://incas.cs.illinois.edu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = uiuc_incas_client.Configuration(
    host = "https://incas.cs.illinois.edu/api/v1"
)


# Enter a context with an instance of the API client
with uiuc_incas_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = message_api.MessageApi(api_client)
    message_enrichment_meta = [
        MessageEnrichmentMeta(None),
    ] # [MessageEnrichmentMeta] | The new enrichment meta to add

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.message_enrichments_post(message_enrichment_meta)
        pprint(api_response)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling MessageApi->message_enrichments_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_enrichment_meta** | [**[MessageEnrichmentMeta]**](MessageEnrichmentMeta.md)| The new enrichment meta to add |

### Return type

[**MessageEnrichmentMeta**](MessageEnrichmentMeta.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A list of newly added message enrichment meta |  -  |
**400** | Invalid input |  -  |
**409** | Input already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_enrichments_put**
> MessageEnrichmentMeta message_enrichments_put(message_enrichment_meta)



Updates message enrichment meta (after all messages have been added) by providerName, enrichmentName and version

### Example


```python
import time
import uiuc_incas_client
from uiuc_incas_client.api import message_api
from uiuc_incas_client.model.message_enrichment_meta import MessageEnrichmentMeta
from pprint import pprint
# Defining the host is optional and defaults to https://incas.cs.illinois.edu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = uiuc_incas_client.Configuration(
    host = "https://incas.cs.illinois.edu/api/v1"
)


# Enter a context with an instance of the API client
with uiuc_incas_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = message_api.MessageApi(api_client)
    message_enrichment_meta = [
        MessageEnrichmentMeta(None),
    ] # [MessageEnrichmentMeta] | The new enrichment meta to update
    enrichment_name = "category" # str |  (optional)
    provider_name = "providerName_example" # str |  (optional)
    version = "version_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.message_enrichments_put(message_enrichment_meta)
        pprint(api_response)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling MessageApi->message_enrichments_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.message_enrichments_put(message_enrichment_meta, enrichment_name=enrichment_name, provider_name=provider_name, version=version)
        pprint(api_response)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling MessageApi->message_enrichments_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_enrichment_meta** | [**[MessageEnrichmentMeta]**](MessageEnrichmentMeta.md)| The new enrichment meta to update |
 **enrichment_name** | **str**|  | [optional]
 **provider_name** | **str**|  | [optional]
 **version** | **str**|  | [optional]

### Return type

[**MessageEnrichmentMeta**](MessageEnrichmentMeta.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of newly added message enrichment meta |  -  |
**400** | Invalid input |  -  |
**409** | Input already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_id_enrichments_delete**
> message_id_enrichments_delete(id, enrichment_name, provider_name, version)



Delete the enrichments for specific message by type, providerName and version

### Example


```python
import time
import uiuc_incas_client
from uiuc_incas_client.api import message_api
from pprint import pprint
# Defining the host is optional and defaults to https://incas.cs.illinois.edu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = uiuc_incas_client.Configuration(
    host = "https://incas.cs.illinois.edu/api/v1"
)


# Enter a context with an instance of the API client
with uiuc_incas_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = message_api.MessageApi(api_client)
    id = "id_example" # str | Message ID
    enrichment_name = "category" # str | 
    provider_name = "providerName_example" # str | 
    version = "version_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.message_id_enrichments_delete(id, enrichment_name, provider_name, version)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling MessageApi->message_id_enrichments_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Message ID |
 **enrichment_name** | **str**|  |
 **provider_name** | **str**|  |
 **version** | **str**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Deleted |  -  |
**404** | id not found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_id_enrichments_get**
> [MessageEnrichment] message_id_enrichments_get(id)



Returns all visible matched enrichment for the specific message by type, providerName and version

### Example


```python
import time
import uiuc_incas_client
from uiuc_incas_client.api import message_api
from uiuc_incas_client.model.message_enrichment import MessageEnrichment
from pprint import pprint
# Defining the host is optional and defaults to https://incas.cs.illinois.edu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = uiuc_incas_client.Configuration(
    host = "https://incas.cs.illinois.edu/api/v1"
)


# Enter a context with an instance of the API client
with uiuc_incas_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = message_api.MessageApi(api_client)
    id = "id_example" # str | Message ID
    enrichment_name = "category" # str |  (optional)
    provider_name = "providerName_example" # str |  (optional)
    version = "version_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.message_id_enrichments_get(id)
        pprint(api_response)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling MessageApi->message_id_enrichments_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.message_id_enrichments_get(id, enrichment_name=enrichment_name, provider_name=provider_name, version=version)
        pprint(api_response)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling MessageApi->message_id_enrichments_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Message ID |
 **enrichment_name** | **str**|  | [optional]
 **provider_name** | **str**|  | [optional]
 **version** | **str**|  | [optional]

### Return type

[**[MessageEnrichment]**](MessageEnrichment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of message enrichments |  -  |
**404** | Not found |  -  |
**400** | Invalid query |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_id_enrichments_post**
> [MessageEnrichment] message_id_enrichments_post(id, message_enrichment)



Creates new enrichments for specific message

### Example


```python
import time
import uiuc_incas_client
from uiuc_incas_client.api import message_api
from uiuc_incas_client.model.message_enrichment import MessageEnrichment
from pprint import pprint
# Defining the host is optional and defaults to https://incas.cs.illinois.edu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = uiuc_incas_client.Configuration(
    host = "https://incas.cs.illinois.edu/api/v1"
)


# Enter a context with an instance of the API client
with uiuc_incas_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = message_api.MessageApi(api_client)
    id = "id_example" # str | Message ID
    message_enrichment = [
        MessageEnrichment(None),
    ] # [MessageEnrichment] | The new enrichment to add

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.message_id_enrichments_post(id, message_enrichment)
        pprint(api_response)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling MessageApi->message_id_enrichments_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Message ID |
 **message_enrichment** | [**[MessageEnrichment]**](MessageEnrichment.md)| The new enrichment to add |

### Return type

[**[MessageEnrichment]**](MessageEnrichment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A list of new message enrichments |  -  |
**400** | Invalid input |  -  |
**409** | Input already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_id_enrichments_put**
> [MessageEnrichment] message_id_enrichments_put(id, enrichment_name, provider_name, version, message_enrichment)



Update the enrichments for specific message by type, providerName and version

### Example


```python
import time
import uiuc_incas_client
from uiuc_incas_client.api import message_api
from uiuc_incas_client.model.message_enrichment import MessageEnrichment
from pprint import pprint
# Defining the host is optional and defaults to https://incas.cs.illinois.edu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = uiuc_incas_client.Configuration(
    host = "https://incas.cs.illinois.edu/api/v1"
)


# Enter a context with an instance of the API client
with uiuc_incas_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = message_api.MessageApi(api_client)
    id = "id_example" # str | Message ID
    enrichment_name = "category" # str | 
    provider_name = "providerName_example" # str | 
    version = "version_example" # str | 
    message_enrichment = [
        MessageEnrichment(None),
    ] # [MessageEnrichment] | The new enrichments to update

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.message_id_enrichments_put(id, enrichment_name, provider_name, version, message_enrichment)
        pprint(api_response)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling MessageApi->message_id_enrichments_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Message ID |
 **enrichment_name** | **str**|  |
 **provider_name** | **str**|  |
 **version** | **str**|  |
 **message_enrichment** | [**[MessageEnrichment]**](MessageEnrichment.md)| The new enrichments to update |

### Return type

[**[MessageEnrichment]**](MessageEnrichment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of updated message enrichments |  -  |
**404** | Not found |  -  |
**400** | Invalid query |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_id_get**
> UiucMessage message_id_get(id)



Returns specific message by id

### Example


```python
import time
import uiuc_incas_client
from uiuc_incas_client.api import message_api
from uiuc_incas_client.model.uiuc_message import UiucMessage
from pprint import pprint
# Defining the host is optional and defaults to https://incas.cs.illinois.edu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = uiuc_incas_client.Configuration(
    host = "https://incas.cs.illinois.edu/api/v1"
)


# Enter a context with an instance of the API client
with uiuc_incas_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = message_api.MessageApi(api_client)
    id = "id_example" # str | Message ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.message_id_get(id)
        pprint(api_response)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling MessageApi->message_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Message ID |

### Return type

[**UiucMessage**](UiucMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Required message |  -  |
**404** | Not found |  -  |
**400** | Invalid query |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

