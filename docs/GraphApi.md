# uiuc_incas_client.GraphApi

All URIs are relative to *https://incas.cs.illinois.edu/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**actor_actor_graph_get**](GraphApi.md#actor_actor_graph_get) | **GET** /actorActorGraph | 
[**actor_actor_graph_id_delete**](GraphApi.md#actor_actor_graph_id_delete) | **DELETE** /actorActorGraph/{id} | 
[**actor_actor_graph_id_get**](GraphApi.md#actor_actor_graph_id_get) | **GET** /actorActorGraph/{id} | 
[**actor_actor_graph_id_neighbor_get**](GraphApi.md#actor_actor_graph_id_neighbor_get) | **GET** /actorActorGraph/{id}/neighbor | 
[**actor_actor_graph_id_put**](GraphApi.md#actor_actor_graph_id_put) | **PUT** /actorActorGraph/{id} | 
[**actor_actor_graph_post**](GraphApi.md#actor_actor_graph_post) | **POST** /actorActorGraph | 
[**actor_message_graph_get**](GraphApi.md#actor_message_graph_get) | **GET** /actorMessageGraph | 
[**actor_message_graph_id_delete**](GraphApi.md#actor_message_graph_id_delete) | **DELETE** /actorMessageGraph/{id} | 
[**actor_message_graph_id_get**](GraphApi.md#actor_message_graph_id_get) | **GET** /actorMessageGraph/{id} | 
[**actor_message_graph_id_neighbor_get**](GraphApi.md#actor_message_graph_id_neighbor_get) | **GET** /actorMessageGraph/{id}/neighbor | 
[**actor_message_graph_id_put**](GraphApi.md#actor_message_graph_id_put) | **PUT** /actorMessageGraph/{id} | 
[**actor_message_graph_post**](GraphApi.md#actor_message_graph_post) | **POST** /actorMessageGraph | 
[**message_message_graph_get**](GraphApi.md#message_message_graph_get) | **GET** /messageMessageGraph | 
[**message_message_graph_id_delete**](GraphApi.md#message_message_graph_id_delete) | **DELETE** /messageMessageGraph/{id} | 
[**message_message_graph_id_get**](GraphApi.md#message_message_graph_id_get) | **GET** /messageMessageGraph/{id} | 
[**message_message_graph_id_neighbor_get**](GraphApi.md#message_message_graph_id_neighbor_get) | **GET** /messageMessageGraph/{id}/neighbor | 
[**message_message_graph_id_put**](GraphApi.md#message_message_graph_id_put) | **PUT** /messageMessageGraph/{id} | 
[**message_message_graph_post**](GraphApi.md#message_message_graph_post) | **POST** /messageMessageGraph | 


# **actor_actor_graph_get**
> str actor_actor_graph_get(provider_name, time_stamp)



Gets graph id by providerName, timestamp and version

### Example


```python
import time
import uiuc_incas_client
from uiuc_incas_client.api import graph_api
from pprint import pprint
# Defining the host is optional and defaults to https://incas.cs.illinois.edu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = uiuc_incas_client.Configuration(
    host = "https://incas.cs.illinois.edu/api/v1"
)


# Enter a context with an instance of the API client
with uiuc_incas_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = graph_api.GraphApi(api_client)
    provider_name = "providerName_example" # str | 
    time_stamp = "timeStamp_example" # str | 
    version = "version_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.actor_actor_graph_get(provider_name, time_stamp)
        pprint(api_response)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling GraphApi->actor_actor_graph_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.actor_actor_graph_get(provider_name, time_stamp, version=version)
        pprint(api_response)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling GraphApi->actor_actor_graph_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_name** | **str**|  |
 **time_stamp** | **str**|  |
 **version** | **str**|  | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Required graph id |  -  |
**404** | Not found |  -  |
**400** | Invalid query |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_actor_graph_id_delete**
> actor_actor_graph_id_delete(id)



Delete the specific graph by id

### Example


```python
import time
import uiuc_incas_client
from uiuc_incas_client.api import graph_api
from pprint import pprint
# Defining the host is optional and defaults to https://incas.cs.illinois.edu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = uiuc_incas_client.Configuration(
    host = "https://incas.cs.illinois.edu/api/v1"
)


# Enter a context with an instance of the API client
with uiuc_incas_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = graph_api.GraphApi(api_client)
    id = "id_example" # str | Graph ID

    # example passing only required values which don't have defaults set
    try:
        api_instance.actor_actor_graph_id_delete(id)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling GraphApi->actor_actor_graph_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Graph ID |

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

# **actor_actor_graph_id_get**
> [ActorActorGraph] actor_actor_graph_id_get(id)



Gets specific actor-actor graph information by id

### Example


```python
import time
import uiuc_incas_client
from uiuc_incas_client.api import graph_api
from uiuc_incas_client.model.actor_actor_graph import ActorActorGraph
from pprint import pprint
# Defining the host is optional and defaults to https://incas.cs.illinois.edu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = uiuc_incas_client.Configuration(
    host = "https://incas.cs.illinois.edu/api/v1"
)


# Enter a context with an instance of the API client
with uiuc_incas_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = graph_api.GraphApi(api_client)
    id = "id_example" # str | Graph ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.actor_actor_graph_id_get(id)
        pprint(api_response)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling GraphApi->actor_actor_graph_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Graph ID |

### Return type

[**[ActorActorGraph]**](ActorActorGraph.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Required graph |  -  |
**404** | Not found |  -  |
**400** | Invalid query |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_actor_graph_id_neighbor_get**
> [[UiucActor]] actor_actor_graph_id_neighbor_get(id, actor_id)



Gets the neighbors for specific node from specific graph by graph id and actor id

### Example


```python
import time
import uiuc_incas_client
from uiuc_incas_client.api import graph_api
from uiuc_incas_client.model.uiuc_actor import UiucActor
from pprint import pprint
# Defining the host is optional and defaults to https://incas.cs.illinois.edu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = uiuc_incas_client.Configuration(
    host = "https://incas.cs.illinois.edu/api/v1"
)


# Enter a context with an instance of the API client
with uiuc_incas_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = graph_api.GraphApi(api_client)
    id = "id_example" # str | Graph ID
    actor_id = "actorID_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.actor_actor_graph_id_neighbor_get(id, actor_id)
        pprint(api_response)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling GraphApi->actor_actor_graph_id_neighbor_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Graph ID |
 **actor_id** | **str**|  |

### Return type

**[[UiucActor]]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Required neigbours |  -  |
**404** | Not found |  -  |
**400** | Invalid query |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_actor_graph_id_put**
> ActorActorGraph actor_actor_graph_id_put(id, actor_actor_graph)



Update the specific actor-actor graph by id

### Example


```python
import time
import uiuc_incas_client
from uiuc_incas_client.api import graph_api
from uiuc_incas_client.model.actor_actor_graph import ActorActorGraph
from pprint import pprint
# Defining the host is optional and defaults to https://incas.cs.illinois.edu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = uiuc_incas_client.Configuration(
    host = "https://incas.cs.illinois.edu/api/v1"
)


# Enter a context with an instance of the API client
with uiuc_incas_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = graph_api.GraphApi(api_client)
    id = "id_example" # str | Graph ID
    actor_actor_graph = ActorActorGraph(None) # ActorActorGraph | The new graph to update

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.actor_actor_graph_id_put(id, actor_actor_graph)
        pprint(api_response)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling GraphApi->actor_actor_graph_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Graph ID |
 **actor_actor_graph** | [**ActorActorGraph**](ActorActorGraph.md)| The new graph to update |

### Return type

[**ActorActorGraph**](ActorActorGraph.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated graph |  -  |
**404** | Not found |  -  |
**400** | Invalid query |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_actor_graph_post**
> [ActorActorGraph] actor_actor_graph_post(actor_actor_graph)



Creates new graphs

### Example


```python
import time
import uiuc_incas_client
from uiuc_incas_client.api import graph_api
from uiuc_incas_client.model.actor_actor_graph import ActorActorGraph
from pprint import pprint
# Defining the host is optional and defaults to https://incas.cs.illinois.edu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = uiuc_incas_client.Configuration(
    host = "https://incas.cs.illinois.edu/api/v1"
)


# Enter a context with an instance of the API client
with uiuc_incas_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = graph_api.GraphApi(api_client)
    actor_actor_graph = [
        ActorActorGraph(None),
    ] # [ActorActorGraph] | The new graphs to add

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.actor_actor_graph_post(actor_actor_graph)
        pprint(api_response)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling GraphApi->actor_actor_graph_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **actor_actor_graph** | [**[ActorActorGraph]**](ActorActorGraph.md)| The new graphs to add |

### Return type

[**[ActorActorGraph]**](ActorActorGraph.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A list of new graphs |  -  |
**400** | Invalid input |  -  |
**409** | Input already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_message_graph_get**
> str actor_message_graph_get(provider_name, time_stamp)



Gets graph id by providerName, timestamp and version

### Example


```python
import time
import uiuc_incas_client
from uiuc_incas_client.api import graph_api
from pprint import pprint
# Defining the host is optional and defaults to https://incas.cs.illinois.edu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = uiuc_incas_client.Configuration(
    host = "https://incas.cs.illinois.edu/api/v1"
)


# Enter a context with an instance of the API client
with uiuc_incas_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = graph_api.GraphApi(api_client)
    provider_name = "providerName_example" # str | 
    time_stamp = "timeStamp_example" # str | 
    version = "version_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.actor_message_graph_get(provider_name, time_stamp)
        pprint(api_response)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling GraphApi->actor_message_graph_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.actor_message_graph_get(provider_name, time_stamp, version=version)
        pprint(api_response)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling GraphApi->actor_message_graph_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_name** | **str**|  |
 **time_stamp** | **str**|  |
 **version** | **str**|  | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Required graph id |  -  |
**404** | Not found |  -  |
**400** | Invalid query |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_message_graph_id_delete**
> actor_message_graph_id_delete(id)



Delete the specific graph by id

### Example


```python
import time
import uiuc_incas_client
from uiuc_incas_client.api import graph_api
from pprint import pprint
# Defining the host is optional and defaults to https://incas.cs.illinois.edu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = uiuc_incas_client.Configuration(
    host = "https://incas.cs.illinois.edu/api/v1"
)


# Enter a context with an instance of the API client
with uiuc_incas_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = graph_api.GraphApi(api_client)
    id = "id_example" # str | Graph ID

    # example passing only required values which don't have defaults set
    try:
        api_instance.actor_message_graph_id_delete(id)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling GraphApi->actor_message_graph_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Graph ID |

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

# **actor_message_graph_id_get**
> [ActorMessageGraph] actor_message_graph_id_get(id)



Gets specific actor-message graph information by id

### Example


```python
import time
import uiuc_incas_client
from uiuc_incas_client.api import graph_api
from uiuc_incas_client.model.actor_message_graph import ActorMessageGraph
from pprint import pprint
# Defining the host is optional and defaults to https://incas.cs.illinois.edu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = uiuc_incas_client.Configuration(
    host = "https://incas.cs.illinois.edu/api/v1"
)


# Enter a context with an instance of the API client
with uiuc_incas_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = graph_api.GraphApi(api_client)
    id = "id_example" # str | Graph ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.actor_message_graph_id_get(id)
        pprint(api_response)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling GraphApi->actor_message_graph_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Graph ID |

### Return type

[**[ActorMessageGraph]**](ActorMessageGraph.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Required graph |  -  |
**404** | Not found |  -  |
**400** | Invalid query |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_message_graph_id_neighbor_get**
> [[bool, date, datetime, dict, float, int, list, str, none_type]] actor_message_graph_id_neighbor_get(id)



Gets the neighbors for specific node from specific graph by graph id and message or actor id

### Example


```python
import time
import uiuc_incas_client
from uiuc_incas_client.api import graph_api
from pprint import pprint
# Defining the host is optional and defaults to https://incas.cs.illinois.edu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = uiuc_incas_client.Configuration(
    host = "https://incas.cs.illinois.edu/api/v1"
)


# Enter a context with an instance of the API client
with uiuc_incas_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = graph_api.GraphApi(api_client)
    id = "id_example" # str | Graph ID
    message_id = "messageID_example" # str |  (optional)
    actor_id = "actorID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.actor_message_graph_id_neighbor_get(id)
        pprint(api_response)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling GraphApi->actor_message_graph_id_neighbor_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.actor_message_graph_id_neighbor_get(id, message_id=message_id, actor_id=actor_id)
        pprint(api_response)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling GraphApi->actor_message_graph_id_neighbor_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Graph ID |
 **message_id** | **str**|  | [optional]
 **actor_id** | **str**|  | [optional]

### Return type

**[[bool, date, datetime, dict, float, int, list, str, none_type]]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Required neigbours |  -  |
**404** | Not found |  -  |
**400** | Invalid query |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_message_graph_id_put**
> ActorMessageGraph actor_message_graph_id_put(id, actor_message_graph)



Update the specific actor-message graph by id

### Example


```python
import time
import uiuc_incas_client
from uiuc_incas_client.api import graph_api
from uiuc_incas_client.model.actor_message_graph import ActorMessageGraph
from pprint import pprint
# Defining the host is optional and defaults to https://incas.cs.illinois.edu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = uiuc_incas_client.Configuration(
    host = "https://incas.cs.illinois.edu/api/v1"
)


# Enter a context with an instance of the API client
with uiuc_incas_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = graph_api.GraphApi(api_client)
    id = "id_example" # str | Graph ID
    actor_message_graph = ActorMessageGraph(None) # ActorMessageGraph | The new graph to update

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.actor_message_graph_id_put(id, actor_message_graph)
        pprint(api_response)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling GraphApi->actor_message_graph_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Graph ID |
 **actor_message_graph** | [**ActorMessageGraph**](ActorMessageGraph.md)| The new graph to update |

### Return type

[**ActorMessageGraph**](ActorMessageGraph.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated graph |  -  |
**404** | Not found |  -  |
**400** | Invalid query |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_message_graph_post**
> [ActorMessageGraph] actor_message_graph_post(actor_message_graph)



Creates new graphs

### Example


```python
import time
import uiuc_incas_client
from uiuc_incas_client.api import graph_api
from uiuc_incas_client.model.actor_message_graph import ActorMessageGraph
from pprint import pprint
# Defining the host is optional and defaults to https://incas.cs.illinois.edu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = uiuc_incas_client.Configuration(
    host = "https://incas.cs.illinois.edu/api/v1"
)


# Enter a context with an instance of the API client
with uiuc_incas_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = graph_api.GraphApi(api_client)
    actor_message_graph = [
        ActorMessageGraph(None),
    ] # [ActorMessageGraph] | The new graphs to add

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.actor_message_graph_post(actor_message_graph)
        pprint(api_response)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling GraphApi->actor_message_graph_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **actor_message_graph** | [**[ActorMessageGraph]**](ActorMessageGraph.md)| The new graphs to add |

### Return type

[**[ActorMessageGraph]**](ActorMessageGraph.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A list of new graphs |  -  |
**400** | Invalid input |  -  |
**409** | Input already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_message_graph_get**
> str message_message_graph_get(provider_name, time_stamp)



Gets graph id by providerName, timestamp and version

### Example


```python
import time
import uiuc_incas_client
from uiuc_incas_client.api import graph_api
from pprint import pprint
# Defining the host is optional and defaults to https://incas.cs.illinois.edu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = uiuc_incas_client.Configuration(
    host = "https://incas.cs.illinois.edu/api/v1"
)


# Enter a context with an instance of the API client
with uiuc_incas_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = graph_api.GraphApi(api_client)
    provider_name = "providerName_example" # str | 
    time_stamp = "timeStamp_example" # str | 
    version = "version_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.message_message_graph_get(provider_name, time_stamp)
        pprint(api_response)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling GraphApi->message_message_graph_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.message_message_graph_get(provider_name, time_stamp, version=version)
        pprint(api_response)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling GraphApi->message_message_graph_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_name** | **str**|  |
 **time_stamp** | **str**|  |
 **version** | **str**|  | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Required graph id |  -  |
**404** | Not found |  -  |
**400** | Invalid query |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_message_graph_id_delete**
> message_message_graph_id_delete(id)



Delete the specific graph by id

### Example


```python
import time
import uiuc_incas_client
from uiuc_incas_client.api import graph_api
from pprint import pprint
# Defining the host is optional and defaults to https://incas.cs.illinois.edu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = uiuc_incas_client.Configuration(
    host = "https://incas.cs.illinois.edu/api/v1"
)


# Enter a context with an instance of the API client
with uiuc_incas_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = graph_api.GraphApi(api_client)
    id = "id_example" # str | Graph ID

    # example passing only required values which don't have defaults set
    try:
        api_instance.message_message_graph_id_delete(id)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling GraphApi->message_message_graph_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Graph ID |

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

# **message_message_graph_id_get**
> [MessageMessageGraph] message_message_graph_id_get(id)



Gets specific message-message graph information by id

### Example


```python
import time
import uiuc_incas_client
from uiuc_incas_client.api import graph_api
from uiuc_incas_client.model.message_message_graph import MessageMessageGraph
from pprint import pprint
# Defining the host is optional and defaults to https://incas.cs.illinois.edu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = uiuc_incas_client.Configuration(
    host = "https://incas.cs.illinois.edu/api/v1"
)


# Enter a context with an instance of the API client
with uiuc_incas_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = graph_api.GraphApi(api_client)
    id = "id_example" # str | Graph ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.message_message_graph_id_get(id)
        pprint(api_response)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling GraphApi->message_message_graph_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Graph ID |

### Return type

[**[MessageMessageGraph]**](MessageMessageGraph.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Required graph |  -  |
**404** | Not found |  -  |
**400** | Invalid query |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_message_graph_id_neighbor_get**
> [[UiucMessage]] message_message_graph_id_neighbor_get(id, message_id)



Gets the neighbors for specific node from specific graph by graph id and message's id

### Example


```python
import time
import uiuc_incas_client
from uiuc_incas_client.api import graph_api
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
    api_instance = graph_api.GraphApi(api_client)
    id = "id_example" # str | Graph ID
    message_id = "messageID_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.message_message_graph_id_neighbor_get(id, message_id)
        pprint(api_response)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling GraphApi->message_message_graph_id_neighbor_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Graph ID |
 **message_id** | **str**|  |

### Return type

**[[UiucMessage]]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Required neigbours |  -  |
**404** | Not found |  -  |
**400** | Invalid query |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_message_graph_id_put**
> MessageMessageGraph message_message_graph_id_put(id, message_message_graph)



Update the specific message-message graph by id

### Example


```python
import time
import uiuc_incas_client
from uiuc_incas_client.api import graph_api
from uiuc_incas_client.model.message_message_graph import MessageMessageGraph
from pprint import pprint
# Defining the host is optional and defaults to https://incas.cs.illinois.edu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = uiuc_incas_client.Configuration(
    host = "https://incas.cs.illinois.edu/api/v1"
)


# Enter a context with an instance of the API client
with uiuc_incas_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = graph_api.GraphApi(api_client)
    id = "id_example" # str | Graph ID
    message_message_graph = MessageMessageGraph(None) # MessageMessageGraph | The new graph to update

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.message_message_graph_id_put(id, message_message_graph)
        pprint(api_response)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling GraphApi->message_message_graph_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Graph ID |
 **message_message_graph** | [**MessageMessageGraph**](MessageMessageGraph.md)| The new graph to update |

### Return type

[**MessageMessageGraph**](MessageMessageGraph.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated graph |  -  |
**404** | Not found |  -  |
**400** | Invalid query |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_message_graph_post**
> [MessageMessageGraph] message_message_graph_post(message_message_graph)



Creates new graphs

### Example


```python
import time
import uiuc_incas_client
from uiuc_incas_client.api import graph_api
from uiuc_incas_client.model.message_message_graph import MessageMessageGraph
from pprint import pprint
# Defining the host is optional and defaults to https://incas.cs.illinois.edu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = uiuc_incas_client.Configuration(
    host = "https://incas.cs.illinois.edu/api/v1"
)


# Enter a context with an instance of the API client
with uiuc_incas_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = graph_api.GraphApi(api_client)
    message_message_graph = [
        MessageMessageGraph(None),
    ] # [MessageMessageGraph] | The new graphs to add

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.message_message_graph_post(message_message_graph)
        pprint(api_response)
    except uiuc_incas_client.ApiException as e:
        print("Exception when calling GraphApi->message_message_graph_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_message_graph** | [**[MessageMessageGraph]**](MessageMessageGraph.md)| The new graphs to add |

### Return type

[**[MessageMessageGraph]**](MessageMessageGraph.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A list of new graphs |  -  |
**400** | Invalid input |  -  |
**409** | Input already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

