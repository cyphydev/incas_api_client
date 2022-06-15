# uiuc_incas_client.GraphApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**actor_actor_graph_id_delete**](GraphApi.md#actor_actor_graph_id_delete) | **DELETE** /actorActorGraph/{id} | 
[**actor_actor_graph_id_get**](GraphApi.md#actor_actor_graph_id_get) | **GET** /actorActorGraph/{id} | 
[**actor_actor_graph_id_neighbor_get**](GraphApi.md#actor_actor_graph_id_neighbor_get) | **GET** /actorActorGraph/{id}/neighbor | 
[**actor_actor_graph_id_put**](GraphApi.md#actor_actor_graph_id_put) | **PUT** /actorActorGraph/{id} | 
[**actor_actor_graph_list_get**](GraphApi.md#actor_actor_graph_list_get) | **GET** /actorActorGraph/list | 
[**actor_actor_graph_post**](GraphApi.md#actor_actor_graph_post) | **POST** /actorActorGraph | 
[**actor_message_graph_id_delete**](GraphApi.md#actor_message_graph_id_delete) | **DELETE** /actorMessageGraph/{id} | 
[**actor_message_graph_id_get**](GraphApi.md#actor_message_graph_id_get) | **GET** /actorMessageGraph/{id} | 
[**actor_message_graph_id_neighbor_get**](GraphApi.md#actor_message_graph_id_neighbor_get) | **GET** /actorMessageGraph/{id}/neighbor | 
[**actor_message_graph_id_put**](GraphApi.md#actor_message_graph_id_put) | **PUT** /actorMessageGraph/{id} | 
[**actor_message_graph_list_get**](GraphApi.md#actor_message_graph_list_get) | **GET** /actorMessageGraph/list | 
[**actor_message_graph_post**](GraphApi.md#actor_message_graph_post) | **POST** /actorMessageGraph | 
[**message_message_graph_id_delete**](GraphApi.md#message_message_graph_id_delete) | **DELETE** /messageMessageGraph/{id} | 
[**message_message_graph_id_get**](GraphApi.md#message_message_graph_id_get) | **GET** /messageMessageGraph/{id} | 
[**message_message_graph_id_neighbor_get**](GraphApi.md#message_message_graph_id_neighbor_get) | **GET** /messageMessageGraph/{id}/neighbor | 
[**message_message_graph_id_put**](GraphApi.md#message_message_graph_id_put) | **PUT** /messageMessageGraph/{id} | 
[**message_message_graph_list_get**](GraphApi.md#message_message_graph_list_get) | **GET** /messageMessageGraph/list | 
[**message_message_graph_post**](GraphApi.md#message_message_graph_post) | **POST** /messageMessageGraph | 

# **actor_actor_graph_id_delete**
> actor_actor_graph_id_delete(id)



Delete the specific graph by id.

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = uiuc_incas_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = uiuc_incas_client.GraphApi(uiuc_incas_client.ApiClient(configuration))
id = 'id_example' # str | Graph ID

try:
    api_instance.actor_actor_graph_id_delete(id)
except ApiException as e:
    print("Exception when calling GraphApi->actor_actor_graph_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Graph ID | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_actor_graph_id_get**
> ActorActorGraph actor_actor_graph_id_get(id)



Gets specific actor-actor graph information by id.

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = uiuc_incas_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = uiuc_incas_client.GraphApi(uiuc_incas_client.ApiClient(configuration))
id = 'id_example' # str | Graph ID

try:
    api_response = api_instance.actor_actor_graph_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->actor_actor_graph_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Graph ID | 

### Return type

[**ActorActorGraph**](ActorActorGraph.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_actor_graph_id_neighbor_get**
> list[GraphEdge] actor_actor_graph_id_neighbor_get(id, actor_id)



Gets the neighbors for specific node from specific graph by graph id and actor id.

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = uiuc_incas_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = uiuc_incas_client.GraphApi(uiuc_incas_client.ApiClient(configuration))
id = 'id_example' # str | Graph ID
actor_id = 'actor_id_example' # str | 

try:
    api_response = api_instance.actor_actor_graph_id_neighbor_get(id, actor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->actor_actor_graph_id_neighbor_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Graph ID | 
 **actor_id** | **str**|  | 

### Return type

[**list[GraphEdge]**](GraphEdge.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_actor_graph_id_put**
> str actor_actor_graph_id_put(body, id)



Update the specific actor-actor graph by id.

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = uiuc_incas_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = uiuc_incas_client.GraphApi(uiuc_incas_client.ApiClient(configuration))
body = uiuc_incas_client.ActorActorGraph() # ActorActorGraph | The new graph to update
id = 'id_example' # str | Graph ID

try:
    api_response = api_instance.actor_actor_graph_id_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->actor_actor_graph_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActorActorGraph**](ActorActorGraph.md)| The new graph to update | 
 **id** | **str**| Graph ID | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_actor_graph_list_get**
> list[str] actor_actor_graph_list_get(provider_name=provider_name, graph_name=graph_name, distance_name=distance_name, version=version, time_stamp=time_stamp)



Gets graph IDs by providing query keys.

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = uiuc_incas_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = uiuc_incas_client.GraphApi(uiuc_incas_client.ApiClient(configuration))
provider_name = 'provider_name_example' # str |  (optional)
graph_name = 'graph_name_example' # str |  (optional)
distance_name = 'distance_name_example' # str |  (optional)
version = 'version_example' # str |  (optional)
time_stamp = 'time_stamp_example' # str |  (optional)

try:
    api_response = api_instance.actor_actor_graph_list_get(provider_name=provider_name, graph_name=graph_name, distance_name=distance_name, version=version, time_stamp=time_stamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->actor_actor_graph_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_name** | **str**|  | [optional] 
 **graph_name** | **str**|  | [optional] 
 **distance_name** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 
 **time_stamp** | **str**|  | [optional] 

### Return type

**list[str]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_actor_graph_post**
> str actor_actor_graph_post(body)



Submits a new graph.

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = uiuc_incas_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = uiuc_incas_client.GraphApi(uiuc_incas_client.ApiClient(configuration))
body = uiuc_incas_client.ActorActorGraph() # ActorActorGraph | The new graphs to add

try:
    api_response = api_instance.actor_actor_graph_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->actor_actor_graph_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActorActorGraph**](ActorActorGraph.md)| The new graphs to add | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_message_graph_id_delete**
> actor_message_graph_id_delete(id)



Delete the specific graph by id.

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = uiuc_incas_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = uiuc_incas_client.GraphApi(uiuc_incas_client.ApiClient(configuration))
id = 'id_example' # str | Graph ID

try:
    api_instance.actor_message_graph_id_delete(id)
except ApiException as e:
    print("Exception when calling GraphApi->actor_message_graph_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Graph ID | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_message_graph_id_get**
> ActorMessageGraph actor_message_graph_id_get(id)



Gets specific actor-message graph information by id.

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = uiuc_incas_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = uiuc_incas_client.GraphApi(uiuc_incas_client.ApiClient(configuration))
id = 'id_example' # str | Graph ID

try:
    api_response = api_instance.actor_message_graph_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->actor_message_graph_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Graph ID | 

### Return type

[**ActorMessageGraph**](ActorMessageGraph.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_message_graph_id_neighbor_get**
> list[GraphEdge] actor_message_graph_id_neighbor_get(id, message_id=message_id, actor_id=actor_id)



Gets the neighbors for specific node from specific graph by graph id and message or actor id.

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = uiuc_incas_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = uiuc_incas_client.GraphApi(uiuc_incas_client.ApiClient(configuration))
id = 'id_example' # str | Graph ID
message_id = 'message_id_example' # str |  (optional)
actor_id = 'actor_id_example' # str |  (optional)

try:
    api_response = api_instance.actor_message_graph_id_neighbor_get(id, message_id=message_id, actor_id=actor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->actor_message_graph_id_neighbor_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Graph ID | 
 **message_id** | **str**|  | [optional] 
 **actor_id** | **str**|  | [optional] 

### Return type

[**list[GraphEdge]**](GraphEdge.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_message_graph_id_put**
> str actor_message_graph_id_put(body, id)



Update the specific actor-message graph by id.

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = uiuc_incas_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = uiuc_incas_client.GraphApi(uiuc_incas_client.ApiClient(configuration))
body = uiuc_incas_client.ActorMessageGraph() # ActorMessageGraph | The new graph to update
id = 'id_example' # str | Graph ID

try:
    api_response = api_instance.actor_message_graph_id_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->actor_message_graph_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActorMessageGraph**](ActorMessageGraph.md)| The new graph to update | 
 **id** | **str**| Graph ID | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_message_graph_list_get**
> list[str] actor_message_graph_list_get(provider_name=provider_name, graph_name=graph_name, distance_name=distance_name, version=version, time_stamp=time_stamp)



Gets graph IDs by providing query keys.

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = uiuc_incas_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = uiuc_incas_client.GraphApi(uiuc_incas_client.ApiClient(configuration))
provider_name = 'provider_name_example' # str |  (optional)
graph_name = 'graph_name_example' # str |  (optional)
distance_name = 'distance_name_example' # str |  (optional)
version = 'version_example' # str |  (optional)
time_stamp = 'time_stamp_example' # str |  (optional)

try:
    api_response = api_instance.actor_message_graph_list_get(provider_name=provider_name, graph_name=graph_name, distance_name=distance_name, version=version, time_stamp=time_stamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->actor_message_graph_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_name** | **str**|  | [optional] 
 **graph_name** | **str**|  | [optional] 
 **distance_name** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 
 **time_stamp** | **str**|  | [optional] 

### Return type

**list[str]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_message_graph_post**
> str actor_message_graph_post(body)



Submits a new graph.

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = uiuc_incas_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = uiuc_incas_client.GraphApi(uiuc_incas_client.ApiClient(configuration))
body = uiuc_incas_client.ActorMessageGraph() # ActorMessageGraph | The new graphs to add

try:
    api_response = api_instance.actor_message_graph_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->actor_message_graph_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActorMessageGraph**](ActorMessageGraph.md)| The new graphs to add | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_message_graph_id_delete**
> message_message_graph_id_delete(id)



Delete the specific graph by id.

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = uiuc_incas_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = uiuc_incas_client.GraphApi(uiuc_incas_client.ApiClient(configuration))
id = 'id_example' # str | Graph ID

try:
    api_instance.message_message_graph_id_delete(id)
except ApiException as e:
    print("Exception when calling GraphApi->message_message_graph_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Graph ID | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_message_graph_id_get**
> MessageMessageGraph message_message_graph_id_get(id)



Gets specific message-message graph information by id.

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = uiuc_incas_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = uiuc_incas_client.GraphApi(uiuc_incas_client.ApiClient(configuration))
id = 'id_example' # str | Graph ID

try:
    api_response = api_instance.message_message_graph_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->message_message_graph_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Graph ID | 

### Return type

[**MessageMessageGraph**](MessageMessageGraph.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_message_graph_id_neighbor_get**
> list[GraphEdge] message_message_graph_id_neighbor_get(id, message_id)



Gets the neighbors for specific node from specific graph by graph id and message's id.

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = uiuc_incas_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = uiuc_incas_client.GraphApi(uiuc_incas_client.ApiClient(configuration))
id = 'id_example' # str | Graph ID
message_id = 'message_id_example' # str | 

try:
    api_response = api_instance.message_message_graph_id_neighbor_get(id, message_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->message_message_graph_id_neighbor_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Graph ID | 
 **message_id** | **str**|  | 

### Return type

[**list[GraphEdge]**](GraphEdge.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_message_graph_id_put**
> str message_message_graph_id_put(body, id)



Update the specific message-message graph by id.

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = uiuc_incas_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = uiuc_incas_client.GraphApi(uiuc_incas_client.ApiClient(configuration))
body = uiuc_incas_client.MessageMessageGraph() # MessageMessageGraph | The new graph to update
id = 'id_example' # str | Graph ID

try:
    api_response = api_instance.message_message_graph_id_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->message_message_graph_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MessageMessageGraph**](MessageMessageGraph.md)| The new graph to update | 
 **id** | **str**| Graph ID | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_message_graph_list_get**
> list[str] message_message_graph_list_get(provider_name=provider_name, graph_name=graph_name, distance_name=distance_name, version=version, time_stamp=time_stamp)



Gets graph IDs by providing query keys.

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = uiuc_incas_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = uiuc_incas_client.GraphApi(uiuc_incas_client.ApiClient(configuration))
provider_name = 'provider_name_example' # str |  (optional)
graph_name = 'graph_name_example' # str |  (optional)
distance_name = 'distance_name_example' # str |  (optional)
version = 'version_example' # str |  (optional)
time_stamp = 'time_stamp_example' # str |  (optional)

try:
    api_response = api_instance.message_message_graph_list_get(provider_name=provider_name, graph_name=graph_name, distance_name=distance_name, version=version, time_stamp=time_stamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->message_message_graph_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_name** | **str**|  | [optional] 
 **graph_name** | **str**|  | [optional] 
 **distance_name** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 
 **time_stamp** | **str**|  | [optional] 

### Return type

**list[str]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_message_graph_post**
> str message_message_graph_post(body)



Submits a new graph.

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = uiuc_incas_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = uiuc_incas_client.GraphApi(uiuc_incas_client.ApiClient(configuration))
body = uiuc_incas_client.MessageMessageGraph() # MessageMessageGraph | The new graph to add

try:
    api_response = api_instance.message_message_graph_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->message_message_graph_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MessageMessageGraph**](MessageMessageGraph.md)| The new graph to add | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

