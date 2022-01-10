# uiuc_incas_client.ActorApi

All URIs are relative to *https://incas.cs.illinois.edu:8443/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**actor_batch_get**](ActorApi.md#actor_batch_get) | **POST** /actor/batchGet | 
[**actor_count_get**](ActorApi.md#actor_count_get) | **GET** /actor/count | 
[**actor_enrichments_batch_delete**](ActorApi.md#actor_enrichments_batch_delete) | **POST** /actor/enrichments/batchDelete | 
[**actor_enrichments_batch_get**](ActorApi.md#actor_enrichments_batch_get) | **POST** /actor/enrichments/batchGet | 
[**actor_enrichments_batch_post**](ActorApi.md#actor_enrichments_batch_post) | **POST** /actor/enrichments/batch | 
[**actor_enrichments_batch_put**](ActorApi.md#actor_enrichments_batch_put) | **PUT** /actor/enrichments/batch | 
[**actor_enrichments_meta_delete**](ActorApi.md#actor_enrichments_meta_delete) | **DELETE** /actor/enrichments/meta | 
[**actor_enrichments_meta_get**](ActorApi.md#actor_enrichments_meta_get) | **GET** /actor/enrichments/meta | 
[**actor_enrichments_meta_post**](ActorApi.md#actor_enrichments_meta_post) | **POST** /actor/enrichments/meta | 
[**actor_enrichments_meta_put**](ActorApi.md#actor_enrichments_meta_put) | **PUT** /actor/enrichments/meta | 
[**actor_id_enrichments_delete**](ActorApi.md#actor_id_enrichments_delete) | **DELETE** /actor/{id}/enrichments | 
[**actor_id_enrichments_get**](ActorApi.md#actor_id_enrichments_get) | **GET** /actor/{id}/enrichments | 
[**actor_id_enrichments_post**](ActorApi.md#actor_id_enrichments_post) | **POST** /actor/{id}/enrichments | 
[**actor_id_enrichments_put**](ActorApi.md#actor_id_enrichments_put) | **PUT** /actor/{id}/enrichments | 
[**actor_id_get**](ActorApi.md#actor_id_get) | **GET** /actor/{id} | 
[**actor_list_get**](ActorApi.md#actor_list_get) | **GET** /actor/list | 

# **actor_batch_get**
> list[UiucActor] actor_batch_get(body)



Returns a batch of actors given a list of IDs and specifications.

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = uiuc_incas_client.ActorApi()
body = uiuc_incas_client.ActorBatchGetBody() # ActorBatchGetBody | List of IDs and specifications

try:
    api_response = api_instance.actor_batch_get(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorApi->actor_batch_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActorBatchGetBody**](ActorBatchGetBody.md)| List of IDs and specifications | 

### Return type

[**list[UiucActor]**](UiucActor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_count_get**
> int actor_count_get()



Return the number of actor IDs available.

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = uiuc_incas_client.ActorApi()

try:
    api_response = api_instance.actor_count_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorApi->actor_count_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_enrichments_batch_delete**
> actor_enrichments_batch_delete(body)



Deletes a batch of enrichments given a list of IDs and specifications.

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = uiuc_incas_client.ActorApi()
body = uiuc_incas_client.EnrichmentsBatchDeleteBody1() # EnrichmentsBatchDeleteBody1 | List of IDs and specifications

try:
    api_instance.actor_enrichments_batch_delete(body)
except ApiException as e:
    print("Exception when calling ActorApi->actor_enrichments_batch_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EnrichmentsBatchDeleteBody1**](EnrichmentsBatchDeleteBody1.md)| List of IDs and specifications | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_enrichments_batch_get**
> dict(str, list[ActorEnrichment]) actor_enrichments_batch_get(body)



Returns a batch of enrichments given a list of IDs and specifications.

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = uiuc_incas_client.ActorApi()
body = uiuc_incas_client.EnrichmentsBatchGetBody1() # EnrichmentsBatchGetBody1 | List of IDs and specifications

try:
    api_response = api_instance.actor_enrichments_batch_get(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorApi->actor_enrichments_batch_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EnrichmentsBatchGetBody1**](EnrichmentsBatchGetBody1.md)| List of IDs and specifications | 

### Return type

**dict(str, list[ActorEnrichment])**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_enrichments_batch_post**
> actor_enrichments_batch_post(body)



Submits a enrichment for each actor ID.

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = uiuc_incas_client.ActorApi()
body = NULL # dict(str, ActorEnrichment) | Map of IDs and enrichments

try:
    api_instance.actor_enrichments_batch_post(body)
except ApiException as e:
    print("Exception when calling ActorApi->actor_enrichments_batch_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, ActorEnrichment)**](dict.md)| Map of IDs and enrichments | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_enrichments_batch_put**
> actor_enrichments_batch_put(body)



Updates a enrichment for each actor ID.

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = uiuc_incas_client.ActorApi()
body = NULL # dict(str, ActorEnrichment) | Map of IDs and enrichments

try:
    api_instance.actor_enrichments_batch_put(body)
except ApiException as e:
    print("Exception when calling ActorApi->actor_enrichments_batch_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, ActorEnrichment)**](dict.md)| Map of IDs and enrichments | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_enrichments_meta_delete**
> actor_enrichments_meta_delete(enrichment_name, provider_name, version)



Delete a specific message enrichment meta by providerName, enrichmentName and version.

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = uiuc_incas_client.ActorApi()
enrichment_name = 'enrichment_name_example' # str | 
provider_name = 'provider_name_example' # str | 
version = 'version_example' # str | 

try:
    api_instance.actor_enrichments_meta_delete(enrichment_name, provider_name, version)
except ApiException as e:
    print("Exception when calling ActorApi->actor_enrichments_meta_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_enrichments_meta_get**
> list[ActorEnrichmentMeta] actor_enrichments_meta_get(enrichment_name=enrichment_name, provider_name=provider_name, version=version)



Returns current actor enrichment metas by providerName, enrichmentName and version.

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = uiuc_incas_client.ActorApi()
enrichment_name = 'enrichment_name_example' # str |  (optional)
provider_name = 'provider_name_example' # str |  (optional)
version = 'version_example' # str |  (optional)

try:
    api_response = api_instance.actor_enrichments_meta_get(enrichment_name=enrichment_name, provider_name=provider_name, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorApi->actor_enrichments_meta_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrichment_name** | **str**|  | [optional] 
 **provider_name** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 

### Return type

[**list[ActorEnrichmentMeta]**](ActorEnrichmentMeta.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_enrichments_meta_post**
> actor_enrichments_meta_post(body)



Submits an actor enrichment meta (post after all actors have been added).

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = uiuc_incas_client.ActorApi()
body = uiuc_incas_client.ActorEnrichmentMeta() # ActorEnrichmentMeta | The new enrichment meta to add

try:
    api_instance.actor_enrichments_meta_post(body)
except ApiException as e:
    print("Exception when calling ActorApi->actor_enrichments_meta_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActorEnrichmentMeta**](ActorEnrichmentMeta.md)| The new enrichment meta to add | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_enrichments_meta_put**
> actor_enrichments_meta_put(body)



Updates an actor enrichment meta (after all actors have been added) by providerName, enrichmentName and version.

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = uiuc_incas_client.ActorApi()
body = uiuc_incas_client.ActorEnrichmentMeta() # ActorEnrichmentMeta | The new enrichment meta to update

try:
    api_instance.actor_enrichments_meta_put(body)
except ApiException as e:
    print("Exception when calling ActorApi->actor_enrichments_meta_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActorEnrichmentMeta**](ActorEnrichmentMeta.md)| The new enrichment meta to update | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_id_enrichments_delete**
> actor_id_enrichments_delete(id, enrichment_name, provider_name, version)



Delete the enrichments for specific actor by type, providerName and version

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = uiuc_incas_client.ActorApi()
id = 'id_example' # str | Actor ID
enrichment_name = 'enrichment_name_example' # str | 
provider_name = 'provider_name_example' # str | 
version = 'version_example' # str | 

try:
    api_instance.actor_id_enrichments_delete(id, enrichment_name, provider_name, version)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_id_enrichments_get**
> list[ActorEnrichment] actor_id_enrichments_get(id, enrichment_name=enrichment_name, provider_name=provider_name, version=version, dev=dev)



Returns all matched enrichment for the specific actor by type, providerName and version.

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = uiuc_incas_client.ActorApi()
id = 'id_example' # str | Actor ID
enrichment_name = 'enrichment_name_example' # str |  (optional)
provider_name = 'provider_name_example' # str |  (optional)
version = 'version_example' # str |  (optional)
dev = true # bool |  (optional)

try:
    api_response = api_instance.actor_id_enrichments_get(id, enrichment_name=enrichment_name, provider_name=provider_name, version=version, dev=dev)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorApi->actor_id_enrichments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Actor ID | 
 **enrichment_name** | **str**|  | [optional] 
 **provider_name** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 
 **dev** | **bool**|  | [optional] 

### Return type

[**list[ActorEnrichment]**](ActorEnrichment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_id_enrichments_post**
> actor_id_enrichments_post(body, id)



Submits a new enrichment for specific message.

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = uiuc_incas_client.ActorApi()
body = uiuc_incas_client.ActorEnrichment() # ActorEnrichment | The new enrichment to add
id = 'id_example' # str | Actor ID

try:
    api_instance.actor_id_enrichments_post(body, id)
except ApiException as e:
    print("Exception when calling ActorApi->actor_id_enrichments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActorEnrichment**](ActorEnrichment.md)| The new enrichment to add | 
 **id** | **str**| Actor ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_id_enrichments_put**
> actor_id_enrichments_put(body, id)



Update the enrichments for specific actor by type, providerName and version.

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = uiuc_incas_client.ActorApi()
body = uiuc_incas_client.ActorEnrichment() # ActorEnrichment | The new enrichments to update
id = 'id_example' # str | Actor ID

try:
    api_instance.actor_id_enrichments_put(body, id)
except ApiException as e:
    print("Exception when calling ActorApi->actor_id_enrichments_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActorEnrichment**](ActorEnrichment.md)| The new enrichments to update | 
 **id** | **str**| Actor ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_id_get**
> UiucActor actor_id_get(id, with_enrichment=with_enrichment, enrichment_name=enrichment_name, provider_name=provider_name, version=version, dev=dev)



Returns specific actor by id.

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = uiuc_incas_client.ActorApi()
id = 'id_example' # str | Actor ID
with_enrichment = true # bool | Whether to retrieve enrichments (optional)
enrichment_name = 'enrichment_name_example' # str |  (optional)
provider_name = 'provider_name_example' # str |  (optional)
version = 'version_example' # str |  (optional)
dev = true # bool |  (optional)

try:
    api_response = api_instance.actor_id_get(id, with_enrichment=with_enrichment, enrichment_name=enrichment_name, provider_name=provider_name, version=version, dev=dev)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorApi->actor_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Actor ID | 
 **with_enrichment** | **bool**| Whether to retrieve enrichments | [optional] 
 **enrichment_name** | **str**|  | [optional] 
 **provider_name** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 
 **dev** | **bool**|  | [optional] 

### Return type

[**UiucActor**](UiucActor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_list_get**
> list[str] actor_list_get(begin, end)



Return list of actor IDs available in [begin, end).

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = uiuc_incas_client.ActorApi()
begin = 56 # int | Begin
end = 56 # int | End

try:
    api_response = api_instance.actor_list_get(begin, end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorApi->actor_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **begin** | **int**| Begin | 
 **end** | **int**| End | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

