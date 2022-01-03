# uiuc_incas_client.MessageApi

All URIs are relative to *https://incas.cs.illinois.edu:8443/api/v1*

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
> actor_enrichments_delete(enrichment_name=enrichment_name, provider_name=provider_name, version=version)



Delete specific message enrichment meta by providerName, enrichmentName and version

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = uiuc_incas_client.MessageApi()
enrichment_name = 'enrichment_name_example' # str |  (optional)
provider_name = 'provider_name_example' # str |  (optional)
version = 'version_example' # str |  (optional)

try:
    api_instance.actor_enrichments_delete(enrichment_name=enrichment_name, provider_name=provider_name, version=version)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_enrichments_delete**
> message_enrichments_delete(enrichment_name=enrichment_name, provider_name=provider_name, version=version)



Delete specific message enrichment meta by providerName, enrichmentName and version

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = uiuc_incas_client.MessageApi()
enrichment_name = 'enrichment_name_example' # str |  (optional)
provider_name = 'provider_name_example' # str |  (optional)
version = 'version_example' # str |  (optional)

try:
    api_instance.message_enrichments_delete(enrichment_name=enrichment_name, provider_name=provider_name, version=version)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_enrichments_get**
> MessageEnrichmentMeta message_enrichments_get(enrichment_name=enrichment_name, provider_name=provider_name, version=version)



Returns current message enrichment meta by providerName, enrichmentName and version

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = uiuc_incas_client.MessageApi()
enrichment_name = 'enrichment_name_example' # str |  (optional)
provider_name = 'provider_name_example' # str |  (optional)
version = 'version_example' # str |  (optional)

try:
    api_response = api_instance.message_enrichments_get(enrichment_name=enrichment_name, provider_name=provider_name, version=version)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_enrichments_post**
> MessageEnrichmentMeta message_enrichments_post(body)



Creates message enrichment meta (post after all messages have been added)

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = uiuc_incas_client.MessageApi()
body = [uiuc_incas_client.MessageEnrichmentMeta()] # list[MessageEnrichmentMeta] | The new enrichment meta to add

try:
    api_response = api_instance.message_enrichments_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageApi->message_enrichments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[MessageEnrichmentMeta]**](MessageEnrichmentMeta.md)| The new enrichment meta to add | 

### Return type

[**MessageEnrichmentMeta**](MessageEnrichmentMeta.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_enrichments_put**
> MessageEnrichmentMeta message_enrichments_put(body, enrichment_name=enrichment_name, provider_name=provider_name, version=version)



Updates message enrichment meta (after all messages have been added) by providerName, enrichmentName and version

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = uiuc_incas_client.MessageApi()
body = [uiuc_incas_client.MessageEnrichmentMeta()] # list[MessageEnrichmentMeta] | The new enrichment meta to update
enrichment_name = 'enrichment_name_example' # str |  (optional)
provider_name = 'provider_name_example' # str |  (optional)
version = 'version_example' # str |  (optional)

try:
    api_response = api_instance.message_enrichments_put(body, enrichment_name=enrichment_name, provider_name=provider_name, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageApi->message_enrichments_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[MessageEnrichmentMeta]**](MessageEnrichmentMeta.md)| The new enrichment meta to update | 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_id_enrichments_delete**
> message_id_enrichments_delete(id, enrichment_name, provider_name, version)



Delete the enrichments for specific message by type, providerName and version

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = uiuc_incas_client.MessageApi()
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_id_enrichments_get**
> list[MessageEnrichment] message_id_enrichments_get(id, enrichment_name=enrichment_name, provider_name=provider_name, version=version)



Returns all visible matched enrichment for the specific message by type, providerName and version

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = uiuc_incas_client.MessageApi()
id = 'id_example' # str | Message ID
enrichment_name = 'enrichment_name_example' # str |  (optional)
provider_name = 'provider_name_example' # str |  (optional)
version = 'version_example' # str |  (optional)

try:
    api_response = api_instance.message_id_enrichments_get(id, enrichment_name=enrichment_name, provider_name=provider_name, version=version)
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

### Return type

[**list[MessageEnrichment]**](MessageEnrichment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_id_enrichments_post**
> list[MessageEnrichment] message_id_enrichments_post(body, id)



Creates new enrichments for specific message

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = uiuc_incas_client.MessageApi()
body = [uiuc_incas_client.MessageEnrichment()] # list[MessageEnrichment] | The new enrichment to add
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
 **body** | [**list[MessageEnrichment]**](MessageEnrichment.md)| The new enrichment to add | 
 **id** | **str**| Message ID | 

### Return type

[**list[MessageEnrichment]**](MessageEnrichment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_id_enrichments_put**
> list[MessageEnrichment] message_id_enrichments_put(body, enrichment_name, provider_name, version, id)



Update the enrichments for specific message by type, providerName and version

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = uiuc_incas_client.MessageApi()
body = [uiuc_incas_client.MessageEnrichment()] # list[MessageEnrichment] | The new enrichments to update
enrichment_name = 'enrichment_name_example' # str | 
provider_name = 'provider_name_example' # str | 
version = 'version_example' # str | 
id = 'id_example' # str | Message ID

try:
    api_response = api_instance.message_id_enrichments_put(body, enrichment_name, provider_name, version, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageApi->message_id_enrichments_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[MessageEnrichment]**](MessageEnrichment.md)| The new enrichments to update | 
 **enrichment_name** | **str**|  | 
 **provider_name** | **str**|  | 
 **version** | **str**|  | 
 **id** | **str**| Message ID | 

### Return type

[**list[MessageEnrichment]**](MessageEnrichment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_id_get**
> UiucMessage message_id_get(id)



Returns specific message by id

### Example
```python
from __future__ import print_function
import time
import uiuc_incas_client
from uiuc_incas_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = uiuc_incas_client.MessageApi()
id = 'id_example' # str | Message ID

try:
    api_response = api_instance.message_id_get(id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

