# swagger_client.ActorApi

All URIs are relative to *https://virtserver.swaggerhub.com/incas/incas/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**actor_enrichments_delete**](ActorApi.md#actor_enrichments_delete) | **DELETE** /actor/enrichments | 
[**actor_enrichments_get**](ActorApi.md#actor_enrichments_get) | **GET** /actor/enrichments | 
[**actor_enrichments_post**](ActorApi.md#actor_enrichments_post) | **POST** /actor/enrichments | 
[**actor_enrichments_put**](ActorApi.md#actor_enrichments_put) | **PUT** /actor/enrichments | 
[**actor_id_enrichments_delete**](ActorApi.md#actor_id_enrichments_delete) | **DELETE** /actor/{id}/enrichments | 
[**actor_id_enrichments_get**](ActorApi.md#actor_id_enrichments_get) | **GET** /actor/{id}/enrichments | 
[**actor_id_enrichments_post**](ActorApi.md#actor_id_enrichments_post) | **POST** /actor/{id}/enrichments | 
[**actor_id_enrichments_put**](ActorApi.md#actor_id_enrichments_put) | **PUT** /actor/{id}/enrichments | 
[**actor_id_get**](ActorApi.md#actor_id_get) | **GET** /actor/{id} | 

# **actor_enrichments_delete**
> actor_enrichments_delete(enrichment_name=enrichment_name, provider_name=provider_name, version=version)



Delete specific actor enrichment meta by providerName, enrichmentName and version

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActorApi()
enrichment_name = 'enrichment_name_example' # str |  (optional)
provider_name = 'provider_name_example' # str |  (optional)
version = 'version_example' # str |  (optional)

try:
    api_instance.actor_enrichments_delete(enrichment_name=enrichment_name, provider_name=provider_name, version=version)
except ApiException as e:
    print("Exception when calling ActorApi->actor_enrichments_delete: %s\n" % e)
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

# **actor_enrichments_get**
> ActorEnrichmentMeta actor_enrichments_get(enrichment_name=enrichment_name, provider_name=provider_name, version=version)



Returns current actor enrichment meta by providerName, enrichmentName and version

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActorApi()
enrichment_name = 'enrichment_name_example' # str |  (optional)
provider_name = 'provider_name_example' # str |  (optional)
version = 'version_example' # str |  (optional)

try:
    api_response = api_instance.actor_enrichments_get(enrichment_name=enrichment_name, provider_name=provider_name, version=version)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_enrichments_post**
> ActorEnrichmentMeta actor_enrichments_post(body)



Creates actor enrichment meta (post after all actors have been added)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActorApi()
body = [swagger_client.ActorEnrichmentMeta()] # list[ActorEnrichmentMeta] | The new enrichment meta to add

try:
    api_response = api_instance.actor_enrichments_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorApi->actor_enrichments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ActorEnrichmentMeta]**](ActorEnrichmentMeta.md)| The new enrichment meta to add | 

### Return type

[**ActorEnrichmentMeta**](ActorEnrichmentMeta.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_enrichments_put**
> ActorEnrichmentMeta actor_enrichments_put(body, enrichment_name=enrichment_name, provider_name=provider_name, version=version)



Updates actor enrichment meta (after all actors have been added) by providerName, enrichmentName and version

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActorApi()
body = [swagger_client.ActorEnrichmentMeta()] # list[ActorEnrichmentMeta] | The new enrichment meta to update
enrichment_name = 'enrichment_name_example' # str |  (optional)
provider_name = 'provider_name_example' # str |  (optional)
version = 'version_example' # str |  (optional)

try:
    api_response = api_instance.actor_enrichments_put(body, enrichment_name=enrichment_name, provider_name=provider_name, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorApi->actor_enrichments_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ActorEnrichmentMeta]**](ActorEnrichmentMeta.md)| The new enrichment meta to update | 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_id_enrichments_delete**
> actor_id_enrichments_delete(id, enrichment_name, provider_name, version)



Delete the enrichments for specific actor by type, providerName and version

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActorApi()
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
> list[ActorEnrichment] actor_id_enrichments_get(id, enrichment_name=enrichment_name, provider_name=provider_name, version=version)



Returns all matched enrichment for the specific actor by type, providerName and version

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActorApi()
id = 'id_example' # str | Actor ID
enrichment_name = 'enrichment_name_example' # str |  (optional)
provider_name = 'provider_name_example' # str |  (optional)
version = 'version_example' # str |  (optional)

try:
    api_response = api_instance.actor_id_enrichments_get(id, enrichment_name=enrichment_name, provider_name=provider_name, version=version)
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

### Return type

[**list[ActorEnrichment]**](ActorEnrichment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_id_enrichments_post**
> list[ActorEnrichment] actor_id_enrichments_post(body, id)



Creates new enrichments for specific message

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActorApi()
body = [swagger_client.ActorEnrichment()] # list[ActorEnrichment] | The new enrichment to add
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
 **body** | [**list[ActorEnrichment]**](ActorEnrichment.md)| The new enrichment to add | 
 **id** | **str**| Actor ID | 

### Return type

[**list[ActorEnrichment]**](ActorEnrichment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_id_enrichments_put**
> list[ActorEnrichment] actor_id_enrichments_put(body, enrichment_name, provider_name, version, id)



Update the enrichments for specific actor by type, providerName and version

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActorApi()
body = [swagger_client.ActorEnrichment()] # list[ActorEnrichment] | The new enrichments to update
enrichment_name = 'enrichment_name_example' # str | 
provider_name = 'provider_name_example' # str | 
version = 'version_example' # str | 
id = 'id_example' # str | Message ID

try:
    api_response = api_instance.actor_id_enrichments_put(body, enrichment_name, provider_name, version, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorApi->actor_id_enrichments_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ActorEnrichment]**](ActorEnrichment.md)| The new enrichments to update | 
 **enrichment_name** | **str**|  | 
 **provider_name** | **str**|  | 
 **version** | **str**|  | 
 **id** | **str**| Message ID | 

### Return type

[**list[ActorEnrichment]**](ActorEnrichment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actor_id_get**
> Actor actor_id_get(id)



Returns specific actor by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActorApi()
id = 'id_example' # str | Actor ID

try:
    api_response = api_instance.actor_id_get(id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

