# uiuc_incas_client.ActorApi

All URIs are relative to *https://incas.cs.illinois.edu/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**actor_enrichments_get**](ActorApi.md#actor_enrichments_get) | **GET** /actor/enrichments | 
[**actor_enrichments_post**](ActorApi.md#actor_enrichments_post) | **POST** /actor/enrichments | 
[**actor_enrichments_put**](ActorApi.md#actor_enrichments_put) | **PUT** /actor/enrichments | 
[**actor_id_enrichments_delete**](ActorApi.md#actor_id_enrichments_delete) | **DELETE** /actor/{id}/enrichments | 
[**actor_id_enrichments_get**](ActorApi.md#actor_id_enrichments_get) | **GET** /actor/{id}/enrichments | 
[**actor_id_enrichments_post**](ActorApi.md#actor_id_enrichments_post) | **POST** /actor/{id}/enrichments | 
[**actor_id_enrichments_put**](ActorApi.md#actor_id_enrichments_put) | **PUT** /actor/{id}/enrichments | 
[**actor_id_get**](ActorApi.md#actor_id_get) | **GET** /actor/{id} | 


# **actor_enrichments_get**
> ActorEnrichmentMeta actor_enrichments_get()



Returns current actor enrichment meta by providerName, enrichmentName and version

### Example


```python
import time
import uiuc_incas_client
from uiuc_incas_client.api import actor_api
from uiuc_incas_client.model.actor_enrichment_meta import ActorEnrichmentMeta
from pprint import pprint
# Defining the host is optional and defaults to https://incas.cs.illinois.edu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = uiuc_incas_client.Configuration(
    host = "https://incas.cs.illinois.edu/api/v1"
)


# Enter a context with an instance of the API client
with uiuc_incas_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = actor_api.ActorApi(api_client)
    enrichment_name = "category" # str |  (optional)
    provider_name = "providerName_example" # str |  (optional)
    version = "version_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.actor_enrichments_get(enrichment_name=enrichment_name, provider_name=provider_name, version=version)
        pprint(api_response)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling ActorApi->actor_enrichments_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrichment_name** | **str**|  | [optional]
 **provider_name** | **str**|  | [optional]
 **version** | **str**|  | [optional]

### Return type

[**ActorEnrichmentMeta**](ActorEnrichmentMeta.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of actor enrichment meta |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_enrichments_post**
> ActorEnrichmentMeta actor_enrichments_post(actor_enrichment_meta)



Creates actor enrichment meta (post after all actors have been added)

### Example


```python
import time
import uiuc_incas_client
from uiuc_incas_client.api import actor_api
from uiuc_incas_client.model.actor_enrichment_meta import ActorEnrichmentMeta
from pprint import pprint
# Defining the host is optional and defaults to https://incas.cs.illinois.edu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = uiuc_incas_client.Configuration(
    host = "https://incas.cs.illinois.edu/api/v1"
)


# Enter a context with an instance of the API client
with uiuc_incas_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = actor_api.ActorApi(api_client)
    actor_enrichment_meta = [
        ActorEnrichmentMeta(None),
    ] # [ActorEnrichmentMeta] | The new enrichment meta to add

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.actor_enrichments_post(actor_enrichment_meta)
        pprint(api_response)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling ActorApi->actor_enrichments_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **actor_enrichment_meta** | [**[ActorEnrichmentMeta]**](ActorEnrichmentMeta.md)| The new enrichment meta to add |

### Return type

[**ActorEnrichmentMeta**](ActorEnrichmentMeta.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A list of newly added Actor enrichment meta |  -  |
**400** | Invalid input |  -  |
**409** | Input already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_enrichments_put**
> ActorEnrichmentMeta actor_enrichments_put(actor_enrichment_meta)



Updates actor enrichment meta (after all actors have been added) by providerName, enrichmentName and version

### Example


```python
import time
import uiuc_incas_client
from uiuc_incas_client.api import actor_api
from uiuc_incas_client.model.actor_enrichment_meta import ActorEnrichmentMeta
from pprint import pprint
# Defining the host is optional and defaults to https://incas.cs.illinois.edu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = uiuc_incas_client.Configuration(
    host = "https://incas.cs.illinois.edu/api/v1"
)


# Enter a context with an instance of the API client
with uiuc_incas_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = actor_api.ActorApi(api_client)
    actor_enrichment_meta = [
        ActorEnrichmentMeta(None),
    ] # [ActorEnrichmentMeta] | The new enrichment meta to update
    enrichment_name = "category" # str |  (optional)
    provider_name = "providerName_example" # str |  (optional)
    version = "version_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.actor_enrichments_put(actor_enrichment_meta)
        pprint(api_response)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling ActorApi->actor_enrichments_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.actor_enrichments_put(actor_enrichment_meta, enrichment_name=enrichment_name, provider_name=provider_name, version=version)
        pprint(api_response)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling ActorApi->actor_enrichments_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **actor_enrichment_meta** | [**[ActorEnrichmentMeta]**](ActorEnrichmentMeta.md)| The new enrichment meta to update |
 **enrichment_name** | **str**|  | [optional]
 **provider_name** | **str**|  | [optional]
 **version** | **str**|  | [optional]

### Return type

[**ActorEnrichmentMeta**](ActorEnrichmentMeta.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of newly added actor enrichment meta |  -  |
**400** | Invalid input |  -  |
**409** | Input already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_id_enrichments_delete**
> actor_id_enrichments_delete(id, enrichment_name, provider_name, version)



Delete the enrichments for specific actor by type, providerName and version

### Example


```python
import time
import uiuc_incas_client
from uiuc_incas_client.api import actor_api
from pprint import pprint
# Defining the host is optional and defaults to https://incas.cs.illinois.edu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = uiuc_incas_client.Configuration(
    host = "https://incas.cs.illinois.edu/api/v1"
)


# Enter a context with an instance of the API client
with uiuc_incas_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = actor_api.ActorApi(api_client)
    id = "id_example" # str | Actor ID
    enrichment_name = "category" # str | 
    provider_name = "providerName_example" # str | 
    version = "version_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.actor_id_enrichments_delete(id, enrichment_name, provider_name, version)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling ActorApi->actor_id_enrichments_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Actor ID |
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

# **actor_id_enrichments_get**
> [ActorEnrichment] actor_id_enrichments_get(id)



Returns all matched enrichment for the specific actor by type, providerName and version

### Example


```python
import time
import uiuc_incas_client
from uiuc_incas_client.api import actor_api
from uiuc_incas_client.model.actor_enrichment import ActorEnrichment
from pprint import pprint
# Defining the host is optional and defaults to https://incas.cs.illinois.edu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = uiuc_incas_client.Configuration(
    host = "https://incas.cs.illinois.edu/api/v1"
)


# Enter a context with an instance of the API client
with uiuc_incas_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = actor_api.ActorApi(api_client)
    id = "id_example" # str | Actor ID
    enrichment_name = "category" # str |  (optional)
    provider_name = "providerName_example" # str |  (optional)
    version = "version_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.actor_id_enrichments_get(id)
        pprint(api_response)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling ActorApi->actor_id_enrichments_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.actor_id_enrichments_get(id, enrichment_name=enrichment_name, provider_name=provider_name, version=version)
        pprint(api_response)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling ActorApi->actor_id_enrichments_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Actor ID |
 **enrichment_name** | **str**|  | [optional]
 **provider_name** | **str**|  | [optional]
 **version** | **str**|  | [optional]

### Return type

[**[ActorEnrichment]**](ActorEnrichment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of actor enrichments |  -  |
**404** | Not found |  -  |
**400** | Invalid query |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_id_enrichments_post**
> [ActorEnrichment] actor_id_enrichments_post(id, actor_enrichment)



Creates new enrichments for specific message

### Example


```python
import time
import uiuc_incas_client
from uiuc_incas_client.api import actor_api
from uiuc_incas_client.model.actor_enrichment import ActorEnrichment
from pprint import pprint
# Defining the host is optional and defaults to https://incas.cs.illinois.edu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = uiuc_incas_client.Configuration(
    host = "https://incas.cs.illinois.edu/api/v1"
)


# Enter a context with an instance of the API client
with uiuc_incas_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = actor_api.ActorApi(api_client)
    id = "id_example" # str | Actor ID
    actor_enrichment = [
        ActorEnrichment(None),
    ] # [ActorEnrichment] | The new enrichment to add

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.actor_id_enrichments_post(id, actor_enrichment)
        pprint(api_response)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling ActorApi->actor_id_enrichments_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Actor ID |
 **actor_enrichment** | [**[ActorEnrichment]**](ActorEnrichment.md)| The new enrichment to add |

### Return type

[**[ActorEnrichment]**](ActorEnrichment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A list of new actor enrichments |  -  |
**400** | Invalid input |  -  |
**409** | Input already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_id_enrichments_put**
> [ActorEnrichment] actor_id_enrichments_put(id, enrichment_name, provider_name, version, actor_enrichment)



Update the enrichments for specific actor by type, providerName and version

### Example


```python
import time
import uiuc_incas_client
from uiuc_incas_client.api import actor_api
from uiuc_incas_client.model.actor_enrichment import ActorEnrichment
from pprint import pprint
# Defining the host is optional and defaults to https://incas.cs.illinois.edu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = uiuc_incas_client.Configuration(
    host = "https://incas.cs.illinois.edu/api/v1"
)


# Enter a context with an instance of the API client
with uiuc_incas_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = actor_api.ActorApi(api_client)
    id = "id_example" # str | Message ID
    enrichment_name = "category" # str | 
    provider_name = "providerName_example" # str | 
    version = "version_example" # str | 
    actor_enrichment = [
        ActorEnrichment(None),
    ] # [ActorEnrichment] | The new enrichments to update

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.actor_id_enrichments_put(id, enrichment_name, provider_name, version, actor_enrichment)
        pprint(api_response)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling ActorApi->actor_id_enrichments_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Message ID |
 **enrichment_name** | **str**|  |
 **provider_name** | **str**|  |
 **version** | **str**|  |
 **actor_enrichment** | [**[ActorEnrichment]**](ActorEnrichment.md)| The new enrichments to update |

### Return type

[**[ActorEnrichment]**](ActorEnrichment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of updated actor enrichments |  -  |
**404** | Not found |  -  |
**400** | Invalid query |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_id_get**
> Actor actor_id_get(id)



Returns specific actor by id

### Example


```python
import time
import uiuc_incas_client
from uiuc_incas_client.api import actor_api
from uiuc_incas_client.model.actor import Actor
from pprint import pprint
# Defining the host is optional and defaults to https://incas.cs.illinois.edu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = uiuc_incas_client.Configuration(
    host = "https://incas.cs.illinois.edu/api/v1"
)


# Enter a context with an instance of the API client
with uiuc_incas_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = actor_api.ActorApi(api_client)
    id = "id_example" # str | Actor ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.actor_id_get(id)
        pprint(api_response)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling ActorApi->actor_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Actor ID |

### Return type

[**Actor**](Actor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of actor enrichments |  -  |
**404** | Not found |  -  |
**400** | Invalid query |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

