# uiuc_incas_client.MessageApi

All URIs are relative to *https://incas.cs.illinois.edu:8443/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**message_batch_get**](MessageApi.md#message_batch_get) | **POST** /message/batchGet | 
[**message_count_get**](MessageApi.md#message_count_get) | **GET** /message/count | 
[**message_enrichments_batch_delete**](MessageApi.md#message_enrichments_batch_delete) | **POST** /message/enrichments/batchDelete | 
[**message_enrichments_batch_delete_validate**](MessageApi.md#message_enrichments_batch_delete_validate) | **POST** /message/enrichments/batchDelete/validate | 
[**message_enrichments_batch_get**](MessageApi.md#message_enrichments_batch_get) | **POST** /message/enrichments/batchGet | 
[**message_enrichments_batch_post**](MessageApi.md#message_enrichments_batch_post) | **POST** /message/enrichments/batch | 
[**message_enrichments_batch_post_validate**](MessageApi.md#message_enrichments_batch_post_validate) | **POST** /message/enrichments/batch/validate | 
[**message_enrichments_batch_put**](MessageApi.md#message_enrichments_batch_put) | **PUT** /message/enrichments/batch | 
[**message_enrichments_batch_put_validate**](MessageApi.md#message_enrichments_batch_put_validate) | **PUT** /message/enrichments/batch/validate | 
[**message_enrichments_meta_delete**](MessageApi.md#message_enrichments_meta_delete) | **DELETE** /message/enrichments/meta | 
[**message_enrichments_meta_get**](MessageApi.md#message_enrichments_meta_get) | **GET** /message/enrichments/meta | 
[**message_enrichments_meta_post**](MessageApi.md#message_enrichments_meta_post) | **POST** /message/enrichments/meta | 
[**message_enrichments_meta_put**](MessageApi.md#message_enrichments_meta_put) | **PUT** /message/enrichments/meta | 
[**message_id_enrichments_delete**](MessageApi.md#message_id_enrichments_delete) | **DELETE** /message/{id}/enrichments | 
[**message_id_enrichments_get**](MessageApi.md#message_id_enrichments_get) | **GET** /message/{id}/enrichments | 
[**message_id_enrichments_post**](MessageApi.md#message_id_enrichments_post) | **POST** /message/{id}/enrichments | 
[**message_id_enrichments_put**](MessageApi.md#message_id_enrichments_put) | **PUT** /message/{id}/enrichments | 
[**message_id_get**](MessageApi.md#message_id_get) | **GET** /message/{id} | 
[**message_list_get**](MessageApi.md#message_list_get) | **GET** /message/list | 

# **message_batch_get**
> list[UiucMessage] message_batch_get(body)



Returns a batch of messages given a list of IDs and specifications.

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
api_instance = uiuc_incas_client.MessageApi(uiuc_incas_client.ApiClient(configuration))
body = uiuc_incas_client.MessageBatchGetBody() # MessageBatchGetBody | List of IDs and specifications

try:
    api_response = api_instance.message_batch_get(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageApi->message_batch_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MessageBatchGetBody**](MessageBatchGetBody.md)| List of IDs and specifications | 

### Return type

[**list[UiucMessage]**](UiucMessage.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_count_get**
> int message_count_get(media_type)



Return the number of message IDs available.

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
api_instance = uiuc_incas_client.MessageApi(uiuc_incas_client.ApiClient(configuration))
media_type = 'media_type_example' # str | Type of entity to retrieve

try:
    api_response = api_instance.message_count_get(media_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageApi->message_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_type** | **str**| Type of entity to retrieve | 

### Return type

**int**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_enrichments_batch_delete**
> message_enrichments_batch_delete(body)



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
api_instance = uiuc_incas_client.MessageApi(uiuc_incas_client.ApiClient(configuration))
body = uiuc_incas_client.MessageEnrichmentsBatchDeleteBody() # MessageEnrichmentsBatchDeleteBody | List of IDs and specifications

try:
    api_instance.message_enrichments_batch_delete(body)
except ApiException as e:
    print("Exception when calling MessageApi->message_enrichments_batch_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MessageEnrichmentsBatchDeleteBody**](MessageEnrichmentsBatchDeleteBody.md)| List of IDs and specifications | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_enrichments_batch_delete_validate**
> MessageEnrichmentsBatchDeleteValidationResponse message_enrichments_batch_delete_validate(body)



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
api_instance = uiuc_incas_client.MessageApi(uiuc_incas_client.ApiClient(configuration))
body = uiuc_incas_client.MessageEnrichmentsBatchDeleteBody() # MessageEnrichmentsBatchDeleteBody | List of IDs and specifications

try:
    api_response = api_instance.message_enrichments_batch_delete_validate(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageApi->message_enrichments_batch_delete_validate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MessageEnrichmentsBatchDeleteBody**](MessageEnrichmentsBatchDeleteBody.md)| List of IDs and specifications | 

### Return type

[**MessageEnrichmentsBatchDeleteValidationResponse**](MessageEnrichmentsBatchDeleteValidationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_enrichments_batch_get**
> dict(str, list[MessageEnrichment]) message_enrichments_batch_get(body)



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
api_instance = uiuc_incas_client.MessageApi(uiuc_incas_client.ApiClient(configuration))
body = uiuc_incas_client.MessageEnrichmentsBatchGetBody() # MessageEnrichmentsBatchGetBody | List of IDs and specifications

try:
    api_response = api_instance.message_enrichments_batch_get(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageApi->message_enrichments_batch_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MessageEnrichmentsBatchGetBody**](MessageEnrichmentsBatchGetBody.md)| List of IDs and specifications | 

### Return type

**dict(str, list[MessageEnrichment])**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_enrichments_batch_post**
> str message_enrichments_batch_post(body)



Submits a enrichment for each message ID.

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
api_instance = uiuc_incas_client.MessageApi(uiuc_incas_client.ApiClient(configuration))
body = NULL # dict(str, MessageEnrichment) | Map of IDs and enrichments

try:
    api_response = api_instance.message_enrichments_batch_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageApi->message_enrichments_batch_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, MessageEnrichment)**](dict.md)| Map of IDs and enrichments | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_enrichments_batch_post_validate**
> MessageEnrichmentsBatchValidationResponse message_enrichments_batch_post_validate(body)



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
api_instance = uiuc_incas_client.MessageApi(uiuc_incas_client.ApiClient(configuration))
body = NULL # dict(str, MessageEnrichment) | List of IDs and specifications

try:
    api_response = api_instance.message_enrichments_batch_post_validate(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageApi->message_enrichments_batch_post_validate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, MessageEnrichment)**](dict.md)| List of IDs and specifications | 

### Return type

[**MessageEnrichmentsBatchValidationResponse**](MessageEnrichmentsBatchValidationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_enrichments_batch_put**
> str message_enrichments_batch_put(body)



Updates a enrichment for each message ID.

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
api_instance = uiuc_incas_client.MessageApi(uiuc_incas_client.ApiClient(configuration))
body = NULL # dict(str, MessageEnrichment) | Map of IDs and enrichments

try:
    api_response = api_instance.message_enrichments_batch_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageApi->message_enrichments_batch_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, MessageEnrichment)**](dict.md)| Map of IDs and enrichments | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_enrichments_batch_put_validate**
> MessageEnrichmentsBatchValidationResponse message_enrichments_batch_put_validate(body)



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
api_instance = uiuc_incas_client.MessageApi(uiuc_incas_client.ApiClient(configuration))
body = NULL # dict(str, MessageEnrichment) | List of IDs and specifications

try:
    api_response = api_instance.message_enrichments_batch_put_validate(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageApi->message_enrichments_batch_put_validate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, MessageEnrichment)**](dict.md)| List of IDs and specifications | 

### Return type

[**MessageEnrichmentsBatchValidationResponse**](MessageEnrichmentsBatchValidationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_enrichments_meta_delete**
> message_enrichments_meta_delete(enrichment_name, provider_name, version)



Delete specific message enrichment meta by providerName, enrichmentName and version.

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
api_instance = uiuc_incas_client.MessageApi(uiuc_incas_client.ApiClient(configuration))
enrichment_name = 'enrichment_name_example' # str | 
provider_name = 'provider_name_example' # str | 
version = 'version_example' # str | 

try:
    api_instance.message_enrichments_meta_delete(enrichment_name, provider_name, version)
except ApiException as e:
    print("Exception when calling MessageApi->message_enrichments_meta_delete: %s\n" % e)
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

# **message_enrichments_meta_get**
> list[MessageEnrichmentMeta] message_enrichments_meta_get(enrichment_name=enrichment_name, provider_name=provider_name, version=version)



Returns current message enrichment metas by providerName, enrichmentName and version.

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
api_instance = uiuc_incas_client.MessageApi(uiuc_incas_client.ApiClient(configuration))
enrichment_name = 'enrichment_name_example' # str |  (optional)
provider_name = 'provider_name_example' # str |  (optional)
version = 'version_example' # str |  (optional)

try:
    api_response = api_instance.message_enrichments_meta_get(enrichment_name=enrichment_name, provider_name=provider_name, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageApi->message_enrichments_meta_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrichment_name** | **str**|  | [optional] 
 **provider_name** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 

### Return type

[**list[MessageEnrichmentMeta]**](MessageEnrichmentMeta.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_enrichments_meta_post**
> str message_enrichments_meta_post(body)



Submits a message enrichment meta (post after all messages have been added).

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
api_instance = uiuc_incas_client.MessageApi(uiuc_incas_client.ApiClient(configuration))
body = uiuc_incas_client.MessageEnrichmentMeta() # MessageEnrichmentMeta | The new enrichment meta to add

try:
    api_response = api_instance.message_enrichments_meta_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageApi->message_enrichments_meta_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MessageEnrichmentMeta**](MessageEnrichmentMeta.md)| The new enrichment meta to add | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_enrichments_meta_put**
> str message_enrichments_meta_put(body)



Updates message enrichment meta (after all messages have been added) by providerName, enrichmentName and version.

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
api_instance = uiuc_incas_client.MessageApi(uiuc_incas_client.ApiClient(configuration))
body = uiuc_incas_client.MessageEnrichmentMeta() # MessageEnrichmentMeta | The new enrichment meta to update

try:
    api_response = api_instance.message_enrichments_meta_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageApi->message_enrichments_meta_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MessageEnrichmentMeta**](MessageEnrichmentMeta.md)| The new enrichment meta to update | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_id_enrichments_delete**
> message_id_enrichments_delete(id, enrichment_name, provider_name, version)



Delete a enrichment for specific message by type, providerName and version.

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
api_instance = uiuc_incas_client.MessageApi(uiuc_incas_client.ApiClient(configuration))
id = 'id_example' # str | Message ID
enrichment_name = 'enrichment_name_example' # str | 
provider_name = 'provider_name_example' # str | 
version = 'version_example' # str | 

try:
    api_instance.message_id_enrichments_delete(id, enrichment_name, provider_name, version)
except ApiException as e:
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

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_id_enrichments_get**
> list[MessageEnrichment] message_id_enrichments_get(id, enrichment_name=enrichment_name, provider_name=provider_name, version=version, dev=dev)



Returns all visible matched enrichment for the specific message by type, providerName and version.

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
api_instance = uiuc_incas_client.MessageApi(uiuc_incas_client.ApiClient(configuration))
id = 'id_example' # str | Message ID
enrichment_name = 'enrichment_name_example' # str |  (optional)
provider_name = 'provider_name_example' # str |  (optional)
version = 'version_example' # str |  (optional)
dev = true # bool |  (optional)

try:
    api_response = api_instance.message_id_enrichments_get(id, enrichment_name=enrichment_name, provider_name=provider_name, version=version, dev=dev)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageApi->message_id_enrichments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Message ID | 
 **enrichment_name** | **str**|  | [optional] 
 **provider_name** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 
 **dev** | **bool**|  | [optional] 

### Return type

[**list[MessageEnrichment]**](MessageEnrichment.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_id_enrichments_post**
> str message_id_enrichments_post(body, id)



Submits a new enrichment for specific message.

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
api_instance = uiuc_incas_client.MessageApi(uiuc_incas_client.ApiClient(configuration))
body = uiuc_incas_client.MessageEnrichment() # MessageEnrichment | The new enrichment to add
id = 'id_example' # str | Message ID

try:
    api_response = api_instance.message_id_enrichments_post(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageApi->message_id_enrichments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MessageEnrichment**](MessageEnrichment.md)| The new enrichment to add | 
 **id** | **str**| Message ID | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_id_enrichments_put**
> str message_id_enrichments_put(body, id)



Update a enrichment for specific message by type, providerName and version.

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
api_instance = uiuc_incas_client.MessageApi(uiuc_incas_client.ApiClient(configuration))
body = uiuc_incas_client.MessageEnrichment() # MessageEnrichment | The new enrichments to update
id = 'id_example' # str | Message ID

try:
    api_response = api_instance.message_id_enrichments_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageApi->message_id_enrichments_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MessageEnrichment**](MessageEnrichment.md)| The new enrichments to update | 
 **id** | **str**| Message ID | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_id_get**
> UiucMessage message_id_get(id, with_enrichment=with_enrichment, enrichment_name=enrichment_name, provider_name=provider_name, version=version, dev=dev)



Returns specific message by id.

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
api_instance = uiuc_incas_client.MessageApi(uiuc_incas_client.ApiClient(configuration))
id = 'id_example' # str | Message ID
with_enrichment = true # bool | Whether to retrieve enrichments (optional)
enrichment_name = 'enrichment_name_example' # str |  (optional)
provider_name = 'provider_name_example' # str |  (optional)
version = 'version_example' # str |  (optional)
dev = true # bool |  (optional)

try:
    api_response = api_instance.message_id_get(id, with_enrichment=with_enrichment, enrichment_name=enrichment_name, provider_name=provider_name, version=version, dev=dev)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageApi->message_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Message ID | 
 **with_enrichment** | **bool**| Whether to retrieve enrichments | [optional] 
 **enrichment_name** | **str**|  | [optional] 
 **provider_name** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 
 **dev** | **bool**|  | [optional] 

### Return type

[**UiucMessage**](UiucMessage.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_list_get**
> list[MessageIdResponse] message_list_get(begin, end, media_type)



Return list of message IDs available in [begin, end).

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
api_instance = uiuc_incas_client.MessageApi(uiuc_incas_client.ApiClient(configuration))
begin = 56 # int | Begin
end = 56 # int | End
media_type = 'media_type_example' # str | Type of entity to retrieve

try:
    api_response = api_instance.message_list_get(begin, end, media_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageApi->message_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **begin** | **int**| Begin | 
 **end** | **int**| End | 
 **media_type** | **str**| Type of entity to retrieve | 

### Return type

[**list[MessageIdResponse]**](MessageIdResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

