# swagger_client.GraphApi

All URIs are relative to *https://virtserver.swaggerhub.com/incas/incas/1.0.0*

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
> str actor_actor_graph_get(provider_name, time_stamp, version=version)



Gets graph id by providerName, timestamp and version

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GraphApi()
provider_name = 'provider_name_example' # str | 
time_stamp = 'time_stamp_example' # str | 
version = 'version_example' # str |  (optional)

try:
    api_response = api_instance.actor_actor_graph_get(provider_name, time_stamp, version=version)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_actor_graph_id_delete**
> actor_actor_graph_id_delete(id, provider_name, time_stamp, version)



Delete the specific graph by id, providerName, timestamp and version

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GraphApi()
id = 'id_example' # str | Graph ID
provider_name = 'provider_name_example' # str | 
time_stamp = 'time_stamp_example' # str | 
version = 'version_example' # str | 

try:
    api_instance.actor_actor_graph_id_delete(id, provider_name, time_stamp, version)
except ApiException as e:
    print("Exception when calling GraphApi->actor_actor_graph_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Graph ID | 
 **provider_name** | **str**|  | 
 **time_stamp** | **str**|  | 
 **version** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_actor_graph_id_get**
> list[ActorActorGraph] actor_actor_graph_id_get(id, provider_name=provider_name, time_stamp=time_stamp, version=version)



Gets specific actor-actor graph information by id, timeStamp, providerName and version

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GraphApi()
id = 'id_example' # str | Graph ID
provider_name = 'provider_name_example' # str |  (optional)
time_stamp = 'time_stamp_example' # str |  (optional)
version = 'version_example' # str |  (optional)

try:
    api_response = api_instance.actor_actor_graph_id_get(id, provider_name=provider_name, time_stamp=time_stamp, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->actor_actor_graph_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Graph ID | 
 **provider_name** | **str**|  | [optional] 
 **time_stamp** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 

### Return type

[**list[ActorActorGraph]**](ActorActorGraph.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_actor_graph_id_neighbor_get**
> list[list[UiucActor]] actor_actor_graph_id_neighbor_get(id, provider_name, graph_type, version, actor_id)



Gets the neighbors for specific node from specific graph by graph id, providerName and version and actor id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GraphApi()
id = 'id_example' # str | Graph ID
provider_name = 'provider_name_example' # str | 
graph_type = 'graph_type_example' # str | 
version = 'version_example' # str | 
actor_id = 'actor_id_example' # str | 

try:
    api_response = api_instance.actor_actor_graph_id_neighbor_get(id, provider_name, graph_type, version, actor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->actor_actor_graph_id_neighbor_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Graph ID | 
 **provider_name** | **str**|  | 
 **graph_type** | **str**|  | 
 **version** | **str**|  | 
 **actor_id** | **str**|  | 

### Return type

**list[list[UiucActor]]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_actor_graph_id_put**
> ActorActorGraph actor_actor_graph_id_put(body, provider_name, time_stamp, version, id)



Update the specific actor-actor graph by id, providerName, timestamp and version

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GraphApi()
body = swagger_client.ActorActorGraph() # ActorActorGraph | The new graph to update
provider_name = 'provider_name_example' # str | 
time_stamp = 'time_stamp_example' # str | 
version = 'version_example' # str | 
id = 'id_example' # str | Graph ID

try:
    api_response = api_instance.actor_actor_graph_id_put(body, provider_name, time_stamp, version, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->actor_actor_graph_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActorActorGraph**](ActorActorGraph.md)| The new graph to update | 
 **provider_name** | **str**|  | 
 **time_stamp** | **str**|  | 
 **version** | **str**|  | 
 **id** | **str**| Graph ID | 

### Return type

[**ActorActorGraph**](ActorActorGraph.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_actor_graph_post**
> list[ActorActorGraph] actor_actor_graph_post(body)



Creates new graphs

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GraphApi()
body = [swagger_client.ActorActorGraph()] # list[ActorActorGraph] | The new graphs to add

try:
    api_response = api_instance.actor_actor_graph_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->actor_actor_graph_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ActorActorGraph]**](ActorActorGraph.md)| The new graphs to add | 

### Return type

[**list[ActorActorGraph]**](ActorActorGraph.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_message_graph_get**
> str actor_message_graph_get(provider_name, time_stamp, version=version)



Gets graph id by providerName, timestamp and version

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GraphApi()
provider_name = 'provider_name_example' # str | 
time_stamp = 'time_stamp_example' # str | 
version = 'version_example' # str |  (optional)

try:
    api_response = api_instance.actor_message_graph_get(provider_name, time_stamp, version=version)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_message_graph_id_delete**
> actor_message_graph_id_delete(id, provider_name, time_stamp, version)



Delete the specific graph by id, providerName, timestamp and version

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GraphApi()
id = 'id_example' # str | Graph ID
provider_name = 'provider_name_example' # str | 
time_stamp = 'time_stamp_example' # str | 
version = 'version_example' # str | 

try:
    api_instance.actor_message_graph_id_delete(id, provider_name, time_stamp, version)
except ApiException as e:
    print("Exception when calling GraphApi->actor_message_graph_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Graph ID | 
 **provider_name** | **str**|  | 
 **time_stamp** | **str**|  | 
 **version** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_message_graph_id_get**
> list[ActorMessageGraph] actor_message_graph_id_get(id, provider_name=provider_name, time_stamp=time_stamp, version=version)



Gets specific actor-message graph information by id, timeStamp, providerName and version

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GraphApi()
id = 'id_example' # str | Graph ID
provider_name = 'provider_name_example' # str |  (optional)
time_stamp = 'time_stamp_example' # str |  (optional)
version = 'version_example' # str |  (optional)

try:
    api_response = api_instance.actor_message_graph_id_get(id, provider_name=provider_name, time_stamp=time_stamp, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->actor_message_graph_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Graph ID | 
 **provider_name** | **str**|  | [optional] 
 **time_stamp** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 

### Return type

[**list[ActorMessageGraph]**](ActorMessageGraph.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_message_graph_id_neighbor_get**
> list[list[object]] actor_message_graph_id_neighbor_get(id, provider_name, graph_type, version, message_id=message_id, actor_id=actor_id)



Gets the neighbors for specific node from specific graph by graph id, providerName and version and message or actor id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GraphApi()
id = 'id_example' # str | Graph ID
provider_name = 'provider_name_example' # str | 
graph_type = 'graph_type_example' # str | 
version = 'version_example' # str | 
message_id = 'message_id_example' # str |  (optional)
actor_id = 'actor_id_example' # str |  (optional)

try:
    api_response = api_instance.actor_message_graph_id_neighbor_get(id, provider_name, graph_type, version, message_id=message_id, actor_id=actor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->actor_message_graph_id_neighbor_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Graph ID | 
 **provider_name** | **str**|  | 
 **graph_type** | **str**|  | 
 **version** | **str**|  | 
 **message_id** | **str**|  | [optional] 
 **actor_id** | **str**|  | [optional] 

### Return type

**list[list[object]]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_message_graph_id_put**
> ActorMessageGraph actor_message_graph_id_put(body, provider_name, time_stamp, version, id)



Update the specific actor-message graph by id, providerName, timestamp and version

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GraphApi()
body = swagger_client.ActorMessageGraph() # ActorMessageGraph | The new graph to update
provider_name = 'provider_name_example' # str | 
time_stamp = 'time_stamp_example' # str | 
version = 'version_example' # str | 
id = 'id_example' # str | Graph ID

try:
    api_response = api_instance.actor_message_graph_id_put(body, provider_name, time_stamp, version, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->actor_message_graph_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActorMessageGraph**](ActorMessageGraph.md)| The new graph to update | 
 **provider_name** | **str**|  | 
 **time_stamp** | **str**|  | 
 **version** | **str**|  | 
 **id** | **str**| Graph ID | 

### Return type

[**ActorMessageGraph**](ActorMessageGraph.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_message_graph_post**
> list[ActorMessageGraph] actor_message_graph_post(body)



Creates new graphs

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GraphApi()
body = [swagger_client.ActorMessageGraph()] # list[ActorMessageGraph] | The new graphs to add

try:
    api_response = api_instance.actor_message_graph_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->actor_message_graph_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ActorMessageGraph]**](ActorMessageGraph.md)| The new graphs to add | 

### Return type

[**list[ActorMessageGraph]**](ActorMessageGraph.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_message_graph_get**
> str message_message_graph_get(provider_name, time_stamp, version=version)



Gets graph id by providerName, timestamp and version

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GraphApi()
provider_name = 'provider_name_example' # str | 
time_stamp = 'time_stamp_example' # str | 
version = 'version_example' # str |  (optional)

try:
    api_response = api_instance.message_message_graph_get(provider_name, time_stamp, version=version)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_message_graph_id_delete**
> message_message_graph_id_delete(id, provider_name, time_stamp, version)



Delete the specific graph by id, providerName, timestamp and version

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GraphApi()
id = 'id_example' # str | Graph ID
provider_name = 'provider_name_example' # str | 
time_stamp = 'time_stamp_example' # str | 
version = 'version_example' # str | 

try:
    api_instance.message_message_graph_id_delete(id, provider_name, time_stamp, version)
except ApiException as e:
    print("Exception when calling GraphApi->message_message_graph_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Graph ID | 
 **provider_name** | **str**|  | 
 **time_stamp** | **str**|  | 
 **version** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_message_graph_id_get**
> list[MessageMessageGraph] message_message_graph_id_get(id, provider_name=provider_name, time_stamp=time_stamp, version=version)



Gets specific message-message graph information by id, timeStamp, providerName and version

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GraphApi()
id = 'id_example' # str | Graph ID
provider_name = 'provider_name_example' # str |  (optional)
time_stamp = 'time_stamp_example' # str |  (optional)
version = 'version_example' # str |  (optional)

try:
    api_response = api_instance.message_message_graph_id_get(id, provider_name=provider_name, time_stamp=time_stamp, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->message_message_graph_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Graph ID | 
 **provider_name** | **str**|  | [optional] 
 **time_stamp** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 

### Return type

[**list[MessageMessageGraph]**](MessageMessageGraph.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_message_graph_id_neighbor_get**
> list[list[UiucMessage]] message_message_graph_id_neighbor_get(id, provider_name, graph_type, version, message_id)



Gets the neighbors for specific node from specific graph by graph id, providerName and version and message's id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GraphApi()
id = 'id_example' # str | Graph ID
provider_name = 'provider_name_example' # str | 
graph_type = 'graph_type_example' # str | 
version = 'version_example' # str | 
message_id = 'message_id_example' # str | 

try:
    api_response = api_instance.message_message_graph_id_neighbor_get(id, provider_name, graph_type, version, message_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->message_message_graph_id_neighbor_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Graph ID | 
 **provider_name** | **str**|  | 
 **graph_type** | **str**|  | 
 **version** | **str**|  | 
 **message_id** | **str**|  | 

### Return type

**list[list[UiucMessage]]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_message_graph_id_put**
> MessageMessageGraph message_message_graph_id_put(body, provider_name, time_stamp, version, id)



Update the specific message-message graph by id, providerName, timestamp and version

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GraphApi()
body = swagger_client.MessageMessageGraph() # MessageMessageGraph | The new graph to update
provider_name = 'provider_name_example' # str | 
time_stamp = 'time_stamp_example' # str | 
version = 'version_example' # str | 
id = 'id_example' # str | Graph ID

try:
    api_response = api_instance.message_message_graph_id_put(body, provider_name, time_stamp, version, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->message_message_graph_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MessageMessageGraph**](MessageMessageGraph.md)| The new graph to update | 
 **provider_name** | **str**|  | 
 **time_stamp** | **str**|  | 
 **version** | **str**|  | 
 **id** | **str**| Graph ID | 

### Return type

[**MessageMessageGraph**](MessageMessageGraph.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_message_graph_post**
> list[MessageMessageGraph] message_message_graph_post(body)



Creates new graphs

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GraphApi()
body = [swagger_client.MessageMessageGraph()] # list[MessageMessageGraph] | The new graphs to add

try:
    api_response = api_instance.message_message_graph_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->message_message_graph_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[MessageMessageGraph]**](MessageMessageGraph.md)| The new graphs to add | 

### Return type

[**list[MessageMessageGraph]**](MessageMessageGraph.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

