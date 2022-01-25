# uiuc_incas_client.ActorApi

All URIs are relative to *https://incas.cs.illinois.edu:8443/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**actor_batch_get**](ActorApi.md#actor_batch_get) | **POST** /actor/batchGet | 
[**actor_count_get**](ActorApi.md#actor_count_get) | **GET** /actor/count | 
[**actor_enrichments_batch_delete**](ActorApi.md#actor_enrichments_batch_delete) | **POST** /actor/enrichments/batchDelete | 
[**actor_enrichments_batch_delete_validate**](ActorApi.md#actor_enrichments_batch_delete_validate) | **POST** /actor/enrichments/batchDelete/validate | 
[**actor_enrichments_batch_get**](ActorApi.md#actor_enrichments_batch_get) | **POST** /actor/enrichments/batchGet | 
[**actor_enrichments_batch_post**](ActorApi.md#actor_enrichments_batch_post) | **POST** /actor/enrichments/batch | 
[**actor_enrichments_batch_post_validate**](ActorApi.md#actor_enrichments_batch_post_validate) | **POST** /actor/enrichments/batch/validate | 
[**actor_enrichments_batch_put**](ActorApi.md#actor_enrichments_batch_put) | **PUT** /actor/enrichments/batch | 
[**actor_enrichments_batch_put_validate**](ActorApi.md#actor_enrichments_batch_put_validate) | **PUT** /actor/enrichments/batch/validate | 
[**actor_enrichments_meta_delete**](ActorApi.md#actor_enrichments_meta_delete) | **DELETE** /actor/enrichments/meta | 
[**actor_enrichments_meta_get**](ActorApi.md#actor_enrichments_meta_get) | **GET** /actor/enrichments/meta | 
[**actor_enrichments_meta_post**](ActorApi.md#actor_enrichments_meta_post) | **POST** /actor/enrichments/meta | 
[**actor_enrichments_meta_put**](ActorApi.md#actor_enrichments_meta_put) | **PUT** /actor/enrichments/meta | 
[**actor_id_enrichments_delete**](ActorApi.md#actor_id_enrichments_delete) | **DELETE** /actor/{id}/enrichments | 
[**actor_id_enrichments_get**](ActorApi.md#actor_id_enrichments_get) | **GET** /actor/{id}/enrichments | 
[**actor_id_enrichments_post**](ActorApi.md#actor_id_enrichments_post) | **POST** /actor/{id}/enrichments | 
[**actor_id_enrichments_put**](ActorApi.md#actor_id_enrichments_put) | **PUT** /actor/{id}/enrichments | 
[**actor_id_get**](ActorApi.md#actor_id_get) | **GET** /actor/{id} | 
[**actor_id_segments_delete**](ActorApi.md#actor_id_segments_delete) | **DELETE** /actor/{id}/segments | 
[**actor_id_segments_get**](ActorApi.md#actor_id_segments_get) | **GET** /actor/{id}/segments | 
[**actor_id_segments_post**](ActorApi.md#actor_id_segments_post) | **POST** /actor/{id}/segments | 
[**actor_id_segments_put**](ActorApi.md#actor_id_segments_put) | **PUT** /actor/{id}/segments | 
[**actor_list_get**](ActorApi.md#actor_list_get) | **GET** /actor/list | 
[**actor_segment_batch_delete**](ActorApi.md#actor_segment_batch_delete) | **POST** /actor/segments/batchDelete | 
[**actor_segments_batch_delete_validate**](ActorApi.md#actor_segments_batch_delete_validate) | **POST** /actor/segments/batchDelete/validate | 
[**actor_segments_batch_get**](ActorApi.md#actor_segments_batch_get) | **POST** /actor/segments/batchGet | 
[**actor_segments_batch_post**](ActorApi.md#actor_segments_batch_post) | **POST** /actor/segments/batch | 
[**actor_segments_batch_post_validate**](ActorApi.md#actor_segments_batch_post_validate) | **POST** /actor/segments/batch/validate | 
[**actor_segments_batch_put**](ActorApi.md#actor_segments_batch_put) | **PUT** /actor/segments/batch | 
[**actor_segments_batch_put_validate**](ActorApi.md#actor_segments_batch_put_validate) | **PUT** /actor/segments/batch/validate | 

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

# Configure API key authorization: ApiKeyAuth
configuration = uiuc_incas_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
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

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_count_get**
> int actor_count_get(media_type, entity_type=entity_type)



Return the number of actor IDs available.

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
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
media_type = 'media_type_example' # str | Type of entity to retrieve
entity_type = 'entity_type_example' # str | Type of entity to retrieve (optional)

try:
    api_response = api_instance.actor_count_get(media_type, entity_type=entity_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorApi->actor_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_type** | **str**| Type of entity to retrieve | 
 **entity_type** | **str**| Type of entity to retrieve | [optional] 

### Return type

**int**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

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

# Configure API key authorization: ApiKeyAuth
configuration = uiuc_incas_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
body = uiuc_incas_client.ActorEnrichmentsBatchDeleteBody() # ActorEnrichmentsBatchDeleteBody | List of IDs and specifications

try:
    api_instance.actor_enrichments_batch_delete(body)
except ApiException as e:
    print("Exception when calling ActorApi->actor_enrichments_batch_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActorEnrichmentsBatchDeleteBody**](ActorEnrichmentsBatchDeleteBody.md)| List of IDs and specifications | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_enrichments_batch_delete_validate**
> ActorEnrichmentsBatchDeleteValidationResponse actor_enrichments_batch_delete_validate(body)



Validation endpoint for batch enrichment deletion, successful attempt will return a token.

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
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
body = uiuc_incas_client.ActorEnrichmentsBatchDeleteBody() # ActorEnrichmentsBatchDeleteBody | List of IDs and specifications

try:
    api_response = api_instance.actor_enrichments_batch_delete_validate(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorApi->actor_enrichments_batch_delete_validate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActorEnrichmentsBatchDeleteBody**](ActorEnrichmentsBatchDeleteBody.md)| List of IDs and specifications | 

### Return type

[**ActorEnrichmentsBatchDeleteValidationResponse**](ActorEnrichmentsBatchDeleteValidationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

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

# Configure API key authorization: ApiKeyAuth
configuration = uiuc_incas_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
body = uiuc_incas_client.ActorEnrichmentsBatchGetBody() # ActorEnrichmentsBatchGetBody | List of IDs and specifications

try:
    api_response = api_instance.actor_enrichments_batch_get(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorApi->actor_enrichments_batch_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActorEnrichmentsBatchGetBody**](ActorEnrichmentsBatchGetBody.md)| List of IDs and specifications | 

### Return type

**dict(str, list[ActorEnrichment])**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_enrichments_batch_post**
> str actor_enrichments_batch_post(body)



Submits a enrichment for each actor ID.

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
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
body = NULL # dict(str, ActorEnrichment) | Map of IDs and enrichments

try:
    api_response = api_instance.actor_enrichments_batch_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorApi->actor_enrichments_batch_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, ActorEnrichment)**](dict.md)| Map of IDs and enrichments | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_enrichments_batch_post_validate**
> ActorEnrichmentsBatchValidationResponse actor_enrichments_batch_post_validate(body)



Validation endpoint for batch enrichment creation, successful attempt will return a token.

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
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
body = NULL # dict(str, ActorEnrichment) | List of IDs and specifications

try:
    api_response = api_instance.actor_enrichments_batch_post_validate(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorApi->actor_enrichments_batch_post_validate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, ActorEnrichment)**](dict.md)| List of IDs and specifications | 

### Return type

[**ActorEnrichmentsBatchValidationResponse**](ActorEnrichmentsBatchValidationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_enrichments_batch_put**
> str actor_enrichments_batch_put(body)



Updates a enrichment for each actor ID.

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
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
body = NULL # dict(str, ActorEnrichment) | Map of IDs and enrichments

try:
    api_response = api_instance.actor_enrichments_batch_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorApi->actor_enrichments_batch_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, ActorEnrichment)**](dict.md)| Map of IDs and enrichments | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_enrichments_batch_put_validate**
> ActorEnrichmentsBatchValidationResponse actor_enrichments_batch_put_validate(body)



Validation endpoint for batch enrichment update, successful attempt will return a token.

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
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
body = NULL # dict(str, ActorEnrichment) | List of IDs and specifications

try:
    api_response = api_instance.actor_enrichments_batch_put_validate(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorApi->actor_enrichments_batch_put_validate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, ActorEnrichment)**](dict.md)| List of IDs and specifications | 

### Return type

[**ActorEnrichmentsBatchValidationResponse**](ActorEnrichmentsBatchValidationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_enrichments_meta_delete**
> actor_enrichments_meta_delete(enrichment_name, provider_name, version)



Delete a specific actor enrichment meta by providerName, enrichmentName and version.

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
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
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

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

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

# Configure API key authorization: ApiKeyAuth
configuration = uiuc_incas_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
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

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_enrichments_meta_post**
> str actor_enrichments_meta_post(body)



Submits an actor enrichment meta (post after all actors have been added).

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
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
body = uiuc_incas_client.ActorEnrichmentMeta() # ActorEnrichmentMeta | The new enrichment meta to add

try:
    api_response = api_instance.actor_enrichments_meta_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorApi->actor_enrichments_meta_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActorEnrichmentMeta**](ActorEnrichmentMeta.md)| The new enrichment meta to add | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_enrichments_meta_put**
> str actor_enrichments_meta_put(body)



Updates an actor enrichment meta (after all actors have been added) by providerName, enrichmentName and version.

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
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
body = uiuc_incas_client.ActorEnrichmentMeta() # ActorEnrichmentMeta | The new enrichment meta to update

try:
    api_response = api_instance.actor_enrichments_meta_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorApi->actor_enrichments_meta_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActorEnrichmentMeta**](ActorEnrichmentMeta.md)| The new enrichment meta to update | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

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

# Configure API key authorization: ApiKeyAuth
configuration = uiuc_incas_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
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

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

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

# Configure API key authorization: ApiKeyAuth
configuration = uiuc_incas_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
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

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_id_enrichments_post**
> str actor_id_enrichments_post(body, id)



Submits a new enrichment for specific actor.

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
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
body = uiuc_incas_client.ActorEnrichment() # ActorEnrichment | The new enrichment to add
id = 'id_example' # str | Actor ID

try:
    api_response = api_instance.actor_id_enrichments_post(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorApi->actor_id_enrichments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActorEnrichment**](ActorEnrichment.md)| The new enrichment to add | 
 **id** | **str**| Actor ID | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_id_enrichments_put**
> str actor_id_enrichments_put(body, id)



Update the enrichments for specific actor by type, providerName and version.

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
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
body = uiuc_incas_client.ActorEnrichment() # ActorEnrichment | The new enrichments to update
id = 'id_example' # str | Actor ID

try:
    api_response = api_instance.actor_id_enrichments_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorApi->actor_id_enrichments_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActorEnrichment**](ActorEnrichment.md)| The new enrichments to update | 
 **id** | **str**| Actor ID | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_id_get**
> UiucActor actor_id_get(id, with_enrichment=with_enrichment, with_segment=with_segment, enrichment_name=enrichment_name, enrichment_provider_name=enrichment_provider_name, enrichment_version=enrichment_version, collection_name=collection_name, collection_provider_name=collection_provider_name, collection_version=collection_version, dev=dev)



Returns specific actor by id.

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
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
id = 'id_example' # str | Actor ID
with_enrichment = true # bool | Whether to retrieve enrichments (optional)
with_segment = true # bool | Whether to retrieve segments (optional)
enrichment_name = 'enrichment_name_example' # str |  (optional)
enrichment_provider_name = 'enrichment_provider_name_example' # str |  (optional)
enrichment_version = 'enrichment_version_example' # str |  (optional)
collection_name = 'collection_name_example' # str |  (optional)
collection_provider_name = 'collection_provider_name_example' # str |  (optional)
collection_version = 'collection_version_example' # str |  (optional)
dev = true # bool |  (optional)

try:
    api_response = api_instance.actor_id_get(id, with_enrichment=with_enrichment, with_segment=with_segment, enrichment_name=enrichment_name, enrichment_provider_name=enrichment_provider_name, enrichment_version=enrichment_version, collection_name=collection_name, collection_provider_name=collection_provider_name, collection_version=collection_version, dev=dev)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorApi->actor_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Actor ID | 
 **with_enrichment** | **bool**| Whether to retrieve enrichments | [optional] 
 **with_segment** | **bool**| Whether to retrieve segments | [optional] 
 **enrichment_name** | **str**|  | [optional] 
 **enrichment_provider_name** | **str**|  | [optional] 
 **enrichment_version** | **str**|  | [optional] 
 **collection_name** | **str**|  | [optional] 
 **collection_provider_name** | **str**|  | [optional] 
 **collection_version** | **str**|  | [optional] 
 **dev** | **bool**|  | [optional] 

### Return type

[**UiucActor**](UiucActor.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_id_segments_delete**
> actor_id_segments_delete(id, collection_name, provider_name, version)



Deletes all matched segments for specific actor by segmentCollectionName

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
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
id = 'id_example' # str | Actor ID
collection_name = 'collection_name_example' # str | 
provider_name = 'provider_name_example' # str | 
version = 'version_example' # str | 

try:
    api_instance.actor_id_segments_delete(id, collection_name, provider_name, version)
except ApiException as e:
    print("Exception when calling ActorApi->actor_id_segments_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Actor ID | 
 **collection_name** | **str**|  | 
 **provider_name** | **str**|  | 
 **version** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_id_segments_get**
> list[ActorSegmentCollection] actor_id_segments_get(id, collection_name=collection_name, provider_name=provider_name, version=version, dev=dev)



Returns all matched segment collections the actor belonged to by collectionName.

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
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
id = 'id_example' # str | Actor ID
collection_name = 'collection_name_example' # str |  (optional)
provider_name = 'provider_name_example' # str |  (optional)
version = 'version_example' # str |  (optional)
dev = true # bool |  (optional)

try:
    api_response = api_instance.actor_id_segments_get(id, collection_name=collection_name, provider_name=provider_name, version=version, dev=dev)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorApi->actor_id_segments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Actor ID | 
 **collection_name** | **str**|  | [optional] 
 **provider_name** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 
 **dev** | **bool**|  | [optional] 

### Return type

[**list[ActorSegmentCollection]**](ActorSegmentCollection.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_id_segments_post**
> str actor_id_segments_post(body, id)



Add a new segment collection for the specific actor

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
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
body = uiuc_incas_client.ActorSegmentCollection() # ActorSegmentCollection | The new segment collections to add
id = 'id_example' # str | Actor ID

try:
    api_response = api_instance.actor_id_segments_post(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorApi->actor_id_segments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActorSegmentCollection**](ActorSegmentCollection.md)| The new segment collections to add | 
 **id** | **str**| Actor ID | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_id_segments_put**
> str actor_id_segments_put(body, id)



Update a segment collection for the specific actor by segment name

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
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
body = uiuc_incas_client.ActorSegmentCollection() # ActorSegmentCollection | The segment collections to update
id = 'id_example' # str | Actor ID

try:
    api_response = api_instance.actor_id_segments_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorApi->actor_id_segments_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActorSegmentCollection**](ActorSegmentCollection.md)| The segment collections to update | 
 **id** | **str**| Actor ID | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_list_get**
> list[ActorIdResponse] actor_list_get(begin, end, media_type, entity_type=entity_type)



Return list of actor IDs available in [begin, end).

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
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
begin = 56 # int | Begin
end = 56 # int | End
media_type = 'media_type_example' # str | Type of entity to retrieve
entity_type = 'entity_type_example' # str | Type of entity to retrieve (optional)

try:
    api_response = api_instance.actor_list_get(begin, end, media_type, entity_type=entity_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorApi->actor_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **begin** | **int**| Begin | 
 **end** | **int**| End | 
 **media_type** | **str**| Type of entity to retrieve | 
 **entity_type** | **str**| Type of entity to retrieve | [optional] 

### Return type

[**list[ActorIdResponse]**](ActorIdResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_segment_batch_delete**
> actor_segment_batch_delete(body)



Deletes a batch of segment collections given a list of IDs and specifications.

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
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
body = uiuc_incas_client.ActorSegmentsBatchDeleteBody() # ActorSegmentsBatchDeleteBody | List of IDs and specifications

try:
    api_instance.actor_segment_batch_delete(body)
except ApiException as e:
    print("Exception when calling ActorApi->actor_segment_batch_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActorSegmentsBatchDeleteBody**](ActorSegmentsBatchDeleteBody.md)| List of IDs and specifications | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_segments_batch_delete_validate**
> ActorSegmentsBatchDeleteValidationResponse actor_segments_batch_delete_validate(body)



Validation endpoint for batch segment deletion, successful attempt will return a token.

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
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
body = uiuc_incas_client.ActorSegmentsBatchDeleteBody() # ActorSegmentsBatchDeleteBody | List of IDs and specifications

try:
    api_response = api_instance.actor_segments_batch_delete_validate(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorApi->actor_segments_batch_delete_validate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActorSegmentsBatchDeleteBody**](ActorSegmentsBatchDeleteBody.md)| List of IDs and specifications | 

### Return type

[**ActorSegmentsBatchDeleteValidationResponse**](ActorSegmentsBatchDeleteValidationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_segments_batch_get**
> dict(str, list[ActorSegmentCollection]) actor_segments_batch_get(body)



Returns a batch of segment collections given a list of IDs and specifications.

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
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
body = uiuc_incas_client.ActorSegmentsBatchGetBody() # ActorSegmentsBatchGetBody | List of IDs and specifications

try:
    api_response = api_instance.actor_segments_batch_get(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorApi->actor_segments_batch_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActorSegmentsBatchGetBody**](ActorSegmentsBatchGetBody.md)| List of IDs and specifications | 

### Return type

**dict(str, list[ActorSegmentCollection])**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_segments_batch_post**
> str actor_segments_batch_post(body)



Submits a segment collection for each actor ID.

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
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
body = NULL # dict(str, ActorSegmentCollection) | Map of IDs and segment collections

try:
    api_response = api_instance.actor_segments_batch_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorApi->actor_segments_batch_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, ActorSegmentCollection)**](dict.md)| Map of IDs and segment collections | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_segments_batch_post_validate**
> ActorSegmentsBatchValidationResponse actor_segments_batch_post_validate(body)



Validation endpoint for batch segment creation, successful attempt will return a token.

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
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
body = NULL # dict(str, ActorSegmentCollection) | List of IDs and specifications

try:
    api_response = api_instance.actor_segments_batch_post_validate(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorApi->actor_segments_batch_post_validate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, ActorSegmentCollection)**](dict.md)| List of IDs and specifications | 

### Return type

[**ActorSegmentsBatchValidationResponse**](ActorSegmentsBatchValidationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_segments_batch_put**
> str actor_segments_batch_put(body)



Updates a segment collection for each actor ID.

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
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
body = NULL # dict(str, ActorSegmentCollection) | Map of IDs and segment collections

try:
    api_response = api_instance.actor_segments_batch_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorApi->actor_segments_batch_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, ActorSegmentCollection)**](dict.md)| Map of IDs and segment collections | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_segments_batch_put_validate**
> ActorSegmentsBatchValidationResponse actor_segments_batch_put_validate(body)



Validation endpoint for batch segment update, successful attempt will return a token.

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
api_instance = uiuc_incas_client.ActorApi(uiuc_incas_client.ApiClient(configuration))
body = NULL # dict(str, ActorSegmentCollection) | List of IDs and specifications

try:
    api_response = api_instance.actor_segments_batch_put_validate(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorApi->actor_segments_batch_put_validate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, ActorSegmentCollection)**](dict.md)| List of IDs and specifications | 

### Return type

[**ActorSegmentsBatchValidationResponse**](ActorSegmentsBatchValidationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

